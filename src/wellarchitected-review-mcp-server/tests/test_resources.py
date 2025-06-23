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

"""Tests for the resources module."""

import pytest
from unittest.mock import Mock

from awslabs.wellarchitected_review_mcp_server.core.resources import (
    get_pillar_details,
    get_lens_details,
    get_best_practice,
    PILLARS,
    LENSES,
    BEST_PRACTICES,
)


def test_get_pillar_details_valid_pillar():
    """Test getting details for a valid pillar."""
    ctx = Mock()
    result = get_pillar_details(ctx, pillar_name="operational-excellence")
    
    assert "pillar" in result
    assert result["pillar"] == PILLARS["operational-excellence"]
    assert "related_practices" in result
    assert isinstance(result["related_practices"], dict)


def test_get_pillar_details_invalid_pillar():
    """Test getting details for an invalid pillar."""
    ctx = Mock()
    result = get_pillar_details(ctx, pillar_name="nonexistent-pillar")
    
    assert "error" in result
    assert "available_pillars" in result
    assert isinstance(result["available_pillars"], list)


def test_get_lens_details_valid_lens():
    """Test getting details for a valid lens."""
    ctx = Mock()
    result = get_lens_details(ctx, lens_name="serverless")
    
    assert "lens" in result
    assert result["lens"] == LENSES["serverless"]
    assert "pillars" in result
    assert isinstance(result["pillars"], dict)


def test_get_lens_details_invalid_lens():
    """Test getting details for an invalid lens."""
    ctx = Mock()
    result = get_lens_details(ctx, lens_name="nonexistent-lens")
    
    assert "error" in result
    assert "available_lenses" in result
    assert isinstance(result["available_lenses"], list)


def test_get_best_practice_valid_practice():
    """Test getting details for a valid best practice."""
    ctx = Mock()
    result = get_best_practice(ctx, practice_id="OPS1")
    
    assert "practice" in result
    assert result["practice"] == BEST_PRACTICES["OPS1"]
    assert "pillar" in result


def test_get_best_practice_invalid_practice():
    """Test getting details for an invalid best practice."""
    ctx = Mock()
    result = get_best_practice(ctx, practice_id="NONEXISTENT1")
    
    assert "error" in result
    assert "available_practices" in result
    assert isinstance(result["available_practices"], list)
