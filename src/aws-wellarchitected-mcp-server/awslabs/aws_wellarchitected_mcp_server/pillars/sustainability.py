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
    "SUS01": BestPractice(
        id="SUS01",
        title="Optimize Resource Utilization",
        pillar=Pillar.SUSTAINABILITY,
        description="Maximize utilization of provisioned resources",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you monitoring resource utilization?",
            "Do you right-size resources based on actual usage?",
            "Are you using serverless where appropriate?"
        ],
        implementation_guidance=[
            "Use CloudWatch to monitor utilization",
            "Implement auto-scaling to match demand",
            "Consider serverless architectures for variable workloads"
        ]
    ),
    "SUS02": BestPractice(
        id="SUS02",
        title="Use Managed Services",
        pillar=Pillar.SUSTAINABILITY,
        description="Leverage AWS managed services to reduce operational overhead",
        risk_level=RiskLevel.LOW,
        questions=[
            "Are you using managed services where possible?",
            "Do you have a strategy for reducing operational overhead?",
            "Are you leveraging serverless technologies?"
        ],
        implementation_guidance=[
            "Use RDS instead of self-managed databases",
            "Leverage Lambda for event-driven processing",
            "Consider managed container services like Fargate"
        ]
    )
}