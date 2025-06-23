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

"""Tool implementations for the AWS Well-Architected Review MCP server."""

import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from mcp.context import Context

from .resources import PILLARS, LENSES, BEST_PRACTICES


logger = logging.getLogger(__name__)


class ArchitectureReviewRequest(BaseModel):
    """Model for architecture review request."""

    architecture_description: str = Field(
        ..., description="Description of the architecture to review"
    )
    services: List[str] = Field(
        ..., description="List of AWS services used in the architecture"
    )
    lens: Optional[str] = Field(
        default="well-architected", 
        description="Well-Architected lens to apply (default: well-architected)"
    )
    pillars: Optional[List[str]] = Field(
        default=None,
        description="List of specific pillars to focus on. If not provided, all pillars from the selected lens will be used."
    )


def get_wellarchitected_pillars(ctx: Context) -> Dict[str, Any]:
    """Get list of available Well-Architected pillars.
    
    Args:
        ctx: The context object.
    
    Returns:
        Dictionary with list of pillars and their details.
    """
    return {
        "pillars": PILLARS,
    }


def get_wellarchitected_lens(
    ctx: Context,
    *,
    lens_name: str = "well-architected"
) -> Dict[str, Any]:
    """Get Well-Architected lens details.
    
    Args:
        ctx: The context object.
        lens_name: The name of the lens to get (default: "well-architected").
    
    Returns:
        Dictionary with lens details.
    """
    lens_name = lens_name.lower()
    if lens_name not in LENSES:
        return {
            "error": f"Lens '{lens_name}' not found",
            "available_lenses": list(LENSES.keys())
        }
    
    lens = LENSES[lens_name]
    
    return {
        "lens": lens,
        "pillars": [PILLARS.get(pillar, {}) for pillar in lens["pillars"]]
    }


def review_architecture(
    ctx: Context,
    *,
    architecture_description: str,
    services: List[str],
    lens: str = "well-architected",
    pillars: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Review an architecture based on AWS Well-Architected Framework.
    
    Args:
        ctx: The context object.
        architecture_description: Description of the architecture to review.
        services: List of AWS services used in the architecture.
        lens: Well-Architected lens to apply (default: "well-architected").
        pillars: List of specific pillars to focus on.
    
    Returns:
        Dictionary with review results.
    """
    lens = lens.lower()
    if lens not in LENSES:
        return {
            "error": f"Lens '{lens}' not found",
            "available_lenses": list(LENSES.keys())
        }
    
    # Determine which pillars to include in the review
    lens_data = LENSES[lens]
    lens_pillars = lens_data["pillars"]
    
    if pillars:
        # Filter to only include the requested pillars that are valid for this lens
        review_pillars = [p.lower() for p in pillars if p.lower() in lens_pillars]
        if not review_pillars:
            return {
                "error": f"None of the requested pillars are valid for the '{lens}' lens",
                "available_pillars_for_lens": lens_pillars
            }
    else:
        # Use all pillars for this lens
        review_pillars = lens_pillars
    
    # Find best practices relevant to each pillar and service
    findings_by_pillar = {}
    for pillar_name in review_pillars:
        pillar = PILLARS.get(pillar_name, {})
        
        # Find best practices for this pillar
        pillar_practices = {
            id: practice for id, practice in BEST_PRACTICES.items()
            if practice.get("pillar") == pillar_name
        }
        
        findings_by_pillar[pillar_name] = {
            "pillar": pillar,
            "practices": pillar_practices,
            "findings": []  # This would be populated with actual analysis in a real implementation
        }
        
    # Generate a summary with recommendations
    recommendations = {
        "high_priority": [
            "Implement AWS Well-Architected Tool for continuous assessment",
            "Document your workload architecture using architectural diagrams",
            "Regularly review your architecture against the latest Well-Architected guidance"
        ],
        "medium_priority": [
            "Schedule quarterly Well-Architected reviews",
            "Implement automated checks for critical best practices",
            "Create a roadmap for addressing identified gaps"
        ],
        "low_priority": [
            "Train your team on Well-Architected Framework concepts",
            "Establish architectural decision records",
            "Implement a feedback loop for continuous improvement"
        ]
    }
    
    return {
        "review_summary": {
            "lens": lens_data,
            "services_reviewed": services,
            "pillars_reviewed": [PILLARS[p] for p in review_pillars],
        },
        "findings": findings_by_pillar,
        "recommendations": recommendations
    }


def get_wellarchitected_guidance(
    ctx: Context,
    *,
    service: Optional[str] = None,
    pillar: Optional[str] = None,
    practice_id: Optional[str] = None
) -> Dict[str, Any]:
    """Get Well-Architected guidance for specific services, pillars, or best practices.
    
    Args:
        ctx: The context object.
        service: Specific AWS service to get guidance for.
        pillar: Specific pillar to get guidance for.
        practice_id: Specific best practice ID to get guidance for.
    
    Returns:
        Dictionary with guidance information.
    """
    if not any([service, pillar, practice_id]):
        return {
            "error": "At least one of service, pillar, or practice_id must be provided",
            "available_pillars": list(PILLARS.keys()),
            "available_practices": list(BEST_PRACTICES.keys())
        }
    
    results = {}
    
    # Get guidance for a specific practice
    if practice_id:
        practice_id = practice_id.upper()
        if practice_id not in BEST_PRACTICES:
            return {
                "error": f"Best practice '{practice_id}' not found",
                "available_practices": list(BEST_PRACTICES.keys())
            }
        
        practice = BEST_PRACTICES[practice_id]
        practice_pillar = practice.get("pillar", "")
        pillar_info = PILLARS.get(practice_pillar, {})
        
        results["practice"] = practice
        results["pillar"] = pillar_info
    
    # Get guidance for a specific pillar
    elif pillar:
        pillar = pillar.lower()
        if pillar not in PILLARS:
            return {
                "error": f"Pillar '{pillar}' not found",
                "available_pillars": list(PILLARS.keys())
            }
        
        pillar_info = PILLARS[pillar]
        # Find practices for this pillar
        pillar_practices = {
            id: practice for id, practice in BEST_PRACTICES.items()
            if practice.get("pillar") == pillar
        }
        
        results["pillar"] = pillar_info
        results["practices"] = pillar_practices
    
    # Get guidance for a specific service
    elif service:
        # This would be populated with service-specific guidance in a real implementation
        results["service"] = service
        results["service_guidance"] = {
            "message": f"Guidance for {service} would be provided here in a real implementation"
        }
    
    return results
