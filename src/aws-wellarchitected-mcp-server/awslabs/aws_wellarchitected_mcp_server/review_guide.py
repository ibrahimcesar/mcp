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

"""AWS Well-Architected Review Guide and Introduction."""

from typing import List
from .models import Pillar

def get_review_introduction() -> str:
    """Get introduction explaining what a Well-Architected Review is."""
    return """
# AWS Well-Architected Review

## What is a Well-Architected Review?

An AWS Well-Architected Review is a systematic evaluation of your cloud workload against AWS best practices across six key pillars. This review helps you:

- **Identify risks** in your current architecture
- **Discover opportunities** for improvement
- **Learn best practices** for cloud architecture
- **Create an action plan** for optimization

## The Six Pillars

1. **Operational Excellence** - Run and monitor systems to deliver business value
2. **Security** - Protect information, systems, and assets
3. **Reliability** - Recover from failures and meet demand
4. **Performance Efficiency** - Use computing resources efficiently
5. **Cost Optimization** - Avoid unnecessary costs
6. **Sustainability** - Minimize environmental impact

## Three-Phase Review Process

### 1. LEARN Phase
- Understand your workload's business context
- Document current architecture and requirements
- Identify stakeholders and success criteria

### 2. MEASURE Phase
- Evaluate your workload against best practices
- Assess each selected pillar comprehensively
- Identify gaps and improvement opportunities

### 3. IMPROVE Phase
- Create prioritized improvement plan
- Implement high-impact changes
- Track progress and measure success

## Review Benefits

- **Risk Mitigation**: Identify and address potential issues before they impact your business
- **Cost Optimization**: Discover opportunities to reduce costs while maintaining performance
- **Performance Enhancement**: Optimize your workload for better user experience
- **Security Strengthening**: Implement security best practices and controls
- **Operational Excellence**: Improve monitoring, automation, and incident response
- **Sustainability**: Reduce environmental impact of your cloud workload

## Time Investment

- **Learn Phase**: 4-8 hours
- **Measure Phase**: 1-3 days per pillar
- **Improve Phase**: 2-8 weeks (depending on scope)

The review is an investment in your workload's future success, reliability, and efficiency.
"""

def get_pillar_selection_guide() -> str:
    """Get guide for selecting pillars to review."""
    return """
# Pillar Selection Guide

Choose the pillars most relevant to your current priorities and concerns:

## Operational Excellence
**Choose if you want to improve:**
- Deployment processes and automation
- Monitoring and observability
- Incident response procedures
- Change management practices

## Security
**Choose if you want to assess:**
- Identity and access management
- Data protection and encryption
- Network security controls
- Incident response capabilities

## Reliability
**Choose if you want to evaluate:**
- System resilience and fault tolerance
- Disaster recovery capabilities
- Monitoring and alerting
- Service level objectives

## Performance Efficiency
**Choose if you want to optimize:**
- Resource selection and sizing
- Application performance
- Scalability and elasticity
- Technology choices

## Cost Optimization
**Choose if you want to:**
- Reduce unnecessary spending
- Improve resource utilization
- Implement cost controls
- Track and allocate costs

## Sustainability
**Choose if you want to:**
- Reduce environmental impact
- Optimize resource efficiency
- Implement sustainable practices
- Measure carbon footprint

## Recommendations

- **First-time review**: Start with 2-3 pillars most critical to your business
- **Comprehensive review**: Include all 6 pillars for complete assessment
- **Focused review**: Select 1-2 pillars for specific concerns or compliance requirements
"""

def format_pillar_options() -> str:
    """Format pillar options for user selection."""
    pillars = [
        ("1", Pillar.OPERATIONAL_EXCELLENCE, "Operational Excellence - Operations and monitoring"),
        ("2", Pillar.SECURITY, "Security - Protect data and systems"),
        ("3", Pillar.RELIABILITY, "Reliability - System resilience and recovery"),
        ("4", Pillar.PERFORMANCE_EFFICIENCY, "Performance Efficiency - Optimize resources"),
        ("5", Pillar.COST_OPTIMIZATION, "Cost Optimization - Manage costs effectively"),
        ("6", Pillar.SUSTAINABILITY, "Sustainability - Minimize environmental impact")
    ]
    
    options = "Please select the pillars you want to include in your review:\n\n"
    for num, pillar, description in pillars:
        options += f"{num}. {description}\n"
    
    options += "\nYou can select multiple pillars (e.g., 1,3,5) or 'all' for a comprehensive review."
    
    return options

def get_pillar_details(pillar: Pillar) -> str:
    """Get detailed information about a specific pillar."""
    details = {
        Pillar.OPERATIONAL_EXCELLENCE: {
            "focus": "Running and monitoring systems to deliver business value and continually improve processes",
            "key_areas": [
                "Organization and culture",
                "Prepare for operations",
                "Operate workloads",
                "Evolve operations"
            ],
            "typical_findings": [
                "Manual deployment processes",
                "Insufficient monitoring and alerting",
                "Lack of runbooks and procedures",
                "No automated incident response"
            ]
        },
        Pillar.SECURITY: {
            "focus": "Protecting information, systems, and assets while delivering business value",
            "key_areas": [
                "Security foundations",
                "Identity and access management",
                "Detection and response",
                "Infrastructure protection",
                "Data protection",
                "Application security"
            ],
            "typical_findings": [
                "Overprivileged access",
                "Unencrypted data",
                "Missing security monitoring",
                "Inadequate incident response"
            ]
        },
        Pillar.RELIABILITY: {
            "focus": "Ensuring workloads perform their intended functions correctly and consistently",
            "key_areas": [
                "Foundations and service limits",
                "Workload architecture",
                "Change management",
                "Failure management"
            ],
            "typical_findings": [
                "Single points of failure",
                "Insufficient backup and recovery",
                "Lack of chaos engineering",
                "No disaster recovery testing"
            ]
        },
        Pillar.PERFORMANCE_EFFICIENCY: {
            "focus": "Using computing resources efficiently to meet requirements",
            "key_areas": [
                "Architecture selection",
                "Compute and hardware",
                "Data management",
                "Networking and content delivery"
            ],
            "typical_findings": [
                "Oversized or undersized resources",
                "Inefficient data access patterns",
                "Suboptimal network configuration",
                "Lack of performance monitoring"
            ]
        },
        Pillar.COST_OPTIMIZATION: {
            "focus": "Avoiding unnecessary costs and maximizing return on investment",
            "key_areas": [
                "Cloud financial management",
                "Expenditure awareness",
                "Cost-effective resources",
                "Demand and supply management"
            ],
            "typical_findings": [
                "Unused or underutilized resources",
                "Lack of cost visibility",
                "No Reserved Instance strategy",
                "Missing cost optimization automation"
            ]
        },
        Pillar.SUSTAINABILITY: {
            "focus": "Minimizing environmental impact of cloud workloads",
            "key_areas": [
                "Region selection",
                "Demand alignment",
                "Software and architecture",
                "Data management",
                "Hardware and services"
            ],
            "typical_findings": [
                "Inefficient resource utilization",
                "Unnecessary data storage",
                "Non-optimized compute selection",
                "Lack of sustainability metrics"
            ]
        }
    }
    
    pillar_info = details[pillar]
    return f"""
## {pillar.value.replace('_', ' ').title()}

**Focus**: {pillar_info['focus']}

**Key Areas Assessed**:
{chr(10).join(f'- {area}' for area in pillar_info['key_areas'])}

**Typical Findings**:
{chr(10).join(f'- {finding}' for finding in pillar_info['typical_findings'])}
"""