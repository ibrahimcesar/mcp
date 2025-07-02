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

"""AWS Well-Architected MCP Server implementation."""

import argparse
from awslabs.aws_wellarchitected_mcp_server.adr_generator import ADRGenerator
from awslabs.aws_wellarchitected_mcp_server.models import Pillar, ReviewScope
from awslabs.aws_wellarchitected_mcp_server.reviewer import WellArchitectedReviewer
from awslabs.aws_wellarchitected_mcp_server.display_utils import format_risk_level, format_pillar, format_pillar_simple
from loguru import logger
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from typing import Dict, List, Optional


mcp = FastMCP(
    'awslabs.aws-wellarchitected-mcp-server',
    instructions="""
    # AWS Well-Architected MCP Server

    This MCP server provides comprehensive AWS Well-Architected Framework reviews:

    ## Core Features:
    1. **Well-Architected Reviews**: Analyze systems against all 6 pillars
    2. **Best Practice Assessment**: Evaluate compliance with AWS best practices  
    3. **Architecture Decision Records**: Generate ADRs for each best practice
    4. **Risk Assessment**: Identify and prioritize risks (High/Medium/Low)
    5. **Documentation Analysis**: Review and validate documentation currency
    6. **Implementation Guidance**: Provide specific recommendations and fixes

    ## Six Pillars Covered:
    - **Operational Excellence**: Infrastructure as Code, Monitoring, Automation
    - **Security**: Identity, Data Protection, Infrastructure Security
    - **Reliability**: Fault Tolerance, Recovery, Scaling
    - **Performance Efficiency**: Resource Selection, Monitoring, Trade-offs
    - **Cost Optimization**: Cost-Effective Resources, Matching Supply/Demand
    - **Sustainability**: Environmental Impact, Resource Efficiency

    ## Usage:
    Use the `review` command with context about your architecture and optionally specify:
    - Which pillars to focus on
    - Documentation paths to analyze
    - Output directory for ADRs

    The server will analyze each best practice, generate ADRs with trade-offs, and ask if you want to implement fixes.
    """,
    dependencies=['pydantic', 'loguru'],
)


@mcp.tool()
async def review(
    context: str = Field(description="Description of the system/workload to review"),
    pillars: Optional[List[str]] = Field(
        description="Specific pillars to review (OPERATIONAL_EXCELLENCE, SECURITY, RELIABILITY, PERFORMANCE_EFFICIENCY, COST_OPTIMIZATION, SUSTAINABILITY). If not specified, all pillars will be reviewed.",
        default=None
    ),
    documentation_paths: Optional[List[str]] = Field(
        description="Paths to documentation files to analyze",
        default=None
    ),
    output_directory: str = Field(
        description="Directory to save ADR files",
        default="./well-architected-adrs"
    )
) -> Dict:
    """Perform a comprehensive AWS Well-Architected Framework review.
    
    This tool analyzes your architecture against AWS Well-Architected best practices,
    generates Architecture Decision Records (ADRs) for each practice, and provides
    specific recommendations for improvement.
    
    Args:
        context: Description of your system/workload
        pillars: Optional list of specific pillars to review
        documentation_paths: Optional paths to documentation files
        output_directory: Directory to save generated ADR files
        
    Returns:
        Comprehensive review results with assessments and ADRs
    """
    try:
        logger.info("Starting AWS Well-Architected Framework review")
        
        # Parse pillars if provided
        selected_pillars = []
        if pillars:
            for pillar_str in pillars:
                try:
                    pillar = Pillar(pillar_str.upper())
                    selected_pillars.append(pillar)
                except ValueError:
                    logger.warning(f"Invalid pillar: {pillar_str}")
        
        # Create review scope
        scope = ReviewScope(
            pillars=selected_pillars,
            context_description=context,
            documentation_paths=documentation_paths
        )
        
        # Perform review
        reviewer = WellArchitectedReviewer()
        result = reviewer.perform_review(scope)
        
        # Generate ADRs
        adr_generator = ADRGenerator(output_directory)
        generated_files = adr_generator.generate_all_adrs(result.assessments)
        
        # Prepare response
        response = {
            "review_summary": {
                "total_best_practices_reviewed": len(result.assessments),
                "pillars_reviewed": [p.value for p in scope.pillars] if scope.pillars else "ALL",
                "risk_summary": {
                    "high_risk_items": result.overall_risk_summary.get("HIGH", 0),
                    "medium_risk_items": result.overall_risk_summary.get("MEDIUM", 0), 
                    "low_risk_items": result.overall_risk_summary.get("LOW", 0)
                },
                "documentation_status": result.documentation_status
            },
            "assessments": [],
            "generated_adr_files": generated_files,
            "high_level_recommendations": result.recommendations_summary
        }
        
        # Add assessment details
        for assessment in result.assessments:
            assessment_data = {
                "best_practice_id": assessment.best_practice_id,
                "title": assessment.title,
                "pillar": assessment.pillar.value,
                "pillar_display": format_pillar_simple(assessment.pillar),
                "status": assessment.status.value,
                "risk_level": assessment.risk_level.value,
                "risk_level_display": format_risk_level(assessment.risk_level),
                "current_implementation": assessment.current_implementation,
                "gaps_identified": assessment.gaps_identified,
                "recommendations": assessment.recommendations,
                "adr": {
                    "title": assessment.adr.title,
                    "status": assessment.adr.status,
                    "context": assessment.adr.context,
                    "decision": assessment.adr.decision,
                    "consequences": assessment.adr.consequences,
                    "trade_offs": [
                        {"benefit": to.benefit, "cost": to.cost} 
                        for to in assessment.adr.trade_offs
                    ],
                    "alternatives_considered": assessment.adr.alternatives_considered,
                    "implementation_notes": assessment.adr.implementation_notes
                }
            }
            response["assessments"].append(assessment_data)
        
        logger.info(f"Review completed. Generated {len(generated_files)} ADR files.")
        
        return response
        
    except Exception as e:
        logger.error(f"Error during Well-Architected review: {e}")
        raise


@mcp.tool()
async def list_pillars() -> Dict:
    """List all AWS Well-Architected Framework pillars.
    
    Returns:
        Dictionary containing all available pillars and their descriptions
    """
    pillars_info = {
        "OPERATIONAL_EXCELLENCE": {
            "name": "Operational Excellence",
            "description": "The ability to support development and run workloads effectively, gain insight into their operations, and to continuously improve supporting processes and procedures to deliver business value."
        },
        "SECURITY": {
            "name": "Security", 
            "description": "The ability to protect data, systems, and assets to take advantage of cloud technologies to improve your security."
        },
        "RELIABILITY": {
            "name": "Reliability",
            "description": "The ability of a workload to perform its intended function correctly and consistently when it's expected to."
        },
        "PERFORMANCE_EFFICIENCY": {
            "name": "Performance Efficiency",
            "description": "The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve."
        },
        "COST_OPTIMIZATION": {
            "name": "Cost Optimization", 
            "description": "The ability to run systems to deliver business value at the lowest price point."
        },
        "SUSTAINABILITY": {
            "name": "Sustainability",
            "description": "The ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload."
        }
    }
    
    return {
        "pillars": pillars_info,
        "total_pillars": len(pillars_info),
        "usage_note": "Use these pillar names in the 'pillars' parameter of the review command"
    }


@mcp.tool()
async def get_best_practices(
    pillar: Optional[str] = Field(
        description="Specific pillar to get best practices for. If not specified, returns all best practices.",
        default=None
    )
) -> Dict:
    """Get Well-Architected best practices for a specific pillar or all pillars.
    
    Args:
        pillar: Optional pillar name to filter best practices
        
    Returns:
        Dictionary containing best practices information
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import (
        get_all_best_practices_list,
        get_best_practices_by_pillar
    )
    
    try:
        if pillar:
            pillar_enum = Pillar(pillar.upper())
            best_practices = get_best_practices_by_pillar(pillar_enum)
            title = f"Best Practices for {pillar_enum.value}"
        else:
            best_practices = get_all_best_practices_list()
            title = "All Well-Architected Best Practices"
        
        practices_data = []
        for bp in best_practices:
            practices_data.append({
                "id": bp.id,
                "title": bp.title,
                "pillar": bp.pillar.value,
                "description": bp.description,
                "risk_level": bp.risk_level.value,
                "questions": bp.questions,
                "implementation_guidance": bp.implementation_guidance
            })
        
        return {
            "title": title,
            "total_practices": len(practices_data),
            "best_practices": practices_data
        }
        
    except ValueError as e:
        logger.error(f"Invalid pillar specified: {pillar}")
        return {
            "error": f"Invalid pillar: {pillar}",
            "valid_pillars": [p.value for p in Pillar]
        }


@mcp.tool()
async def collect_user_input(
    best_practice_id: str = Field(description="ID of the best practice requiring user input (e.g., 'OPS01-BP01')"),
    responses: Dict[str, str] = Field(description="Dictionary of question-answer pairs for the assessment")
) -> Dict:
    """Collect user input for best practices that cannot be assessed from code alone.
    
    This tool handles any Well-Architected best practice that requires human input
    by collecting responses to specific questions and generating tailored ADRs.
    
    Args:
        best_practice_id: ID of the best practice needing assessment
        responses: Dictionary mapping questions to user responses
        
    Returns:
        Assessment results and generated ADR based on user input
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import WELL_ARCHITECTED_BEST_PRACTICES
    from awslabs.aws_wellarchitected_mcp_server.models import (
        ArchitecturalDecisionRecord, BestPracticeAssessment, BestPracticeStatus, TradeOff
    )
    
    try:
        if best_practice_id not in WELL_ARCHITECTED_BEST_PRACTICES:
            return {"error": f"Best practice {best_practice_id} not found"}
        
        bp = WELL_ARCHITECTED_BEST_PRACTICES[best_practice_id]
        
        if not (hasattr(bp, 'requires_user_input') and bp.requires_user_input):
            return {"error": f"Best practice {best_practice_id} does not require user input"}
        
        # Analyze responses
        positive_indicators = ["yes", "regularly", "established", "implemented", "active", "systematic"]
        negative_indicators = ["no", "never", "rarely", "ad-hoc", "informal", "none"]
        
        response_values = [str(v).lower() for v in responses.values()]
        positive_count = sum(1 for response in response_values 
                           if any(indicator in response for indicator in positive_indicators))
        negative_count = sum(1 for response in response_values 
                           if any(indicator in response for indicator in negative_indicators))
        
        # Determine status
        total_responses = len(responses)
        if positive_count >= total_responses * 0.8:
            status = BestPracticeStatus.COMPLIANT
        elif positive_count >= total_responses * 0.5:
            status = BestPracticeStatus.NEEDS_REVIEW
        else:
            status = BestPracticeStatus.NON_COMPLIANT
        
        # Generate gaps and recommendations
        gaps = []
        recommendations = list(bp.implementation_guidance)
        
        for question, answer in responses.items():
            if any(neg in answer.lower() for neg in negative_indicators):
                gaps.append(f"Gap identified in: {question}")
        
        # Generate ADR
        adr = ArchitecturalDecisionRecord(
            title=f"ADR: {bp.title} Assessment",
            status="Assessed" if status == BestPracticeStatus.COMPLIANT else "Needs Improvement",
            context=f"User input assessment for {bp.title}. Status: {status.value}",
            decision="Implement systematic approach" if status != BestPracticeStatus.COMPLIANT else "Continue current practices with improvements",
            consequences=[
                "Improved alignment with Well-Architected principles",
                "Better operational practices",
                "Enhanced business outcomes"
            ],
            trade_offs=[
                TradeOff(
                    benefit="Better compliance with best practices",
                    cost="Time and effort for implementation"
                )
            ],
            alternatives_considered=[
                "Continue current approach",
                "Partial implementation",
                "Full best practice implementation (recommended)"
            ],
            implementation_notes=f"Priority: {bp.risk_level.value}. Address identified gaps."
        )
        
        return {
            "assessment": {
                "best_practice_id": bp.id,
                "title": bp.title,
                "status": status.value,
                "risk_level": bp.risk_level.value,
                "user_responses": responses,
                "gaps_identified": gaps,
                "recommendations": recommendations
            },
            "adr": {
                "title": adr.title,
                "status": adr.status,
                "context": adr.context,
                "decision": adr.decision,
                "consequences": adr.consequences,
                "trade_offs": [{"benefit": to.benefit, "cost": to.cost} for to in adr.trade_offs],
                "alternatives_considered": adr.alternatives_considered,
                "implementation_notes": adr.implementation_notes
            }
        }
        
    except Exception as e:
        logger.error(f"Error collecting user input: {e}")
        return {"error": str(e)}


@mcp.tool()
async def evaluate_customer_needs(
    stakeholder_engagement: str = Field(description="How do you currently engage stakeholders (business, dev, ops) to understand customer needs?"),
    customer_feedback_mechanisms: str = Field(description="What mechanisms do you have to capture external customer feedback?"),
    customer_outcome_focus: str = Field(description="How do you work backwards from customer outcomes when planning?"),
    business_alignment: str = Field(description="How do operational practices support your business outcomes?"),
    support_data_review: str = Field(description="Do you review historical customer support data for decision making?"),
    feature_validation: str = Field(description="How do you validate new features with customers before development?")
) -> Dict:
    """Evaluate external customer needs assessment (OPS01-BP01).
    
    This tool helps assess how well you evaluate and understand external customer needs
    by collecting information about your current practices and generating a tailored ADR.
    
    Args:
        stakeholder_engagement: Current stakeholder engagement practices
        customer_feedback_mechanisms: Existing customer feedback collection methods
        customer_outcome_focus: How you prioritize based on customer outcomes
        business_alignment: How operations support business outcomes
        support_data_review: Use of historical support data
        feature_validation: Customer validation processes for new features
        
    Returns:
        Detailed assessment and ADR for customer needs evaluation
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import WELL_ARCHITECTED_BEST_PRACTICES
    from awslabs.aws_wellarchitected_mcp_server.models import (
        ArchitecturalDecisionRecord, BestPracticeAssessment, BestPracticeStatus, TradeOff
    )
    
    try:
        bp = WELL_ARCHITECTED_BEST_PRACTICES["OPS01-BP01"]
        
        # Analyze responses to determine status
        responses = {
            "stakeholder_engagement": stakeholder_engagement.lower(),
            "customer_feedback_mechanisms": customer_feedback_mechanisms.lower(),
            "customer_outcome_focus": customer_outcome_focus.lower(),
            "business_alignment": business_alignment.lower(),
            "support_data_review": support_data_review.lower(),
            "feature_validation": feature_validation.lower()
        }
        
        # Score based on positive indicators
        positive_indicators = ["yes", "regularly", "established", "implemented", "active", "systematic"]
        negative_indicators = ["no", "never", "rarely", "ad-hoc", "informal", "none"]
        
        positive_count = sum(1 for response in responses.values() 
                           if any(indicator in response for indicator in positive_indicators))
        negative_count = sum(1 for response in responses.values() 
                           if any(indicator in response for indicator in negative_indicators))
        
        # Determine status
        if positive_count >= 5:
            status = BestPracticeStatus.COMPLIANT
        elif positive_count >= 3:
            status = BestPracticeStatus.NEEDS_REVIEW
        else:
            status = BestPracticeStatus.NON_COMPLIANT
        
        # Generate gaps and recommendations based on responses
        gaps = []
        recommendations = []
        
        if "no" in responses["stakeholder_engagement"] or "rarely" in responses["stakeholder_engagement"]:
            gaps.append("Limited stakeholder engagement across business, development, and operations teams")
            recommendations.append("Establish regular cross-functional meetings to discuss customer needs")
        
        if "no" in responses["customer_feedback_mechanisms"] or "none" in responses["customer_feedback_mechanisms"]:
            gaps.append("Lack of systematic customer feedback collection mechanisms")
            recommendations.append("Implement customer feedback tools (surveys, support analytics, user interviews)")
        
        if "no" in responses["support_data_review"]:
            gaps.append("Historical support data not being used for decision making")
            recommendations.append("Review support ticket trends and customer impact data regularly")
        
        # Generate ADR
        adr = ArchitecturalDecisionRecord(
            title=f"ADR: {bp.title} - Customer Needs Assessment",
            status="Assessed" if status == BestPracticeStatus.COMPLIANT else "Needs Improvement",
            context=f"Assessment of current practices for evaluating external customer needs. Current status: {status.value}",
            decision="Implement systematic approach to evaluate and understand external customer needs" if status != BestPracticeStatus.COMPLIANT else "Continue current customer needs evaluation practices with minor improvements",
            consequences=[
                "Improved customer satisfaction and retention",
                "Better alignment between operational practices and business outcomes",
                "More informed decision making based on customer data"
            ],
            trade_offs=[
                TradeOff(
                    benefit="Better customer outcomes and business alignment",
                    cost="Time investment in stakeholder coordination and feedback collection"
                ),
                TradeOff(
                    benefit="Data-driven decision making",
                    cost="Need for tools and processes to collect and analyze customer feedback"
                )
            ],
            alternatives_considered=[
                "Continue current ad-hoc approach (not recommended)",
                "Implement minimal feedback collection",
                "Full systematic customer needs evaluation program (recommended)"
            ],
            implementation_notes=f"Priority: {bp.risk_level.value}. Focus on areas identified in assessment."
        )
        
        return {
            "assessment": {
                "best_practice_id": bp.id,
                "title": bp.title,
                "status": status.value,
                "risk_level": bp.risk_level.value,
                "current_practices_analysis": {
                    "stakeholder_engagement": stakeholder_engagement,
                    "feedback_mechanisms": customer_feedback_mechanisms,
                    "outcome_focus": customer_outcome_focus,
                    "business_alignment": business_alignment,
                    "data_review": support_data_review,
                    "feature_validation": feature_validation
                },
                "gaps_identified": gaps,
                "recommendations": recommendations
            },
            "adr": {
                "title": adr.title,
                "status": adr.status,
                "context": adr.context,
                "decision": adr.decision,
                "consequences": adr.consequences,
                "trade_offs": [{"benefit": to.benefit, "cost": to.cost} for to in adr.trade_offs],
                "alternatives_considered": adr.alternatives_considered,
                "implementation_notes": adr.implementation_notes
            },
            "next_steps": [
                "Review the generated ADR and recommendations",
                "Prioritize implementation based on identified gaps",
                "Establish regular review cycles for customer needs assessment",
                "Consider using this assessment in your regular Well-Architected reviews"
            ]
        }
        
    except Exception as e:
        logger.error(f"Error evaluating customer needs: {e}")
        return {"error": str(e)}


@mcp.tool()
async def create_review_plan(
    workload_name: str = Field(description="Name of the workload to review"),
    selected_pillars: Optional[List[str]] = Field(
        description="Pillars to include in review (OPERATIONAL_EXCELLENCE, SECURITY, RELIABILITY, PERFORMANCE_EFFICIENCY, COST_OPTIMIZATION, SUSTAINABILITY)",
        default=None
    )
) -> Dict:
    """Create a comprehensive Well-Architected review plan with three phases: Learn, Measure, Improve.
    
    Args:
        workload_name: Name of the workload being reviewed
        selected_pillars: Optional list of pillars to focus on
        
    Returns:
        Structured review plan with phases and steps
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import get_all_best_practices
    from awslabs.aws_wellarchitected_mcp_server.review import WellArchitectedReview
    from awslabs.aws_wellarchitected_mcp_server.review_guide import get_review_introduction, format_pillar_options
    
    try:
        # Parse pillars
        pillars = []
        if selected_pillars:
            for pillar_str in selected_pillars:
                try:
                    pillar = Pillar(pillar_str.upper())
                    pillars.append(pillar)
                except ValueError:
                    logger.warning(f"Invalid pillar: {pillar_str}")
        else:
            pillars = list(Pillar)
        
        # Create review
        best_practices = get_all_best_practices()
        review = WellArchitectedReview(best_practices)
        plan = review.create_review_plan(workload_name, pillars)
        
        # Format response
        response = {
            "introduction": get_review_introduction(),
            "review_plan": {
                "workload_name": plan.workload_name,
                "estimated_duration": plan.estimated_duration,
                "prerequisites": plan.prerequisites,
                "phases": {}
            }
        }
        
        # Add phase details
        for phase, steps in plan.phases.items():
            response["review_plan"]["phases"][phase.value] = {
                "name": phase.value.title(),
                "step_count": len(steps),
                "steps": [
                    {
                        "id": step.id,
                        "title": step.title,
                        "description": step.description,
                        "pillar": step.pillar.value,
                        "questions": step.questions,
                        "validation_criteria": step.validation_criteria,
                        "estimated_effort": step.estimated_effort,
                        "dependencies": step.dependencies or []
                    }
                    for step in steps
                ]
            }
        
        return response
        
    except Exception as e:
        logger.error(f"Error creating review plan: {e}")
        return {"error": str(e)}


@mcp.tool()
async def get_priority_analysis(
    selected_pillars: Optional[List[str]] = Field(
        description="Pillars to analyze (OPERATIONAL_EXCELLENCE, SECURITY, RELIABILITY, PERFORMANCE_EFFICIENCY, COST_OPTIMIZATION, SUSTAINABILITY)",
        default=None
    ),
    count: int = Field(description="Number of top priorities to return (3, 5, or 10)", default=5)
) -> Dict:
    """Get top priority best practices based on risk and relationships.
    
    Args:
        selected_pillars: Optional list of pillars to focus on
        count: Number of top priorities to return
        
    Returns:
        Prioritized list of best practices with implementation guidance
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import get_all_best_practices
    from awslabs.aws_wellarchitected_mcp_server.priority_analyzer import PriorityAnalyzer, format_priority_recommendations, get_implementation_roadmap
    
    try:
        # Parse pillars
        pillars = []
        if selected_pillars:
            for pillar_str in selected_pillars:
                try:
                    pillar = Pillar(pillar_str.upper())
                    pillars.append(pillar)
                except ValueError:
                    logger.warning(f"Invalid pillar: {pillar_str}")
        else:
            pillars = list(Pillar)
        
        # Get priorities
        best_practices = get_all_best_practices()
        analyzer = PriorityAnalyzer(best_practices)
        priorities = analyzer.get_top_priorities(pillars, count)
        
        # Format response
        priority_items = []
        for item in priorities:
            bp = item.best_practice
            priority_items.append({
                "rank": item.implementation_order,
                "best_practice": {
                    "id": bp.id,
                    "title": bp.title,
                    "pillar": bp.pillar.value,
                    "risk_level": bp.risk_level.value,
                    "description": bp.description
                },
                "priority_score": item.priority_score,
                "impact_reason": item.impact_reason,
                "related_practices": [
                    {"id": rp.id, "title": rp.title}
                    for rp in item.related_practices
                ],
                "implementation_guidance": bp.implementation_guidance
            })
        
        return {
            "summary": {
                "total_priorities": len(priorities),
                "pillars_analyzed": [p.value for p in pillars],
                "analysis_focus": "High impact, manageable complexity items for first iteration"
            },
            "priorities": priority_items,
            "implementation_roadmap": get_implementation_roadmap(priorities),
            "formatted_report": format_priority_recommendations(priorities)
        }
        
    except Exception as e:
        logger.error(f"Error getting priority analysis: {e}")
        return {"error": str(e)}


@mcp.tool()
async def get_eisenhower_matrix(
    selected_pillars: Optional[List[str]] = Field(
        description="Pillars to analyze (OPERATIONAL_EXCELLENCE, SECURITY, RELIABILITY, PERFORMANCE_EFFICIENCY, COST_OPTIMIZATION, SUSTAINABILITY)",
        default=None
    )
) -> Dict:
    """Create Eisenhower Matrix for Well-Architected best practices prioritization.
    
    Args:
        selected_pillars: Optional list of pillars to focus on
        
    Returns:
        Eisenhower Matrix with practices categorized by urgency and importance
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import get_all_best_practices
    from awslabs.aws_wellarchitected_mcp_server.eisenhower_matrix import EisenhowerMatrix, format_eisenhower_matrix, get_matrix_summary
    
    try:
        # Parse pillars
        pillars = []
        if selected_pillars:
            for pillar_str in selected_pillars:
                try:
                    pillar = Pillar(pillar_str.upper())
                    pillars.append(pillar)
                except ValueError:
                    logger.warning(f"Invalid pillar: {pillar_str}")
        else:
            pillars = list(Pillar)
        
        # Create matrix
        best_practices = get_all_best_practices()
        matrix = EisenhowerMatrix(best_practices)
        eisenhower_matrix = matrix.create_matrix(pillars)
        
        # Format response
        matrix_data = {}
        for quadrant, items in eisenhower_matrix.items():
            matrix_data[quadrant.value] = {
                "name": quadrant.value.replace('_', ' ').title(),
                "count": len(items),
                "items": [
                    {
                        "best_practice": {
                            "id": item.best_practice.id,
                            "title": item.best_practice.title,
                            "pillar": item.best_practice.pillar.value,
                            "risk_level": item.best_practice.risk_level.value
                        },
                        "urgency_score": item.urgency_score,
                        "importance_score": item.importance_score,
                        "action_recommendation": item.action_recommendation
                    }
                    for item in items[:10]  # Limit to top 10 per quadrant
                ]
            }
        
        return {
            "matrix": matrix_data,
            "visual_matrix": format_eisenhower_matrix(eisenhower_matrix),
            "summary": get_matrix_summary(eisenhower_matrix),
            "pillars_analyzed": [p.value for p in pillars]
        }
        
    except Exception as e:
        logger.error(f"Error creating Eisenhower matrix: {e}")
        return {"error": str(e)}


@mcp.tool()
async def get_smart_solutions(
    selected_pillars: Optional[List[str]] = Field(
        description="Pillars to analyze (OPERATIONAL_EXCELLENCE, SECURITY, RELIABILITY, PERFORMANCE_EFFICIENCY, COST_OPTIMIZATION, SUSTAINABILITY)",
        default=None
    ),
    focus_on_quick_wins: bool = Field(description="Focus only on quick wins (high impact, low complexity)", default=True)
) -> Dict:
    """Generate SMART solutions for Well-Architected improvements.
    
    Args:
        selected_pillars: Optional list of pillars to focus on
        focus_on_quick_wins: Whether to focus on quick wins only
        
    Returns:
        SMART solutions with implementation guidance
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import get_all_best_practices
    from awslabs.aws_wellarchitected_mcp_server.priority_analyzer import PriorityAnalyzer
    from awslabs.aws_wellarchitected_mcp_server.solution_framework import SolutionFramework, format_smart_solutions, get_quick_wins
    from awslabs.aws_wellarchitected_mcp_server.solution_guidelines import get_solution_guidelines, format_guidelines
    
    try:
        # Parse pillars
        pillars = []
        if selected_pillars:
            for pillar_str in selected_pillars:
                try:
                    pillar = Pillar(pillar_str.upper())
                    pillars.append(pillar)
                except ValueError:
                    logger.warning(f"Invalid pillar: {pillar_str}")
        else:
            pillars = list(Pillar)
        
        # Get top priorities
        best_practices = get_all_best_practices()
        analyzer = PriorityAnalyzer(best_practices)
        priorities = analyzer.get_top_priorities(pillars, 10)
        
        # Generate SMART solutions
        solution_framework = SolutionFramework(best_practices)
        guidelines = get_solution_guidelines()
        
        solutions = []
        for priority_item in priorities:
            bp = priority_item.best_practice
            solution = solution_framework.generate_smart_solution(
                bp, 
                {'default_owner': 'Architecture Team'},
                guidelines
            )
            solutions.append(solution)
        
        # Filter for quick wins if requested
        if focus_on_quick_wins:
            solutions = get_quick_wins(solutions)
        
        # Format response
        solution_data = []
        for solution in solutions:
            solution_data.append({
                "best_practice_id": solution.best_practice_id,
                "smart_criteria": {
                    "specific": solution.specific,
                    "measurable": solution.measurable,
                    "achievable": solution.achievable,
                    "relevant": solution.relevant,
                    "time_bound": solution.time_bound
                },
                "characteristics": {
                    "owner": solution.owner,
                    "complexity": solution.complexity.value,
                    "business_impact": solution.business_impact.value,
                    "is_two_way_door": solution.is_two_way_door,
                    "pattern_reference": solution.pattern_reference
                },
                "implementation": {
                    "prerequisites": solution.prerequisites,
                    "success_criteria": solution.success_criteria,
                    "rollback_plan": solution.rollback_plan
                }
            })
        
        return {
            "guidelines": format_guidelines(),
            "solutions": solution_data,
            "formatted_guide": format_smart_solutions(solutions),
            "summary": {
                "total_solutions": len(solutions),
                "focus": "Quick wins" if focus_on_quick_wins else "All priorities",
                "pillars_analyzed": [p.value for p in pillars]
            }
        }
        
    except Exception as e:
        logger.error(f"Error generating SMART solutions: {e}")
        return {"error": str(e)}


@mcp.tool()
async def ask_implementation_fix(
    best_practice_id: str = Field(description="ID of the best practice to implement"),
    current_context: str = Field(description="Current implementation context"),
    preferred_approach: Optional[str] = Field(
        description="Preferred implementation approach",
        default=None
    )
) -> Dict:
    """Ask for specific implementation guidance to fix a Well-Architected best practice.
    
    This tool provides detailed, actionable steps to implement a specific best practice
    based on your current context and preferred approach.
    
    Args:
        best_practice_id: ID of the best practice (e.g., 'OPS01', 'SEC01')
        current_context: Description of your current implementation
        preferred_approach: Optional preferred implementation approach
        
    Returns:
        Detailed implementation guidance and steps
    """
    from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import WELL_ARCHITECTED_BEST_PRACTICES
    
    try:
        if best_practice_id not in WELL_ARCHITECTED_BEST_PRACTICES:
            return {
                "error": f"Best practice {best_practice_id} not found",
                "available_practices": list(WELL_ARCHITECTED_BEST_PRACTICES.keys())
            }
        
        bp = WELL_ARCHITECTED_BEST_PRACTICES[best_practice_id]
        
        # Generate specific implementation steps
        implementation_steps = _generate_implementation_steps(bp, current_context, preferred_approach)
        
        return {
            "best_practice": {
                "id": bp.id,
                "title": bp.title,
                "pillar": bp.pillar.value,
                "description": bp.description,
                "risk_level": bp.risk_level.value
            },
            "current_context_analysis": _analyze_current_context(current_context, bp),
            "implementation_steps": implementation_steps,
            "estimated_effort": _estimate_implementation_effort(bp),
            "prerequisites": _get_prerequisites(bp),
            "success_criteria": _get_success_criteria(bp),
            "monitoring_recommendations": _get_monitoring_recommendations(bp)
        }
        
    except Exception as e:
        logger.error(f"Error generating implementation guidance: {e}")
        return {"error": str(e)}


def _generate_implementation_steps(best_practice, current_context: str, preferred_approach: Optional[str]) -> List[Dict]:
    """Generate specific implementation steps for a best practice."""
    steps = []
    
    # Base implementation steps based on best practice
    base_steps = {
        "OPS01-BP01": [
            {"step": 1, "action": "Use collect_user_input tool", "details": "Provide responses to assessment questions"},
            {"step": 2, "action": "Review generated assessment", "details": "Analyze gaps and recommendations"},
            {"step": 3, "action": "Implement improvements", "details": "Address identified gaps"},
            {"step": 4, "action": "Regular reassessment", "details": "Periodic review of practices"}
        ],
        "OPS01": [
            {"step": 1, "action": "Choose IaC tool", "details": "Select CloudFormation, CDK, or Terraform"},
            {"step": 2, "action": "Create templates", "details": "Define infrastructure as code templates"},
            {"step": 3, "action": "Set up CI/CD", "details": "Implement automated deployment pipeline"},
            {"step": 4, "action": "Version control", "details": "Store templates in Git repository"}
        ],
        "SEC01": [
            {"step": 1, "action": "Audit current IAM", "details": "Review existing users, roles, and policies"},
            {"step": 2, "action": "Implement least privilege", "details": "Remove unnecessary permissions"},
            {"step": 3, "action": "Enable MFA", "details": "Require MFA for all human users"},
            {"step": 4, "action": "Use roles for applications", "details": "Replace user credentials with IAM roles"}
        ]
    }
    
    steps = base_steps.get(best_practice.id, [
        {"step": 1, "action": "Assess current state", "details": "Evaluate current implementation"},
        {"step": 2, "action": "Plan implementation", "details": "Create implementation plan"},
        {"step": 3, "action": "Execute changes", "details": "Implement best practice"},
        {"step": 4, "action": "Validate and monitor", "details": "Verify implementation and set up monitoring"}
    ])
    
    return steps


def _analyze_current_context(context: str, best_practice) -> str:
    """Analyze the current context for implementation guidance."""
    if not context.strip():
        return "No current context provided. Starting from baseline implementation."
    
    context_lower = context.lower()
    
    # Simple analysis based on keywords
    if any(keyword in context_lower for keyword in ["existing", "current", "already"]):
        return "Existing implementation detected. Focus on enhancement and optimization."
    else:
        return "New implementation required. Start with foundational setup."


def _estimate_implementation_effort(best_practice) -> Dict:
    """Estimate implementation effort for a best practice."""
    effort_mapping = {
        "HIGH": {"time": "2-4 weeks", "complexity": "High", "resources": "Senior engineer + team"},
        "MEDIUM": {"time": "1-2 weeks", "complexity": "Medium", "resources": "Mid-level engineer"},
        "LOW": {"time": "2-5 days", "complexity": "Low", "resources": "Any engineer"}
    }
    
    return effort_mapping.get(best_practice.risk_level.value, effort_mapping["MEDIUM"])


def _get_prerequisites(best_practice) -> List[str]:
    """Get prerequisites for implementing a best practice."""
    prereq_mapping = {
        "OPS01-BP01": ["Stakeholder access", "Customer feedback tools", "Support data access"],
        "OPS01": ["AWS CLI configured", "Git repository", "CI/CD platform access"],
        "SEC01": ["AWS account admin access", "IAM permissions", "MFA device"],
        "REL01": ["Multi-AZ setup capability", "Backup strategy defined"],
        "PERF01": ["Performance baseline established", "Monitoring tools configured"],
        "COST01": ["Cost Explorer access", "Billing permissions"],
        "SUS01": ["Resource utilization data", "Monitoring setup"]
    }
    
    return prereq_mapping.get(best_practice.id, ["AWS account access", "Appropriate permissions"])


def _get_success_criteria(best_practice) -> List[str]:
    """Get success criteria for a best practice implementation."""
    criteria_mapping = {
        "OPS01-BP01": ["Regular stakeholder meetings established", "Customer feedback mechanisms active", "Support data reviewed regularly"],
        "OPS01": ["Infrastructure deployed via code", "Changes tracked in version control", "Automated deployments working"],
        "SEC01": ["All users have MFA enabled", "Least privilege implemented", "No hardcoded credentials"],
        "REL01": ["Multi-AZ deployment confirmed", "Backup/restore tested", "Failover procedures documented"],
        "PERF01": ["Right-sized instances deployed", "Performance monitoring active", "Optimization recommendations implemented"],
        "COST01": ["Cost monitoring enabled", "Budget alerts configured", "Regular cost reviews scheduled"],
        "SUS01": ["Resource utilization optimized", "Unused resources identified", "Efficiency metrics tracked"]
    }
    
    return criteria_mapping.get(best_practice.id, ["Implementation completed", "Best practice validated", "Monitoring in place"])


def _get_monitoring_recommendations(best_practice) -> List[str]:
    """Get monitoring recommendations for a best practice."""
    monitoring_mapping = {
        "OPS01-BP01": ["Monitor customer satisfaction metrics", "Track stakeholder engagement frequency", "Alert on customer feedback trends"],
        "OPS01": ["Track deployment success rates", "Monitor infrastructure drift", "Alert on failed deployments"],
        "SEC01": ["Monitor failed login attempts", "Track privilege escalations", "Alert on policy changes"],
        "REL01": ["Monitor system availability", "Track backup success", "Alert on failover events"],
        "PERF01": ["Monitor resource utilization", "Track response times", "Alert on performance degradation"],
        "COST01": ["Monitor cost trends", "Track budget variance", "Alert on cost anomalies"],
        "SUS01": ["Monitor resource efficiency", "Track utilization trends", "Alert on waste"]
    }
    
    return monitoring_mapping.get(best_practice.id, ["Monitor implementation status", "Track compliance metrics", "Set up relevant alerts"])


def main():
    """Run the MCP server with CLI argument support."""
    parser = argparse.ArgumentParser(
        description='AWS Well-Architected MCP Server - Comprehensive architecture reviews and ADR generation'
    )
    parser.add_argument('--region', help='AWS region to use for operations')
    
    args = parser.parse_args()
    
    if args.region:
        logger.info(f'Using AWS region: {args.region}')
    
    logger.info('Starting AWS Well-Architected MCP Server')
    mcp.run()


if __name__ == '__main__':
    main()