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

"""Performance Efficiency pillar best practices."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import BestPractice
from typing import Dict

PERFORMANCE_EFFICIENCY_BEST_PRACTICES: Dict[str, BestPractice] = {
    "PERF01-BP01": BestPractice(
        id="PERF01-BP01",
        title="Learn About and Understand Available Cloud Services and Features",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Learn about and understand the cloud services and features that are available to you",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you stay current with new AWS services and features?",
            "Do you understand the performance characteristics of different services?",
            "Are you leveraging managed services where appropriate?",
            "Do you evaluate new services for potential performance benefits?"
        ],
        implementation_guidance=[
            "Regularly review AWS service announcements and updates",
            "Attend AWS events and training sessions",
            "Experiment with new services in non-production environments",
            "Use AWS documentation and whitepapers for service guidance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_understand_cloud_services_and_features.html",
        related_best_practices=["PERF01-BP02", "PERF01-BP05"],
        requires_user_input=True
    ),
    "PERF01-BP02": BestPractice(
        id="PERF01-BP02",
        title="Use Guidance from Your Cloud Provider or an Appropriate Partner",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use guidance, documentation, and best practices from your cloud provider or an appropriate partner",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you follow AWS architectural guidance and best practices?",
            "Are you using AWS Well-Architected Framework principles?",
            "Do you leverage AWS partner expertise when needed?",
            "Are you following service-specific best practices?"
        ],
        implementation_guidance=[
            "Use AWS Well-Architected Framework for architectural guidance",
            "Follow AWS service-specific best practices documentation",
            "Engage with AWS solutions architects and partners",
            "Use AWS reference architectures as starting points"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_guidance_architecture_patterns_best_practices.html",
        related_best_practices=["PERF01-BP01", "PERF01-BP05"],
        requires_user_input=True
    ),
    "PERF01-BP03": BestPractice(
        id="PERF01-BP03",
        title="Factor Cost Requirements into Decisions",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Architect for cost when making decisions, and use a data-driven approach",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you consider cost implications when making performance decisions?",
            "Are you balancing performance requirements with cost constraints?",
            "Do you use cost-performance analysis for architectural choices?",
            "Are you optimizing for the right cost-performance ratio?"
        ],
        implementation_guidance=[
            "Use AWS Cost Explorer to understand cost implications",
            "Implement cost-performance benchmarking",
            "Consider Reserved Instances and Savings Plans for predictable workloads",
            "Use AWS Compute Optimizer for cost-performance recommendations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_factor_cost_into_architectural_decisions.html",
        related_best_practices=["PERF01-BP04", "PERF01-BP07"],
        requires_user_input=True
    ),
    "PERF01-BP04": BestPractice(
        id="PERF01-BP04",
        title="Evaluate the Available Options and Trade-offs",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Understand the options available and the trade-offs between them",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you evaluate multiple architectural options?",
            "Are you aware of the trade-offs between different approaches?",
            "Do you consider performance, cost, and operational complexity?",
            "Are architectural decisions documented with rationale?"
        ],
        implementation_guidance=[
            "Create architectural decision records (ADRs)",
            "Evaluate multiple options using proof of concepts",
            "Consider performance, cost, security, and operational trade-offs",
            "Use AWS service comparison tools and documentation"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_evaluate_trade_offs.html",
        related_best_practices=["PERF01-BP03", "PERF01-BP06"],
        requires_user_input=True
    ),
    "PERF01-BP05": BestPractice(
        id="PERF01-BP05",
        title="Use Policies and Reference Architectures",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use internal policies and existing reference architectures when selecting services",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have organizational policies for service selection?",
            "Are you using proven reference architectures?",
            "Do you have standardized architectural patterns?",
            "Are architectural decisions aligned with organizational standards?"
        ],
        implementation_guidance=[
            "Develop organizational architectural standards and policies",
            "Use AWS reference architectures as templates",
            "Create reusable architectural patterns and components",
            "Establish architectural review processes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_policies_and_reference_architectures.html",
        related_best_practices=["PERF01-BP01", "PERF01-BP02"],
        requires_user_input=True
    ),
    "PERF01-BP06": BestPractice(
        id="PERF01-BP06",
        title="Use Benchmarking to Drive Architectural Decisions",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use benchmarking when making architectural decisions for your workload",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use benchmarking to validate architectural decisions?",
            "Are performance tests conducted before production deployment?",
            "Do you have baseline performance metrics?",
            "Are benchmarks representative of production workloads?"
        ],
        implementation_guidance=[
            "Establish performance baselines for key metrics",
            "Use realistic test data and scenarios",
            "Benchmark different architectural options",
            "Automate performance testing in CI/CD pipelines"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_benchmarking.html",
        related_best_practices=["PERF01-BP04", "PERF01-BP07"]
    ),
    "PERF01-BP07": BestPractice(
        id="PERF01-BP07",
        title="Use a Data-Driven Approach for Architectural Choices",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use a data-driven approach to select the highest-performing architecture",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use data and metrics to drive architectural decisions?",
            "Are performance decisions based on empirical evidence?",
            "Do you collect and analyze performance data regularly?",
            "Are architectural changes validated with performance data?"
        ],
        implementation_guidance=[
            "Implement comprehensive monitoring and observability",
            "Use performance data to validate architectural decisions",
            "Establish data-driven decision-making processes",
            "Regularly review and analyze performance metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_data_driven_approach.html",
        related_best_practices=["PERF01-BP03", "PERF01-BP06"]
    ),
    "PERF02-BP01": BestPractice(
        id="PERF02-BP01",
        title="Select the Best Compute Options for Your Workload",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Select the best compute options for your workload by understanding performance characteristics",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you selected the most appropriate compute options for your workload?",
            "Do you understand the performance characteristics of different compute types?",
            "Are you using specialized compute instances where beneficial?",
            "Do you regularly evaluate new compute options?"
        ],
        implementation_guidance=[
            "Use AWS Compute Optimizer for instance recommendations",
            "Consider GPU instances for compute-intensive workloads",
            "Evaluate ARM-based Graviton processors for cost-performance benefits",
            "Use FPGA instances for specialized acceleration needs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html",
        related_best_practices=["PERF02-BP02", "PERF02-BP04"]
    ),
    "PERF02-BP02": BestPractice(
        id="PERF02-BP02",
        title="Understand the Available Compute Configuration and Features",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Understand how compute configuration options and features impact performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you understand the configuration options available for your compute resources?",
            "Are you using performance-enhancing features like enhanced networking?",
            "Do you understand the impact of different configuration choices?",
            "Are you optimizing compute configurations for your workload?"
        ],
        implementation_guidance=[
            "Use enhanced networking for improved network performance",
            "Configure placement groups for low-latency applications",
            "Understand CPU, memory, and storage configuration options",
            "Use appropriate AMIs optimized for your workload"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_understand_compute_configuration_features.html",
        related_best_practices=["PERF02-BP01", "PERF02-BP03"]
    ),
    "PERF02-BP03": BestPractice(
        id="PERF02-BP03",
        title="Collect Compute-Related Metrics",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Record and track compute-related metrics to better understand performance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you collecting comprehensive compute performance metrics?",
            "Do you monitor CPU, memory, disk, and network utilization?",
            "Are you tracking application-specific performance metrics?",
            "Do you have alerting for performance issues?"
        ],
        implementation_guidance=[
            "Use CloudWatch to monitor instance metrics",
            "Implement custom metrics for application performance",
            "Monitor resource utilization and bottlenecks",
            "Set up alerts for performance thresholds"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_collect_compute_related_metrics.html",
        related_best_practices=["PERF02-BP02", "PERF02-BP04"]
    ),
    "PERF02-BP04": BestPractice(
        id="PERF02-BP04",
        title="Configure and Right-Size Compute Resources",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Configure and right-size compute resources to match workload requirements",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are your compute resources appropriately sized for your workload?",
            "Do you regularly review and adjust resource sizing?",
            "Are you avoiding over-provisioning or under-provisioning?",
            "Do you use data to drive sizing decisions?"
        ],
        implementation_guidance=[
            "Use AWS Compute Optimizer recommendations for right-sizing",
            "Monitor utilization metrics to identify sizing opportunities",
            "Implement automated scaling to match demand",
            "Regular review and adjust instance sizes based on performance data"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_configure_and_right_size_compute_resources.html",
        related_best_practices=["PERF02-BP01", "PERF02-BP05"]
    ),
    "PERF02-BP05": BestPractice(
        id="PERF02-BP05",
        title="Use Dynamic Scaling",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use dynamic scaling to automatically adjust compute resources based on demand",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using auto scaling to match compute capacity with demand?",
            "Do you have appropriate scaling policies configured?",
            "Are scaling actions based on relevant metrics?",
            "Do you test scaling behavior under different load conditions?"
        ],
        implementation_guidance=[
            "Use Auto Scaling Groups for EC2 instances",
            "Configure scaling policies based on CPU, memory, or custom metrics",
            "Use predictive scaling for predictable workload patterns",
            "Test scaling behavior and adjust policies as needed"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_scale_compute_resources_dynamically.html",
        related_best_practices=["PERF02-BP04", "PERF02-BP06"]
    ),
    "PERF02-BP06": BestPractice(
        id="PERF02-BP06",
        title="Use Hardware-Based Compute Accelerators",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use hardware-based compute accelerators to improve performance for specific workloads",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using specialized compute accelerators where beneficial?",
            "Do you understand which workloads benefit from GPU acceleration?",
            "Are you considering FPGA or other specialized processors?",
            "Do you evaluate the cost-performance benefits of accelerators?"
        ],
        implementation_guidance=[
            "Use GPU instances for machine learning and HPC workloads",
            "Consider ARM-based Graviton processors for cost-performance benefits",
            "Use FPGA instances for specialized acceleration needs",
            "Evaluate accelerator options based on workload characteristics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_compute_accelerators.html",
        related_best_practices=["PERF02-BP01", "PERF02-BP05"]
    ),
    "PERF03-BP01": BestPractice(
        id="PERF03-BP01",
        title="Use Purpose-Built Data Stores",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use purpose-built data stores that best support your data access patterns",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using the most appropriate data store for each use case?",
            "Do you understand the access patterns of your data?",
            "Are you leveraging purpose-built databases?",
            "Do you avoid using one-size-fits-all database solutions?"
        ],
        implementation_guidance=[
            "Use relational databases for ACID transactions",
            "Use NoSQL databases for flexible schemas and scale",
            "Use time-series databases for IoT and monitoring data",
            "Use graph databases for relationship-heavy data"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html",
        related_best_practices=["PERF03-BP02", "PERF03-BP04"]
    ),
    "PERF03-BP02": BestPractice(
        id="PERF03-BP02",
        title="Evaluate Available Configuration Options",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Evaluate the various features and configuration options and how they relate to performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Have you evaluated different configuration options for your data stores?",
            "Do you understand the performance implications of different settings?",
            "Are you using appropriate instance types and storage options?",
            "Do you regularly review and optimize configurations?"
        ],
        implementation_guidance=[
            "Use appropriate instance types for database workloads",
            "Configure storage types based on IOPS and throughput requirements",
            "Optimize database parameters for your workload",
            "Use read replicas to distribute read traffic"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_evaluate_configuration_options_data_store.html",
        related_best_practices=["PERF03-BP01", "PERF03-BP03"]
    ),
    "PERF03-BP03": BestPractice(
        id="PERF03-BP03",
        title="Collect and Record Performance Metrics",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Collect and record performance metrics to understand how your data store is performing",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you collecting comprehensive performance metrics for your data stores?",
            "Do you monitor key performance indicators like latency and throughput?",
            "Are you tracking query performance and identifying bottlenecks?",
            "Do you have alerting for performance degradation?"
        ],
        implementation_guidance=[
            "Use CloudWatch to monitor database metrics",
            "Enable Performance Insights for RDS databases",
            "Monitor slow query logs and execution plans",
            "Set up alerts for performance thresholds"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_collect_record_data_store_performance_metrics.html",
        related_best_practices=["PERF03-BP02", "PERF03-BP04"]
    ),
    "PERF03-BP04": BestPractice(
        id="PERF03-BP04",
        title="Implement Strategies to Improve Query Performance",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Implement strategies to improve query performance in your data store",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you optimized your queries for performance?",
            "Are you using appropriate indexes?",
            "Do you partition data effectively?",
            "Are you avoiding expensive operations like full table scans?"
        ],
        implementation_guidance=[
            "Create appropriate indexes for query patterns",
            "Use query optimization techniques",
            "Implement data partitioning strategies",
            "Use materialized views for complex aggregations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_implement_strategies_to_improve_query_performance.html",
        related_best_practices=["PERF03-BP01", "PERF03-BP05"]
    ),
    "PERF03-BP05": BestPractice(
        id="PERF03-BP05",
        title="Implement Data Access Patterns That Utilize Caching",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Implement access patterns that can effectively use caching to improve performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using caching to improve data access performance?",
            "Do you have appropriate cache invalidation strategies?",
            "Are you caching at multiple layers?",
            "Do you monitor cache hit rates and effectiveness?"
        ],
        implementation_guidance=[
            "Use ElastiCache for application-level caching",
            "Implement database query result caching",
            "Use CDN for static content caching",
            "Design cache-friendly data access patterns"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_access_patterns_caching.html",
        related_best_practices=["PERF03-BP04"]
    ),
    "PERF04-BP01": BestPractice(
        id="PERF04-BP01",
        title="Understand How Networking Impacts Performance",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Understand how networking impacts performance and the available options to improve it",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you understand how network latency affects your workload?",
            "Are you aware of bandwidth limitations and requirements?",
            "Do you understand the impact of network protocols?",
            "Are you optimizing for network performance?"
        ],
        implementation_guidance=[
            "Measure and monitor network latency and throughput",
            "Understand the impact of geographic distance",
            "Choose appropriate network protocols",
            "Optimize data transfer patterns"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_understand_how_networking_impacts_performance.html",
        related_best_practices=["PERF04-BP02", "PERF04-BP06"]
    ),
    "PERF04-BP02": BestPractice(
        id="PERF04-BP02",
        title="Evaluate Available Networking Features",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Evaluate networking features in the cloud that may increase performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using enhanced networking features?",
            "Do you leverage placement groups for low latency?",
            "Are you using appropriate network interface types?",
            "Do you take advantage of AWS networking optimizations?"
        ],
        implementation_guidance=[
            "Use enhanced networking (SR-IOV) for better performance",
            "Implement placement groups for low-latency applications",
            "Use appropriate elastic network interfaces",
            "Leverage AWS networking features like jumbo frames"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_evaluate_networking_features.html",
        related_best_practices=["PERF04-BP01", "PERF04-BP03"]
    ),
    "PERF04-BP03": BestPractice(
        id="PERF04-BP03",
        title="Choose Appropriate Dedicated Connectivity or VPN",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Choose dedicated connectivity or VPN for hybrid workloads based on performance requirements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use dedicated connectivity for consistent performance?",
            "Are you using appropriate connection types for your requirements?",
            "Do you have redundant connections for high availability?",
            "Are connection speeds appropriate for your workload?"
        ],
        implementation_guidance=[
            "Use AWS Direct Connect for dedicated connectivity",
            "Implement redundant connections for availability",
            "Choose appropriate connection speeds",
            "Use VPN as backup or for lower-bandwidth requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.html",
        related_best_practices=["PERF04-BP02", "PERF04-BP06"]
    ),
    "PERF04-BP04": BestPractice(
        id="PERF04-BP04",
        title="Use Load Balancing to Distribute Traffic",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use load balancing to distribute traffic across multiple resources",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using load balancing to distribute traffic?",
            "Do you have appropriate load balancing algorithms?",
            "Are you monitoring load balancer performance?",
            "Do you use health checks to ensure traffic goes to healthy instances?"
        ],
        implementation_guidance=[
            "Use Application Load Balancer for HTTP/HTTPS traffic",
            "Use Network Load Balancer for TCP/UDP traffic",
            "Configure appropriate health checks",
            "Monitor load balancer metrics and performance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_load_balancing_distribute_traffic.html",
        related_best_practices=["PERF04-BP05", "PERF04-BP07"]
    ),
    "PERF04-BP05": BestPractice(
        id="PERF04-BP05",
        title="Choose Network Protocols to Improve Performance",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Choose network protocols that can improve performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using the most appropriate network protocols?",
            "Do you understand the performance characteristics of different protocols?",
            "Are you optimizing protocol configurations?",
            "Do you use compression where beneficial?"
        ],
        implementation_guidance=[
            "Use HTTP/2 for improved web performance",
            "Implement gRPC for efficient service communication",
            "Use UDP for low-latency applications where appropriate",
            "Enable compression to reduce bandwidth usage"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_network_protocols_improve_performance.html",
        related_best_practices=["PERF04-BP04", "PERF04-BP01"]
    ),
    "PERF04-BP06": BestPractice(
        id="PERF04-BP06",
        title="Choose Your Workload's Location Based on Network Requirements",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Choose your workload's location based on network requirements and user proximity",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you chosen regions based on user proximity?",
            "Do you use multiple regions for global applications?",
            "Are you using edge locations for content delivery?",
            "Do you consider data sovereignty and compliance requirements?"
        ],
        implementation_guidance=[
            "Deploy workloads close to users to reduce latency",
            "Use CloudFront for global content delivery",
            "Consider multi-region deployments for global applications",
            "Use AWS Global Accelerator for improved global performance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_workload_location_network_requirements.html",
        related_best_practices=["PERF04-BP01", "PERF04-BP07"]
    ),
    "PERF04-BP07": BestPractice(
        id="PERF04-BP07",
        title="Optimize Network Configuration Based on Metrics",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use collected and analyzed data to make informed decisions about optimizing your network configuration",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you monitor network performance metrics?",
            "Are you using data to optimize network configuration?",
            "Do you regularly review and adjust network settings?",
            "Are you identifying and addressing network bottlenecks?"
        ],
        implementation_guidance=[
            "Monitor network latency, throughput, and packet loss",
            "Use VPC Flow Logs to analyze network traffic",
            "Optimize network configurations based on performance data",
            "Regularly review and tune network settings"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_optimize_network_configuration_based_on_metrics.html",
        related_best_practices=["PERF04-BP04", "PERF04-BP06"]
    ),
    "PERF05-BP01": BestPractice(
        id="PERF05-BP01",
        title="Establish Key Performance Indicators (KPIs) to Measure Workload Performance",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Identify and establish KPIs that provide insight into how well your workload is performing",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you established KPIs for your workload performance?",
            "Do your KPIs align with business objectives?",
            "Are you measuring both technical and business metrics?",
            "Do you have baselines for your performance metrics?"
        ],
        implementation_guidance=[
            "Define KPIs that align with business outcomes",
            "Establish performance baselines and targets",
            "Monitor both technical metrics (latency, throughput) and business metrics",
            "Regularly review and update KPIs as requirements change"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html",
        related_best_practices=["PERF05-BP02", "PERF05-BP07"]
    ),
    "PERF05-BP02": BestPractice(
        id="PERF05-BP02",
        title="Use Monitoring Solutions to Understand the Areas Where Performance Can Be Improved",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use monitoring solutions to identify performance bottlenecks and improvement opportunities",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using comprehensive monitoring solutions?",
            "Do you have visibility into all layers of your application stack?",
            "Are you monitoring user experience and business metrics?",
            "Do you have alerting for performance issues?"
        ],
        implementation_guidance=[
            "Use CloudWatch for infrastructure and application monitoring",
            "Implement distributed tracing with AWS X-Ray",
            "Monitor user experience with CloudWatch RUM",
            "Set up alerts for performance degradation"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.html",
        related_best_practices=["PERF05-BP01", "PERF05-BP03"]
    ),
    "PERF05-BP03": BestPractice(
        id="PERF05-BP03",
        title="Define a Process to Improve Workload Performance",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Define a repeatable process to evaluate new services, design patterns, and resource types",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a defined process for performance improvement?",
            "Are performance improvements prioritized and tracked?",
            "Do you regularly evaluate new services and features?",
            "Are performance improvements integrated into your development lifecycle?"
        ],
        implementation_guidance=[
            "Establish regular performance review cycles",
            "Create processes to evaluate new AWS services and features",
            "Prioritize performance improvements based on business impact",
            "Integrate performance considerations into development workflows"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html",
        related_best_practices=["PERF05-BP02", "PERF05-BP04"],
        requires_user_input=True
    ),
    "PERF05-BP04": BestPractice(
        id="PERF05-BP04",
        title="Load Test Your Workload",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Deploy and load test your workload to verify it can handle production traffic",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform load testing before production deployment?",
            "Are your load tests representative of production traffic patterns?",
            "Do you test different load scenarios and failure conditions?",
            "Are load test results used to optimize performance?"
        ],
        implementation_guidance=[
            "Implement automated load testing in CI/CD pipelines",
            "Use realistic test data and traffic patterns",
            "Test various load scenarios including peak and burst traffic",
            "Use load test results to identify bottlenecks and optimize performance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html",
        related_best_practices=["PERF05-BP03", "PERF05-BP05"]
    ),
    "PERF05-BP05": BestPractice(
        id="PERF05-BP05",
        title="Use Automation to Proactively Remediate Performance Issues",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use automation to detect and remediate performance issues before they impact users",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated responses to performance issues?",
            "Are performance problems detected and resolved proactively?",
            "Do you use auto-scaling to handle demand changes?",
            "Are remediation actions logged and monitored?"
        ],
        implementation_guidance=[
            "Implement auto-scaling based on performance metrics",
            "Use automated remediation with AWS Systems Manager",
            "Set up automated responses to performance alerts",
            "Monitor and log all automated remediation actions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.html",
        related_best_practices=["PERF05-BP04", "PERF05-BP06"]
    ),
    "PERF05-BP06": BestPractice(
        id="PERF05-BP06",
        title="Keep Your Workload, the Underlying System, and All Service Components Up to Date",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Stay current with new resource types and services to improve performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you keep your workload and dependencies up to date?",
            "Are you regularly updating to newer service versions?",
            "Do you evaluate new AWS services and features?",
            "Are updates tested for performance impact?"
        ],
        implementation_guidance=[
            "Establish regular update cycles for workload components",
            "Monitor AWS service announcements for new features",
            "Test updates in non-production environments first",
            "Evaluate performance impact of updates before deployment"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_keep_workload_and_services_up_to_date.html",
        related_best_practices=["PERF05-BP05", "PERF05-BP07"],
        requires_user_input=True
    ),
    "PERF05-BP07": BestPractice(
        id="PERF05-BP07",
        title="Review Metrics at Regular Intervals",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="As part of a continuous improvement process, review metrics with cross-functional teams",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you regularly review performance metrics with stakeholders?",
            "Are performance trends analyzed and acted upon?",
            "Do you have regular performance review meetings?",
            "Are performance insights shared across teams?"
        ],
        implementation_guidance=[
            "Schedule regular performance review meetings",
            "Create performance dashboards for stakeholders",
            "Analyze performance trends and identify improvement opportunities",
            "Share performance insights and learnings across teams"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_review_metrics.html",
        related_best_practices=["PERF05-BP01", "PERF05-BP06"],
        requires_user_input=True
    )
}