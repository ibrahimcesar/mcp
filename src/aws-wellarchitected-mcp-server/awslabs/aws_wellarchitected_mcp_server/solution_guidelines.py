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

"""Solution guidelines for Well-Architected improvements."""

from dataclasses import dataclass
from typing import List

@dataclass
class SolutionGuidelines:
    """Overall guidelines for proposed Well-Architected solutions."""
    
    # SMART Criteria
    smart_principles: List[str] = None
    
    # Solution Characteristics
    ownership_requirements: List[str] = None
    complexity_preferences: List[str] = None
    adaptability_requirements: List[str] = None
    pattern_preferences: List[str] = None
    
    def __post_init__(self):
        if self.smart_principles is None:
            self.smart_principles = [
                "Specific: Solutions must have clear, well-defined outcomes",
                "Measurable: Success criteria must be quantifiable and trackable", 
                "Achievable: Implementation must be realistic with available resources",
                "Relevant: Solutions must address the identified business risk or need",
                "Time-bound: Clear timeline and milestones must be established"
            ]
        
        if self.ownership_requirements is None:
            self.ownership_requirements = [
                "Every solution must have a clearly identified owner",
                "Owner must have authority to implement the solution",
                "Owner must be accountable for solution success",
                "Escalation path must be defined for blocked implementations"
            ]
        
        if self.complexity_preferences is None:
            self.complexity_preferences = [
                "Simple over complex: Always choose simplicity when possible",
                "Break complex solutions into smaller, manageable components",
                "Prefer solutions using existing tools and services",
                "Avoid over-engineering - solve the immediate problem first"
            ]
        
        if self.adaptability_requirements is None:
            self.adaptability_requirements = [
                "Two-way door solutions: Prefer reversible implementations",
                "Solutions should be extensible and designed to evolve",
                "Avoid static solutions that cannot adapt over time",
                "Design for future requirements and changing business needs"
            ]
        
        if self.pattern_preferences is None:
            self.pattern_preferences = [
                "Pattern-based: Use proven, reusable solutions",
                "Leverage AWS Architecture Center patterns and references",
                "Don't reinvent the wheel - reuse existing patterns",
                "Codify solutions for reuse across teams and projects",
                "Share successful patterns with the broader organization"
            ]

def get_solution_guidelines() -> SolutionGuidelines:
    """Get the standard solution guidelines."""
    return SolutionGuidelines()

def format_guidelines() -> str:
    """Format solution guidelines as markdown."""
    guidelines = get_solution_guidelines()
    
    return f"""# Well-Architected Solution Guidelines

## SMART Criteria
All proposed solutions must follow SMART principles:

{chr(10).join(f'- {principle}' for principle in guidelines.smart_principles)}

## Ownership Requirements
{chr(10).join(f'- {req}' for req in guidelines.ownership_requirements)}

## Complexity Management
{chr(10).join(f'- {pref}' for pref in guidelines.complexity_preferences)}

## Adaptability Requirements
{chr(10).join(f'- {req}' for req in guidelines.adaptability_requirements)}

## Pattern-Based Approach
{chr(10).join(f'- {pref}' for pref in guidelines.pattern_preferences)}

## Implementation Philosophy

The output of this analysis will provide a set of risks that have the most impact on your business, and at the same time, they are not too complex to implement. These will be good candidates to start implementing in the first iteration.

### Key Principles:
1. **Impact over Effort**: Focus on high-impact, low-complexity solutions first
2. **Iterative Improvement**: Build momentum with quick wins, then tackle complex items
3. **Business Alignment**: Every solution must address a real business need
4. **Sustainable Change**: Prefer solutions that can evolve with your architecture
5. **Knowledge Sharing**: Document and share successful patterns for reuse
"""

def validate_solution_against_guidelines(solution_description: str) -> List[str]:
    """Validate a solution description against guidelines."""
    guidelines = get_solution_guidelines()
    issues = []
    
    # Check for SMART criteria
    if not any(keyword in solution_description.lower() for keyword in ['specific', 'measure', 'timeline', 'outcome']):
        issues.append("Solution should include specific outcomes and measurable criteria")
    
    # Check for ownership
    if not any(keyword in solution_description.lower() for keyword in ['owner', 'responsible', 'accountable']):
        issues.append("Solution should identify a clear owner or responsible party")
    
    # Check for complexity consideration
    if any(keyword in solution_description.lower() for keyword in ['complex', 'complicated', 'sophisticated']):
        issues.append("Consider if a simpler approach could achieve the same outcome")
    
    # Check for pattern reference
    if not any(keyword in solution_description.lower() for keyword in ['pattern', 'reference', 'aws', 'best practice']):
        issues.append("Consider referencing established patterns or AWS best practices")
    
    return issues