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

"""AWS Well-Architected Framework best practices definitions."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from typing import Dict, List, NamedTuple


class BestPractice(NamedTuple):
    """Definition of a Well-Architected best practice."""
    id: str
    title: str
    pillar: Pillar
    area: str
    description: str
    risk_level: RiskLevel
    questions: List[str]
    implementation_guidance: List[str]
    requires_user_input: bool = False
    url: str = ""
    related_best_practices: List[str] = []


# Well-Architected Framework Best Practices
# Import from individual pillar files
from awslabs.aws_wellarchitected_mcp_server.pillars.operational_excellence import OPERATIONAL_EXCELLENCE_BEST_PRACTICES
from awslabs.aws_wellarchitected_mcp_server.pillars.security import SECURITY_BEST_PRACTICES
from awslabs.aws_wellarchitected_mcp_server.pillars.reliability import RELIABILITY_BEST_PRACTICES
from awslabs.aws_wellarchitected_mcp_server.pillars.performance_efficiency import PERFORMANCE_EFFICIENCY_BEST_PRACTICES
from awslabs.aws_wellarchitected_mcp_server.pillars.cost_optimization import COST_OPTIMIZATION_BEST_PRACTICES
from awslabs.aws_wellarchitected_mcp_server.pillars.sustainability import SUSTAINABILITY_BEST_PRACTICES

# Combine all pillar best practices
WELL_ARCHITECTED_BEST_PRACTICES: Dict[str, BestPractice] = {
    **OPERATIONAL_EXCELLENCE_BEST_PRACTICES,
    **SECURITY_BEST_PRACTICES,
    **RELIABILITY_BEST_PRACTICES,
    **PERFORMANCE_EFFICIENCY_BEST_PRACTICES,
    **COST_OPTIMIZATION_BEST_PRACTICES,
    **SUSTAINABILITY_BEST_PRACTICES
}

def get_best_practices_by_pillar(pillar: Pillar) -> List[BestPractice]:
    """Get all best practices for a specific pillar."""
    return [bp for bp in WELL_ARCHITECTED_BEST_PRACTICES.values() if bp.pillar == pillar]


def get_all_best_practices() -> Dict[str, BestPractice]:
    """Get all Well-Architected best practices."""
    return WELL_ARCHITECTED_BEST_PRACTICES

def get_all_best_practices_list() -> List[BestPractice]:
    """Get all Well-Architected best practices as a list."""
    return list(WELL_ARCHITECTED_BEST_PRACTICES.values())