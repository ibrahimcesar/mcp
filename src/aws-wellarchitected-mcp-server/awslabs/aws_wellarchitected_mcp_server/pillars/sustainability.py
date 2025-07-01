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

"""Sustainability pillar best practices."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import BestPractice
from typing import Dict

SUSTAINABILITY_BEST_PRACTICES: Dict[str, BestPractice] = {
    "SUS01-BP01": BestPractice(
        id="SUS01-BP01",
        title="Choose Region Based on Both Business Requirements and Sustainability Goals",
        pillar=Pillar.SUSTAINABILITY,
        description="Select AWS regions that align with both business requirements and sustainability objectives",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you consider sustainability factors when selecting regions?",
            "Are you aware of the carbon intensity of different AWS regions?",
            "Do you balance business requirements with environmental impact?",
            "Are you using regions with renewable energy sources?"
        ],
        implementation_guidance=[
            "Choose regions with lower carbon intensity when possible",
            "Consider AWS regions powered by renewable energy",
            "Balance latency, compliance, and sustainability requirements",
            "Use AWS Customer Carbon Footprint Tool for insights"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html",
        related_best_practices=["SUS02-BP01"],
        requires_user_input=True
    ),
    "SUS02-BP01": BestPractice(
        id="SUS02-BP01",
        title="Scale Infrastructure with User Load",
        pillar=Pillar.SUSTAINABILITY,
        description="Scale infrastructure dynamically to match user demand and minimize waste",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Does your infrastructure scale with user demand?",
            "Are you using auto-scaling to match capacity with load?",
            "Do you have mechanisms to scale down during low usage?",
            "Are you monitoring utilization to optimize scaling?"
        ],
        implementation_guidance=[
            "Implement auto-scaling groups for EC2 instances",
            "Use Application Load Balancer with target tracking",
            "Configure predictive scaling for predictable patterns",
            "Monitor CloudWatch metrics to optimize scaling policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html",
        related_best_practices=["SUS02-BP02", "SUS02-BP03"]
    ),
    "SUS02-BP02": BestPractice(
        id="SUS02-BP02",
        title="Align SLA with Sustainability Goals",
        pillar=Pillar.SUSTAINABILITY,
        description="Align service level agreements with sustainability objectives",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are your SLAs aligned with sustainability goals?",
            "Do you consider environmental impact in service commitments?",
            "Are you balancing performance requirements with sustainability?",
            "Do you communicate sustainability commitments to users?"
        ],
        implementation_guidance=[
            "Define SLAs that balance performance and sustainability",
            "Consider carbon-aware SLA tiers",
            "Implement sustainability metrics in service agreements",
            "Educate stakeholders on sustainability trade-offs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html",
        related_best_practices=["SUS02-BP01", "SUS02-BP04"],
        requires_user_input=True
    ),
    "SUS02-BP03": BestPractice(
        id="SUS02-BP03",
        title="Stop the Creation and Maintenance of Unused Assets",
        pillar=Pillar.SUSTAINABILITY,
        description="Eliminate creation and maintenance of unused or underutilized assets",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have processes to identify unused assets?",
            "Are you regularly decommissioning unused resources?",
            "Do you prevent creation of unnecessary assets?",
            "Are you tracking asset utilization over time?"
        ],
        implementation_guidance=[
            "Implement resource tagging for lifecycle management",
            "Use AWS Config to identify unused resources",
            "Set up automated cleanup for temporary resources",
            "Regular review and decommission unused assets"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html",
        related_best_practices=["SUS02-BP01", "SUS02-BP05"]
    ),
    "SUS02-BP04": BestPractice(
        id="SUS02-BP04",
        title="Optimize Areas of Code That Consume the Most Time or Resources",
        pillar=Pillar.SUSTAINABILITY,
        description="Focus optimization efforts on code areas with highest resource consumption",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you profile your applications to identify resource-intensive code?",
            "Are you optimizing the most resource-consuming functions?",
            "Do you measure the impact of code optimizations?",
            "Are you using efficient algorithms and data structures?"
        ],
        implementation_guidance=[
            "Use AWS X-Ray for application profiling",
            "Implement performance monitoring and alerting",
            "Optimize database queries and data access patterns",
            "Use efficient algorithms and minimize computational complexity"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a5.html",
        related_best_practices=["SUS02-BP02", "SUS02-BP06"]
    ),
    "SUS02-BP05": BestPractice(
        id="SUS02-BP05",
        title="Optimize Impact on Customer Devices and Equipment",
        pillar=Pillar.SUSTAINABILITY,
        description="Minimize the environmental impact on customer devices and equipment",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you consider the impact on customer devices?",
            "Are you optimizing for efficient client-side processing?",
            "Do you minimize data transfer to reduce device energy consumption?",
            "Are you designing for older or less powerful devices?"
        ],
        implementation_guidance=[
            "Optimize client-side code for efficiency",
            "Minimize data transfer and payload sizes",
            "Use efficient data formats and compression",
            "Design responsive interfaces that work on various devices"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a6.html",
        related_best_practices=["SUS02-BP03", "SUS02-BP07"],
        requires_user_input=True
    ),
    "SUS02-BP06": BestPractice(
        id="SUS02-BP06",
        title="Use Efficient Protocols and Minimize Data Transfer",
        pillar=Pillar.SUSTAINABILITY,
        description="Use efficient network protocols and minimize unnecessary data transfer",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using efficient network protocols?",
            "Do you minimize unnecessary data transfer?",
            "Are you using compression and caching effectively?",
            "Do you optimize API responses and data formats?"
        ],
        implementation_guidance=[
            "Use HTTP/2 and modern protocols",
            "Implement data compression and caching",
            "Optimize API responses and reduce payload sizes",
            "Use CDN to reduce data transfer distances"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a7.html",
        related_best_practices=["SUS02-BP04", "SUS03-BP01"]
    ),
    "SUS03-BP01": BestPractice(
        id="SUS03-BP01",
        title="Optimize Software and Architecture for Asynchronous and Scheduled Jobs",
        pillar=Pillar.SUSTAINABILITY,
        description="Design software to efficiently handle asynchronous and scheduled workloads",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using asynchronous processing where appropriate?",
            "Do you schedule non-urgent tasks for off-peak hours?",
            "Are you batching operations for efficiency?",
            "Do you use queuing systems for workload management?"
        ],
        implementation_guidance=[
            "Use SQS and SNS for asynchronous processing",
            "Schedule batch jobs during off-peak hours",
            "Implement efficient queuing and batching strategies",
            "Use EventBridge for event-driven architectures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html",
        related_best_practices=["SUS02-BP06", "SUS03-BP02"]
    ),
    "SUS03-BP02": BestPractice(
        id="SUS03-BP02",
        title="Remove or Refactor Workload Components with Low or No Use",
        pillar=Pillar.SUSTAINABILITY,
        description="Identify and remove or refactor underutilized workload components",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly review workload components for utilization?",
            "Are you removing or refactoring unused components?",
            "Do you have metrics to identify low-use features?",
            "Are you consolidating similar functionalities?"
        ],
        implementation_guidance=[
            "Use application monitoring to identify unused features",
            "Regularly review and remove dead code",
            "Consolidate similar functionalities",
            "Implement feature flags to control component usage"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html",
        related_best_practices=["SUS03-BP01", "SUS03-BP03"]
    ),
    "SUS03-BP03": BestPractice(
        id="SUS03-BP03",
        title="Optimize Areas of Code That Consume the Most Time or Resources",
        pillar=Pillar.SUSTAINABILITY,
        description="Focus optimization efforts on the most resource-intensive code areas",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you profile your code to identify resource hotspots?",
            "Are you optimizing the most resource-consuming functions?",
            "Do you measure the environmental impact of code changes?",
            "Are you using efficient algorithms and data structures?"
        ],
        implementation_guidance=[
            "Use profiling tools to identify performance bottlenecks",
            "Optimize database queries and data access patterns",
            "Use efficient algorithms and minimize computational complexity",
            "Implement caching for frequently accessed data"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html",
        related_best_practices=["SUS03-BP02", "SUS03-BP04"]
    ),
    "SUS03-BP04": BestPractice(
        id="SUS03-BP04",
        title="Optimize Impact on Customer Devices and Equipment",
        pillar=Pillar.SUSTAINABILITY,
        description="Design software to minimize impact on customer devices and equipment",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you consider the impact on customer device performance?",
            "Are you optimizing client-side resource usage?",
            "Do you minimize battery drain on mobile devices?",
            "Are you designing for device longevity?"
        ],
        implementation_guidance=[
            "Optimize client-side code for performance and battery life",
            "Minimize background processing and network requests",
            "Use efficient rendering and UI frameworks",
            "Design for backward compatibility with older devices"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a5.html",
        related_best_practices=["SUS03-BP03", "SUS03-BP05"],
        requires_user_input=True
    ),
    "SUS03-BP05": BestPractice(
        id="SUS03-BP05",
        title="Use Programming Languages and Frameworks That Support Sustainability Goals",
        pillar=Pillar.SUSTAINABILITY,
        description="Choose programming languages and frameworks that align with sustainability objectives",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you consider energy efficiency when choosing programming languages?",
            "Are you using frameworks that optimize resource usage?",
            "Do you evaluate the environmental impact of technology choices?",
            "Are you staying current with sustainable development practices?"
        ],
        implementation_guidance=[
            "Choose energy-efficient programming languages when appropriate",
            "Use frameworks that optimize resource utilization",
            "Consider the full lifecycle impact of technology choices",
            "Stay informed about sustainable development practices"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a6.html",
        related_best_practices=["SUS03-BP04"],
        requires_user_input=True
    ),
    "SUS04-BP01": BestPractice(
        id="SUS04-BP01",
        title="Implement a Data Classification Policy",
        pillar=Pillar.SUSTAINABILITY,
        description="Classify data to optimize storage and processing based on business value and access patterns",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a data classification policy?",
            "Are you categorizing data based on business value and access patterns?",
            "Do you apply different storage strategies based on data classification?",
            "Are data retention policies aligned with business requirements?"
        ],
        implementation_guidance=[
            "Develop data classification policies based on business value",
            "Implement automated data classification tools",
            "Use appropriate storage classes for different data types",
            "Regularly review and update data classifications"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html",
        related_best_practices=["SUS04-BP02", "SUS04-BP03"],
        requires_user_input=True
    ),
    "SUS04-BP02": BestPractice(
        id="SUS04-BP02",
        title="Use Technologies That Support Data Access and Storage Patterns",
        pillar=Pillar.SUSTAINABILITY,
        description="Select storage technologies that align with data access patterns to optimize efficiency",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using storage technologies that match your access patterns?",
            "Do you use different storage tiers for different data types?",
            "Are you leveraging intelligent tiering for cost and efficiency?",
            "Do you regularly review storage usage patterns?"
        ],
        implementation_guidance=[
            "Use S3 Intelligent Tiering for automatic optimization",
            "Choose appropriate storage classes based on access patterns",
            "Implement lifecycle policies for data management",
            "Monitor and analyze storage access patterns"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a3.html",
        related_best_practices=["SUS04-BP01", "SUS04-BP04"]
    ),
    "SUS04-BP03": BestPractice(
        id="SUS04-BP03",
        title="Use Lifecycle Policies to Delete Unnecessary Data",
        pillar=Pillar.SUSTAINABILITY,
        description="Implement lifecycle policies to automatically delete data that is no longer needed",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have lifecycle policies to manage data retention?",
            "Are you automatically deleting unnecessary data?",
            "Do you have clear data retention requirements?",
            "Are you monitoring data growth and cleanup effectiveness?"
        ],
        implementation_guidance=[
            "Implement S3 lifecycle policies for automatic data management",
            "Define clear data retention policies",
            "Use automated deletion for temporary and log data",
            "Monitor data growth and cleanup effectiveness"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html",
        related_best_practices=["SUS04-BP01", "SUS04-BP05"]
    ),
    "SUS04-BP04": BestPractice(
        id="SUS04-BP04",
        title="Minimize Data Movement Across Networks",
        pillar=Pillar.SUSTAINABILITY,
        description="Reduce unnecessary data movement to minimize network resource consumption",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you minimize unnecessary data movement?",
            "Are you using data locality principles in your architecture?",
            "Do you cache frequently accessed data close to consumers?",
            "Are you optimizing data transfer patterns?"
        ],
        implementation_guidance=[
            "Use CloudFront for content delivery and caching",
            "Implement data locality in application design",
            "Use regional data replication strategically",
            "Optimize API responses to minimize data transfer"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html",
        related_best_practices=["SUS04-BP02", "SUS04-BP06"]
    ),
    "SUS04-BP05": BestPractice(
        id="SUS04-BP05",
        title="Back Up Data Only When Difficult to Recreate",
        pillar=Pillar.SUSTAINABILITY,
        description="Implement selective backup strategies focusing on data that is difficult or impossible to recreate",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a selective backup strategy?",
            "Are you backing up only critical and irreplaceable data?",
            "Do you regularly review backup requirements?",
            "Are you using efficient backup and recovery methods?"
        ],
        implementation_guidance=[
            "Classify data based on backup necessity",
            "Use incremental and differential backup strategies",
            "Implement point-in-time recovery for critical data",
            "Regularly test and validate backup procedures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html",
        related_best_practices=["SUS04-BP03", "SUS04-BP07"],
        requires_user_input=True
    ),
    "SUS04-BP06": BestPractice(
        id="SUS04-BP06",
        title="Use Shared File Systems or Object Storage to Access Common Data",
        pillar=Pillar.SUSTAINABILITY,
        description="Use shared storage solutions to avoid data duplication and improve efficiency",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using shared storage for common data?",
            "Do you avoid unnecessary data duplication?",
            "Are you using centralized data repositories?",
            "Do you have strategies to prevent data silos?"
        ],
        implementation_guidance=[
            "Use EFS for shared file system access",
            "Implement centralized data lakes with S3",
            "Use shared databases for common data",
            "Avoid data duplication across applications"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a7.html",
        related_best_practices=["SUS04-BP04", "SUS04-BP08"]
    ),
    "SUS04-BP07": BestPractice(
        id="SUS04-BP07",
        title="Minimize Data Production",
        pillar=Pillar.SUSTAINABILITY,
        description="Reduce unnecessary data generation and collection to minimize storage and processing requirements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you minimize unnecessary data production?",
            "Are you collecting only essential data?",
            "Do you have data minimization policies?",
            "Are you regularly reviewing data collection practices?"
        ],
        implementation_guidance=[
            "Implement data minimization principles",
            "Collect only necessary data for business purposes",
            "Use sampling techniques for large datasets",
            "Regularly review and optimize data collection"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a8.html",
        related_best_practices=["SUS04-BP05", "SUS04-BP08"],
        requires_user_input=True
    ),
    "SUS04-BP08": BestPractice(
        id="SUS04-BP08",
        title="Use Compression and Deduplication",
        pillar=Pillar.SUSTAINABILITY,
        description="Implement compression and deduplication to reduce storage requirements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using compression for data storage?",
            "Do you implement deduplication strategies?",
            "Are you using efficient data formats?",
            "Do you regularly optimize data storage efficiency?"
        ],
        implementation_guidance=[
            "Use compression for data at rest and in transit",
            "Implement deduplication for backup and archive data",
            "Choose efficient data formats and encodings",
            "Use columnar storage formats for analytics workloads"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a9.html",
        related_best_practices=["SUS04-BP06", "SUS04-BP07"]
    ),
    "SUS05-BP01": BestPractice(
        id="SUS05-BP01",
        title="Use the Minimum Amount of Hardware to Meet Your Needs",
        pillar=Pillar.SUSTAINABILITY,
        description="Right-size hardware resources to meet requirements without over-provisioning",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using the minimum hardware necessary?",
            "Do you regularly right-size your resources?",
            "Are you monitoring resource utilization?",
            "Do you have processes to identify over-provisioned resources?"
        ],
        implementation_guidance=[
            "Use AWS Compute Optimizer for right-sizing recommendations",
            "Monitor resource utilization with CloudWatch",
            "Implement auto-scaling to match demand",
            "Regularly review and optimize resource allocation"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a2.html",
        related_best_practices=["SUS05-BP02", "SUS05-BP03"]
    ),
    "SUS05-BP02": BestPractice(
        id="SUS05-BP02",
        title="Use Instance Types with the Least Impact",
        pillar=Pillar.SUSTAINABILITY,
        description="Select instance types that provide the best performance per unit of environmental impact",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you consider environmental impact when selecting instance types?",
            "Are you using energy-efficient instance types?",
            "Do you evaluate performance per watt for your workloads?",
            "Are you using AWS Graviton processors where appropriate?"
        ],
        implementation_guidance=[
            "Use AWS Graviton processors for better performance per watt",
            "Choose instance types optimized for your workload characteristics",
            "Consider ARM-based instances for cost and energy efficiency",
            "Evaluate newer generation instances for efficiency improvements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a3.html",
        related_best_practices=["SUS05-BP01", "SUS05-BP04"]
    ),
    "SUS05-BP03": BestPractice(
        id="SUS05-BP03",
        title="Use Managed Services",
        pillar=Pillar.SUSTAINABILITY,
        description="Leverage AWS managed services to improve resource efficiency and reduce operational overhead",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using managed services where appropriate?",
            "Do you leverage serverless architectures?",
            "Are you using managed databases and storage services?",
            "Do you consider the efficiency benefits of managed services?"
        ],
        implementation_guidance=[
            "Use RDS instead of self-managed databases",
            "Leverage Lambda for serverless compute",
            "Use managed container services like Fargate",
            "Consider managed analytics and ML services"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html",
        related_best_practices=["SUS05-BP01", "SUS05-BP04"]
    ),
    "SUS05-BP04": BestPractice(
        id="SUS05-BP04",
        title="Optimize Your Use of Hardware-Based Compute Accelerators",
        pillar=Pillar.SUSTAINABILITY,
        description="Use hardware accelerators efficiently to maximize performance per unit of energy consumed",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using hardware accelerators efficiently?",
            "Do you optimize workloads for GPU or other accelerators?",
            "Are you sharing accelerator resources effectively?",
            "Do you monitor accelerator utilization?"
        ],
        implementation_guidance=[
            "Use GPU instances for appropriate workloads like ML training",
            "Optimize code for accelerator architectures",
            "Share accelerator resources across multiple workloads",
            "Monitor accelerator utilization and optimize usage"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a5.html",
        related_best_practices=["SUS05-BP02", "SUS05-BP03"]
    ),
    "SUS06-BP01": BestPractice(
        id="SUS06-BP01",
        title="Adopt Methods That Can Rapidly Introduce Sustainability Improvements",
        pillar=Pillar.SUSTAINABILITY,
        description="Use development methods that enable rapid implementation of sustainability improvements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have processes to rapidly implement sustainability improvements?",
            "Are sustainability considerations integrated into your development lifecycle?",
            "Do you use agile methods for sustainability initiatives?",
            "Are you measuring and tracking sustainability improvements?"
        ],
        implementation_guidance=[
            "Integrate sustainability into agile development processes",
            "Use continuous integration for sustainability improvements",
            "Implement rapid prototyping for green initiatives",
            "Establish feedback loops for sustainability metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a1.html",
        related_best_practices=["SUS06-BP02", "SUS06-BP03"],
        requires_user_input=True
    ),
    "SUS06-BP02": BestPractice(
        id="SUS06-BP02",
        title="Keep Your Workload Up-to-Date",
        pillar=Pillar.SUSTAINABILITY,
        description="Maintain current versions of software and services to benefit from efficiency improvements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you keep your workload components up-to-date?",
            "Are you regularly updating to newer, more efficient versions?",
            "Do you have processes for evaluating and adopting updates?",
            "Are you tracking the sustainability benefits of updates?"
        ],
        implementation_guidance=[
            "Establish regular update cycles for all components",
            "Monitor AWS service announcements for efficiency improvements",
            "Test updates in non-production environments first",
            "Track performance and efficiency gains from updates"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a2.html",
        related_best_practices=["SUS06-BP01", "SUS06-BP04"]
    ),
    "SUS06-BP03": BestPractice(
        id="SUS06-BP03",
        title="Increase Utilization of Build Environments",
        pillar=Pillar.SUSTAINABILITY,
        description="Optimize build environments to maximize utilization and minimize waste",
        risk_level=RiskLevel.LOW,
        questions=[
            "Are you optimizing build environment utilization?",
            "Do you use shared or containerized build environments?",
            "Are you minimizing idle time in build processes?",
            "Do you use efficient build tools and practices?"
        ],
        implementation_guidance=[
            "Use containerized build environments",
            "Implement build caching and parallelization",
            "Share build resources across teams",
            "Use efficient CI/CD tools and practices"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a3.html",
        related_best_practices=["SUS06-BP01", "SUS06-BP05"]
    ),
    "SUS06-BP04": BestPractice(
        id="SUS06-BP04",
        title="Use Managed Device Farms for Testing",
        pillar=Pillar.SUSTAINABILITY,
        description="Use managed device farms to reduce the environmental impact of testing",
        risk_level=RiskLevel.LOW,
        questions=[
            "Are you using managed device farms for testing?",
            "Do you optimize test execution to minimize resource usage?",
            "Are you sharing testing resources efficiently?",
            "Do you use cloud-based testing services?"
        ],
        implementation_guidance=[
            "Use AWS Device Farm for mobile testing",
            "Implement efficient test strategies to minimize execution time",
            "Use cloud-based testing services instead of physical devices",
            "Share testing resources across development teams"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a4.html",
        related_best_practices=["SUS06-BP02", "SUS06-BP05"]
    ),
    "SUS06-BP05": BestPractice(
        id="SUS06-BP05",
        title="Use Automation to Reduce the Environmental Impact of Development and Test",
        pillar=Pillar.SUSTAINABILITY,
        description="Implement automation to reduce manual effort and improve efficiency in development and testing",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using automation to reduce manual effort?",
            "Do you have automated testing and deployment processes?",
            "Are you using infrastructure as code?",
            "Do you automate resource provisioning and cleanup?"
        ],
        implementation_guidance=[
            "Implement automated testing and deployment pipelines",
            "Use infrastructure as code for consistent provisioning",
            "Automate resource cleanup after testing",
            "Use automated scaling and optimization tools"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a5.html",
        related_best_practices=["SUS06-BP03", "SUS06-BP04"]
    )
}