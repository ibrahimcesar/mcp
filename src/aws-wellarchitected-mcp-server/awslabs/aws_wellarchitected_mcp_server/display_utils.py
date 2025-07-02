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

"""Display utilities for consistent emoji usage across the Well-Architected MCP server."""

from .models import Pillar, RiskLevel

# Risk level emojis
RISK_EMOJIS = {
    RiskLevel.HIGH: "🔴",
    RiskLevel.MEDIUM: "🟡", 
    RiskLevel.LOW: "🟢"
}

# Pillar emojis
PILLAR_EMOJIS = {
    Pillar.OPERATIONAL_EXCELLENCE: "🔧",
    Pillar.SECURITY: "🔒",
    Pillar.RELIABILITY: "🛡️",
    Pillar.PERFORMANCE_EFFICIENCY: "⚡",
    Pillar.COST_OPTIMIZATION: "💰",
    Pillar.SUSTAINABILITY: "🌱"
}

def format_risk_level(risk_level: RiskLevel) -> str:
    """Format risk level with emoji."""
    emoji = RISK_EMOJIS.get(risk_level, "")
    return f"{emoji} **{risk_level.value.upper()}**"

def format_pillar(pillar: Pillar) -> str:
    """Format pillar with emoji."""
    emoji = PILLAR_EMOJIS.get(pillar, "")
    pillar_name = pillar.value.replace('_', ' ').title()
    return f"{emoji} **{pillar_name}**"

def format_pillar_simple(pillar: Pillar) -> str:
    """Format pillar with emoji (simple format)."""
    emoji = PILLAR_EMOJIS.get(pillar, "")
    pillar_name = pillar.value.replace('_', ' ').title()
    return f"{emoji} {pillar_name}"