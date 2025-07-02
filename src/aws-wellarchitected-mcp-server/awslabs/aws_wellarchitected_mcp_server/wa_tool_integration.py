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

"""AWS Well-Architected Tool integration for MCP server."""

import boto3
from typing import Dict, List, Optional
from loguru import logger
from .models import Pillar, RiskLevel
from .display_utils import format_pillar_simple, format_risk_level

class WAToolIntegration:
    """Integration with AWS Well-Architected Tool API for WAFR (Well-Architected Framework Reviews)."""
    
    def __init__(self, aws_profile: Optional[str] = None, region: str = "us-east-1"):
        """Initialize AWS Well-Architected Tool client."""
        try:
            session = boto3.Session(profile_name=aws_profile) if aws_profile else boto3.Session()
            self.client = session.client('wellarchitected', region_name=region)
            self.region = region
        except Exception as e:
            logger.error(f"Failed to initialize AWS Well-Architected client: {e}")
            raise

    def list_workloads(self) -> Dict:
        """List all Well-Architected workloads."""
        try:
            response = self.client.list_workloads()
            workloads = []
            
            for workload in response.get('WorkloadSummaries', []):
                workloads.append({
                    'workload_id': workload['WorkloadId'],
                    'workload_name': workload['WorkloadName'],
                    'description': workload.get('Description', ''),
                    'environment': workload.get('Environment', ''),
                    'updated_at': workload.get('UpdatedAt', '').isoformat() if workload.get('UpdatedAt') else '',
                    'pillars': workload.get('PillarPriorities', []),
                    'risk_counts': workload.get('RiskCounts', {})
                })
            
            return {
                'workloads': workloads,
                'total_count': len(workloads)
            }
            
        except Exception as e:
            logger.error(f"Error listing workloads: {e}")
            return {'error': str(e)}

    def get_workload_details(self, workload_id: str) -> Dict:
        """Get detailed information about a specific workload."""
        try:
            response = self.client.get_workload(WorkloadId=workload_id)
            workload = response['Workload']
            
            return {
                'workload_id': workload['WorkloadId'],
                'workload_name': workload['WorkloadName'],
                'description': workload.get('Description', ''),
                'environment': workload.get('Environment', ''),
                'aws_regions': workload.get('AwsRegions', []),
                'architectural_design': workload.get('ArchitecturalDesign', ''),
                'review_owner': workload.get('ReviewOwner', ''),
                'industry_type': workload.get('IndustryType', ''),
                'industry': workload.get('Industry', ''),
                'pillars': workload.get('PillarPriorities', []),
                'risk_counts': workload.get('RiskCounts', {}),
                'updated_at': workload.get('UpdatedAt', '').isoformat() if workload.get('UpdatedAt') else ''
            }
            
        except Exception as e:
            logger.error(f"Error getting workload details: {e}")
            return {'error': str(e)}

    def get_workload_answers(self, workload_id: str, pillar_id: Optional[str] = None) -> Dict:
        """Get answers for a workload's WAFR (Well-Architected Framework Review)."""
        try:
            params = {'WorkloadId': workload_id}
            if pillar_id:
                params['PillarId'] = pillar_id
                
            response = self.client.list_answers(**params)
            answers = []
            
            for answer in response.get('AnswerSummaries', []):
                answers.append({
                    'question_id': answer['QuestionId'],
                    'pillar_id': answer['PillarId'],
                    'question_title': answer['QuestionTitle'],
                    'risk': answer.get('Risk', 'UNANSWERED'),
                    'reason': answer.get('Reason', ''),
                    'selected_choices': answer.get('SelectedChoices', []),
                    'is_applicable': answer.get('IsApplicable', True)
                })
            
            return {
                'workload_id': workload_id,
                'pillar_id': pillar_id,
                'answers': answers,
                'total_answers': len(answers)
            }
            
        except Exception as e:
            logger.error(f"Error getting workload answers: {e}")
            return {'error': str(e)}

    def create_workload(self, workload_name: str, description: str, environment: str, 
                       aws_regions: List[str], review_owner: str) -> Dict:
        """Create a new Well-Architected workload."""
        try:
            response = self.client.create_workload(
                WorkloadName=workload_name,
                Description=description,
                Environment=environment,
                AwsRegions=aws_regions,
                ReviewOwner=review_owner,
                Lenses=['wellarchitected']
            )
            
            return {
                'workload_id': response['WorkloadId'],
                'workload_arn': response['WorkloadArn'],
                'message': f'Successfully created workload: {workload_name}'
            }
            
        except Exception as e:
            logger.error(f"Error creating workload: {e}")
            return {'error': str(e)}

    def update_answer(self, workload_id: str, question_id: str, selected_choices: List[str], 
                     notes: Optional[str] = None, is_applicable: bool = True) -> Dict:
        """Update an answer for a Well-Architected question."""
        try:
            params = {
                'WorkloadId': workload_id,
                'QuestionId': question_id,
                'SelectedChoices': selected_choices,
                'IsApplicable': is_applicable
            }
            
            if notes:
                params['Notes'] = notes
                
            response = self.client.update_answer(**params)
            
            return {
                'workload_id': workload_id,
                'question_id': question_id,
                'answer': {
                    'risk': response['Answer'].get('Risk', 'UNANSWERED'),
                    'selected_choices': response['Answer'].get('SelectedChoices', []),
                    'is_applicable': response['Answer'].get('IsApplicable', True)
                },
                'message': 'Answer updated successfully'
            }
            
        except Exception as e:
            logger.error(f"Error updating answer: {e}")
            return {'error': str(e)}

    def export_workload_data(self, workload_id: str) -> Dict:
        """Export comprehensive workload data for MCP analysis."""
        try:
            # Get workload details
            workload_details = self.get_workload_details(workload_id)
            if 'error' in workload_details:
                return workload_details
            
            # Get all answers
            all_answers = self.get_workload_answers(workload_id)
            if 'error' in all_answers:
                return all_answers
            
            # Format for MCP compatibility
            export_data = {
                'workload_info': workload_details,
                'assessment_data': {
                    'total_questions': all_answers['total_answers'],
                    'answers_by_pillar': {},
                    'risk_summary': {}
                },
                'export_timestamp': boto3.Session().region_name,
                'mcp_compatible': True
            }
            
            # Group answers by pillar
            pillar_groups = {}
            risk_counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'UNANSWERED': 0}
            
            for answer in all_answers['answers']:
                pillar = answer['pillar_id']
                if pillar not in pillar_groups:
                    pillar_groups[pillar] = []
                
                pillar_groups[pillar].append(answer)
                risk_counts[answer['risk']] = risk_counts.get(answer['risk'], 0) + 1
            
            export_data['assessment_data']['answers_by_pillar'] = pillar_groups
            export_data['assessment_data']['risk_summary'] = risk_counts
            
            return export_data
            
        except Exception as e:
            logger.error(f"Error exporting workload data: {e}")
            return {'error': str(e)}

def format_wa_tool_response(data: Dict, response_type: str) -> str:
    """Format Well-Architected Tool responses with emojis."""
    if response_type == "workload_list":
        if not data.get('workloads'):
            return "No workloads found in AWS Well-Architected Tool."
        
        formatted = f"# 🏗️ AWS Well-Architected Workloads ({data['total_count']})\n\n"
        
        for workload in data['workloads']:
            risk_summary = workload.get('risk_counts', {})
            high_risk = risk_summary.get('HIGH', 0)
            medium_risk = risk_summary.get('MEDIUM', 0)
            
            formatted += f"## {workload['workload_name']}\n"
            formatted += f"**ID**: `{workload['workload_id']}`\n"
            formatted += f"**Environment**: {workload.get('environment', 'Not specified')}\n"
            formatted += f"**Description**: {workload.get('description', 'No description')}\n"
            
            if high_risk > 0 or medium_risk > 0:
                formatted += f"**Risks**: 🔴 {high_risk} High, 🟡 {medium_risk} Medium\n"
            
            formatted += f"**Last Updated**: {workload.get('updated_at', 'Unknown')}\n\n"
        
        return formatted
    
    elif response_type == "workload_details":
        formatted = f"# 🏗️ {data['workload_name']}\n\n"
        formatted += f"**Workload ID**: `{data['workload_id']}`\n"
        formatted += f"**Environment**: {data.get('environment', 'Not specified')}\n"
        formatted += f"**AWS Regions**: {', '.join(data.get('aws_regions', []))}\n"
        formatted += f"**Review Owner**: {data.get('review_owner', 'Not specified')}\n"
        formatted += f"**Industry**: {data.get('industry', 'Not specified')}\n\n"
        
        if data.get('description'):
            formatted += f"**Description**: {data['description']}\n\n"
        
        risk_counts = data.get('risk_counts', {})
        if risk_counts:
            formatted += "## Risk Summary\n"
            formatted += f"- 🔴 **High Risk**: {risk_counts.get('HIGH', 0)}\n"
            formatted += f"- 🟡 **Medium Risk**: {risk_counts.get('MEDIUM', 0)}\n"
            formatted += f"- 🟢 **Low Risk**: {risk_counts.get('LOW', 0)}\n"
            formatted += f"- ⚪ **Not Reviewed**: {risk_counts.get('UNANSWERED', 0)}\n\n"
        
        return formatted
    
    return str(data)