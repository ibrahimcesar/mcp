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
        related_best_practices=["PERF01-BP02", "PERF01-BP05"]
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
        related_best_practices=["PERF01-BP01", "PERF01-BP05"]
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
        related_best_practices=["PERF01-BP04", "PERF01-BP07"]
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
        related_best_practices=["PERF01-BP03", "PERF01-BP06"]
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
        related_best_practices=["PERF01-BP01", "PERF01-BP02"]
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
    )
}