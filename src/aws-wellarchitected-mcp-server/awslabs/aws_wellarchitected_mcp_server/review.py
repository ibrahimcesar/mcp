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

"""AWS Well-Architected Review functionality."""

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional
from .models import Pillar, RiskLevel
from .well_architected_framework import BestPractice

class ReviewPhase(Enum):
    """Review phases based on AWS Well-Architected methodology."""
    LEARN = "learn"
    MEASURE = "measure"
    IMPROVE = "improve"

class ReviewStatus(Enum):
    """Status of a review item."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    NEEDS_ATTENTION = "needs_attention"

@dataclass
class ReviewStep:
    """A step in the Well-Architected review process."""
    id: str
    title: str
    description: str
    phase: ReviewPhase
    pillar: Pillar
    questions: List[str]
    validation_criteria: List[str]
    estimated_effort: str  # e.g., "1-2 hours", "1 day", "1 week"
    dependencies: List[str] = None  # Other step IDs this depends on

@dataclass
class ReviewResult:
    """Result of a review step assessment."""
    step_id: str
    status: ReviewStatus
    risk_level: RiskLevel
    findings: List[str]
    recommendations: List[str]
    notes: Optional[str] = None

@dataclass
class ReviewPlan:
    """Complete review plan with phases."""
    workload_name: str
    phases: Dict[ReviewPhase, List[ReviewStep]]
    estimated_duration: str
    prerequisites: List[str]

class WellArchitectedReview:
    """Main class for conducting Well-Architected reviews."""
    
    def __init__(self, best_practices: Dict[str, BestPractice]):
        self.best_practices = best_practices
        self.review_steps = self._generate_review_steps()
    
    def _generate_review_steps(self) -> List[ReviewStep]:
        """Generate review steps from best practices."""
        steps = []
        
        # Generate measure steps for each pillar
        pillar_steps = self._generate_pillar_steps()
        steps.extend(pillar_steps)
        
        return steps
    
    def _generate_pillar_steps(self) -> List[ReviewStep]:
        """Generate comprehensive assessment steps for each pillar."""
        steps = []
        
        # Learn phase steps - foundational understanding
        learn_steps = [
            ReviewStep(
                id="learn-001",
                title="Understand Business Context",
                description="Gather information about the workload's business purpose, requirements, and constraints",
                phase=ReviewPhase.LEARN,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                questions=[
                    "What is the business purpose of this workload?",
                    "What are the key business requirements?",
                    "What are the compliance and regulatory requirements?",
                    "Who are the key stakeholders?"
                ],
                validation_criteria=[
                    "Business requirements documented",
                    "Stakeholders identified",
                    "Compliance requirements understood"
                ],
                estimated_effort="2-4 hours"
            ),
            ReviewStep(
                id="learn-002",
                title="Document Current Architecture",
                description="Create comprehensive documentation of the current workload architecture",
                phase=ReviewPhase.LEARN,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                questions=[
                    "What is the current architecture design?",
                    "What AWS services are being used?",
                    "How do components interact?",
                    "What are the data flows?"
                ],
                validation_criteria=[
                    "Architecture diagrams created",
                    "Service inventory completed",
                    "Data flows documented"
                ],
                estimated_effort="4-8 hours",
                dependencies=["learn-001"]
            )
        ]
        

        
        # Improve phase steps - implementation of improvements
        improve_steps = [
            ReviewStep(
                id="improve-001",
                title="Create Improvement Plan",
                description="Develop prioritized plan for implementing identified improvements across all assessed pillars",
                phase=ReviewPhase.IMPROVE,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                questions=[
                    "What are the highest priority improvements across all pillars?",
                    "What is the implementation timeline?",
                    "What resources are required?",
                    "How will success be measured?",
                    "What are the dependencies between improvements?"
                ],
                validation_criteria=[
                    "Improvements prioritized by risk and impact",
                    "Implementation timeline defined",
                    "Success metrics established",
                    "Resource requirements identified"
                ],
                estimated_effort="1-2 days"
            ),
            ReviewStep(
                id="improve-002",
                title="Implement High-Priority Improvements",
                description="Execute the most critical improvements identified in the review",
                phase=ReviewPhase.IMPROVE,
                pillar=Pillar.OPERATIONAL_EXCELLENCE,
                questions=[
                    "Have high-risk issues been addressed?",
                    "Are security improvements implemented?",
                    "Is monitoring and alerting enhanced?",
                    "Are operational procedures updated?",
                    "Have architectural changes been validated?"
                ],
                validation_criteria=[
                    "High-risk findings remediated",
                    "Implementation validated",
                    "Documentation updated",
                    "Success metrics tracked"
                ],
                estimated_effort="2-8 weeks",
                dependencies=["improve-001"]
            )
        ]
        
        # Add all pillar assessment steps
        for pillar in Pillar:
            steps.append(self._create_pillar_assessment_step(pillar))
        
        # Add learn and improve steps
        steps.extend(learn_steps)
        steps.extend(improve_steps)
        
        return steps
    
    def _create_pillar_assessment_step(self, pillar: Pillar) -> ReviewStep:
        """Create assessment step for a specific pillar."""
        pillar_configs = {
            Pillar.OPERATIONAL_EXCELLENCE: {
                "title": "Operational Excellence Assessment",
                "description": "Evaluate all operational excellence best practices covering organization, preparation, operations, and evolution",
                "questions": [
                    "How do you determine what your priorities are?",
                    "How do you structure your organization to support your business outcomes?",
                    "How does your organizational culture support your business outcomes?",
                    "How do you design your workload so that you can understand its state?",
                    "How do you reduce defects, ease remediation, and improve flow into production?",
                    "How do you mitigate deployment risks?",
                    "How do you know that you are ready to support a workload?",
                    "How do you understand the health of your workload?",
                    "How do you understand the health of your operations?",
                    "How do you manage workload and operations events?",
                    "How do you evolve operations?"
                ],
                "effort": "2-3 days"
            },
            Pillar.SECURITY: {
                "title": "Security Assessment",
                "description": "Evaluate all security best practices covering foundations, identity, permissions, detection, infrastructure, data, incident response, and application security",
                "questions": [
                    "How do you securely operate your workload?",
                    "How do you manage identities for people and machines?",
                    "How do you manage permissions for people and machines?",
                    "How do you detect and investigate security events?",
                    "How do you protect your network resources?",
                    "How do you protect your compute resources?",
                    "How do you classify your data?",
                    "How do you protect your data at rest?",
                    "How do you protect your data in transit?",
                    "How do you anticipate, respond to, and recover from incidents?",
                    "How do you incorporate and validate the security properties of applications throughout the design, development, and deployment lifecycle?"
                ],
                "effort": "2-3 days"
            },
            Pillar.RELIABILITY: {
                "title": "Reliability Assessment",
                "description": "Evaluate all reliability best practices covering foundations, workload architecture, change management, and failure management",
                "questions": [
                    "How do you manage service quotas and constraints?",
                    "How do you plan your network topology?",
                    "How do you design your workload service architecture?",
                    "How do you design interactions in a distributed system to prevent failures?",
                    "How do you design interactions in a distributed system to mitigate or withstand failures?",
                    "How do you monitor workload resources?",
                    "How do you design your workload to adapt to changes in demand?",
                    "How do you implement change?",
                    "How do you back up data?",
                    "How do you use fault isolation to protect your workload?",
                    "How do you design your workload to withstand component failures?",
                    "How do you test reliability?",
                    "How do you plan for disaster recovery (DR)?"
                ],
                "effort": "2-3 days"
            },
            Pillar.PERFORMANCE_EFFICIENCY: {
                "title": "Performance Efficiency Assessment",
                "description": "Evaluate all performance efficiency best practices covering architecture selection, compute, data management, networking, and process",
                "questions": [
                    "How do you select the best performing architecture?",
                    "How do you select your compute solution?",
                    "How do you select your storage solution?",
                    "How do you select your database solution?",
                    "How do you configure your networking solution?",
                    "How do you evolve your workload to take advantage of new releases?"
                ],
                "effort": "1-2 days"
            },
            Pillar.COST_OPTIMIZATION: {
                "title": "Cost Optimization Assessment",
                "description": "Evaluate all cost optimization best practices covering cloud financial management, expenditure awareness, cost-effective resources, and demand management",
                "questions": [
                    "How do you implement cloud financial management?",
                    "How do you govern usage?",
                    "How do you monitor usage and cost?",
                    "How do you decommission resources?",
                    "How do you evaluate cost when you select services?",
                    "How do you meet cost targets when you select resource type, size and number?",
                    "How do you use pricing models to reduce cost?",
                    "How do you plan for data transfer charges?",
                    "How do you manage demand, and supply resources?",
                    "How do you evaluate new services?"
                ],
                "effort": "1-2 days"
            },
            Pillar.SUSTAINABILITY: {
                "title": "Sustainability Assessment",
                "description": "Evaluate all sustainability best practices covering region selection, demand alignment, software architecture, data management, hardware selection, and process",
                "questions": [
                    "How do you select Regions to support your sustainability goals?",
                    "How do you align your workload to demand?",
                    "How do you take advantage of software and architecture patterns to support your sustainability goals?",
                    "How do you take advantage of data access and usage patterns to support your sustainability goals?",
                    "How do your hardware patterns support your sustainability goals?",
                    "How do your development and deployment processes support your sustainability goals?"
                ],
                "effort": "1-2 days"
            }
        }
        
        config = pillar_configs[pillar]
        return ReviewStep(
            id=f"measure-{pillar.value.lower().replace('_', '-')}",
            title=config["title"],
            description=config["description"],
            phase=ReviewPhase.MEASURE,
            pillar=pillar,
            questions=config["questions"],
            validation_criteria=[
                f"All {pillar.value.replace('_', ' ').lower()} best practices evaluated",
                "Risk levels assessed for each practice",
                "Gaps and improvement opportunities identified",
                "Recommendations prioritized by impact"
            ],
            estimated_effort=config["effort"],
            dependencies=["learn-002"]
        )
    
    def create_review_plan(self, workload_name: str, selected_pillars: List[Pillar] = None) -> ReviewPlan:
        """Create a comprehensive review plan."""
        if selected_pillars is None:
            selected_pillars = list(Pillar)
        
        # Filter steps by selected pillars
        filtered_steps = [step for step in self.review_steps 
                         if step.pillar in selected_pillars]
        
        # Group steps by phase
        phases = {
            ReviewPhase.LEARN: [step for step in filtered_steps if step.phase == ReviewPhase.LEARN],
            ReviewPhase.MEASURE: [step for step in filtered_steps if step.phase == ReviewPhase.MEASURE],
            ReviewPhase.IMPROVE: [step for step in filtered_steps if step.phase == ReviewPhase.IMPROVE]
        }
        
        return ReviewPlan(
            workload_name=workload_name,
            phases=phases,
            estimated_duration="2-4 weeks",
            prerequisites=[
                "Access to workload architecture documentation",
                "Access to AWS accounts and resources",
                "Stakeholder availability for interviews",
                "Technical team availability for assessments"
            ]
        )
    
    def get_pillar_steps(self, pillar: Pillar) -> List[ReviewStep]:
        """Get all review steps for a specific pillar."""
        return [step for step in self.review_steps if step.pillar == pillar]
    
    def get_phase_steps(self, phase: ReviewPhase) -> List[ReviewStep]:
        """Get all review steps for a specific phase."""
        return [step for step in self.review_steps if step.phase == phase]
    
    def validate_step_dependencies(self, step_id: str, completed_steps: List[str]) -> bool:
        """Check if a step's dependencies are satisfied."""
        step = next((s for s in self.review_steps if s.id == step_id), None)
        if not step or not step.dependencies:
            return True
        
        return all(dep in completed_steps for dep in step.dependencies)