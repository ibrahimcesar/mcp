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

"""Review templates and checklists for Well-Architected reviews."""

from typing import Dict, List
from .models import Pillar
from .review import ReviewStep, ReviewPhase

class ReviewTemplates:
    """Templates for different types of Well-Architected reviews."""
    
    @staticmethod
    def get_comprehensive_steps() -> List[ReviewStep]:
        """Get comprehensive review steps covering all pillars."""
        return [
            # LEARN PHASE - Foundation
            ReviewStep(
                id="learn-foundation-001",
                title="Business Context Discovery",
                description="Understand business drivers, requirements, and success criteria",
                phase=ReviewPhase.LEARN,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                best_practice_id="OPS01-BP01",
                questions=[
                    "What business problem does this workload solve?",
                    "What are the key performance indicators (KPIs)?",
                    "What are the availability requirements?",
                    "What compliance standards must be met?"
                ],
                validation_criteria=[
                    "Business requirements documented",
                    "Success metrics defined",
                    "Compliance requirements identified"
                ],
                estimated_effort="2-4 hours"
            ),
            
            # MEASURE PHASE - Assessment by Pillar
            ReviewStep(
                id="measure-ops-001",
                title="Operational Excellence Assessment",
                description="Evaluate operational practices and procedures",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                best_practice_id="OPS01-BP01",
                questions=[
                    "Are operational procedures documented and tested?",
                    "Is infrastructure managed as code?",
                    "Are deployments automated and reversible?",
                    "Is operational health monitored and alerted?"
                ],
                validation_criteria=[
                    "Runbooks and procedures exist",
                    "IaC implementation verified",
                    "CI/CD pipeline assessed"
                ],
                estimated_effort="1 day"
            ),
            
            ReviewStep(
                id="measure-security-001",
                title="Security Posture Assessment",
                description="Comprehensive security evaluation across all layers",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.SECURITY,
                best_practice_id="SEC01-BP01",
                questions=[
                    "Is identity and access management properly implemented?",
                    "Are security controls automated and monitored?",
                    "Is data encrypted at rest and in transit?",
                    "Are security incidents detected and responded to?"
                ],
                validation_criteria=[
                    "IAM policies reviewed",
                    "Encryption status verified",
                    "Security monitoring confirmed"
                ],
                estimated_effort="1-2 days"
            ),
            
            # IMPROVE PHASE - Action Planning
            ReviewStep(
                id="improve-plan-001",
                title="Risk-Based Improvement Planning",
                description="Create prioritized improvement plan based on risk assessment",
                phase=ReviewPhase.IMPROVE,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                best_practice_id="OPS01-BP03",
                questions=[
                    "What are the highest risk findings?",
                    "What improvements provide the most value?",
                    "What is the implementation sequence?",
                    "How will progress be tracked?"
                ],
                validation_criteria=[
                    "Risks prioritized by impact and likelihood",
                    "Implementation roadmap created",
                    "Success metrics defined"
                ],
                estimated_effort="4-8 hours"
            )
        ]
    
    @staticmethod
    def get_security_focused_steps() -> List[ReviewStep]:
        """Get security-focused review steps."""
        return [
            ReviewStep(
                id="sec-identity-001",
                title="Identity and Access Management Review",
                description="Assess IAM implementation and access controls",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.SECURITY,
                best_practice_id="SEC02-BP01",
                questions=[
                    "Are users authenticated with strong mechanisms?",
                    "Is least privilege access implemented?",
                    "Are credentials rotated regularly?",
                    "Is access reviewed periodically?"
                ],
                validation_criteria=[
                    "MFA enabled for all users",
                    "IAM policies follow least privilege",
                    "Access review process exists"
                ],
                estimated_effort="4-6 hours"
            ),
            
            ReviewStep(
                id="sec-data-001",
                title="Data Protection Assessment",
                description="Evaluate data classification and protection measures",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.SECURITY,
                best_practice_id="SEC07-BP01",
                questions=[
                    "Is data classified by sensitivity?",
                    "Is encryption implemented appropriately?",
                    "Are data access patterns monitored?",
                    "Is data backup and recovery tested?"
                ],
                validation_criteria=[
                    "Data classification scheme exists",
                    "Encryption at rest and in transit verified",
                    "Access logging enabled"
                ],
                estimated_effort="6-8 hours"
            )
        ]
    
    @staticmethod
    def get_cost_optimization_steps() -> List[ReviewStep]:
        """Get cost optimization focused review steps."""
        return [
            ReviewStep(
                id="cost-visibility-001",
                title="Cost Visibility and Governance",
                description="Assess cost monitoring and governance practices",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.COST_OPTIMIZATION,
                best_practice_id="COST01-BP01",
                questions=[
                    "Is cost ownership clearly defined?",
                    "Are costs monitored and reported regularly?",
                    "Are budgets and alerts configured?",
                    "Is cost allocation implemented?"
                ],
                validation_criteria=[
                    "Cost center ownership defined",
                    "Regular cost reporting exists",
                    "Budget alerts configured"
                ],
                estimated_effort="4-6 hours"
            ),
            
            ReviewStep(
                id="cost-optimization-001",
                title="Resource Optimization Assessment",
                description="Evaluate resource utilization and optimization opportunities",
                phase=ReviewPhase.MEASURE,
                pillar=Pillar.COST_OPTIMIZATION,
                best_practice_id="COST05-BP01",
                questions=[
                    "Are resources right-sized for workload needs?",
                    "Are Reserved Instances or Savings Plans used?",
                    "Are unused resources identified and removed?",
                    "Is auto-scaling implemented where appropriate?"
                ],
                validation_criteria=[
                    "Resource utilization analyzed",
                    "Commitment discounts evaluated",
                    "Unused resources identified"
                ],
                estimated_effort="6-8 hours"
            )
        ]

def format_review_plan_markdown(plan) -> str:
    """Format a review plan as markdown."""
    markdown = f"""# Well-Architected Review Plan: {plan.workload_name}

## Overview
- **Estimated Duration**: {plan.estimated_duration}
- **Phases**: {len(plan.phases)} phases
- **Total Steps**: {sum(len(steps) for steps in plan.phases.values())}

## Prerequisites
{chr(10).join(f'- {prereq}' for prereq in plan.prerequisites)}

"""
    
    for phase, steps in plan.phases.items():
        markdown += f"""## Phase {phase.value.title()}
{chr(10).join(f'### {step.title}' + chr(10) + f'**Pillar**: {step.pillar.value}' + chr(10) + f'**Effort**: {step.estimated_effort}' + chr(10) + step.description + chr(10) for step in steps)}
"""
    
    return markdown