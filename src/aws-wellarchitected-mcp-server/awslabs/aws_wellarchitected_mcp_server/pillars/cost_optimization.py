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
    "COST01-BP01": BestPractice(
        id="COST01-BP01",
        title="Establish a Cloud Financial Management Function",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",
        description="Establish a dedicated function to manage cloud financial operations and cost optimization",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a dedicated cloud financial management function?",
            "Are roles and responsibilities clearly defined for cost management?",
            "Do you have processes for cost governance and optimization?",
            "Are cost management activities integrated into your organization?"
        ],
        implementation_guidance=[
            "Establish a Cloud Center of Excellence or FinOps team",
            "Define clear roles and responsibilities for cost management",
            "Implement cost governance processes and policies",
            "Integrate cost considerations into architectural decisions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_function.html",
        related_best_practices=["COST01-BP02", "COST01-BP03"],
        requires_user_input=True
    ),
    "COST01-BP02": BestPractice(
        id="COST01-BP02",
        title="Establish a Partnership Between Finance and Technology",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",
        description="Establish a partnership between finance and technology teams to optimize cloud costs",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do finance and technology teams collaborate on cloud cost management?",
            "Are cost considerations integrated into technical decision-making?",
            "Do you have shared accountability for cloud costs?",
            "Are there regular reviews between finance and technology teams?"
        ],
        implementation_guidance=[
            "Create cross-functional teams with finance and technology representatives",
            "Establish shared KPIs and accountability for cloud costs",
            "Implement regular cost review meetings between teams",
            "Integrate cost considerations into architectural review processes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_partnership.html",
        related_best_practices=["COST01-BP01", "COST01-BP03"],
        requires_user_input=True
    ),
    "COST01-BP03": BestPractice(
        id="COST01-BP03",
        title="Establish Cloud Budgets and Forecasts",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",
        description="Establish budgets and forecasts to track and predict cloud spending",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have established budgets for cloud spending?",
            "Are you forecasting future cloud costs?",
            "Do you track actual spending against budgets?",
            "Are budget alerts configured for cost overruns?"
        ],
        implementation_guidance=[
            "Use AWS Budgets to set spending limits",
            "Implement cost forecasting based on historical data",
            "Set up budget alerts for proactive cost management",
            "Review and adjust budgets regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_budget_forecast.html",
        related_best_practices=["COST01-BP01", "COST01-BP04"],
        requires_user_input=True
    ),
    "COST01-BP04": BestPractice(
        id="COST01-BP04",
        title="Implement Cost Awareness in Your Organizational Processes",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",
        description="Integrate cost awareness into organizational processes and decision-making",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are cost considerations integrated into your development processes?",
            "Do teams understand the cost implications of their decisions?",
            "Are cost metrics visible to relevant stakeholders?",
            "Do you have cost-aware architectural review processes?"
        ],
        implementation_guidance=[
            "Include cost considerations in architectural reviews",
            "Provide cost visibility dashboards to teams",
            "Train teams on cost optimization best practices",
            "Integrate cost metrics into performance reviews"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_cost_awareness.html",
        related_best_practices=["COST01-BP03", "COST01-BP05"],
        requires_user_input=True
    ),
    "COST01-BP05": BestPractice(
        id="COST01-BP05",
        title="Report and Notify on Cost Optimization",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",

        description="Implement regular reporting and notifications on cost optimization activities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have regular cost optimization reporting?",
            "Are stakeholders notified of cost anomalies?",
            "Do you track and report on cost optimization initiatives?",
            "Are cost reports accessible to relevant teams?"
        ],
        implementation_guidance=[
            "Create automated cost reports and dashboards",
            "Set up cost anomaly detection and notifications",
            "Track ROI of cost optimization initiatives",
            "Share cost optimization successes across the organization"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_usage_report.html",
        related_best_practices=["COST01-BP04", "COST01-BP06"],
        requires_user_input=True
    ),
    "COST01-BP06": BestPractice(
        id="COST01-BP06",
        title="Monitor Cost Proactively",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",

        description="Implement proactive cost monitoring to identify and address cost issues early",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have proactive cost monitoring in place?",
            "Are cost trends analyzed regularly?",
            "Do you have automated alerts for cost anomalies?",
            "Are cost optimization opportunities identified proactively?"
        ],
        implementation_guidance=[
            "Use AWS Cost Anomaly Detection for automated monitoring",
            "Set up regular cost trend analysis",
            "Implement automated cost optimization recommendations",
            "Schedule regular cost optimization reviews"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_scheduled.html",
        related_best_practices=["COST01-BP05", "COST01-BP07"]
    ),
    "COST01-BP07": BestPractice(
        id="COST01-BP07",
        title="Keep Up-to-Date with New Service Releases",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",

        description="Stay current with new AWS services and features that can provide cost optimization opportunities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you stay informed about new AWS services and features?",
            "Are new cost optimization opportunities evaluated regularly?",
            "Do you have a process for adopting cost-effective new services?",
            "Are teams trained on new cost optimization features?"
        ],
        implementation_guidance=[
            "Subscribe to AWS announcements and cost optimization updates",
            "Regularly evaluate new services for cost optimization potential",
            "Create processes for adopting new cost-effective services",
            "Train teams on new cost optimization features and best practices"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_culture.html",
        related_best_practices=["COST01-BP06", "COST01-BP08"],
        requires_user_input=True
    ),
    "COST01-BP08": BestPractice(
        id="COST01-BP08",
        title="Create a Cost-Aware Culture",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",

        description="Foster a culture where cost optimization is everyone's responsibility",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Is cost optimization part of your organizational culture?",
            "Do employees understand their role in cost management?",
            "Are cost optimization achievements recognized and rewarded?",
            "Do you have cost optimization training programs?"
        ],
        implementation_guidance=[
            "Establish cost optimization as a shared responsibility",
            "Recognize and reward cost optimization achievements",
            "Provide regular training on cost optimization best practices",
            "Include cost optimization in job descriptions and performance metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_quantify_value.html",
        related_best_practices=["COST01-BP07"],
        requires_user_input=True
    ),
    "COST01-BP09": BestPractice(
        id="COST01-BP09",
        title="Quantify Business Value from Cost Optimization",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Practice Cloud Financial Management",

        description="Quantify the business value achieved through cost optimization efforts",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you quantify the business value from cost optimization?",
            "Are cost savings tracked and reported?",
            "Do you measure ROI of optimization efforts?"
        ],
        implementation_guidance=[
            "Track and report cost savings achieved",
            "Calculate ROI of optimization initiatives",
            "Communicate business value to stakeholders"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_quantify_value.html",
        requires_user_input=True
    ),
    "COST02-BP01": BestPractice(
        id="COST02-BP01",
        title="Develop Policies Based on Your Organization Requirements",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Develop and implement policies that align with organizational requirements for cost governance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have policies that govern cloud resource usage?",
            "Are policies aligned with organizational requirements?",
            "Do policies address cost optimization and governance?",
            "Are policies regularly reviewed and updated?"
        ],
        implementation_guidance=[
            "Create policies for resource provisioning and usage",
            "Align policies with business and compliance requirements",
            "Implement automated policy enforcement",
            "Regularly review and update policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_policies.html",
        related_best_practices=["COST02-BP02", "COST02-BP05"],
        requires_user_input=True
    ),
    "COST02-BP02": BestPractice(
        id="COST02-BP02",
        title="Implement Goals and Targets",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Implement cost optimization goals and targets to drive accountability",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have defined cost optimization goals and targets?",
            "Are goals measurable and time-bound?",
            "Do you track progress against targets?",
            "Are goals communicated across the organization?"
        ],
        implementation_guidance=[
            "Set specific, measurable cost optimization targets",
            "Align goals with business objectives",
            "Track and report on goal achievement",
            "Communicate goals and progress to stakeholders"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_goal_target.html",
        related_best_practices=["COST02-BP01", "COST02-BP03"],
        requires_user_input=True
    ),
    "COST02-BP03": BestPractice(
        id="COST02-BP03",
        title="Implement an Account Structure",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Implement a multi-account structure to provide cost isolation and governance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use a multi-account structure for cost isolation?",
            "Are accounts organized by business unit, environment, or function?",
            "Do you have centralized billing and cost management?",
            "Are account structures aligned with organizational boundaries?"
        ],
        implementation_guidance=[
            "Use AWS Organizations for multi-account management",
            "Organize accounts by business unit, environment, or function",
            "Implement consolidated billing for cost visibility",
            "Use Service Control Policies for governance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_account_structure.html",
        related_best_practices=["COST02-BP02", "COST02-BP04"]
    ),
    "COST02-BP04": BestPractice(
        id="COST02-BP04",
        title="Implement Groups and Roles",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Implement groups and roles to manage access and accountability for cost optimization",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have defined groups and roles for cost management?",
            "Are permissions aligned with cost responsibilities?",
            "Do you use least privilege access for cost-related actions?",
            "Are roles regularly reviewed and updated?"
        ],
        implementation_guidance=[
            "Define roles and responsibilities for cost management",
            "Use IAM groups and roles for access control",
            "Implement least privilege access principles",
            "Regularly review and update role assignments"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_groups_roles.html",
        related_best_practices=["COST02-BP03", "COST02-BP05"],
        requires_user_input=True
    ),
    "COST02-BP05": BestPractice(
        id="COST02-BP05",
        title="Implement Cost Controls",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Implement controls to prevent cost overruns and enforce cost governance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have controls to prevent cost overruns?",
            "Are spending limits enforced automatically?",
            "Do you have approval processes for high-cost resources?",
            "Are cost controls regularly monitored and updated?"
        ],
        implementation_guidance=[
            "Use AWS Budgets for spending limits and alerts",
            "Implement Service Control Policies for resource restrictions",
            "Use approval workflows for high-cost resources",
            "Monitor and adjust controls based on usage patterns"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_controls.html",
        related_best_practices=["COST02-BP01", "COST02-BP06"]
    ),
    "COST02-BP06": BestPractice(
        id="COST02-BP06",
        title="Track Project Lifecycle",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Governance",

        description="Track costs throughout the project lifecycle to ensure cost-effective resource usage",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you track costs throughout the project lifecycle?",
            "Are cost estimates compared to actual spending?",
            "Do you have processes for cost optimization during projects?",
            "Are lessons learned captured for future projects?"
        ],
        implementation_guidance=[
            "Implement cost tracking from project initiation to completion",
            "Compare estimated vs. actual costs regularly",
            "Conduct cost optimization reviews during project phases",
            "Capture and share cost optimization lessons learned"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_track_lifecycle.html",
        related_best_practices=["COST02-BP05"],
        requires_user_input=True
    ),
    "COST03-BP01": BestPractice(
        id="COST03-BP01",
        title="Configure Detailed Information Sources",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Configure detailed billing and cost information sources for comprehensive cost visibility",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have detailed billing information configured?",
            "Are you using AWS Cost and Usage Reports?",
            "Do you have granular cost and usage data?",
            "Are all cost sources properly configured?"
        ],
        implementation_guidance=[
            "Enable AWS Cost and Usage Reports for detailed billing data",
            "Configure AWS Cost Explorer for cost analysis",
            "Use AWS Budgets for cost tracking and alerts",
            "Enable detailed billing features in all accounts"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_detailed_source.html",
        related_best_practices=["COST03-BP02", "COST03-BP05"]
    ),
    "COST03-BP02": BestPractice(
        id="COST03-BP02",
        title="Identify Cost Attribution Categories",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Identify and implement cost attribution categories for organizational cost allocation",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have defined cost attribution categories?",
            "Are costs allocated to business units or projects?",
            "Do you use consistent tagging for cost attribution?",
            "Are attribution categories aligned with organizational structure?"
        ],
        implementation_guidance=[
            "Define cost attribution categories based on organizational structure",
            "Implement consistent tagging strategies",
            "Use cost allocation tags for automated attribution",
            "Regularly review and update attribution categories"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_org_information.html",
        related_best_practices=["COST03-BP01", "COST03-BP03"],
        requires_user_input=True
    ),
    "COST03-BP03": BestPractice(
        id="COST03-BP03",
        title="Establish Organization Metrics",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Establish metrics that provide insights into cost and usage across the organization",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have established cost and usage metrics?",
            "Are metrics aligned with business objectives?",
            "Do you track efficiency and utilization metrics?",
            "Are metrics regularly reviewed and updated?"
        ],
        implementation_guidance=[
            "Define key cost and usage metrics",
            "Align metrics with business objectives and KPIs",
            "Track efficiency metrics like cost per transaction",
            "Implement automated metric collection and reporting"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_define_attribution.html",
        related_best_practices=["COST03-BP02", "COST03-BP04"],
        requires_user_input=True
    ),
    "COST03-BP04": BestPractice(
        id="COST03-BP04",
        title="Configure Billing and Cost Management Tools",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Configure AWS billing and cost management tools for comprehensive cost monitoring",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are AWS cost management tools properly configured?",
            "Do you use Cost Explorer for cost analysis?",
            "Are budgets and alerts configured?",
            "Do you have cost anomaly detection enabled?"
        ],
        implementation_guidance=[
            "Configure AWS Cost Explorer for detailed cost analysis",
            "Set up AWS Budgets with appropriate alerts",
            "Enable AWS Cost Anomaly Detection",
            "Use AWS Cost and Usage Reports for detailed analysis"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_define_kpi.html",
        related_best_practices=["COST03-BP03", "COST03-BP05"]
    ),
    "COST03-BP05": BestPractice(
        id="COST03-BP05",
        title="Add Organization Information to Cost and Usage",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Add organizational information to cost and usage data for better attribution and analysis",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you add organizational context to cost data?",
            "Are resources tagged with organizational information?",
            "Do you have consistent tagging across all resources?",
            "Is organizational information used for cost allocation?"
        ],
        implementation_guidance=[
            "Implement comprehensive resource tagging strategies",
            "Use cost allocation tags for organizational attribution",
            "Automate tagging through policies and templates",
            "Regularly audit and enforce tagging compliance"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_config_tools.html",
        related_best_practices=["COST03-BP01", "COST03-BP06"]
    ),
    "COST03-BP06": BestPractice(
        id="COST03-BP06",
        title="Allocate Costs Based on Workload Metrics",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Monitor cost and usage",

        description="Allocate costs based on workload metrics to understand true cost per business outcome",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you allocate costs based on workload metrics?",
            "Are costs attributed to business outcomes?",
            "Do you track cost per unit of business value?",
            "Are allocation methods regularly reviewed and updated?"
        ],
        implementation_guidance=[
            "Define workload metrics that correlate with business value",
            "Implement cost allocation based on usage metrics",
            "Track cost per business outcome or transaction",
            "Use automated tools for metric-based cost allocation"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_monitor_usage_allocate_outcome.html",
        related_best_practices=["COST03-BP05"],
        requires_user_input=True
    ),
    "COST04-BP01": BestPractice(
        id="COST04-BP01",
        title="Track Resources Over Their Lifetime",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Decommission resources",

        description="Track resources throughout their lifecycle to identify decommissioning opportunities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you track resources throughout their lifecycle?",
            "Are resource usage patterns monitored?",
            "Do you identify underutilized or unused resources?",
            "Are resource lifecycles documented and managed?"
        ],
        implementation_guidance=[
            "Implement resource lifecycle tracking",
            "Monitor resource utilization patterns",
            "Use AWS Trusted Advisor for resource optimization recommendations",
            "Set up automated alerts for underutilized resources"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_track.html",
        related_best_practices=["COST04-BP02", "COST04-BP03"]
    ),
    "COST04-BP02": BestPractice(
        id="COST04-BP02",
        title="Implement a Decommissioning Process",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Decommission resources",

        description="Implement a systematic process for decommissioning unused resources",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a defined decommissioning process?",
            "Are decommissioning procedures documented?",
            "Do you have approval workflows for resource decommissioning?",
            "Are decommissioning activities tracked and reported?"
        ],
        implementation_guidance=[
            "Define clear decommissioning procedures and workflows",
            "Implement approval processes for resource termination",
            "Document decommissioning procedures and responsibilities",
            "Track and report on decommissioning activities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_implement_process.html",
        related_best_practices=["COST04-BP01", "COST04-BP03"],
        requires_user_input=True
    ),
    "COST04-BP03": BestPractice(
        id="COST04-BP03",
        title="Decommission Resources",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Decommission resources",

        description="Actively decommission resources that are no longer needed",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly decommission unused resources?",
            "Are decommissioning activities performed systematically?",
            "Do you verify resource dependencies before decommissioning?",
            "Are decommissioning results tracked and measured?"
        ],
        implementation_guidance=[
            "Regularly identify and decommission unused resources",
            "Verify dependencies and impacts before decommissioning",
            "Use automated tools for safe resource decommissioning",
            "Track cost savings from decommissioning activities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_decommission.html",
        related_best_practices=["COST04-BP02", "COST04-BP04"]
    ),
    "COST04-BP04": BestPractice(
        id="COST04-BP04",
        title="Decommission Resources Automatically",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Decommission resources",

        description="Implement automated decommissioning for resources that are no longer needed",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated decommissioning processes?",
            "Are resources automatically terminated when no longer needed?",
            "Do you use scheduling for temporary resources?",
            "Are automated decommissioning rules regularly reviewed?"
        ],
        implementation_guidance=[
            "Implement automated resource scheduling and termination",
            "Use AWS Instance Scheduler for automated start/stop",
            "Set up automated cleanup for temporary resources",
            "Regularly review and update automation rules"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_decomm_automated.html",
        related_best_practices=["COST04-BP03", "COST04-BP05"]
    ),
    "COST04-BP05": BestPractice(
        id="COST04-BP05",
        title="Enforce Data Retention Policies",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Decommission resources",

        description="Enforce data retention policies to optimize storage costs",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have defined data retention policies?",
            "Are retention policies automatically enforced?",
            "Do you use appropriate storage classes for different data types?",
            "Are retention policies regularly reviewed and updated?"
        ],
        implementation_guidance=[
            "Define data retention policies based on business and compliance requirements",
            "Use S3 lifecycle policies for automated data management",
            "Implement appropriate storage classes for different data types",
            "Regularly review and update retention policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html",
        related_best_practices=["COST04-BP04"]
    ),
    "COST05-BP01": BestPractice(
        id="COST05-BP01",
        title="Perform Cost Analysis for Different Usage Over Time",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Analyze costs for different usage patterns and time periods to select cost-effective services",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you analyze costs for different usage patterns?",
            "Are cost comparisons performed over different time periods?",
            "Do you consider usage variability in service selection?",
            "Are cost analyses updated regularly as usage patterns change?"
        ],
        implementation_guidance=[
            "Analyze historical usage patterns and costs",
            "Compare costs across different service options",
            "Consider usage variability and seasonality",
            "Use AWS Cost Explorer for detailed cost analysis"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_requirements.html",
        related_best_practices=["COST05-BP02", "COST05-BP03"]
    ),
    "COST05-BP02": BestPractice(
        id="COST05-BP02",
        title="Select Service Components to Optimize Cost in Line with Organization Priorities",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Select service components that optimize cost while meeting organizational priorities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you select services based on organizational priorities?",
            "Are cost considerations balanced with other requirements?",
            "Do you evaluate all available service options?",
            "Are service selections regularly reviewed and optimized?"
        ],
        implementation_guidance=[
            "Evaluate all available service options for each use case",
            "Balance cost with performance, security, and reliability requirements",
            "Consider managed services to reduce operational overhead",
            "Regularly review service selections for optimization opportunities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_analyze_all.html",
        related_best_practices=["COST05-BP01", "COST05-BP03"],
        requires_user_input=True
    ),
    "COST05-BP03": BestPractice(
        id="COST05-BP03",
        title="Perform a Thorough Analysis of Each Component",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Perform thorough analysis of each service component to ensure cost-effective selection",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you perform thorough analysis of service components?",
            "Are all cost factors considered in the analysis?",
            "Do you evaluate long-term cost implications?",
            "Are analyses documented and shared?"
        ],
        implementation_guidance=[
            "Analyze all cost components including compute, storage, and data transfer",
            "Consider both direct and indirect costs",
            "Evaluate long-term cost trends and projections",
            "Document analysis results for future reference"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_thorough_analysis.html",
        related_best_practices=["COST05-BP02", "COST05-BP04"],
        requires_user_input=True
    ),
    "COST05-BP04": BestPractice(
        id="COST05-BP04",
        title="Select Software with Cost-Effective Licensing",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Select software with licensing models that provide cost-effective solutions",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you evaluate software licensing costs?",
            "Are licensing models aligned with usage patterns?",
            "Do you consider open-source alternatives?",
            "Are licensing costs tracked and optimized?"
        ],
        implementation_guidance=[
            "Evaluate different licensing models and their cost implications",
            "Consider open-source alternatives where appropriate",
            "Use AWS License Manager to track and optimize licenses",
            "Regularly review licensing costs and usage"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_licensing.html",
        related_best_practices=["COST05-BP03", "COST05-BP05"],
        requires_user_input=True
    ),
    "COST05-BP05": BestPractice(
        id="COST05-BP05",
        title="Select Services for This Workload to Optimize Cost",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Select services specifically optimized for cost while meeting workload requirements",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are services selected specifically for cost optimization?",
            "Do selected services meet all workload requirements?",
            "Are cost-optimized service configurations used?",
            "Are service selections regularly reviewed for cost optimization?"
        ],
        implementation_guidance=[
            "Choose services that provide the best cost-performance ratio",
            "Use cost-optimized service configurations",
            "Consider serverless and managed services to reduce costs",
            "Regularly review and optimize service selections"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_select_for_cost.html",
        related_best_practices=["COST05-BP04", "COST05-BP06"],
        requires_user_input=True
    ),
    "COST05-BP06": BestPractice(
        id="COST05-BP06",
        title="Perform Cost Analysis for Different Usage Over Time",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Evaluate cost when selecting services",

        description="Analyze how costs change with different usage patterns over time",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you analyze cost changes over different time periods?",
            "Are usage pattern variations considered in cost analysis?",
            "Do you project future costs based on usage trends?",
            "Are cost analyses updated as usage patterns evolve?"
        ],
        implementation_guidance=[
            "Analyze costs across different time periods and usage patterns",
            "Use historical data to project future costs",
            "Consider seasonal and cyclical usage variations",
            "Update cost models as usage patterns change"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_analyze_over_time.html",
        related_best_practices=["COST05-BP05"],
        requires_user_input=True
    ),
    "COST06-BP01": BestPractice(
        id="COST06-BP01",
        title="Perform Cost Modeling",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the correct resource type, size, and number",

        description="Perform cost modeling to understand the cost implications of different resource configurations",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform cost modeling for resource selection?",
            "Are different resource configurations compared for cost?",
            "Do cost models include all relevant factors?",
            "Are cost models updated regularly?"
        ],
        implementation_guidance=[
            "Create detailed cost models for different resource options",
            "Include all cost factors in modeling",
            "Use AWS Pricing Calculator for cost estimation",
            "Regularly update models with actual usage data"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.html",
        related_best_practices=["COST06-BP02", "COST06-BP03"],
        requires_user_input=True
    ),
    "COST06-BP02": BestPractice(
        id="COST06-BP02",
        title="Select Resource Type and Size Based on Data",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the correct resource type, size, and number",

        description="Select resource types and sizes based on performance and utilization data",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you select resources based on actual usage data?",
            "Are resource types and sizes optimized for workload requirements?",
            "Do you use performance data to guide resource selection?",
            "Are resource selections regularly reviewed and optimized?"
        ],
        implementation_guidance=[
            "Use performance and utilization data to guide resource selection",
            "Right-size resources based on actual requirements",
            "Use AWS Compute Optimizer for resource recommendations",
            "Regularly review and adjust resource configurations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html",
        related_best_practices=["COST06-BP01", "COST06-BP03"]
    ),
    "COST06-BP03": BestPractice(
        id="COST06-BP03",
        title="Select Resource Type and Size Based on Metrics",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the correct resource type, size, and number",

        description="Use metrics to select appropriate resource types and sizes for optimal cost-performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use metrics to guide resource selection?",
            "Are resource decisions based on performance metrics?",
            "Do you monitor resource utilization metrics?",
            "Are metrics used to optimize resource configurations?"
        ],
        implementation_guidance=[
            "Monitor key performance and utilization metrics",
            "Use metrics to identify optimization opportunities",
            "Set up automated alerts for resource optimization",
            "Regularly analyze metrics to guide resource decisions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_metrics.html",
        related_best_practices=["COST06-BP02", "COST06-BP04"]
    ),
    "COST06-BP04": BestPractice(
        id="COST06-BP04",
        title="Use Shared Resources",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the correct resource type, size, and number",

        description="Use shared resources to reduce costs through economies of scale",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use shared resources where appropriate?",
            "Are resources shared across multiple workloads?",
            "Do you leverage economies of scale?",
            "Are shared resource costs allocated appropriately?"
        ],
        implementation_guidance=[
            "Identify opportunities for resource sharing",
            "Use shared services and infrastructure where appropriate",
            "Implement proper cost allocation for shared resources",
            "Monitor shared resource utilization and costs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_shared.html",
        related_best_practices=["COST06-BP03"],
        requires_user_input=True
    ),
    "COST07-BP01": BestPractice(
        id="COST07-BP01",
        title="Perform Pricing Model Analysis",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the best pricing model",

        description="Analyze different pricing models to select the most cost-effective options",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you analyze different pricing models?",
            "Are pricing options compared for cost-effectiveness?",
            "Do you consider usage patterns in pricing model selection?",
            "Are pricing model decisions regularly reviewed?"
        ],
        implementation_guidance=[
            "Compare On-Demand, Reserved, and Spot pricing options",
            "Analyze usage patterns to determine optimal pricing models",
            "Use AWS Cost Explorer to analyze pricing options",
            "Regularly review and optimize pricing model selections"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_analysis.html",
        related_best_practices=["COST07-BP02", "COST07-BP04"],
        requires_user_input=True
    ),
    "COST07-BP02": BestPractice(
        id="COST07-BP02",
        title="Choose Regions Based on Cost",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the best pricing model",

        description="Select AWS regions based on cost considerations while meeting other requirements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you consider cost when selecting regions?",
            "Are regional pricing differences analyzed?",
            "Do you balance cost with latency and compliance requirements?",
            "Are regional cost decisions regularly reviewed?"
        ],
        implementation_guidance=[
            "Compare pricing across different AWS regions",
            "Balance cost with latency and compliance requirements",
            "Consider data transfer costs between regions",
            "Regularly review regional cost implications"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_region_cost.html",
        related_best_practices=["COST07-BP01", "COST07-BP03"],
        requires_user_input=True
    ),
    "COST07-BP03": BestPractice(
        id="COST07-BP03",
        title="Select Third-Party Agreements with Cost-Efficient Terms",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the best pricing model",

        description="Negotiate and select third-party agreements with cost-efficient terms",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you negotiate cost-efficient third-party agreements?",
            "Are third-party costs regularly reviewed and optimized?",
            "Do you consider alternative vendors for cost optimization?",
            "Are third-party agreements aligned with usage patterns?"
        ],
        implementation_guidance=[
            "Negotiate volume discounts and favorable terms",
            "Regularly review third-party costs and agreements",
            "Consider alternative vendors for cost optimization",
            "Align agreements with actual usage patterns"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_third_party.html",
        related_best_practices=["COST07-BP02", "COST07-BP04"],
        requires_user_input=True
    ),
    "COST07-BP04": BestPractice(
        id="COST07-BP04",
        title="Implement Pricing Models for All Components",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the best pricing model",

        description="Implement appropriate pricing models for all workload components",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are appropriate pricing models implemented for all components?",
            "Do pricing models align with usage patterns?",
            "Are pricing model implementations regularly optimized?",
            "Do you track the effectiveness of pricing model choices?"
        ],
        implementation_guidance=[
            "Implement Reserved Instances for predictable workloads",
            "Use Spot Instances for fault-tolerant workloads",
            "Apply Savings Plans for flexible compute usage",
            "Regularly review and optimize pricing model implementations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_implement_models.html",
        related_best_practices=["COST07-BP01", "COST07-BP05"]
    ),
    "COST07-BP05": BestPractice(
        id="COST07-BP05",
        title="Perform Regular Analysis of Pricing Options",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Select the best pricing model",

        description="Regularly analyze pricing options to ensure continued cost optimization",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you regularly analyze pricing options?",
            "Are new pricing models evaluated as they become available?",
            "Do you track changes in usage patterns that affect pricing?",
            "Are pricing optimizations implemented based on analysis?"
        ],
        implementation_guidance=[
            "Schedule regular reviews of pricing options",
            "Evaluate new pricing models and features as they become available",
            "Monitor usage pattern changes that affect pricing",
            "Implement pricing optimizations based on analysis results"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_master_analysis.html",
        related_best_practices=["COST07-BP04"],
        requires_user_input=True
    ),
    "COST08-BP01": BestPractice(
        id="COST08-BP01",
        title="Implement Data Transfer Cost Modeling",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Plan for data transfer",

        description="Model data transfer costs to understand and optimize data movement expenses",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you model data transfer costs in your architecture?",
            "Are data transfer patterns analyzed for cost optimization?",
            "Do you understand the cost implications of data movement?",
            "Are data transfer costs tracked and optimized?"
        ],
        implementation_guidance=[
            "Model data transfer costs between services and regions",
            "Analyze data flow patterns for cost optimization opportunities",
            "Use AWS Cost Explorer to track data transfer costs",
            "Consider data locality to minimize transfer costs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_modeling.html",
        related_best_practices=["COST08-BP02", "COST08-BP03"]
    ),
    "COST08-BP02": BestPractice(
        id="COST08-BP02",
        title="Select Components to Optimize Data Transfer Costs",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Plan for data transfer",

        description="Select components and architectures that minimize data transfer costs",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you select components to minimize data transfer costs?",
            "Are data transfer costs considered in architectural decisions?",
            "Do you use content delivery networks to reduce transfer costs?",
            "Are data compression and caching strategies implemented?"
        ],
        implementation_guidance=[
            "Use CloudFront CDN to reduce data transfer costs",
            "Implement data compression to reduce transfer volumes",
            "Use caching strategies to minimize repeated data transfers",
            "Consider regional data placement to reduce cross-region transfers"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized_components.html",
        related_best_practices=["COST08-BP01", "COST08-BP03"]
    ),
    "COST08-BP03": BestPractice(
        id="COST08-BP03",
        title="Implement Services to Reduce Data Transfer Costs",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Plan for data transfer",

        description="Implement AWS services specifically designed to reduce data transfer costs",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use AWS services designed to reduce data transfer costs?",
            "Are you leveraging AWS Direct Connect for consistent data transfer?",
            "Do you use AWS DataSync for efficient data transfer?",
            "Are you optimizing data transfer with appropriate AWS services?"
        ],
        implementation_guidance=[
            "Use AWS Direct Connect for predictable data transfer costs",
            "Implement AWS DataSync for efficient data synchronization",
            "Use AWS Storage Gateway to optimize hybrid data transfer",
            "Consider AWS Snowball family for large data transfers"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_implement_services.html",
        related_best_practices=["COST08-BP02"]
    ),
    "COST09-BP01": BestPractice(
        id="COST09-BP01",
        title="Perform Analysis on the Workload Demand",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Manage demand and supply resources",

        description="Analyze workload demand patterns to optimize resource provisioning and costs",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you analyze workload demand patterns?",
            "Are demand forecasts used for resource planning?",
            "Do you understand peak and off-peak usage patterns?",
            "Are demand analysis results used to optimize costs?"
        ],
        implementation_guidance=[
            "Analyze historical usage patterns and trends",
            "Use demand forecasting for capacity planning",
            "Identify peak and off-peak usage periods",
            "Use demand analysis to optimize resource provisioning"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.html",
        related_best_practices=["COST09-BP02", "COST09-BP03"],
        requires_user_input=True
    ),
    "COST09-BP02": BestPractice(
        id="COST09-BP02",
        title="Implement a Buffer or Throttle to Manage Demand",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Manage demand and supply resources",

        description="Implement buffering or throttling mechanisms to manage demand and control costs",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you implement buffering or throttling to manage demand?",
            "Are demand spikes handled cost-effectively?",
            "Do you use queuing mechanisms to smooth demand?",
            "Are throttling policies implemented to control costs?"
        ],
        implementation_guidance=[
            "Use SQS queues to buffer demand spikes",
            "Implement API throttling to control request rates",
            "Use auto-scaling policies with appropriate thresholds",
            "Consider using spot instances for buffered workloads"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_buffer_throttle.html",
        related_best_practices=["COST09-BP01", "COST09-BP03"]
    ),
    "COST09-BP03": BestPractice(
        id="COST09-BP03",
        title="Supply Resources Dynamically",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Manage demand and supply resources",

        description="Dynamically supply resources based on demand to optimize costs",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you supply resources dynamically based on demand?",
            "Are resources automatically scaled up and down?",
            "Do you use serverless architectures where appropriate?",
            "Are resource provisioning decisions automated?"
        ],
        implementation_guidance=[
            "Use Auto Scaling to dynamically adjust capacity",
            "Implement serverless architectures with Lambda",
            "Use container orchestration for dynamic resource allocation",
            "Automate resource provisioning based on demand metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html",
        related_best_practices=["COST09-BP01", "COST09-BP02"]
    ),
    "COST10-BP01": BestPractice(
        id="COST10-BP01",
        title="Develop a Workload Review Process",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Define review process",

        description="Develop a process to regularly review workloads for cost optimization opportunities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a regular workload review process?",
            "Are cost optimization opportunities identified systematically?",
            "Do reviews include evaluation of new services and features?",
            "Are review findings implemented and tracked?"
        ],
        implementation_guidance=[
            "Establish regular workload review cycles",
            "Create standardized review processes and checklists",
            "Include cost optimization in architectural reviews",
            "Track and implement review recommendations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_process.html",
        related_best_practices=["COST10-BP02"],
        requires_user_input=True
    ),
    "COST10-BP02": BestPractice(
        id="COST10-BP02",
        title="Review and Analyze This Workload Regularly",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Define review process",

        description="Regularly review and analyze workloads to identify cost optimization opportunities",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly review your workload for cost optimization?",
            "Are usage patterns and costs analyzed systematically?",
            "Do you identify and act on optimization opportunities?",
            "Are cost trends monitored and analyzed?"
        ],
        implementation_guidance=[
            "Schedule regular cost optimization reviews",
            "Analyze usage patterns and cost trends",
            "Use AWS Cost Explorer and Trusted Advisor for insights",
            "Implement identified optimization opportunities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_workload.html",
        related_best_practices=["COST10-BP01"],
        requires_user_input=True
    ),
    "COST11-BP01": BestPractice(
        id="COST11-BP01",
        title="Perform Automation for Operations",
        pillar=Pillar.COST_OPTIMIZATION,
        area="Automating operations",

        description="Automate operations to reduce manual effort and associated costs",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you automate operations to reduce manual effort?",
            "Are repetitive tasks automated for cost efficiency?",
            "Do you use automation to optimize resource management?",
            "Are operational costs reduced through automation?"
        ],
        implementation_guidance=[
            "Automate resource provisioning and management",
            "Use AWS Systems Manager for operational automation",
            "Implement automated backup and maintenance tasks",
            "Use Infrastructure as Code for consistent deployments"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_cost_effort_automations_operations.html",
        requires_user_input=True
    )
}