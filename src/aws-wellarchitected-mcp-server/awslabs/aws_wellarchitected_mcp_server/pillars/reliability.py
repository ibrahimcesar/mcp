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
}