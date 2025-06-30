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

"""Well-Architected Framework reviewer implementation."""

import os
from awslabs.aws_wellarchitected_mcp_server.models import (
    ArchitecturalDecisionRecord,
    BestPracticeAssessment,
    BestPracticeStatus,
    ReviewResult,
    ReviewScope,
    RiskLevel,
    TradeOff,
)
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import (
    get_all_best_practices,
    get_best_practices_by_pillar,
)
from loguru import logger
from typing import Dict, List


class WellArchitectedReviewer:
    """Performs Well-Architected Framework reviews."""

    def __init__(self):
        """Initialize the reviewer."""
        self.context = ""
        self.documentation_content = ""

    def analyze_context(self, context: str, documentation_paths: List[str] = None) -> None:
        """Analyze the provided context and documentation."""
        self.context = context
        
        if documentation_paths:
            self.documentation_content = self._read_documentation(documentation_paths)
        
        logger.info(f"Analyzing context: {len(context)} characters")
        if documentation_paths:
            logger.info(f"Documentation paths: {documentation_paths}")

    def _read_documentation(self, paths: List[str]) -> str:
        """Read documentation from provided paths."""
        content = []
        for path in paths:
            try:
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8') as f:
                        content.append(f"=== {path} ===\n{f.read()}\n")
                else:
                    content.append(f"=== {path} (NOT FOUND) ===\n")
            except Exception as e:
                logger.warning(f"Could not read {path}: {e}")
                content.append(f"=== {path} (ERROR: {e}) ===\n")
        
        return "\n".join(content)

    def perform_review(self, scope: ReviewScope) -> ReviewResult:
        """Perform a comprehensive Well-Architected review."""
        logger.info(f"Starting Well-Architected review for pillars: {scope.pillars}")
        
        self.analyze_context(scope.context_description, scope.documentation_paths)
        
        # Get best practices for selected pillars
        if scope.pillars:
            best_practices = []
            for pillar in scope.pillars:
                best_practices.extend(get_best_practices_by_pillar(pillar))
        else:
            best_practices = get_all_best_practices()
        
        assessments = []
        risk_summary = {RiskLevel.LOW: 0, RiskLevel.MEDIUM: 0, RiskLevel.HIGH: 0}
        
        for bp in best_practices:
            assessment = self._assess_best_practice(bp)
            assessments.append(assessment)
            
            if assessment.status != BestPracticeStatus.COMPLIANT:
                risk_summary[assessment.risk_level] += 1
        
        documentation_status = self._assess_documentation_status()
        recommendations = self._generate_high_level_recommendations(assessments)
        
        return ReviewResult(
            scope=scope,
            assessments=assessments,
            overall_risk_summary=risk_summary,
            documentation_status=documentation_status,
            recommendations_summary=recommendations
        )

    def _assess_best_practice(self, best_practice) -> BestPracticeAssessment:
        """Assess a single best practice against the context."""
        # Analyze context for compliance indicators
        context_lower = self.context.lower()
        doc_lower = self.documentation_content.lower()
        combined_content = f"{context_lower} {doc_lower}"
        
        # Simple heuristic-based assessment
        status = self._determine_compliance_status(best_practice, combined_content)
        gaps = self._identify_gaps(best_practice, combined_content, status)
        recommendations = self._generate_recommendations(best_practice, status, gaps)
        current_impl = self._assess_current_implementation(best_practice, combined_content)
        
        # Generate ADR
        adr = self._generate_adr(best_practice, status, gaps, recommendations)
        
        return BestPracticeAssessment(
            best_practice_id=best_practice.id,
            title=best_practice.title,
            pillar=best_practice.pillar,
            status=status,
            risk_level=best_practice.risk_level,
            description=best_practice.description,
            current_implementation=current_impl,
            gaps_identified=gaps,
            recommendations=recommendations,
            adr=adr
        )

    def _determine_compliance_status(self, best_practice, content: str) -> BestPracticeStatus:
        """Determine compliance status based on content analysis."""
        # Check if this practice requires user input
        if hasattr(best_practice, 'requires_user_input') and best_practice.requires_user_input:
            return BestPracticeStatus.NEEDS_REVIEW  # Always requires user input
        
        # Keywords that indicate implementation
        implementation_keywords = {
            "OPS01": ["cloudformation", "cdk", "terraform", "infrastructure as code", "iac"],
            "OPS02": ["cloudwatch", "monitoring", "logs", "alerts", "x-ray", "tracing"],
            "SEC01": ["iam", "roles", "least privilege", "mfa", "multi-factor"],
            "SEC02": ["vpc", "security groups", "waf", "network segmentation"],
            "REL01": ["multi-az", "availability zones", "backup", "disaster recovery"],
            "REL02": ["auto scaling", "scaling groups", "elasticity"],
            "PERF01": ["instance types", "compute optimizer", "right-sizing"],
            "PERF02": ["cache", "elasticache", "cloudfront", "cdn"],
            "COST01": ["cost explorer", "budgets", "cost monitoring"],
            "COST02": ["reserved instances", "savings plans", "ri"],
            "SUS01": ["utilization", "right-size", "serverless", "lambda"],
            "SUS02": ["managed services", "rds", "fargate", "serverless"]
        }
        
        keywords = implementation_keywords.get(best_practice.id, [])
        matches = sum(1 for keyword in keywords if keyword in content)
        
        if matches >= len(keywords) * 0.7:  # 70% of keywords found
            return BestPracticeStatus.COMPLIANT
        elif matches >= len(keywords) * 0.3:  # 30% of keywords found
            return BestPracticeStatus.NEEDS_REVIEW
        else:
            return BestPracticeStatus.NON_COMPLIANT

    def _identify_gaps(self, best_practice, content: str, status: BestPracticeStatus) -> List[str]:
        """Identify gaps in implementation."""
        gaps = []
        
        # Handle practices requiring user input
        if hasattr(best_practice, 'requires_user_input') and best_practice.requires_user_input:
            gaps.extend([
                f"Requires user input to assess {best_practice.title.lower()}",
                "Cannot be evaluated from code/documentation alone",
                "Use 'collect_user_input' tool to provide assessment data"
            ])
            return gaps
        
        if status == BestPracticeStatus.NON_COMPLIANT:
            gaps.append(f"No evidence of {best_practice.title.lower()} implementation found")
            gaps.extend([f"Missing: {guidance}" for guidance in best_practice.implementation_guidance[:2]])
        elif status == BestPracticeStatus.NEEDS_REVIEW:
            gaps.append(f"Partial implementation of {best_practice.title.lower()} detected")
            gaps.append("Implementation may not follow all best practices")
        
        return gaps

    def _generate_recommendations(self, best_practice, status: BestPracticeStatus, gaps: List[str]) -> List[str]:
        """Generate recommendations for improvement."""
        recommendations = []
        
        # Handle practices requiring user input
        if hasattr(best_practice, 'requires_user_input') and best_practice.requires_user_input:
            recommendations.extend([
                f"Use 'collect_user_input' tool for {best_practice.id} assessment",
                "Provide detailed responses to assessment questions",
                "Review generated ADR and implement recommendations"
            ])
            recommendations.extend(best_practice.implementation_guidance)
            return recommendations
        
        if status != BestPracticeStatus.COMPLIANT:
            recommendations.extend(best_practice.implementation_guidance)
            recommendations.append(f"Review and implement {best_practice.title} according to AWS best practices")
        
        return recommendations

    def _assess_current_implementation(self, best_practice, content: str) -> str:
        """Assess the current state of implementation."""
        if not content.strip():
            return "No implementation details provided in context"
        
        # Simple assessment based on content presence
        if len(content) > 100:
            return "Some implementation details found in provided context"
        else:
            return "Limited implementation details available"

    def _generate_adr(self, best_practice, status: BestPracticeStatus, gaps: List[str], recommendations: List[str]) -> ArchitecturalDecisionRecord:
        """Generate an Architecture Decision Record."""
        title = f"ADR: {best_practice.title} Implementation"
        
        if status == BestPracticeStatus.COMPLIANT:
            decision_status = "Accepted"
            decision = f"Implement {best_practice.title} according to AWS Well-Architected best practices"
        else:
            decision_status = "Proposed"
            decision = f"Need to implement {best_practice.title} to meet Well-Architected standards"
        
        context = f"Well-Architected Framework {best_practice.pillar.value} pillar requires: {best_practice.description}"
        
        consequences = [
            f"Improved {best_practice.pillar.value.lower().replace('_', ' ')} posture",
            "Better alignment with AWS best practices",
            "Reduced operational risk"
        ]
        
        trade_offs = [
            TradeOff(
                benefit="Improved system reliability and maintainability",
                cost="Initial implementation effort and potential complexity"
            ),
            TradeOff(
                benefit="Better compliance with industry standards",
                cost="Ongoing operational overhead for maintenance"
            )
        ]
        
        alternatives = [
            "Continue with current implementation (not recommended)",
            "Implement a minimal version of the best practice",
            "Full implementation according to AWS guidelines (recommended)"
        ]
        
        implementation_notes = f"Priority: {best_practice.risk_level.value}. " + " ".join(recommendations[:2])
        
        return ArchitecturalDecisionRecord(
            title=title,
            status=decision_status,
            context=context,
            decision=decision,
            consequences=consequences,
            trade_offs=trade_offs,
            alternatives_considered=alternatives,
            implementation_notes=implementation_notes
        )

    def _assess_documentation_status(self) -> str:
        """Assess the status of documentation."""
        if not self.documentation_content:
            return "No documentation provided for review"
        
        doc_length = len(self.documentation_content)
        if doc_length > 5000:
            return "Comprehensive documentation provided"
        elif doc_length > 1000:
            return "Moderate documentation available"
        else:
            return "Limited documentation provided"

    def _generate_high_level_recommendations(self, assessments: List[BestPracticeAssessment]) -> List[str]:
        """Generate high-level recommendations based on all assessments."""
        recommendations = []
        
        high_risk_count = sum(1 for a in assessments if a.risk_level == RiskLevel.HIGH and a.status != BestPracticeStatus.COMPLIANT)
        medium_risk_count = sum(1 for a in assessments if a.risk_level == RiskLevel.MEDIUM and a.status != BestPracticeStatus.COMPLIANT)
        
        if high_risk_count > 0:
            recommendations.append(f"Address {high_risk_count} high-risk items immediately")
        
        if medium_risk_count > 0:
            recommendations.append(f"Plan to address {medium_risk_count} medium-risk items")
        
        recommendations.append("Implement comprehensive monitoring and logging")
        recommendations.append("Establish regular Well-Architected reviews")
        recommendations.append("Document architectural decisions and trade-offs")
        
        return recommendations