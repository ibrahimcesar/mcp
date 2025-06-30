#!/usr/bin/env python3
"""Example usage of AWS Well-Architected MCP Server."""

import asyncio
from awslabs.aws_wellarchitected_mcp_server.server import review, list_pillars, ask_implementation_fix


async def main():
    """Example workflow using the Well-Architected MCP server."""
    
    # 1. List available pillars
    print("=== Available Pillars ===")
    pillars = await list_pillars()
    print(f"Found {pillars['total_pillars']} pillars")
    
    # 2. Perform a focused review
    print("\n=== Performing Security Review ===")
    context = """
    E-commerce web application:
    - Frontend: React app on S3 + CloudFront
    - Backend: Node.js API on ECS Fargate
    - Database: RDS PostgreSQL with read replicas
    - Authentication: Cognito User Pools
    - File storage: S3 buckets for product images
    - Traffic: 10,000 daily active users
    - Current issues: Using IAM users for application access
    """
    
    result = await review(
        context=context,
        pillars=["SECURITY", "RELIABILITY"],
        output_directory="./example-review"
    )
    
    print(f"Review completed!")
    print(f"- Total practices reviewed: {result['review_summary']['total_best_practices_reviewed']}")
    print(f"- High risk items: {result['review_summary']['risk_summary']['high_risk_items']}")
    print(f"- Generated ADR files: {len(result['generated_adr_files'])}")
    
    # 3. Get implementation guidance for a specific issue
    print("\n=== Getting Implementation Guidance ===")
    guidance = await ask_implementation_fix(
        best_practice_id="SEC01",
        current_context="Currently using IAM users for ECS tasks",
        preferred_approach="Migrate to IAM roles with task definitions"
    )
    
    print(f"Implementation steps for {guidance['best_practice']['title']}:")
    for step in guidance['implementation_steps']:
        print(f"  {step['step']}. {step['action']}: {step['details']}")


if __name__ == "__main__":
    asyncio.run(main())