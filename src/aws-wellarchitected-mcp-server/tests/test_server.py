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

"""Tests for AWS Well-Architected MCP Server."""

import pytest
from awslabs.aws_wellarchitected_mcp_server.models import Pillar, ReviewScope
from awslabs.aws_wellarchitected_mcp_server.reviewer import WellArchitectedReviewer
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import (
    get_all_best_practices,
    get_best_practices_by_pillar,
)


class TestWellArchitectedFramework:
    """Test Well-Architected Framework functionality."""

    def test_get_all_best_practices(self):
        """Test getting all best practices."""
        practices = get_all_best_practices()
        assert len(practices) > 0
        assert all(hasattr(bp, 'id') for bp in practices)
        assert all(hasattr(bp, 'title') for bp in practices)
        assert all(hasattr(bp, 'pillar') for bp in practices)

    def test_get_best_practices_by_pillar(self):
        """Test getting best practices by pillar."""
        security_practices = get_best_practices_by_pillar(Pillar.SECURITY)
        assert len(security_practices) > 0
        assert all(bp.pillar == Pillar.SECURITY for bp in security_practices)

    def test_all_pillars_have_practices(self):
        """Test that all pillars have associated best practices."""
        for pillar in Pillar:
            practices = get_best_practices_by_pillar(pillar)
            assert len(practices) > 0, f"No practices found for pillar {pillar}"


class TestWellArchitectedReviewer:
    """Test Well-Architected Reviewer functionality."""

    def test_reviewer_initialization(self):
        """Test reviewer initialization."""
        reviewer = WellArchitectedReviewer()
        assert reviewer.context == ""
        assert reviewer.documentation_content == ""

    def test_analyze_context(self):
        """Test context analysis."""
        reviewer = WellArchitectedReviewer()
        test_context = "Test application with CloudFormation and monitoring"
        reviewer.analyze_context(test_context)
        assert reviewer.context == test_context

    def test_perform_review_all_pillars(self):
        """Test performing review for all pillars."""
        reviewer = WellArchitectedReviewer()
        scope = ReviewScope(
            pillars=[],  # Empty means all pillars
            context_description="Test e-commerce application with web tier and database"
        )
        
        result = reviewer.perform_review(scope)
        
        assert result.scope == scope
        assert len(result.assessments) > 0
        assert 'HIGH' in result.overall_risk_summary
        assert 'MEDIUM' in result.overall_risk_summary
        assert 'LOW' in result.overall_risk_summary

    def test_perform_review_specific_pillars(self):
        """Test performing review for specific pillars."""
        reviewer = WellArchitectedReviewer()
        scope = ReviewScope(
            pillars=[Pillar.SECURITY, Pillar.RELIABILITY],
            context_description="Microservices application"
        )
        
        result = reviewer.perform_review(scope)
        
        assert len(result.assessments) > 0
        # All assessments should be from the specified pillars
        pillar_values = {assessment.pillar for assessment in result.assessments}
        assert pillar_values.issubset({Pillar.SECURITY, Pillar.RELIABILITY})


class TestModels:
    """Test data models."""

    def test_pillar_enum(self):
        """Test Pillar enum values."""
        expected_pillars = {
            "OPERATIONAL_EXCELLENCE",
            "SECURITY", 
            "RELIABILITY",
            "PERFORMANCE_EFFICIENCY",
            "COST_OPTIMIZATION",
            "SUSTAINABILITY"
        }
        actual_pillars = {pillar.value for pillar in Pillar}
        assert actual_pillars == expected_pillars

    def test_review_scope_creation(self):
        """Test ReviewScope model creation."""
        scope = ReviewScope(
            pillars=[Pillar.SECURITY],
            context_description="Test application",
            documentation_paths=["./test.md"]
        )
        
        assert scope.pillars == [Pillar.SECURITY]
        assert scope.context_description == "Test application"
        assert scope.documentation_paths == ["./test.md"]


if __name__ == "__main__":
    pytest.main([__file__])