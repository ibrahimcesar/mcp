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

"""Cost Optimization pillar best practices."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import BestPractice
from typing import Dict

COST_OPTIMIZATION_BEST_PRACTICES: Dict[str, BestPractice] = {
    "COST01": BestPractice(
        id="COST01",
        title="Implement Cost Monitoring",
        pillar=Pillar.COST_OPTIMIZATION,
        description="Monitor and analyze costs to identify optimization opportunities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have cost monitoring and alerting?",
            "Are you tracking costs by service and project?",
            "Do you regularly review cost optimization opportunities?"
        ],
        implementation_guidance=[
            "Use AWS Cost Explorer and Budgets",
            "Implement cost allocation tags",
            "Set up cost anomaly detection"
        ]
    ),
    "COST02": BestPractice(
        id="COST02",
        title="Use Reserved Instances and Savings Plans",
        pillar=Pillar.COST_OPTIMIZATION,
        description="Commit to usage to reduce costs for predictable workloads",
        risk_level=RiskLevel.LOW,
        questions=[
            "Have you analyzed your usage patterns?",
            "Are you using Reserved Instances for steady-state workloads?",
            "Do you have Savings Plans for flexible compute usage?"
        ],
        implementation_guidance=[
            "Analyze usage with Cost Explorer",
            "Purchase Reserved Instances for predictable workloads",
            "Consider Compute Savings Plans for flexibility"
        ]
    )
}