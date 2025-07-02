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

"""Eisenhower Matrix for Well-Architected best practices prioritization."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from .models import RiskLevel, Pillar
from .well_architected_framework import BestPractice

class MatrixQuadrant(Enum):
    """Eisenhower Matrix quadrants."""
    URGENT_IMPORTANT = "urgent_important"      # Do First
    NOT_URGENT_IMPORTANT = "not_urgent_important"  # Schedule
    URGENT_NOT_IMPORTANT = "urgent_not_important"  # Delegate
    NOT_URGENT_NOT_IMPORTANT = "not_urgent_not_important"  # Eliminate

@dataclass
class MatrixItem:
    """Best practice positioned in Eisenhower Matrix."""
    best_practice: BestPractice
    quadrant: MatrixQuadrant
    urgency_score: int
    importance_score: int
    action_recommendation: str

class EisenhowerMatrix:
    """Creates Eisenhower Matrix for Well-Architected best practices."""
    
    def __init__(self, best_practices: Dict[str, BestPractice]):
        self.best_practices = best_practices
    
    def create_matrix(self, selected_pillars: List[Pillar]) -> Dict[MatrixQuadrant, List[MatrixItem]]:
        """Create Eisenhower Matrix for selected pillars."""
        # Filter practices by pillars
        filtered_practices = {
            bp_id: bp for bp_id, bp in self.best_practices.items()
            if bp.pillar in selected_pillars
        }
        
        # Create matrix items
        matrix_items = []
        for bp in filtered_practices.values():
            urgency = self._calculate_urgency(bp)
            importance = self._calculate_importance(bp)
            quadrant = self._determine_quadrant(urgency, importance)
            action = self._get_action_recommendation(quadrant)
            
            matrix_items.append(MatrixItem(
                best_practice=bp,
                quadrant=quadrant,
                urgency_score=urgency,
                importance_score=importance,
                action_recommendation=action
            ))
        
        # Group by quadrant
        matrix = {quadrant: [] for quadrant in MatrixQuadrant}
        for item in matrix_items:
            matrix[item.quadrant].append(item)
        
        # Sort each quadrant by combined score
        for quadrant in matrix:
            matrix[quadrant].sort(
                key=lambda x: x.urgency_score + x.importance_score,
                reverse=True
            )
        
        return matrix
    
    def _calculate_urgency(self, bp: BestPractice) -> int:
        """Calculate urgency score (1-10)."""
        score = 0
        
        # Risk level urgency
        if bp.risk_level == RiskLevel.HIGH:
            score += 8
        elif bp.risk_level == RiskLevel.MEDIUM:
            score += 5
        else:
            score += 2
        
        # Security and reliability are more urgent
        if bp.pillar in [Pillar.SECURITY, Pillar.RELIABILITY]:
            score += 2
        
        return min(score, 10)
    
    def _calculate_importance(self, bp: BestPractice) -> int:
        """Calculate importance score (1-10)."""
        score = 0
        
        # Foundational practices are more important
        if bp.id.endswith(('-BP01', '-BP02')):
            score += 4
        
        # Practices with many relationships are important
        related_count = len(bp.related_best_practices or [])
        score += min(related_count, 4)
        
        # Pillar-based importance
        pillar_importance = {
            Pillar.SECURITY: 4,
            Pillar.RELIABILITY: 4,
            Pillar.OPERATIONAL_EXCELLENCE: 3,
            Pillar.COST_OPTIMIZATION: 2,
            Pillar.PERFORMANCE_EFFICIENCY: 2,
            Pillar.SUSTAINABILITY: 1
        }
        score += pillar_importance.get(bp.pillar, 1)
        
        return min(score, 10)
    
    def _determine_quadrant(self, urgency: int, importance: int) -> MatrixQuadrant:
        """Determine which quadrant based on urgency and importance scores."""
        urgent_threshold = 6
        important_threshold = 6
        
        is_urgent = urgency >= urgent_threshold
        is_important = importance >= important_threshold
        
        if is_urgent and is_important:
            return MatrixQuadrant.URGENT_IMPORTANT
        elif not is_urgent and is_important:
            return MatrixQuadrant.NOT_URGENT_IMPORTANT
        elif is_urgent and not is_important:
            return MatrixQuadrant.URGENT_NOT_IMPORTANT
        else:
            return MatrixQuadrant.NOT_URGENT_NOT_IMPORTANT
    
    def _get_action_recommendation(self, quadrant: MatrixQuadrant) -> str:
        """Get action recommendation for quadrant."""
        actions = {
            MatrixQuadrant.URGENT_IMPORTANT: "DO FIRST - Implement immediately",
            MatrixQuadrant.NOT_URGENT_IMPORTANT: "SCHEDULE - Plan for implementation",
            MatrixQuadrant.URGENT_NOT_IMPORTANT: "DELEGATE - Quick wins, automate if possible",
            MatrixQuadrant.NOT_URGENT_NOT_IMPORTANT: "ELIMINATE - Consider if needed"
        }
        return actions[quadrant]

def format_eisenhower_matrix(matrix: Dict[MatrixQuadrant, List[MatrixItem]]) -> str:
    """Format Eisenhower Matrix as visual text representation."""
    
    def format_quadrant_items(items: List[MatrixItem], max_items: int = 5) -> str:
        if not items:
            return "No items"
        
        result = ""
        for i, item in enumerate(items[:max_items]):
            bp = item.best_practice
            result += f"• {bp.id}: {bp.title[:40]}{'...' if len(bp.title) > 40 else ''}\n"
        
        if len(items) > max_items:
            result += f"  ... and {len(items) - max_items} more\n"
        
        return result.rstrip()
    
    # Get items for each quadrant
    urgent_important = matrix[MatrixQuadrant.URGENT_IMPORTANT]
    not_urgent_important = matrix[MatrixQuadrant.NOT_URGENT_IMPORTANT]
    urgent_not_important = matrix[MatrixQuadrant.URGENT_NOT_IMPORTANT]
    not_urgent_not_important = matrix[MatrixQuadrant.NOT_URGENT_NOT_IMPORTANT]
    
    matrix_display = f"""
# Eisenhower Matrix - Well-Architected Priorities

```
                    URGENT                    |               NOT URGENT
                                             |
    ┌─────────────────────────────────────────┼─────────────────────────────────────────┐
    │                                         │                                         │
  I │           DO FIRST                      │            SCHEDULE                     │
  M │     ({len(urgent_important)} items)                    │      ({len(not_urgent_important)} items)                      │
  P │                                         │                                         │
  O │ {format_quadrant_items(urgent_important, 3).replace(chr(10), chr(10) + '  │ ')} │ {format_quadrant_items(not_urgent_important, 3).replace(chr(10), chr(10) + '  │ ')} │
  R │                                         │                                         │
  T │                                         │                                         │
  A ├─────────────────────────────────────────┼─────────────────────────────────────────┤
  N │                                         │                                         │
  T │          DELEGATE                       │           ELIMINATE                     │
    │     ({len(urgent_not_important)} items)                    │      ({len(not_urgent_not_important)} items)                      │
    │                                         │                                         │
    │ {format_quadrant_items(urgent_not_important, 3).replace(chr(10), chr(10) + '  │ ')} │ {format_quadrant_items(not_urgent_not_important, 3).replace(chr(10), chr(10) + '  │ ')} │
    │                                         │                                         │
    └─────────────────────────────────────────┼─────────────────────────────────────────┘
```

## Action Plan

### 🔥 DO FIRST - Urgent & Important ({len(urgent_important)} items)
{format_quadrant_items(urgent_important)}

### 📅 SCHEDULE - Important but Not Urgent ({len(not_urgent_important)} items)  
{format_quadrant_items(not_urgent_important)}

### ⚡ DELEGATE - Urgent but Not Important ({len(urgent_not_important)} items)
{format_quadrant_items(urgent_not_important)}

### 🗑️ ELIMINATE - Neither Urgent nor Important ({len(not_urgent_not_important)} items)
{format_quadrant_items(not_urgent_not_important)}
"""
    
    return matrix_display

def get_matrix_summary(matrix: Dict[MatrixQuadrant, List[MatrixItem]]) -> str:
    """Get summary of matrix distribution."""
    total_items = sum(len(items) for items in matrix.values())
    
    summary = f"""# Matrix Summary

**Total Best Practices Analyzed**: {total_items}

**Distribution**:
- 🔥 **DO FIRST** (Urgent & Important): {len(matrix[MatrixQuadrant.URGENT_IMPORTANT])} items ({len(matrix[MatrixQuadrant.URGENT_IMPORTANT])/total_items*100:.1f}%)
- 📅 **SCHEDULE** (Important): {len(matrix[MatrixQuadrant.NOT_URGENT_IMPORTANT])} items ({len(matrix[MatrixQuadrant.NOT_URGENT_IMPORTANT])/total_items*100:.1f}%)
- ⚡ **DELEGATE** (Urgent): {len(matrix[MatrixQuadrant.URGENT_NOT_IMPORTANT])} items ({len(matrix[MatrixQuadrant.URGENT_NOT_IMPORTANT])/total_items*100:.1f}%)
- 🗑️ **ELIMINATE** (Low Priority): {len(matrix[MatrixQuadrant.NOT_URGENT_NOT_IMPORTANT])} items ({len(matrix[MatrixQuadrant.NOT_URGENT_NOT_IMPORTANT])/total_items*100:.1f}%)

**Recommendation**: Focus on DO FIRST items immediately, then schedule IMPORTANT items for systematic implementation.
"""
    
    return summary