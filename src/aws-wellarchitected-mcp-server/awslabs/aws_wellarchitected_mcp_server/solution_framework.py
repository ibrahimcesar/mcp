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

"""Solution framework for Well-Architected improvements with SMART criteria."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from .models import RiskLevel, Pillar
from .well_architected_framework import BestPractice

class ComplexityLevel(Enum):
    """Implementation complexity levels."""
    LOW = "low"        # 1-2 weeks
    MEDIUM = "medium"  # 1-2 months  
    HIGH = "high"      # 3+ months

class ImpactLevel(Enum):
    """Business impact levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class SMARTSolution:
    """SMART solution for a Well-Architected best practice."""
    best_practice_id: str
    
    # SMART Criteria
    specific: str           # Specific outcome
    measurable: str         # How to measure success
    achievable: str         # Why it's achievable
    relevant: str           # Relevance to business
    time_bound: str         # Timeline
    
    # Solution Characteristics
    owner: str              # Who owns implementation
    complexity: ComplexityLevel
    business_impact: ImpactLevel
    is_two_way_door: bool   # Can be evolved/reversed
    pattern_reference: Optional[str] = None  # AWS pattern/reference
    
    # Implementation Details
    prerequisites: List[str] = None
    success_criteria: List[str] = None
    rollback_plan: str = ""

class SolutionFramework:
    """Framework for creating SMART solutions from Well-Architected findings."""
    
    def __init__(self, best_practices: dict):
        self.best_practices = best_practices
    
    def generate_smart_solution(self, bp: BestPractice, context: dict = None, guidelines: 'SolutionGuidelines' = None) -> SMARTSolution:
        """Generate SMART solution for a best practice following guidelines."""
        context = context or {}
        
        # Apply guidelines if provided
        if guidelines:
            context['guidelines'] = guidelines
        
        return SMARTSolution(
            best_practice_id=bp.id,
            specific=self._generate_specific_outcome(bp),
            measurable=self._generate_measurable_criteria(bp),
            achievable=self._generate_achievable_rationale(bp),
            relevant=self._generate_relevance_statement(bp),
            time_bound=self._generate_timeline(bp),
            owner=context.get('default_owner', 'Architecture Team'),
            complexity=self._assess_complexity(bp),
            business_impact=self._assess_business_impact(bp),
            is_two_way_door=self._assess_reversibility(bp),
            pattern_reference=self._get_pattern_reference(bp),
            prerequisites=self._identify_prerequisites(bp),
            success_criteria=self._define_success_criteria(bp),
            rollback_plan=self._create_rollback_plan(bp)
        )
    
    def _generate_specific_outcome(self, bp: BestPractice) -> str:
        """Generate specific outcome statement."""
        outcomes = {
            'SEC': f"Implement {bp.title.lower()} to enhance security posture",
            'REL': f"Establish {bp.title.lower()} to improve system reliability", 
            'PERF': f"Optimize {bp.title.lower()} to enhance performance",
            'COST': f"Implement {bp.title.lower()} to reduce costs",
            'OPS': f"Establish {bp.title.lower()} to improve operations",
            'SUS': f"Implement {bp.title.lower()} to reduce environmental impact"
        }
        
        prefix = bp.id[:3]
        return outcomes.get(prefix, f"Implement {bp.title.lower()}")
    
    def _generate_measurable_criteria(self, bp: BestPractice) -> str:
        """Generate measurable success criteria."""
        if bp.pillar == Pillar.SECURITY:
            return "Security controls implemented and validated, compliance score improved"
        elif bp.pillar == Pillar.RELIABILITY:
            return "System availability metrics improved, MTTR reduced"
        elif bp.pillar == Pillar.PERFORMANCE_EFFICIENCY:
            return "Performance benchmarks met, response times improved"
        elif bp.pillar == Pillar.COST_OPTIMIZATION:
            return "Cost reduction achieved, utilization metrics improved"
        elif bp.pillar == Pillar.OPERATIONAL_EXCELLENCE:
            return "Operational metrics improved, incident response time reduced"
        else:
            return "Implementation validated against best practice criteria"
    
    def _generate_achievable_rationale(self, bp: BestPractice) -> str:
        """Generate achievable rationale."""
        complexity = self._assess_complexity(bp)
        
        if complexity == ComplexityLevel.LOW:
            return "Low complexity implementation using existing AWS services and tools"
        elif complexity == ComplexityLevel.MEDIUM:
            return "Moderate effort required with standard AWS patterns and practices"
        else:
            return "Complex but achievable with proper planning and phased approach"
    
    def _generate_relevance_statement(self, bp: BestPractice) -> str:
        """Generate business relevance statement."""
        relevance_map = {
            Pillar.SECURITY: "Critical for protecting business data and maintaining customer trust",
            Pillar.RELIABILITY: "Essential for business continuity and customer satisfaction",
            Pillar.PERFORMANCE_EFFICIENCY: "Important for user experience and operational efficiency",
            Pillar.COST_OPTIMIZATION: "Directly impacts bottom line and resource efficiency",
            Pillar.OPERATIONAL_EXCELLENCE: "Fundamental for scalable and maintainable operations",
            Pillar.SUSTAINABILITY: "Supports corporate sustainability goals and compliance"
        }
        
        return relevance_map.get(bp.pillar, "Supports overall architectural excellence")
    
    def _generate_timeline(self, bp: BestPractice) -> str:
        """Generate implementation timeline."""
        complexity = self._assess_complexity(bp)
        
        timelines = {
            ComplexityLevel.LOW: "2-4 weeks",
            ComplexityLevel.MEDIUM: "6-12 weeks", 
            ComplexityLevel.HIGH: "3-6 months"
        }
        
        return timelines[complexity]
    
    def _assess_complexity(self, bp: BestPractice) -> ComplexityLevel:
        """Assess implementation complexity."""
        # Foundational practices are typically simpler
        if bp.id.endswith(('-BP01', '-BP02')):
            return ComplexityLevel.LOW
        
        # High risk items might be more complex
        if bp.risk_level == RiskLevel.HIGH:
            return ComplexityLevel.MEDIUM
        
        # Practices with many relationships might be complex
        if len(bp.related_best_practices or []) > 3:
            return ComplexityLevel.MEDIUM
        
        return ComplexityLevel.LOW
    
    def _assess_business_impact(self, bp: BestPractice) -> ImpactLevel:
        """Assess business impact level."""
        if bp.risk_level == RiskLevel.HIGH:
            return ImpactLevel.HIGH
        elif bp.pillar in [Pillar.SECURITY, Pillar.RELIABILITY]:
            return ImpactLevel.HIGH
        elif bp.risk_level == RiskLevel.MEDIUM:
            return ImpactLevel.MEDIUM
        else:
            return ImpactLevel.LOW
    
    def _assess_reversibility(self, bp: BestPractice) -> bool:
        """Assess if solution is a two-way door (reversible)."""
        # Most AWS service configurations are reversible
        # Architectural changes might be less reversible
        if 'architecture' in bp.title.lower() or 'design' in bp.title.lower():
            return False
        return True
    
    def _get_pattern_reference(self, bp: BestPractice) -> Optional[str]:
        """Get AWS pattern reference if available."""
        # Map common patterns to AWS Architecture Center
        pattern_map = {
            'multi-az': 'https://aws.amazon.com/architecture/reference-architecture-diagrams/',
            'backup': 'https://aws.amazon.com/architecture/backup-recovery/',
            'monitoring': 'https://aws.amazon.com/architecture/well-architected/',
            'security': 'https://aws.amazon.com/architecture/security-identity-compliance/',
            'cost': 'https://aws.amazon.com/architecture/cost-optimization/'
        }
        
        title_lower = bp.title.lower()
        for keyword, url in pattern_map.items():
            if keyword in title_lower:
                return url
        
        return "https://aws.amazon.com/architecture/"
    
    def _identify_prerequisites(self, bp: BestPractice) -> List[str]:
        """Identify implementation prerequisites."""
        prerequisites = ["AWS account access", "Appropriate IAM permissions"]
        
        if bp.pillar == Pillar.SECURITY:
            prerequisites.append("Security team approval")
        elif bp.pillar == Pillar.COST_OPTIMIZATION:
            prerequisites.append("Budget approval")
        
        return prerequisites
    
    def _define_success_criteria(self, bp: BestPractice) -> List[str]:
        """Define success criteria."""
        return [
            "Implementation completed as designed",
            "All tests passed successfully", 
            "Documentation updated",
            "Team trained on new processes"
        ]
    
    def _create_rollback_plan(self, bp: BestPractice) -> str:
        """Create rollback plan."""
        if self._assess_reversibility(bp):
            return "Configuration can be reverted through AWS console or IaC templates"
        else:
            return "Rollback requires careful planning - document current state before changes"

def format_smart_solutions(solutions: List[SMARTSolution]) -> str:
    """Format SMART solutions as implementation guide."""
    if not solutions:
        return "No solutions to display."
    
    guide = "# SMART Implementation Solutions\n\n"
    
    for i, solution in enumerate(solutions, 1):
        guide += f"""## {i}. {solution.best_practice_id}

### SMART Criteria
- **Specific**: {solution.specific}
- **Measurable**: {solution.measurable}  
- **Achievable**: {solution.achievable}
- **Relevant**: {solution.relevant}
- **Time-bound**: {solution.time_bound}

### Solution Characteristics
- **Owner**: {solution.owner}
- **Complexity**: {solution.complexity.value.title()}
- **Business Impact**: {solution.business_impact.value.title()}
- **Two-way Door**: {'Yes' if solution.is_two_way_door else 'No'}
- **Pattern Reference**: {solution.pattern_reference or 'N/A'}

### Implementation Details
**Prerequisites**:
{chr(10).join(f'- {prereq}' for prereq in solution.prerequisites or [])}

**Success Criteria**:
{chr(10).join(f'- {criteria}' for criteria in solution.success_criteria or [])}

**Rollback Plan**: {solution.rollback_plan}

---

"""
    
    return guide

def get_quick_wins(solutions: List[SMARTSolution]) -> List[SMARTSolution]:
    """Filter solutions for quick wins (high impact, low complexity)."""
    return [
        solution for solution in solutions
        if solution.complexity == ComplexityLevel.LOW 
        and solution.business_impact in [ImpactLevel.MEDIUM, ImpactLevel.HIGH]
    ]