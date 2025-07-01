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
    "PERF01": BestPractice(
        id="PERF01",
        title="Use Appropriate Instance Types",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Select the right compute resources for your workload",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Have you analyzed your compute requirements?",
            "Are you using the most appropriate instance types?",
            "Do you regularly review and optimize instance selection?"
        ],
        implementation_guidance=[
            "Use AWS Compute Optimizer recommendations",
            "Consider specialized instance types (GPU, memory-optimized)",
            "Regularly review and right-size instances"
        ]
    ),
    "PERF02": BestPractice(
        id="PERF02",
        title="Implement Caching Strategies",
        pillar=Pillar.PERFORMANCE_EFFICIENCY,
        description="Use caching to improve application performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using caching for frequently accessed data?",
            "Do you have CDN for static content?",
            "Are database queries optimized?"
        ],
        implementation_guidance=[
            "Use ElastiCache for application caching",
            "Implement CloudFront for content delivery",
            "Optimize database queries and indexing"
        ]
    )
}