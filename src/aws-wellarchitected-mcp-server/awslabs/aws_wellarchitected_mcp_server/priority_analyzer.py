# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Priority analyzer for Well-Architected best practices."""

from dataclasses import dataclass
from typing import List, Dict, Set
from .models import RiskLevel, Pillar
from .well_architected_framework import BestPractice

@dataclass
class PriorityItem:
    """A prioritized best practice with context."""
    best_practice: BestPractice
    priority_score: int
    related_practices: List[BestPractice]
    impact_reason: str
    implementation_order: int

class PriorityAnalyzer:
    """Analyzes and prioritizes best practices based on risk and relationships."""
    
    def __init__(self, best_practices: Dict[str, BestPractice]):
        self.best_practices = best_practices
        self.risk_weights = {
            RiskLevel.HIGH: 10,
            RiskLevel.MEDIUM: 5,
            RiskLevel.LOW: 2
        }
    
    def get_top_priorities(self, selected_pillars: List[Pillar], count: int = 5) -> List[PriorityItem]:
        """Get top N priority items based on risk and relationships."""
        # Filter best practices by selected pillars
        filtered_practices = {
            bp_id: bp for bp_id, bp in self.best_practices.items()
            if bp.pillar in selected_pillars
        }
        
        # Calculate priority scores
        scored_practices = []
        for bp_id, bp in filtered_practices.items():
            score = self._calculate_priority_score(bp, filtered_practices)
            related = self._get_related_practices(bp, filtered_practices)
            impact_reason = self._get_impact_reason(bp, related)
            
            scored_practices.append((bp, score, related, impact_reason))
        
        # Sort by priority score (descending)
        scored_practices.sort(key=lambda x: x[1], reverse=True)
        
        # Create priority items with implementation order
        priority_items = []
        for i, (bp, score, related, reason) in enumerate(scored_practices[:count]):
            priority_items.append(PriorityItem(
                best_practice=bp,
                priority_score=score,
                related_practices=related,
                impact_reason=reason,
                implementation_order=i + 1
            ))
        
        return priority_items
    
    def _calculate_priority_score(self, bp: BestPractice, all_practices: Dict[str, BestPractice]) -> int:
        """Calculate priority score based on risk level and relationships."""
        base_score = self.risk_weights.get(bp.risk_level, 1)
        
        # Bonus for having related practices (indicates foundational importance)
        related_count = len(bp.related_best_practices or [])
        relationship_bonus = min(related_count * 2, 10)
        
        # Bonus for security and reliability (critical pillars)
        pillar_bonus = 0
        if bp.pillar in [Pillar.SECURITY, Pillar.RELIABILITY]:
            pillar_bonus = 5
        elif bp.pillar == Pillar.OPERATIONAL_EXCELLENCE:
            pillar_bonus = 3
        
        # Bonus for foundational practices (typically BP01, BP02)
        foundational_bonus = 0
        if bp.id.endswith(('-BP01', '-BP02')):
            foundational_bonus = 3
        
        return base_score + relationship_bonus + pillar_bonus + foundational_bonus
    
    def _get_related_practices(self, bp: BestPractice, all_practices: Dict[str, BestPractice]) -> List[BestPractice]:
        """Get related best practices that exist in the filtered set."""
        if not bp.related_best_practices:
            return []
        
        related = []
        for related_id in bp.related_best_practices:
            if related_id in all_practices:
                related.append(all_practices[related_id])
        
        return related
    
    def _get_impact_reason(self, bp: BestPractice, related_practices: List[BestPractice]) -> str:
        """Generate explanation of why this practice is high priority."""
        reasons = []
        
        # Risk level impact
        if bp.risk_level == RiskLevel.HIGH:
            reasons.append("High risk if not implemented")
        
        # Relationship impact
        if len(related_practices) > 0:
            reasons.append(f"Foundational for {len(related_practices)} related practices")
        
        # Pillar-specific impact
        pillar_impacts = {
            Pillar.SECURITY: "Critical for protecting data and systems",
            Pillar.RELIABILITY: "Essential for system availability and resilience",
            Pillar.OPERATIONAL_EXCELLENCE: "Fundamental for operational maturity",
            Pillar.COST_OPTIMIZATION: "Significant cost impact if neglected",
            Pillar.PERFORMANCE_EFFICIENCY: "Major performance implications",
            Pillar.SUSTAINABILITY: "Important for environmental responsibility"
        }
        
        if bp.pillar in pillar_impacts:
            reasons.append(pillar_impacts[bp.pillar])
        
        return "; ".join(reasons) if reasons else "Important for overall architecture quality"

def format_priority_recommendations(priority_items: List[PriorityItem]) -> str:
    """Format priority recommendations as markdown."""
    if not priority_items:
        return "No priority items to display."
    
    markdown = f"# Top {len(priority_items)} Priority Recommendations\n\n"
    
    for item in priority_items:
        bp = item.best_practice
        markdown += f"""## {item.implementation_order}. {bp.title}
**Pillar**: {bp.pillar.value.replace('_', ' ').title()}  
**Risk Level**: {bp.risk_level.value.upper()}  
**Priority Score**: {item.priority_score}

### Why This Matters
{item.impact_reason}

### Description
{bp.description}

### Key Questions to Address
{chr(10).join(f'- {q}' for q in bp.questions)}

### Implementation Guidance
{chr(10).join(f'- {g}' for g in bp.implementation_guidance)}
"""
        
        if item.related_practices:
            markdown += f"""
### Related Practices to Consider
These practices work together and should be implemented in coordination:
{chr(10).join(f'- **{rp.id}**: {rp.title}' for rp in item.related_practices)}
"""
        
        markdown += "\n---\n\n"
    
    return markdown

def get_implementation_roadmap(priority_items: List[PriorityItem]) -> str:
    """Generate implementation roadmap based on priorities."""
    if not priority_items:
        return "No items to create roadmap."
    
    roadmap = "# Implementation Roadmap\n\n"
    
    # Group by phases
    phase1 = priority_items[:2] if len(priority_items) >= 2 else priority_items
    phase2 = priority_items[2:5] if len(priority_items) > 2 else []
    phase3 = priority_items[5:] if len(priority_items) > 5 else []
    
    if phase1:
        roadmap += "## Phase 1: Critical Foundations (Weeks 1-2)\n"
        roadmap += "Focus on highest risk and most foundational practices:\n\n"
        for item in phase1:
            roadmap += f"- **{item.best_practice.id}**: {item.best_practice.title}\n"
        roadmap += "\n"
    
    if phase2:
        roadmap += "## Phase 2: Core Improvements (Weeks 3-6)\n"
        roadmap += "Build on foundations with these important practices:\n\n"
        for item in phase2:
            roadmap += f"- **{item.best_practice.id}**: {item.best_practice.title}\n"
        roadmap += "\n"
    
    if phase3:
        roadmap += "## Phase 3: Advanced Optimization (Weeks 7+)\n"
        roadmap += "Complete the improvements with these practices:\n\n"
        for item in phase3:
            roadmap += f"- **{item.best_practice.id}**: {item.best_practice.title}\n"
        roadmap += "\n"
    
    roadmap += """## Implementation Tips
- Start with Phase 1 items as they often enable or simplify later phases
- Consider related practices together for maximum impact
- Validate each implementation before moving to the next phase
- Adjust timeline based on your team's capacity and complexity
"""
    
    return roadmap