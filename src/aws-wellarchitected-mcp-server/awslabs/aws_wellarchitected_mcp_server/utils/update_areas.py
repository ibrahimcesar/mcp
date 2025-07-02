#!/usr/bin/env python3

"""Script to update all best practices with area information."""

import re
import os

# Area mappings for each pillar
AREA_MAPPINGS = {
    # Operational Excellence
    "OPS01": "Organization priorities",
    "OPS02": "Relationships and ownership", 
    "OPS03": "Organizational culture",
    "OPS04": "Implement observability",
    "OPS05": "Design for operations",
    "OPS06": "Mitigate deployment risks",
    "OPS07": "Operational readiness",
    "OPS08": "Utilizing workload observability",
    "OPS09": "Understanding operational health",
    "OPS10": "Responding to events",
    "OPS11": "Learn, share, and improve",
    
    # Security - Individual best practice mappings
    "SEC01-BP01": "AWS account management and separation",
    "SEC01-BP02": "AWS account management and separation",
    "SEC01-BP03": "Operating your workload securely",
    "SEC01-BP04": "Operating your workload securely",
    "SEC01-BP05": "Operating your workload securely",
    "SEC01-BP06": "Operating your workload securely",
    "SEC01-BP07": "Operating your workload securely",
    "SEC01-BP08": "Operating your workload securely",
    "SEC02": "Identity management",
    "SEC03": "Permissions management",
    "SEC04": "Protecting compute",
    "SEC05": "Protecting networks",
    "SEC06": "Detection",
    "SEC07": "Data classification",
    "SEC08": "Protecting data at rest",
    "SEC09": "Protecting data in transit",
    "SEC10-BP01": "Preparation",
    "SEC10-BP02": "Preparation",
    "SEC10-BP03": "Preparation",
    "SEC10-BP04": "Preparation",
    "SEC10-BP05": "Preparation",
    "SEC10-BP06": "Preparation",
    "SEC10-BP07": "Preparation",
    "SEC10-BP08": "Post-incident activity",
    "SEC11": "Application security",
    
    # Reliability
    "REL01": "Manage service quotas and constraints",
    "REL02": "Plan your network topology",
    "REL03": "Design your workload service architecture",
    "REL04": "Design interactions in a distributed system to prevent failures",
    "REL05": "Design interactions in a distributed system to mitigate or withstand failures",
    "REL06": "Monitor workload resources",
    "REL07": "Design your workload to adapt to changes in demand",
    "REL08": "Implement change",
    "REL09": "Back up data",
    "REL10": "Use fault isolation to protect your workload",
    "REL11": "Design your workload to withstand component failures",
    "REL12": "Test reliability",
    "REL13": "Plan for disaster recovery (DR)",
    
    # Performance Efficiency
    "PERF01": "Architecture selection",
    "PERF02": "Compute and hardware",
    "PERF03": "Data management",
    "PERF04": "Networking and content delivery",
    "PERF05": "Process and culture",
    
    # Cost Optimization
    "COST01": "Practice Cloud Financial Management",
    "COST02": "Governance",
    "COST03": "Monitor cost and usage",
    "COST04": "Decommission resources",
    "COST05": "Evaluate cost when selecting services",
    "COST06": "Select the correct resource type, size, and number",
    "COST07": "Select the best pricing model",
    "COST08": "Plan for data transfer",
    "COST09": "Manage demand and supply resources",
    "COST10": "Define review process",
    "COST11": "Automating operations",
    
    # Sustainability
    "SUS01": "Region selection",
    "SUS02": "Alignment to demand",
    "SUS03": "Software and architecture",
    "SUS04": "Data",
    "SUS05": "Hardware and services",
    "SUS06": "Process and culture"
}

def update_pillar_file(file_path):
    """Update a pillar file with area information."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all BestPractice definitions - handle both with and without existing area
    pattern = r'(\s+)"([A-Z]+\d+-BP\d+)": BestPractice\(\s*\n\s+id="([^"]+)",\s*\n\s+title="([^"]+)",\s*\n\s+pillar=Pillar\.([A-Z_]+),(?:\s*\n\s+area="[^"]+",)?'
    
    def replace_match(match):
        indent = match.group(1)
        bp_id = match.group(2)
        full_id = match.group(3)
        title = match.group(4)
        pillar = match.group(5)
        
        # Extract area code, try full BP ID first, then fall back to prefix
        area = AREA_MAPPINGS.get(bp_id, None)
        if area is None:
            area_code = bp_id.split('-')[0]
            area = AREA_MAPPINGS.get(area_code, "Unknown")
        
        return f'{indent}"{bp_id}": BestPractice(\n{indent}    id="{full_id}",\n{indent}    title="{title}",\n{indent}    pillar=Pillar.{pillar},\n{indent}    area="{area}",'
    
    updated_content = re.sub(pattern, replace_match, content)
    
    with open(file_path, 'w') as f:
        f.write(updated_content)
    
    print(f"Updated {file_path}")

def main():
    """Update all pillar files."""
    pillar_files = [
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/operational_excellence.py",
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/security.py",
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/reliability.py",
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/performance_efficiency.py",
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/cost_optimization.py",
        "src/aws-wellarchitected-mcp-server/awslabs/aws_wellarchitected_mcp_server/pillars/sustainability.py"
    ]
    
    for file_path in pillar_files:
        if os.path.exists(file_path):
            update_pillar_file(file_path)
        else:
            print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()