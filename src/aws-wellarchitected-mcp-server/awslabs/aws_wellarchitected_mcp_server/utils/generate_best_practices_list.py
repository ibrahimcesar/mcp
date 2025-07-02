#!/usr/bin/env python3

"""Generate updated best practices list for README."""

import sys
import os

# Add the package to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src/aws-wellarchitected-mcp-server'))

from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import get_all_best_practices
from awslabs.aws_wellarchitected_mcp_server.models import Pillar

def generate_best_practices_section():
    """Generate the best practices section for README."""
    
    # Get all best practices
    all_best_practices = get_all_best_practices()
    
    # Count by pillar
    pillar_counts = {}
    pillar_practices = {}
    
    for bp_id, bp in all_best_practices.items():
        pillar = bp.pillar
        if pillar not in pillar_counts:
            pillar_counts[pillar] = 0
            pillar_practices[pillar] = []
        
        pillar_counts[pillar] += 1
        pillar_practices[pillar].append((bp_id, bp.title, getattr(bp, 'requires_user_input', False)))
    
    # Generate markdown
    total_practices = len(all_best_practices)
    
    markdown = f"""<details>
<summary>📋 Best Practices Covered</summary>

## Summary
- **Total Best Practices**: {total_practices}
- **Operational Excellence**: {pillar_counts.get(Pillar.OPERATIONAL_EXCELLENCE, 0)} practices
- **Security**: {pillar_counts.get(Pillar.SECURITY, 0)} practices  
- **Reliability**: {pillar_counts.get(Pillar.RELIABILITY, 0)} practices
- **Performance Efficiency**: {pillar_counts.get(Pillar.PERFORMANCE_EFFICIENCY, 0)} practices
- **Cost Optimization**: {pillar_counts.get(Pillar.COST_OPTIMIZATION, 0)} practices
- **Sustainability**: {pillar_counts.get(Pillar.SUSTAINABILITY, 0)} practices

"""
    
    # Add each pillar section
    pillar_names = {
        Pillar.OPERATIONAL_EXCELLENCE: "🔧 Operational Excellence",
        Pillar.SECURITY: "🔒 Security",
        Pillar.RELIABILITY: "🛡️ Reliability", 
        Pillar.PERFORMANCE_EFFICIENCY: "⚡ Performance Efficiency",
        Pillar.COST_OPTIMIZATION: "💰 Cost Optimization",
        Pillar.SUSTAINABILITY: "🌱 Sustainability"
    }
    
    for pillar in [Pillar.OPERATIONAL_EXCELLENCE, Pillar.SECURITY, Pillar.RELIABILITY, 
                   Pillar.PERFORMANCE_EFFICIENCY, Pillar.COST_OPTIMIZATION, Pillar.SUSTAINABILITY]:
        if pillar in pillar_practices:
            markdown += f"### {pillar_names[pillar]}\n"
            
            # Sort practices by ID
            practices = sorted(pillar_practices[pillar], key=lambda x: x[0])
            
            for bp_id, title, requires_input in practices:
                user_input_marker = " *(requires user input)*" if requires_input else ""
                markdown += f"- **{bp_id}**: {title}{user_input_marker}\n"
            
            markdown += "\n"
    
    markdown += "</details>"
    
    return markdown

if __name__ == "__main__":
    print(generate_best_practices_section())