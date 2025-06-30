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

"""Architecture Decision Record (ADR) generator for Well-Architected reviews."""

import os
from awslabs.aws_wellarchitected_mcp_server.models import ArchitecturalDecisionRecord, BestPracticeAssessment
from datetime import datetime
from loguru import logger
from typing import List


class ADRGenerator:
    """Generates and manages Architecture Decision Records."""

    def __init__(self, output_directory: str = "./adrs"):
        """Initialize the ADR generator."""
        self.output_directory = output_directory
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """Ensure the output directory exists."""
        os.makedirs(self.output_directory, exist_ok=True)

    def generate_adr_file(self, assessment: BestPracticeAssessment) -> str:
        """Generate an ADR file for a best practice assessment."""
        adr = assessment.adr
        filename = f"{assessment.best_practice_id.lower()}-{adr.title.lower().replace(' ', '-').replace(':', '')}.md"
        filepath = os.path.join(self.output_directory, filename)
        
        content = self._format_adr_markdown(adr, assessment)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Generated ADR file: {filepath}")
        return filepath

    def generate_all_adrs(self, assessments: List[BestPracticeAssessment]) -> List[str]:
        """Generate ADR files for all assessments."""
        generated_files = []
        
        for assessment in assessments:
            try:
                filepath = self.generate_adr_file(assessment)
                generated_files.append(filepath)
            except Exception as e:
                logger.error(f"Failed to generate ADR for {assessment.best_practice_id}: {e}")
        
        # Generate index file
        index_file = self._generate_index_file(assessments)
        generated_files.append(index_file)
        
        return generated_files

    def _format_adr_markdown(self, adr: ArchitecturalDecisionRecord, assessment: BestPracticeAssessment) -> str:
        """Format an ADR as Markdown."""
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        content = f"""# {adr.title}

**Date:** {date_str}
**Status:** {adr.status}
**Best Practice ID:** {assessment.best_practice_id}
**Pillar:** {assessment.pillar.value}
**Risk Level:** {assessment.risk_level.value}
**Current Status:** {assessment.status.value}

## Context

{adr.context}

### Current Implementation Status
{assessment.current_implementation}

### Identified Gaps
"""
        
        for gap in assessment.gaps_identified:
            content += f"- {gap}\n"
        
        content += f"""
## Decision

{adr.decision}

## Consequences

"""
        
        for consequence in adr.consequences:
            content += f"- {consequence}\n"
        
        content += """
## Trade-offs

"""
        
        for trade_off in adr.trade_offs:
            content += f"""### Benefit
{trade_off.benefit}

### Cost
{trade_off.cost}

"""
        
        content += """## Alternatives Considered

"""
        
        for alternative in adr.alternatives_considered:
            content += f"- {alternative}\n"
        
        content += f"""
## Implementation Notes

{adr.implementation_notes or 'No specific implementation notes provided.'}

## Recommendations

"""
        
        for recommendation in assessment.recommendations:
            content += f"- {recommendation}\n"
        
        content += f"""
## Well-Architected Framework Reference

**Pillar:** {assessment.pillar.value}
**Best Practice:** {assessment.title}
**Description:** {assessment.description}

---
*This ADR was generated as part of an AWS Well-Architected Framework review.*
"""
        
        return content

    def _generate_index_file(self, assessments: List[BestPracticeAssessment]) -> str:
        """Generate an index file for all ADRs."""
        filepath = os.path.join(self.output_directory, "README.md")
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        content = f"""# Architecture Decision Records

**Generated:** {date_str}
**Total ADRs:** {len(assessments)}

This directory contains Architecture Decision Records (ADRs) generated from an AWS Well-Architected Framework review.

## Summary by Pillar

"""
        
        # Group by pillar
        by_pillar = {}
        for assessment in assessments:
            pillar = assessment.pillar.value
            if pillar not in by_pillar:
                by_pillar[pillar] = []
            by_pillar[pillar].append(assessment)
        
        for pillar, pillar_assessments in by_pillar.items():
            content += f"### {pillar}\n\n"
            for assessment in pillar_assessments:
                filename = f"{assessment.best_practice_id.lower()}-{assessment.adr.title.lower().replace(' ', '-').replace(':', '')}.md"
                status_emoji = {
                    "COMPLIANT": "✅",
                    "NON_COMPLIANT": "❌", 
                    "NEEDS_REVIEW": "⚠️",
                    "NOT_APPLICABLE": "➖"
                }.get(assessment.status.value, "❓")
                
                risk_emoji = {
                    "HIGH": "🔴",
                    "MEDIUM": "🟡",
                    "LOW": "🟢"
                }.get(assessment.risk_level.value, "⚪")
                
                content += f"- [{assessment.title}](./{filename}) {status_emoji} {risk_emoji}\n"
            content += "\n"
        
        content += """## Legend

### Status
- ✅ Compliant
- ❌ Non-Compliant  
- ⚠️ Needs Review
- ➖ Not Applicable

### Risk Level
- 🔴 High Risk
- 🟡 Medium Risk
- 🟢 Low Risk

## Usage

Each ADR file contains:
- Context and problem statement
- Architectural decision made
- Consequences and trade-offs
- Implementation recommendations
- Well-Architected Framework references

Review each ADR to understand the current state and recommended improvements for your architecture.
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Generated ADR index file: {filepath}")
        return filepath