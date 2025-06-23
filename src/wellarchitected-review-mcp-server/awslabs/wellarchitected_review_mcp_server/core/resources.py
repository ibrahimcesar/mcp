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

"""Resource handlers for the AWS Well-Architected Review MCP server."""

import logging
from typing import Dict, Any
from fastmcp import Context


logger = logging.getLogger(__name__)

# Dictionary of Well-Architected pillars
PILLARS = {
    "operational-excellence": {
        "name": "Operational Excellence",
        "description": "The ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.",
        "principles": [
            "Perform operations as code",
            "Make frequent, small, reversible changes",
            "Refine operations procedures frequently",
            "Anticipate failure",
            "Learn from all operational failures"
        ]
    },
    "security": {
        "name": "Security",
        "description": "The ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.",
        "principles": [
            "Implement a strong identity foundation",
            "Enable traceability",
            "Apply security at all layers",
            "Automate security best practices",
            "Protect data in transit and at rest",
            "Keep people away from data",
            "Prepare for security events"
        ]
    },
    "reliability": {
        "name": "Reliability",
        "description": "The ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues.",
        "principles": [
            "Test recovery procedures",
            "Automatically recover from failure",
            "Scale horizontally to increase aggregate system availability",
            "Stop guessing capacity",
            "Manage change in automation"
        ]
    },
    "performance-efficiency": {
        "name": "Performance Efficiency",
        "description": "The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.",
        "principles": [
            "Democratize advanced technologies",
            "Go global in minutes",
            "Use serverless architectures",
            "Experiment more often",
            "Mechanical sympathy"
        ]
    },
    "cost-optimization": {
        "name": "Cost Optimization",
        "description": "The ability to run systems to deliver business value at the lowest price point.",
        "principles": [
            "Implement cloud financial management",
            "Adopt a consumption model",
            "Measure overall efficiency",
            "Stop spending money on undifferentiated heavy lifting",
            "Analyze and attribute expenditure"
        ]
    },
    "sustainability": {
        "name": "Sustainability",
        "description": "The ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload.",
        "principles": [
            "Understand your impact",
            "Establish sustainability goals",
            "Maximize utilization",
            "Anticipate and adopt new, more efficient hardware and software offerings",
            "Use managed services",
            "Reduce the downstream impact of your cloud workloads"
        ]
    }
}

# Dictionary of Well-Architected best practices
BEST_PRACTICES = {
    "OPS1": {
        "id": "OPS1",
        "pillar": "operational-excellence",
        "title": "How do you determine what your priorities are?",
        "description": "Everyone should understand their part in enabling business success. Have shared goals in order to set priorities for resources. This will maximize the benefits of your efforts.",
        "recommended_practices": [
            "Evaluate external customer needs",
            "Evaluate internal customer needs", 
            "Evaluate governance requirements",
            "Evaluate compliance requirements",
            "Evaluate threat landscape",
            "Evaluate tradeoffs",
            "Manage benefits and risks"
        ]
    },
    "SEC1": {
        "id": "SEC1",
        "pillar": "security",
        "title": "How do you securely operate your workload?",
        "description": "To operate your workload securely, you must apply overarching best practices to every area of security. Take requirements and processes that you have defined in operational excellence at an organizational and workload level, and apply them to all areas.",
        "recommended_practices": [
            "Separate workloads using accounts",
            "Secure AWS account",
            "Keep up to date with security threats",
            "Evaluate and implement new security services and features regularly",
            "Automate security best practices",
            "Define identity management and permissions"
        ]
    },
    "REL1": {
        "id": "REL1",
        "pillar": "reliability",
        "title": "How do you manage service quotas and constraints?",
        "description": "For cloud-based workload architectures, there are service quotas (which are also referred to as service limits). These quotas exist to prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse.",
        "recommended_practices": [
            "Aware of service quotas and constraints",
            "Manage service quotas across accounts and regions",
            "Accommodate fixed service quotas and constraints through architecture",
            "Monitor and manage quotas",
            "Automate quota management",
            "Ensure there is a sufficient gap between the quota and the maximum usage to accommodate failover"
        ]
    },
    "PERF1": {
        "id": "PERF1",
        "pillar": "performance-efficiency",
        "title": "How do you select the best performing architecture?",
        "description": "Often, multiple approaches are required for optimal performance across a workload. Well-architected systems use multiple solutions and features to improve performance.",
        "recommended_practices": [
            "Use a data-driven approach to select patterns and implementation",
            "Learn about and understand the available services and resources",
            "Define a process for architectural choices",
            "Factor cost requirements into decisions",
            "Use policies or reference architectures",
            "Use guidance from cloud provider or appropriate partners",
            "Benchmark existing workloads",
            "Load test your workload"
        ]
    },
    "COST1": {
        "id": "COST1",
        "pillar": "cost-optimization",
        "title": "How do you implement cloud financial management?",
        "description": "Implementing Cloud Financial Management enables organizations to realize business value and financial success as they optimize their cost and usage and scale on AWS.",
        "recommended_practices": [
            "Establish a cost optimization function",
            "Establish a partnership between finance and technology",
            "Establish cloud budgets and forecasts",
            "Implement cost controls",
            "Track and allocate costs",
            "Report and notify on cost optimization"
        ]
    },
    "SUS1": {
        "id": "SUS1",
        "pillar": "sustainability",
        "title": "How do you select Regions to support your sustainability goals?",
        "description": "Understand the sustainability of the AWS Region that you choose, and the impact of the services that you select within the Region, to help you meet your sustainability goals.",
        "recommended_practices": [
            "Choose Regions close to users to reduce network latency",
            "Choose Regions near renewable energy sources",
            "Choose Regions with lower carbon intensity",
            "Scale down development and test environments when not in use"
        ]
    }
}

# Dictionary of Well-Architected lenses
LENSES = {
    "well-architected": {
        "name": "AWS Well-Architected Framework",
        "description": "The standard framework for reviewing AWS workloads.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization", "sustainability"]
    },
    "serverless": {
        "name": "Serverless Lens",
        "description": "The Serverless Lens helps you design, deploy, and architect your serverless applications following best practices.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "machine-learning": {
        "name": "Machine Learning Lens",
        "description": "The Machine Learning Lens helps you follow best practices for building machine learning workloads.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "saas": {
        "name": "SaaS Lens",
        "description": "The SaaS Lens helps you design, deploy, and architect your SaaS applications on AWS.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "games": {
        "name": "Games Industry Lens",
        "description": "The Games Industry Lens helps you understand how to design, architect, and operate games workloads.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "government": {
        "name": "Government Lens",
        "description": "The Government Lens helps you implement architectures that comply with governmental regulations.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "iot": {
        "name": "IoT Lens",
        "description": "The IoT Lens helps you implement best practices for your IoT workloads.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    },
    "financial-services": {
        "name": "Financial Services Industry Lens",
        "description": "The Financial Services Industry (FSI) Lens helps you design, deploy, and architect your FSI workloads.",
        "pillars": ["operational-excellence", "security", "reliability", "performance-efficiency", "cost-optimization"]
    }
}


def get_pillar_details(ctx: Context, *, pillar_name: str) -> Dict[str, Any]:
    """Get details for a Well-Architected pillar.
    
    Args:
        ctx: The context object.
        pillar_name: The name of the pillar to get details for.
    
    Returns:
        Dictionary with pillar details.
    """
    pillar_name = pillar_name.lower()
    if pillar_name not in PILLARS:
        return {
            "error": f"Pillar '{pillar_name}' not found",
            "available_pillars": list(PILLARS.keys())
        }
    
    pillar = PILLARS[pillar_name]
    
    # Find best practices for this pillar
    related_practices = {
        id: practice for id, practice in BEST_PRACTICES.items()
        if practice["pillar"] == pillar_name
    }
    
    return {
        "pillar": pillar,
        "related_practices": related_practices
    }


def get_lens_details(ctx: Context, *, lens_name: str) -> Dict[str, Any]:
    """Get details for a Well-Architected lens.
    
    Args:
        ctx: The context object.
        lens_name: The name of the lens to get details for.
    
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
    
    # Get details of pillars included in this lens
    lens_pillars = {
        pillar: PILLARS[pillar] 
        for pillar in lens["pillars"]
        if pillar in PILLARS
    }
    
    return {
        "lens": lens,
        "pillars": lens_pillars
    }


def get_best_practice(ctx: Context, *, practice_id: str) -> Dict[str, Any]:
    """Get details for a Well-Architected best practice.
    
    Args:
        ctx: The context object.
        practice_id: The ID of the best practice to get details for.
    
    Returns:
        Dictionary with best practice details.
    """
    practice_id = practice_id.upper()
    if practice_id not in BEST_PRACTICES:
        return {
            "error": f"Best practice '{practice_id}' not found",
            "available_practices": list(BEST_PRACTICES.keys())
        }
    
    practice = BEST_PRACTICES[practice_id]
    
    # Get the associated pillar
    pillar_name = practice.get("pillar")
    pillar = PILLARS.get(pillar_name, {})
    
    return {
        "practice": practice,
        "pillar": pillar
    }
