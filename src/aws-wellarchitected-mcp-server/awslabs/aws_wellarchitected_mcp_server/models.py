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

"""Data models for AWS Well-Architected MCP Server."""

from enum import Enum
from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class RiskLevel(str, Enum):
    """Risk levels for Well-Architected best practices."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Pillar(str, Enum):
    """AWS Well-Architected Framework pillars."""
    OPERATIONAL_EXCELLENCE = "OPERATIONAL_EXCELLENCE"
    SECURITY = "SECURITY"
    RELIABILITY = "RELIABILITY"
    PERFORMANCE_EFFICIENCY = "PERFORMANCE_EFFICIENCY"
    COST_OPTIMIZATION = "COST_OPTIMIZATION"
    SUSTAINABILITY = "SUSTAINABILITY"


class BestPracticeStatus(str, Enum):
    """Status of a best practice implementation."""
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NEEDS_REVIEW = "NEEDS_REVIEW"


class TradeOff(BaseModel):
    """Represents a trade-off in architectural decisions."""
    benefit: str = Field(description="The benefit of this approach")
    cost: str = Field(description="The cost or drawback of this approach")


class ArchitecturalDecisionRecord(BaseModel):
    """Architecture Decision Record for Well-Architected best practices."""
    title: str = Field(description="Title of the ADR")
    status: str = Field(description="Status of the decision (Proposed, Accepted, Deprecated)")
    context: str = Field(description="Context and problem statement")
    decision: str = Field(description="The architectural decision made")
    consequences: List[str] = Field(description="Consequences of this decision")
    trade_offs: List[TradeOff] = Field(description="Trade-offs considered")
    alternatives_considered: List[str] = Field(description="Alternative approaches considered")
    implementation_notes: Optional[str] = Field(description="Implementation guidance", default=None)


class BestPracticeAssessment(BaseModel):
    """Assessment of a Well-Architected best practice."""
    best_practice_id: str = Field(description="Unique identifier for the best practice")
    title: str = Field(description="Title of the best practice")
    pillar: Pillar = Field(description="Well-Architected pillar")
    status: BestPracticeStatus = Field(description="Current implementation status")
    risk_level: RiskLevel = Field(description="Risk level if not implemented")
    description: str = Field(description="Description of the best practice")
    current_implementation: str = Field(description="Current state of implementation")
    gaps_identified: List[str] = Field(description="Identified gaps or issues")
    recommendations: List[str] = Field(description="Recommendations for improvement")
    adr: ArchitecturalDecisionRecord = Field(description="Associated ADR")


class ReviewScope(BaseModel):
    """Scope configuration for Well-Architected review."""
    pillars: List[Pillar] = Field(description="Pillars to include in the review")
    context_description: str = Field(description="Description of the system/workload being reviewed")
    documentation_paths: Optional[List[str]] = Field(description="Paths to relevant documentation", default=None)


class ReviewResult(BaseModel):
    """Result of a Well-Architected review."""
    scope: ReviewScope = Field(description="Review scope configuration")
    assessments: List[BestPracticeAssessment] = Field(description="Best practice assessments")
    overall_risk_summary: Dict[RiskLevel, int] = Field(description="Summary of risk levels")
    documentation_status: str = Field(description="Status of documentation review")
    recommendations_summary: List[str] = Field(description="High-level recommendations")