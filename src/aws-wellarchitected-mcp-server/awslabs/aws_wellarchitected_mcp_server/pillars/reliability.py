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

"""Reliability pillar best practices."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import BestPractice
from typing import Dict

RELIABILITY_BEST_PRACTICES: Dict[str, BestPractice] = {
    # Reliability
    "REL01-BP01": BestPractice(
        id="REL01-BP01",
        title="Become Aware of Service Quotas and Constraints",
        pillar=Pillar.RELIABILITY,
        description="Become aware of service quotas and constraints for your workload architecture",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you aware of service quotas that affect your workload?",
            "Do you understand the constraints of AWS services you use?",
            "Have you documented quota requirements for your architecture?",
            "Do you monitor quota usage across your workload?"
        ],
        implementation_guidance=[
            "Use AWS Service Quotas console to view current quotas",
            "Document quota requirements during architecture design",
            "Understand both soft and hard limits for services",
            "Consider quotas when designing for scale"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.html",
        related_best_practices=["REL01-BP02", "REL01-BP04"]
    ),
    "REL01-BP02": BestPractice(
        id="REL01-BP02",
        title="Manage Service Quotas Across Accounts and Regions",
        pillar=Pillar.RELIABILITY,
        description="Manage service quotas across accounts and regions",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you manage quotas across multiple accounts and regions?",
            "Are quota increases requested proactively?",
            "Do you have a process for quota management?",
            "Are quotas considered in disaster recovery planning?"
        ],
        implementation_guidance=[
            "Implement centralized quota management across accounts",
            "Request quota increases before reaching limits",
            "Use AWS Organizations for quota management",
            "Consider quotas in multi-region deployments"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_limits_considered.html",
        related_best_practices=["REL01-BP01", "REL01-BP03"]
    ),
    "REL01-BP03": BestPractice(
        id="REL01-BP03",
        title="Accommodate Fixed Service Quotas and Constraints",
        pillar=Pillar.RELIABILITY,
        description="Accommodate fixed service quotas and constraints through architecture",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Have you identified fixed quotas that cannot be increased?",
            "Is your architecture designed around fixed constraints?",
            "Do you have workarounds for fixed limitations?",
            "Are fixed quotas documented in your architecture decisions?"
        ],
        implementation_guidance=[
            "Identify and document fixed service quotas",
            "Design architecture to work within fixed constraints",
            "Implement sharding or partitioning strategies",
            "Use multiple regions to work around fixed limits"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_aware_fixed_limits.html",
        related_best_practices=["REL01-BP02"]
    ),
    "REL01-BP04": BestPractice(
        id="REL01-BP04",
        title="Monitor and Manage Quotas",
        pillar=Pillar.RELIABILITY,
        description="Monitor and manage quotas to prevent service disruptions",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you monitor quota usage across your services?",
            "Are there alerts for approaching quota limits?",
            "Do you have automated quota management?",
            "Are quota metrics included in operational dashboards?"
        ],
        implementation_guidance=[
            "Use CloudWatch to monitor quota usage",
            "Set up alerts for quota thresholds",
            "Implement automated quota increase requests",
            "Include quota metrics in operational dashboards"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_monitor_manage_limits.html",
        related_best_practices=["REL01-BP01", "REL01-BP05"]
    ),
    "REL01-BP05": BestPractice(
        id="REL01-BP05",
        title="Automate Quota Monitoring",
        pillar=Pillar.RELIABILITY,
        description="Automate quota monitoring to proactively manage service limits",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated quota monitoring in place?",
            "Are quota violations automatically detected and reported?",
            "Do you have automated responses to quota issues?",
            "Are quota trends analyzed for capacity planning?"
        ],
        implementation_guidance=[
            "Implement automated quota monitoring solutions",
            "Use AWS Config rules for quota compliance",
            "Set up automated notifications for quota issues",
            "Analyze quota trends for capacity planning"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_automated_monitor_limits.html",
        related_best_practices=["REL01-BP04", "REL01-BP06"]
    ),
    "REL01-BP06": BestPractice(
        id="REL01-BP06",
        title="Ensure Sufficient Buffer for Quotas",
        pillar=Pillar.RELIABILITY,
        description="Ensure sufficient buffer between current usage and service quotas",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you maintain sufficient buffer between usage and quotas?",
            "Are buffers calculated based on growth projections?",
            "Do you have different buffer strategies for different services?",
            "Are buffers adjusted based on business requirements?"
        ],
        implementation_guidance=[
            "Maintain 20-30% buffer between usage and quotas",
            "Calculate buffers based on growth projections",
            "Adjust buffers based on service criticality",
            "Review and update buffer strategies regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_suff_buffer_limits.html",
        related_best_practices=["REL01-BP05"]
    ),
    "REL02-BP01": BestPractice(
        id="REL02-BP01",
        title="Ensure Highly Available Network Connectivity for Users",
        pillar=Pillar.RELIABILITY,
        description="Ensure highly available network connectivity for users",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have highly available network connectivity for users?",
            "Are there multiple paths for user connectivity?",
            "Do you use multiple edge locations or CDN?",
            "Are network failures handled gracefully?"
        ],
        implementation_guidance=[
            "Use Amazon CloudFront for global content delivery",
            "Implement multiple connectivity paths",
            "Use AWS Global Accelerator for improved performance",
            "Design for network partition tolerance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ha_conn_users.html",
        related_best_practices=["REL02-BP02"]
    ),
    "REL02-BP02": BestPractice(
        id="REL02-BP02",
        title="Ensure Highly Available Network Connectivity Between Systems",
        pillar=Pillar.RELIABILITY,
        description="Ensure highly available network connectivity between systems in AWS and on-premises",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have redundant network connections between systems?",
            "Are there multiple paths for inter-system communication?",
            "Do you use multiple VPN or Direct Connect connections?",
            "Are network dependencies documented and managed?"
        ],
        implementation_guidance=[
            "Use multiple AWS Direct Connect connections",
            "Implement redundant VPN connections",
            "Use AWS Transit Gateway for complex topologies",
            "Design for network redundancy across availability zones"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ha_conn_private_networks.html",
        related_best_practices=["REL02-BP01", "REL02-BP03"]
    ),
    "REL02-BP03": BestPractice(
        id="REL02-BP03",
        title="Ensure IP Subnet Allocation Accounts for Expansion and Availability",
        pillar=Pillar.RELIABILITY,
        description="Ensure IP subnet allocation accounts for expansion and availability",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do your IP subnets allow for future expansion?",
            "Are subnets distributed across multiple availability zones?",
            "Do you have sufficient IP address space?",
            "Are subnet allocations documented and managed?"
        ],
        implementation_guidance=[
            "Plan IP address space for future growth",
            "Distribute subnets across multiple availability zones",
            "Use appropriate CIDR block sizes",
            "Document and manage subnet allocations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ip_subnet_allocation.html",
        related_best_practices=["REL02-BP02", "REL02-BP04"]
    ),
    "REL02-BP04": BestPractice(
        id="REL02-BP04",
        title="Prefer Hub-and-Spoke Topologies over Many-to-Many Mesh",
        pillar=Pillar.RELIABILITY,
        description="Prefer hub-and-spoke topologies over many-to-many mesh for network design",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you use hub-and-spoke network topologies where appropriate?",
            "Are complex mesh networks avoided when possible?",
            "Do you use AWS Transit Gateway for hub-and-spoke designs?",
            "Are network topologies optimized for manageability?"
        ],
        implementation_guidance=[
            "Use AWS Transit Gateway for hub-and-spoke topologies",
            "Avoid complex many-to-many mesh networks",
            "Centralize network management and routing",
            "Simplify network troubleshooting and monitoring"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_prefer_hub_and_spoke.html",
        related_best_practices=["REL02-BP03"]
    ),
    "REL02-BP05": BestPractice(
        id="REL02-BP05",
        title="Enforce Non-overlapping Private IP Address Ranges",
        pillar=Pillar.RELIABILITY,
        description="Enforce non-overlapping private IP address ranges in multiple private address spaces",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you enforce non-overlapping IP address ranges?",
            "Are IP address allocations centrally managed?",
            "Do you have processes to prevent IP conflicts?",
            "Are IP address ranges documented across environments?"
        ],
        implementation_guidance=[
            "Implement centralized IP address management",
            "Use non-overlapping CIDR blocks across VPCs",
            "Document IP address allocations",
            "Implement automated IP conflict detection"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_non_overlap_ip.html",
        related_best_practices=["REL02-BP03"]
    ),
    "REL03-BP01": BestPractice(
        id="REL03-BP01",
        title="Choose How to Segment Your Workload",
        pillar=Pillar.RELIABILITY,
        description="Choose how to segment your workload to balance reliability and cost",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you chosen appropriate segmentation for your workload?",
            "Do you balance between monolith, SOA, and microservices?",
            "Are segmentation decisions based on business requirements?",
            "Do you consider operational complexity in segmentation?"
        ],
        implementation_guidance=[
            "Choose segmentation based on business domains",
            "Balance reliability benefits with operational complexity",
            "Consider team structure and capabilities",
            "Start with larger segments and decompose as needed"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_monolith_soa_microservice.html",
        related_best_practices=["REL03-BP02"]
    ),
    "REL03-BP02": BestPractice(
        id="REL03-BP02",
        title="Build Services Focused on Specific Business Domains",
        pillar=Pillar.RELIABILITY,
        description="Build services focused on specific business domains and functions",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are services aligned with business domains?",
            "Do services have clear business purposes?",
            "Are service boundaries well-defined?",
            "Do services avoid cross-domain dependencies?"
        ],
        implementation_guidance=[
            "Align services with business capabilities",
            "Use domain-driven design principles",
            "Minimize cross-domain dependencies",
            "Ensure services have clear ownership"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_business_domains.html",
        related_best_practices=["REL03-BP01", "REL03-BP03"]
    ),
    "REL03-BP03": BestPractice(
        id="REL03-BP03",
        title="Provide Service Contracts per API",
        pillar=Pillar.RELIABILITY,
        description="Provide service contracts per API to ensure reliable service interactions",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have well-defined API contracts?",
            "Are API versions managed properly?",
            "Do contracts specify SLAs and error handling?",
            "Are breaking changes managed through versioning?"
        ],
        implementation_guidance=[
            "Define clear API contracts and specifications",
            "Implement proper API versioning strategies",
            "Specify SLAs and error handling in contracts",
            "Use API gateways for contract enforcement"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_api_contracts.html",
        related_best_practices=["REL03-BP02"]
    ),
    "REL04-BP01": BestPractice(
        id="REL04-BP01",
        title="Identify Which Kind of Distributed System Failure to Protect Against",
        pillar=Pillar.RELIABILITY,
        description="Identify which kind of distributed system failure to protect against",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified potential failure modes in your distributed system?",
            "Do you understand cascading failure scenarios?",
            "Are failure modes documented and analyzed?",
            "Do you have strategies for each type of failure?"
        ],
        implementation_guidance=[
            "Conduct failure mode analysis for distributed systems",
            "Identify single points of failure",
            "Analyze cascading failure scenarios",
            "Document failure modes and mitigation strategies"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html",
        related_best_practices=["REL04-BP02"]
    ),
    "REL04-BP02": BestPractice(
        id="REL04-BP02",
        title="Implement Loosely Coupled Dependencies",
        pillar=Pillar.RELIABILITY,
        description="Implement loosely coupled dependencies to improve system resilience",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are your system components loosely coupled?",
            "Do you use asynchronous communication where appropriate?",
            "Are dependencies managed to prevent cascading failures?",
            "Do you use queues and buffers to decouple components?"
        ],
        implementation_guidance=[
            "Use message queues for asynchronous communication",
            "Implement event-driven architectures",
            "Use Amazon SQS and SNS for decoupling",
            "Avoid tight coupling between services"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html",
        related_best_practices=["REL04-BP01", "REL04-BP03"]
    ),
    "REL04-BP03": BestPractice(
        id="REL04-BP03",
        title="Do Constant Work",
        pillar=Pillar.RELIABILITY,
        description="Do constant work to avoid system instability from varying loads",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do your systems perform constant work to maintain stability?",
            "Are resources pre-warmed and ready?",
            "Do you avoid cold start scenarios?",
            "Are system resources consistently utilized?"
        ],
        implementation_guidance=[
            "Pre-warm resources and connections",
            "Use connection pooling and keep-alive mechanisms",
            "Implement background processing for consistency",
            "Avoid large variations in resource utilization"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_constant_work.html",
        related_best_practices=["REL04-BP02"]
    ),
    "REL04-BP04": BestPractice(
        id="REL04-BP04",
        title="Make All Responses Idempotent",
        pillar=Pillar.RELIABILITY,
        description="Make all responses idempotent to handle retries safely",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are your API operations idempotent?",
            "Can operations be safely retried?",
            "Do you handle duplicate requests properly?",
            "Are idempotency keys used where appropriate?"
        ],
        implementation_guidance=[
            "Design APIs to be idempotent",
            "Use idempotency keys for critical operations",
            "Handle duplicate requests gracefully",
            "Implement proper state management for retries"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_idempotent.html",
        related_best_practices=["REL05-BP04"]
    ),
    "REL05-BP01": BestPractice(
        id="REL05-BP01",
        title="Implement Graceful Degradation",
        pillar=Pillar.RELIABILITY,
        description="Implement graceful degradation to transform applicable hard dependencies into soft dependencies",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Does your system degrade gracefully when dependencies fail?",
            "Are non-critical features disabled during failures?",
            "Do you maintain core functionality during partial outages?",
            "Are degradation strategies documented and tested?"
        ],
        implementation_guidance=[
            "Identify critical vs non-critical functionality",
            "Implement feature flags for graceful degradation",
            "Use circuit breakers to prevent cascading failures",
            "Test degradation scenarios regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html",
        related_best_practices=["REL05-BP02"]
    ),
    "REL05-BP02": BestPractice(
        id="REL05-BP02",
        title="Throttle Requests",
        pillar=Pillar.RELIABILITY,
        description="Throttle requests to protect your workload and dependent services",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you implement request throttling?",
            "Are rate limits appropriate for your system capacity?",
            "Do you protect downstream services from overload?",
            "Are throttling policies documented and monitored?"
        ],
        implementation_guidance=[
            "Implement API rate limiting",
            "Use AWS API Gateway for throttling",
            "Set appropriate rate limits based on capacity",
            "Monitor and adjust throttling policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_throttle_requests.html",
        related_best_practices=["REL05-BP01", "REL05-BP03"]
    ),
    "REL05-BP03": BestPractice(
        id="REL05-BP03",
        title="Control and Limit Retry Calls",
        pillar=Pillar.RELIABILITY,
        description="Control and limit retry calls to avoid overwhelming systems",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you implement proper retry logic with backoff?",
            "Are retry attempts limited to prevent system overload?",
            "Do you use exponential backoff and jitter?",
            "Are retry policies appropriate for different error types?"
        ],
        implementation_guidance=[
            "Implement exponential backoff with jitter",
            "Limit maximum retry attempts",
            "Use different retry strategies for different error types",
            "Implement circuit breakers to stop retries when appropriate"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_limit_retries.html",
        related_best_practices=["REL05-BP02", "REL05-BP04"]
    ),
    "REL05-BP04": BestPractice(
        id="REL05-BP04",
        title="Fail Fast and Limit Queues",
        pillar=Pillar.RELIABILITY,
        description="Fail fast and limit queues to prevent resource exhaustion",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do your systems fail fast when overloaded?",
            "Are queue sizes limited to prevent resource exhaustion?",
            "Do you reject requests when capacity is exceeded?",
            "Are failure responses quick and informative?"
        ],
        implementation_guidance=[
            "Implement fast failure mechanisms",
            "Limit queue sizes to prevent memory exhaustion",
            "Use dead letter queues for failed messages",
            "Provide clear error messages for failures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_fail_fast.html",
        related_best_practices=["REL05-BP03", "REL04-BP04"]
    ),
    "REL05-BP05": BestPractice(
        id="REL05-BP05",
        title="Set Client Timeouts",
        pillar=Pillar.RELIABILITY,
        description="Set client timeouts to avoid waiting indefinitely for responses",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you set appropriate timeouts for client requests?",
            "Are timeout values based on service SLAs?",
            "Do you handle timeout scenarios gracefully?",
            "Are timeout configurations documented and monitored?"
        ],
        implementation_guidance=[
            "Set appropriate timeout values for all client calls",
            "Base timeouts on service SLAs and expected response times",
            "Implement timeout handling and fallback mechanisms",
            "Monitor timeout occurrences and adjust as needed"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.html",
        related_best_practices=["REL05-BP04"]
    ),
    "REL05-BP06": BestPractice(
        id="REL05-BP06",
        title="Make Services Stateless Where Possible",
        pillar=Pillar.RELIABILITY,
        description="Make services stateless where possible to improve scalability and resilience",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are your services designed to be stateless?",
            "Is session state externalized from application servers?",
            "Can any instance handle any request?",
            "Are stateful components minimized and well-managed?"
        ],
        implementation_guidance=[
            "Design services to be stateless",
            "Use external stores for session state (Redis, DynamoDB)",
            "Implement horizontal scaling for stateless services",
            "Minimize and isolate stateful components"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_stateless.html",
        related_best_practices=["REL04-BP02"]
    ),
    "REL05-BP07": BestPractice(
        id="REL05-BP07",
        title="Implement Emergency Levers",
        pillar=Pillar.RELIABILITY,
        description="Implement emergency levers to quickly mitigate impact during incidents",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have emergency levers to quickly mitigate issues?",
            "Can you quickly disable features or redirect traffic?",
            "Are emergency procedures documented and tested?",
            "Do you have automated emergency response capabilities?"
        ],
        implementation_guidance=[
            "Implement feature flags for emergency feature disabling",
            "Use traffic routing for emergency traffic redirection",
            "Create emergency runbooks and procedures",
            "Test emergency levers regularly"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_emergency_levers.html",
        related_best_practices=["REL05-BP01"]
    ),
    "REL06-BP01": BestPractice(
        id="REL06-BP01",
        title="Monitor All Components for the Workload",
        pillar=Pillar.RELIABILITY,
        description="Monitor all components for the workload to understand their health and performance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you monitoring all components of your workload?",
            "Do you have visibility into the health of all system components?",
            "Are monitoring metrics comprehensive and actionable?",
            "Do you monitor both infrastructure and application layers?"
        ],
        implementation_guidance=[
            "Use CloudWatch to monitor AWS resources and custom metrics",
            "Implement application-level monitoring and logging",
            "Monitor both technical and business metrics",
            "Set up comprehensive dashboards for system visibility"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_monitor_resources.html",
        related_best_practices=["REL06-BP02", "REL06-BP07"]
    ),
    "REL06-BP02": BestPractice(
        id="REL06-BP02",
        title="Define and Calculate Metrics",
        pillar=Pillar.RELIABILITY,
        description="Store log data and apply filters where necessary to calculate metrics",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you define and calculate meaningful metrics?",
            "Are metrics aligned with business objectives?",
            "Do you have both technical and business metrics?"
        ],
        implementation_guidance=[
            "Define KPIs and SLIs for your workload",
            "Use CloudWatch custom metrics",
            "Calculate business and technical metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_define_metrics.html"
    ),
    "REL06-BP03": BestPractice(
        id="REL06-BP03",
        title="Send Notifications Based on Monitoring",
        pillar=Pillar.RELIABILITY,
        description="Organizations that need to know when operations are impacted receive notifications",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you send notifications based on monitoring data?",
            "Are notifications sent to appropriate stakeholders?",
            "Are notification thresholds properly configured?"
        ],
        implementation_guidance=[
            "Configure CloudWatch alarms with appropriate thresholds",
            "Use SNS for notification delivery",
            "Ensure notifications reach the right people"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_send_notifications.html"
    ),
    "REL06-BP04": BestPractice(
        id="REL06-BP04",
        title="Automate Responses to Events",
        pillar=Pillar.RELIABILITY,
        description="Use automation to take action when an event is detected",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you automate responses to monitoring events?",
            "Are automated responses tested and validated?",
            "Do you have safeguards for automated actions?"
        ],
        implementation_guidance=[
            "Use Lambda functions for automated responses",
            "Implement Systems Manager automation",
            "Test automated responses regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_automate_responses.html"
    ),
    "REL07-BP01": BestPractice(
        id="REL07-BP01",
        title="Use Auto Scaling or Other Scaling Policies",
        pillar=Pillar.RELIABILITY,
        description="Use auto scaling or other scaling policies to adapt to changes in demand",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use auto scaling to adapt to demand changes?",
            "Are scaling policies appropriate for your workload patterns?",
            "Do you scale both horizontally and vertically as needed?",
            "Are scaling actions monitored and optimized?"
        ],
        implementation_guidance=[
            "Use Auto Scaling Groups for EC2 instances",
            "Implement Application Auto Scaling for other services",
            "Configure appropriate scaling policies and thresholds",
            "Monitor scaling actions and optimize policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html",
        related_best_practices=["REL07-BP02", "REL07-BP03"]
    ),
    "REL07-BP04": BestPractice(
        id="REL07-BP04",
        title="Load Test Your Workload",
        pillar=Pillar.RELIABILITY,
        description="Adopt a load testing methodology to measure if scaling activity meets workload requirements",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform regular load testing?",
            "Are load tests representative of production traffic?",
            "Do you test scaling behavior under load?"
        ],
        implementation_guidance=[
            "Implement comprehensive load testing",
            "Use realistic traffic patterns",
            "Test auto-scaling behavior"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_load_tested_adapt.html"
    ),
    "REL08-BP01": BestPractice(
        id="REL08-BP01",
        title="Use Runbooks for Standard Activities",
        pillar=Pillar.RELIABILITY,
        description="Use runbooks for standard activities to ensure consistent execution",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have runbooks for standard operational activities?",
            "Are runbooks kept up-to-date and accessible?",
            "Do runbooks include step-by-step procedures?",
            "Are runbooks tested and validated regularly?"
        ],
        implementation_guidance=[
            "Create comprehensive runbooks for operational procedures",
            "Use AWS Systems Manager Documents for executable runbooks",
            "Keep runbooks version controlled and up-to-date",
            "Test runbooks regularly to ensure accuracy"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_planned_changemgmt.html",
        related_best_practices=["REL08-BP02"]
    ),
    "REL08-BP03": BestPractice(
        id="REL08-BP03",
        title="Integrate Resiliency Testing as Part of Your Deployment",
        pillar=Pillar.RELIABILITY,
        description="This approach reduces configuration drift and ensures consistent deployments",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use immutable infrastructure?",
            "Are deployments consistent and repeatable?",
            "Do you avoid configuration drift?"
        ],
        implementation_guidance=[
            "Use immutable deployment patterns",
            "Implement infrastructure as code",
            "Avoid manual configuration changes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html"
    ),
    "REL08-BP04": BestPractice(
        id="REL08-BP04",
        title="Deploy Using Immutable Infrastructure",
        pillar=Pillar.RELIABILITY,
        description="Deploy using immutable infrastructure to reduce configuration drift",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use immutable infrastructure for deployments?",
            "Are deployments consistent and repeatable?",
            "Do you avoid configuration drift?"
        ],
        implementation_guidance=[
            "Use immutable deployment patterns",
            "Implement infrastructure as code",
            "Replace rather than modify infrastructure"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html"
    ),
    "REL08-BP05": BestPractice(
        id="REL08-BP05",
        title="Deploy Changes with Automation",
        pillar=Pillar.RELIABILITY,
        description="Deployments and patching are automated to eliminate negative impact",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are deployments automated?",
            "Do you use automated patching?",
            "Are deployment processes consistent?"
        ],
        implementation_guidance=[
            "Automate deployment processes",
            "Use CI/CD pipelines",
            "Implement automated patching"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html"
    ),
    "REL09-BP01": BestPractice(
        id="REL09-BP01",
        title="Identify and Back Up All Data That Needs to Be Backed Up",
        pillar=Pillar.RELIABILITY,
        description="Identify and back up all data that needs to be backed up, or reproduce the data from sources",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified all data that needs to be backed up?",
            "Are backup requirements documented for each data type?",
            "Do you understand data dependencies and relationships?",
            "Are backup strategies aligned with business requirements?"
        ],
        implementation_guidance=[
            "Conduct data inventory to identify all critical data",
            "Document backup requirements for each data classification",
            "Use AWS Backup for centralized backup management",
            "Implement automated backup scheduling"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html",
        related_best_practices=["REL09-BP02", "REL09-BP03", "REL09-BP04"]
    ),
    "REL09-BP02": BestPractice(
        id="REL09-BP02",
        title="Secure and Encrypt Backups",
        pillar=Pillar.RELIABILITY,
        description="Secure and encrypt backups to protect data integrity and confidentiality",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are all backups encrypted at rest and in transit?",
            "Do you use appropriate access controls for backup data?",
            "Are backup encryption keys managed securely?",
            "Do you have backup integrity verification processes?"
        ],
        implementation_guidance=[
            "Enable encryption for all backup data",
            "Use AWS KMS for backup encryption key management",
            "Implement least privilege access for backup resources",
            "Verify backup integrity regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_secured_backups_data.html",
        related_best_practices=["REL09-BP01", "REL09-BP03"]
    ),
    "REL09-BP03": BestPractice(
        id="REL09-BP03",
        title="Perform Data Backup Automatically",
        pillar=Pillar.RELIABILITY,
        description="Perform data backup automatically based on a periodic schedule or changes to the dataset",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are backups performed automatically on a regular schedule?",
            "Do you have event-driven backup triggers?",
            "Are backup schedules aligned with business requirements?",
            "Do you monitor backup job success and failures?"
        ],
        implementation_guidance=[
            "Use AWS Backup for automated backup scheduling",
            "Implement event-driven backups for critical changes",
            "Set up backup monitoring and alerting",
            "Automate backup lifecycle management"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html",
        related_best_practices=["REL09-BP01", "REL09-BP04"]
    ),
    "REL09-BP04": BestPractice(
        id="REL09-BP04",
        title="Perform Periodic Recovery of the Data to Verify Backup Integrity and Processes",
        pillar=Pillar.RELIABILITY,
        description="Validate that your backup process implementation meets Recovery Time Objective and Recovery Point Objective",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly test backup recovery procedures?",
            "Are recovery tests documented and scheduled?",
            "Do you validate RTO and RPO requirements?",
            "Are recovery test results tracked and analyzed?"
        ],
        implementation_guidance=[
            "Schedule regular backup recovery testing",
            "Automate recovery testing where possible",
            "Document recovery procedures and test results",
            "Validate recovery times against business requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html",
        related_best_practices=["REL09-BP01", "REL09-BP03"]
    ),
    "REL10-BP01": BestPractice(
        id="REL10-BP01",
        title="Deploy the Workload to Multiple Locations",
        pillar=Pillar.RELIABILITY,
        description="Distribute workload data and resources across multiple Availability Zones or AWS Regions",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Is your workload deployed across multiple Availability Zones?",
            "Do you use multiple AWS Regions for critical workloads?",
            "Are dependencies distributed to avoid single points of failure?",
            "Do you have automated failover between locations?"
        ],
        implementation_guidance=[
            "Deploy across multiple Availability Zones by default",
            "Use multiple Regions for disaster recovery",
            "Implement automated cross-AZ failover",
            "Distribute data stores across multiple locations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html",
        related_best_practices=["REL10-BP02", "REL10-BP03"]
    ),
    "REL10-BP02": BestPractice(
        id="REL10-BP02",
        title="Select the Appropriate Locations for Your Multi-Location Deployment",
        pillar=Pillar.RELIABILITY,
        description="For high availability, always deploy your workload components to multiple Availability Zones",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you selected appropriate Availability Zones for deployment?",
            "Do you understand AZ characteristics and capabilities?",
            "Are workload components distributed optimally?",
            "Do you avoid single AZ dependencies?"
        ],
        implementation_guidance=[
            "Use at least two Availability Zones for all deployments",
            "Understand AZ-specific service availability",
            "Avoid hard dependencies on single AZs",
            "Consider latency and bandwidth between AZs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_single_az_system.html",
        related_best_practices=["REL10-BP01", "REL10-BP03"]
    ),
    "REL10-BP03": BestPractice(
        id="REL10-BP03",
        title="Use Bulkhead Architectures to Limit Scope of Impact",
        pillar=Pillar.RELIABILITY,
        description="Implement bulkhead architectures to prevent failures from impacting multiple components",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use bulkhead patterns to isolate components?",
            "Are failure domains clearly defined and limited?",
            "Do you prevent cascading failures between components?",
            "Are resource pools isolated to limit blast radius?"
        ],
        implementation_guidance=[
            "Implement service isolation using separate resource pools",
            "Use circuit breakers to prevent cascading failures",
            "Isolate critical and non-critical workloads",
            "Implement resource quotas and limits"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html",
        related_best_practices=["REL10-BP01", "REL10-BP02"]
    ),
    "REL11-BP01": BestPractice(
        id="REL11-BP01",
        title="Monitor All Components of the Workload to Detect Failures",
        pillar=Pillar.RELIABILITY,
        description="Continuously monitor the health of your workload so that you can quickly identify when failures occur",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you monitor all workload components for health?",
            "Are failure detection mechanisms comprehensive?",
            "Do you have real-time alerting for failures?",
            "Are monitoring thresholds appropriately configured?"
        ],
        implementation_guidance=[
            "Implement comprehensive health checks for all components",
            "Use CloudWatch for monitoring and alerting",
            "Set up synthetic monitoring for critical user journeys",
            "Monitor both technical and business metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_monitoring_health.html",
        related_best_practices=["REL11-BP02", "REL11-BP03"]
    ),
    "REL11-BP02": BestPractice(
        id="REL11-BP02",
        title="Fail Over to Healthy Resources",
        pillar=Pillar.RELIABILITY,
        description="Ensure that if a resource failure occurs, healthy resources can continue to serve requests",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have automated failover to healthy resources?",
            "Are failover procedures tested regularly?",
            "Do you maintain sufficient capacity for failover scenarios?",
            "Are failover times within acceptable limits?"
        ],
        implementation_guidance=[
            "Implement automated failover using load balancers",
            "Use Auto Scaling to maintain capacity during failures",
            "Test failover procedures regularly",
            "Monitor failover times and success rates"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_failover2good.html",
        related_best_practices=["REL11-BP01", "REL11-BP03"]
    ),
    "REL11-BP03": BestPractice(
        id="REL11-BP03",
        title="Automate Healing on All Layers",
        pillar=Pillar.RELIABILITY,
        description="Upon detection of a failure, use automated capabilities to perform actions to remediate",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have automated healing mechanisms?",
            "Are failed components automatically replaced?",
            "Do you use self-healing architectures?",
            "Are healing actions monitored and logged?"
        ],
        implementation_guidance=[
            "Use Auto Scaling for automatic instance replacement",
            "Implement automated remediation with Systems Manager",
            "Use container orchestration for self-healing",
            "Monitor and log all automated healing actions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_auto_healing_system.html",
        related_best_practices=["REL11-BP01", "REL11-BP02"]
    ),
    "REL11-BP04": BestPractice(
        id="REL11-BP04",
        title="Rely on the Data Plane and Not the Control Plane During Recovery",
        pillar=Pillar.RELIABILITY,
        description="The control plane is used to configure resources, and the data plane is used to deliver service",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you avoid control plane dependencies during recovery?",
            "Are recovery procedures designed to use data plane operations?",
            "Do you pre-provision resources to avoid control plane calls?",
            "Are critical operations independent of control plane availability?"
        ],
        implementation_guidance=[
            "Pre-provision resources to avoid control plane dependencies",
            "Use data plane operations for critical recovery actions",
            "Implement static stability patterns",
            "Cache control plane responses when possible"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_avoid_control_plane.html",
        related_best_practices=["REL11-BP05"]
    ),
    "REL11-BP05": BestPractice(
        id="REL11-BP05",
        title="Use Static Stability to Prevent Bimodal Behavior",
        pillar=Pillar.RELIABILITY,
        description="Workloads should be statically stable and only operate in a single normal mode",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Does your workload exhibit static stability?",
            "Do you avoid bimodal behavior patterns?",
            "Are system behaviors consistent under different conditions?",
            "Do you pre-provision resources to maintain stability?"
        ],
        implementation_guidance=[
            "Design systems to operate in a single stable mode",
            "Pre-provision resources to avoid dynamic scaling dependencies",
            "Avoid conditional logic that creates bimodal behavior",
            "Test system behavior under various load conditions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_static_stability.html",
        related_best_practices=["REL11-BP04"]
    ),
    "REL11-BP06": BestPractice(
        id="REL11-BP06",
        title="Send Notifications When Events Impact Availability",
        pillar=Pillar.RELIABILITY,
        description="Notifications are sent upon the detection of significant events, even if the issue caused by the event was automatically resolved",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you send notifications for availability-impacting events?",
            "Are notifications sent even for auto-resolved issues?",
            "Do notifications include relevant context and impact information?",
            "Are notification recipients appropriate for each event type?"
        ],
        implementation_guidance=[
            "Configure notifications for all availability-impacting events",
            "Include event context and impact assessment in notifications",
            "Use appropriate notification channels for different audiences",
            "Notify even when issues are automatically resolved"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_notifications_sent_system.html",
        related_best_practices=["REL11-BP07"]
    ),
    "REL11-BP07": BestPractice(
        id="REL11-BP07",
        title="Architect Your Product to Meet Availability Targets and Uptime Service Level Agreements (SLAs)",
        pillar=Pillar.RELIABILITY,
        description="Architect to meet your availability targets and any uptime SLAs you have with your customers",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you defined availability targets and SLAs?",
            "Is your architecture designed to meet these targets?",
            "Do you monitor and report on SLA compliance?",
            "Are availability targets realistic and achievable?"
        ],
        implementation_guidance=[
            "Define clear availability targets and SLAs",
            "Design architecture to exceed availability requirements",
            "Implement comprehensive availability monitoring",
            "Regular review and report on SLA performance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_service_level_agreements.html",
        related_best_practices=["REL11-BP06"]
    ),
    "REL12-BP01": BestPractice(
        id="REL12-BP01",
        title="Use Playbooks to Investigate Failures",
        pillar=Pillar.RELIABILITY,
        description="Enable consistent and prompt responses to failure scenarios that are not well understood",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have playbooks for investigating failures?",
            "Are investigation procedures documented and accessible?",
            "Do playbooks include escalation procedures?",
            "Are playbooks updated based on lessons learned?"
        ],
        implementation_guidance=[
            "Create detailed investigation playbooks for common failure scenarios",
            "Include step-by-step troubleshooting procedures",
            "Document escalation paths and contact information",
            "Update playbooks based on incident learnings"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_playbook_resiliency.html",
        related_best_practices=["REL12-BP02"]
    ),
    "REL12-BP02": BestPractice(
        id="REL12-BP02",
        title="Perform Post-Incident Analysis",
        pillar=Pillar.RELIABILITY,
        description="Review customer-impacting events, and identify the contributing factors and preventative action items",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform post-incident analysis for all significant events?",
            "Are root causes identified and documented?",
            "Do you implement preventative measures based on analysis?",
            "Are lessons learned shared across teams?"
        ],
        implementation_guidance=[
            "Conduct blameless post-incident reviews",
            "Use structured root cause analysis methodologies",
            "Implement corrective actions with clear ownership",
            "Share learnings across the organization"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_rca_resiliency.html",
        related_best_practices=["REL12-BP01", "REL12-BP03"]
    ),
    "REL12-BP03": BestPractice(
        id="REL12-BP03",
        title="Test Functional Requirements and Include Resiliency Testing",
        pillar=Pillar.RELIABILITY,
        description="Use techniques such as load testing, penetration testing, chaos engineering, and game days",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform comprehensive resiliency testing?",
            "Are load and stress tests included in your testing strategy?",
            "Do you test failure scenarios and recovery procedures?",
            "Are testing results used to improve system resilience?"
        ],
        implementation_guidance=[
            "Implement comprehensive load and performance testing",
            "Use chaos engineering to test failure scenarios",
            "Conduct regular game days to test incident response",
            "Test backup and recovery procedures regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_non_functional.html",
        related_best_practices=["REL12-BP04", "REL12-BP05"]
    ),
    "REL12-BP04": BestPractice(
        id="REL12-BP04",
        title="Use Chaos Engineering",
        pillar=Pillar.RELIABILITY,
        description="Run chaos engineering experiments regularly to understand how your systems respond to failure",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use chaos engineering to test system resilience?",
            "Are chaos experiments run regularly and systematically?",
            "Do you test different types of failure scenarios?",
            "Are chaos engineering results used to improve system design?"
        ],
        implementation_guidance=[
            "Implement chaos engineering practices using tools like AWS Fault Injection Simulator",
            "Start with small, controlled experiments",
            "Test different failure modes systematically",
            "Use results to improve system resilience"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_failure_injection_resiliency.html",
        related_best_practices=["REL12-BP03", "REL12-BP05"]
    ),
    "REL12-BP05": BestPractice(
        id="REL12-BP05",
        title="Conduct Game Days Regularly",
        pillar=Pillar.RELIABILITY,
        description="Use game days to regularly exercise your procedures for responding to events and failures",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you conduct regular game days?",
            "Are different failure scenarios tested during game days?",
            "Do game days include all relevant team members?",
            "Are game day learnings incorporated into procedures?"
        ],
        implementation_guidance=[
            "Schedule regular game days for different failure scenarios",
            "Include all relevant teams in game day exercises",
            "Test both technical and communication procedures",
            "Document and implement improvements from game days"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_game_days_resiliency.html",
        related_best_practices=["REL12-BP03", "REL12-BP04"]
    ),
    "REL13-BP01": BestPractice(
        id="REL13-BP01",
        title="Define Recovery Objectives for Downtime and Data Loss",
        pillar=Pillar.RELIABILITY,
        description="The workload has a recovery time objective (RTO) and recovery point objective (RPO)",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you defined RTO and RPO for your workload?",
            "Are recovery objectives aligned with business requirements?",
            "Do you understand the cost implications of different recovery objectives?",
            "Are recovery objectives documented and communicated?"
        ],
        implementation_guidance=[
            "Work with business stakeholders to define RTO and RPO",
            "Document recovery objectives for different failure scenarios",
            "Understand cost trade-offs for different recovery strategies",
            "Regularly review and update recovery objectives"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html",
        related_best_practices=["REL13-BP02"]
    ),
    "REL13-BP02": BestPractice(
        id="REL13-BP02",
        title="Use Defined Recovery Strategies to Meet the Recovery Objectives",
        pillar=Pillar.RELIABILITY,
        description="A disaster recovery (DR) strategy has been defined to meet objectives",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a defined disaster recovery strategy?",
            "Does your DR strategy meet defined RTO and RPO objectives?",
            "Are DR procedures documented and accessible?",
            "Do you have appropriate DR infrastructure provisioned?"
        ],
        implementation_guidance=[
            "Choose appropriate DR strategy (backup/restore, pilot light, warm standby, multi-site)",
            "Implement DR infrastructure to meet recovery objectives",
            "Document detailed DR procedures and runbooks",
            "Ensure DR strategy aligns with business requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html",
        related_best_practices=["REL13-BP01", "REL13-BP03"]
    ),
    "REL13-BP03": BestPractice(
        id="REL13-BP03",
        title="Test Disaster Recovery Implementation to Validate the Implementation",
        pillar=Pillar.RELIABILITY,
        description="Regularly test failover to DR to ensure that RTO and RPO are met",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly test your disaster recovery procedures?",
            "Are DR tests comprehensive and realistic?",
            "Do you validate that RTO and RPO objectives are met during tests?",
            "Are DR test results documented and acted upon?"
        ],
        implementation_guidance=[
            "Schedule regular DR testing exercises",
            "Test complete end-to-end recovery scenarios",
            "Measure and validate RTO and RPO during tests",
            "Document test results and implement improvements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html",
        related_best_practices=["REL13-BP02", "REL13-BP04"]
    ),
    "REL13-BP04": BestPractice(
        id="REL13-BP04",
        title="Manage Configuration Drift at the DR Site or Region",
        pillar=Pillar.RELIABILITY,
        description="Ensure that the infrastructure, data, and configuration are as needed at the DR site or region",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you manage configuration drift between primary and DR sites?",
            "Are DR site configurations kept in sync with primary?",
            "Do you have automated processes to detect configuration drift?",
            "Are configuration changes replicated to DR sites?"
        ],
        implementation_guidance=[
            "Use infrastructure as code to maintain consistency",
            "Implement automated configuration drift detection",
            "Establish processes to sync configuration changes",
            "Regularly validate DR site configuration"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_config_drift.html",
        related_best_practices=["REL13-BP03", "REL13-BP05"]
    ),
    "REL13-BP05": BestPractice(
        id="REL13-BP05",
        title="Automate Recovery",
        pillar=Pillar.RELIABILITY,
        description="Use AWS or third-party tools to automate system recovery and reduce recovery time",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated recovery procedures?",
            "Are recovery processes triggered automatically when appropriate?",
            "Do you minimize manual intervention in recovery scenarios?",
            "Are automated recovery procedures tested regularly?"
        ],
        implementation_guidance=[
            "Implement automated failover and recovery procedures",
            "Use AWS services like Route 53 health checks for automatic failover",
            "Minimize manual steps in recovery processes",
            "Test automated recovery procedures regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_auto_recovery.html",
        related_best_practices=["REL13-BP04"]
    )
}
}