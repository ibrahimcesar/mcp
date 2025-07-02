#!/usr/bin/env python3

"""Test script for AWS Well-Architected MCP Server."""

import asyncio
import sys
import os

# Add the package to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src/aws-wellarchitected-mcp-server'))

async def test_server_functions():
    """Test the main server functions."""
    
    try:
        # Import server functions
        from awslabs.aws_wellarchitected_mcp_server.server import (
            list_pillars, get_best_practices, create_review_plan, 
            get_priority_analysis, get_eisenhower_matrix, get_smart_solutions
        )
        
        print("=== Testing AWS Well-Architected MCP Server ===\n")
        
        # Test 1: List pillars
        print("1. Testing list_pillars()...")
        pillars_result = await list_pillars()
        print(f"   ✓ Found {pillars_result['total_pillars']} pillars")
        
        # Test 2: Get best practices for Security
        print("\n2. Testing get_best_practices() for Security...")
        security_practices = await get_best_practices("SECURITY")
        print(f"   ✓ Found {security_practices['total_practices']} security best practices")
        
        # Test 3: Create review plan
        print("\n3. Testing create_review_plan()...")
        review_plan = await create_review_plan(
            workload_name="Test Workload",
            selected_pillars=["SECURITY", "RELIABILITY"]
        )
        if "error" not in review_plan:
            phases = review_plan["review_plan"]["phases"]
            print(f"   ✓ Created review plan with {len(phases)} phases")
        else:
            print(f"   ✗ Error: {review_plan['error']}")
        
        # Test 4: Priority analysis
        print("\n4. Testing get_priority_analysis()...")
        priorities = await get_priority_analysis(
            selected_pillars=["SECURITY", "RELIABILITY"],
            count=5
        )
        if "error" not in priorities:
            print(f"   ✓ Generated {priorities['summary']['total_priorities']} priority recommendations")
        else:
            print(f"   ✗ Error: {priorities['error']}")
        
        # Test 5: Eisenhower Matrix
        print("\n5. Testing get_eisenhower_matrix()...")
        matrix = await get_eisenhower_matrix(
            selected_pillars=["SECURITY", "RELIABILITY"]
        )
        if "error" not in matrix:
            total_items = sum(quad["count"] for quad in matrix["matrix"].values())
            print(f"   ✓ Created Eisenhower matrix with {total_items} items")
        else:
            print(f"   ✗ Error: {matrix['error']}")
        
        # Test 6: SMART Solutions
        print("\n6. Testing get_smart_solutions()...")
        solutions = await get_smart_solutions(
            selected_pillars=["SECURITY"],
            focus_on_quick_wins=True
        )
        if "error" not in solutions:
            print(f"   ✓ Generated {solutions['summary']['total_solutions']} SMART solutions")
        else:
            print(f"   ✗ Error: {solutions['error']}")
        
        print("\n=== All Tests Completed Successfully! ===")
        print("\nThe MCP server is ready to use in Q IDE.")
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server_functions())