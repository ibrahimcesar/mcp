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
    description: str
    risk_level: RiskLevel
    questions: List[str]
    implementation_guidance: List[str]
    requires_user_input: bool = False
    url: str = ""
    related_best_practices: List[str] = []


# Well-Architected Framework Best Practices
WELL_ARCHITECTED_BEST_PRACTICES: Dict[str, BestPractice] = {
    # Operational Excellence
    "OPS01-BP01": BestPractice(
        id="OPS01-BP01",
        title="Evaluate External Customer Needs",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Involve key stakeholders to determine where to focus efforts on external customer needs",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you engage key stakeholders (business, development, operations) to understand customer needs?",
            "Do you have mechanisms to capture external customer feedback?",
            "Do you work backwards from customer outcomes when planning?",
            "Do you understand how operational practices support business outcomes?"
        ],
        implementation_guidance=[
            "Establish regular stakeholder meetings across business, development, and operations teams",
            "Implement customer feedback collection mechanisms (surveys, support tickets, analytics)",
            "Create shared understanding of business functions and team roles",
            "Review historical customer support data to inform decisions"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_ext_cust_needs.html",
        related_best_practices=["OPS11-BP03"]
    ),
    "OPS01-BP02": BestPractice(
        id="OPS01-BP02",
        title="Evaluate Internal Customer Needs",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Involve key stakeholders to determine where to focus efforts on internal customer needs",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you engage internal teams when making operational changes that affect them?",
            "Do you understand the impact of operational decisions on internal customers?",
            "Do you have established priorities for improvement efforts?",
            "Do you update priorities as internal customer needs change?"
        ],
        implementation_guidance=[
            "Consult internal teams before implementing operational changes",
            "Establish shared understanding of business functions across teams",
            "Prioritize improvement efforts based on business impact",
            "Regularly review and update priorities as needs evolve"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_int_cust_needs.html",
        related_best_practices=["OPS11-BP03"]
    ),
    "OPS01-BP03": BestPractice(
        id="OPS01-BP03",
        title="Evaluate Governance Requirements",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Incorporate organizational governance requirements into your workload design and operation",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified governance requirements from stakeholders and governance organizations?",
            "Are governance requirements incorporated into your workload architecture?",
            "Can you demonstrate proof of governance requirement compliance?",
            "Do you regularly review and update governance requirements?"
        ],
        implementation_guidance=[
            "Work with stakeholders to identify governance requirements",
            "Use AWS Config to implement governance-as-code",
            "Leverage Service Control Policies in AWS Organizations",
            "Provide documentation validating governance implementation"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_governance_reqs.html"
    ),
    "OPS01-BP04": BestPractice(
        id="OPS01-BP04",
        title="Evaluate Compliance Requirements",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Incorporate regulatory, industry, and internal compliance requirements into architectural selection",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified applicable compliance frameworks (PCI-DSS, FedRAMP, HIPAA, etc.)?",
            "Are compliance requirements incorporated into your architecture design process?",
            "Can you validate compliance and generate audit reports?",
            "Are team members educated on compliance requirements?"
        ],
        implementation_guidance=[
            "Work with security and governance teams to determine compliance frameworks",
            "Use AWS Security Hub and AWS Config for compliance validation",
            "Leverage AWS Audit Manager for audit report generation",
            "Educate team members on compliance requirements for architectural decisions"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_compliance_reqs.html",
        related_best_practices=["SEC01-BP03", "SEC07-BP02", "SEC10-BP03"]
    ),
    "OPS01-BP05": BestPractice(
        id="OPS01-BP05",
        title="Evaluate Threat Landscape",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Evaluate threats to the business and maintain current information in a risk registry",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you regularly review Well-Architected and Trusted Advisor outputs?",
            "Are you aware of the latest patch status of your services?",
            "Do you understand the risk and impact of known threats?",
            "Do you maintain a threat model with planned mitigations?"
        ],
        implementation_guidance=[
            "Use AWS Trusted Advisor for optimization recommendations",
            "Monitor AWS Security Bulletins for latest threats",
            "Establish and maintain a threat model with priorities",
            "Review probability and cost of threats vs prevention costs"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_threat_landscape.html",
        related_best_practices=["SEC01-BP07"]
    ),
    "OPS01-BP06": BestPractice(
        id="OPS01-BP06",
        title="Evaluate Tradeoffs While Managing Benefits and Risks",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Balance competing interests and make data-driven decisions with a defined governance framework",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a clearly defined decision-making governance framework?",
            "Do you balance benefits against risks when making decisions?",
            "Are external factors (compliance, regulations) incorporated into decision-making?",
            "Do you distinguish between one-way and two-way door decisions?"
        ],
        implementation_guidance=[
            "Establish decision-making framework with defined roles and authority levels",
            "Balance centralized control with decentralized authority for appropriate decisions",
            "Incorporate compliance requirements into decision processes",
            "Use data-driven cost-benefit analysis for major decisions"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_priorities_eval_tradeoffs.html"
    ),
    "OPS02-BP01": BestPractice(
        id="OPS02-BP01",
        title="Resources Have Identified Owners",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Resources must have identified owners for change control, troubleshooting, and other functions",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do resources have identified owners using metadata or central register?",
            "Can team members identify who owns resources?",
            "Do accounts have single owners where possible?",
            "Are alternate contacts populated for AWS accounts?"
        ],
        implementation_guidance=[
            "Use AWS Organizations to manage accounts with alternate contacts",
            "Implement tagging strategy to identify resource owners",
            "Use AWS Config rules to enforce ownership tags",
            "Create documentation for non-AWS resources identifying ownership"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_resource_owners.html",
        related_best_practices=["OPS02-BP02", "OPS02-BP04"]
    ),
    "OPS02-BP02": BestPractice(
        id="OPS02-BP02",
        title="Processes and Procedures Have Identified Owners",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Understand who owns the definition of processes and procedures and why they exist",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are processes and procedures documented in a central discoverable location?",
            "Do processes and procedures have clearly assigned ownership?",
            "Are processes and procedures updated frequently by owners?",
            "Are processes implemented as code where possible?"
        ],
        implementation_guidance=[
            "Document operational activities in discoverable locations",
            "Use AWS Systems Manager for automation documents with ownership metadata",
            "Implement version control for processes and procedures",
            "Convert processes to code using Lambda functions or CloudFormation templates"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_proc_owners.html",
        related_best_practices=["OPS02-BP01", "OPS02-BP04", "OPS11-BP04"]
    ),
    "OPS02-BP03": BestPractice(
        id="OPS02-BP03",
        title="Operations Activities Have Identified Owners Responsible for Their Performance",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Understand who has responsibility to perform specific activities on defined workloads",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are responsibilities clearly defined for performing specific activities on workloads?",
            "Is ownership of processes and fulfillment documented and discoverable?",
            "Do you review and update responsibilities when organizational changes occur?",
            "Are there feedback mechanisms to track defects and improvements?"
        ],
        implementation_guidance=[
            "Document responsibilities using responsibility matrices and role definitions",
            "Use tagging to indicate process and procedure access for workloads",
            "Implement feedback mechanisms with issue tracking for iterative improvement",
            "Automate activities using Lambda functions and Systems Manager documents"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_activity_owners.html",
        related_best_practices=["OPS02-BP01", "OPS02-BP02", "OPS02-BP04", "OPS02-BP05", "OPS11-BP04"]
    ),
    "OPS02-BP04": BestPractice(
        id="OPS02-BP04",
        title="Mechanisms Exist to Manage Responsibilities and Ownership",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Understand responsibilities and how they contribute to business outcomes with clear escalation paths",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do teams have clearly-defined responsibilities aligned to resources and processes?",
            "Are escalation paths documented in a consistent and discoverable manner?",
            "Do you have mechanisms for teams to request clarification of responsibility?",
            "Are roles, responsibilities, and escalation paths readily available when needed?"
        ],
        implementation_guidance=[
            "Create and maintain RACI matrices and team definition documents",
            "Define clear escalation processes with single thread owners",
            "Implement accessible mechanisms for discovering ownership and responsibility",
            "Establish periodic review processes and feedback mechanisms"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_responsibilities_ownership.html",
        related_best_practices=["OPS02-BP01", "OPS02-BP02", "OPS02-BP03", "OPS02-BP05"]
    ),
    "OPS02-BP05": BestPractice(
        id="OPS02-BP05",
        title="Mechanisms Exist to Request Additions, Changes, and Exceptions",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Make requests to owners of processes, procedures, and resources through change management",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Can you make requests to change processes, procedures, and resources based on ownership?",
            "Are changes made in a deliberate manner, weighing benefits and risks?",
            "Is there a documented change management process?",
            "Can stakeholders easily submit change requests?"
        ],
        implementation_guidance=[
            "Document change management process for processes, procedures, and resources",
            "Use AWS Systems Manager Change Manager for workload resource changes",
            "Implement RACI matrix to identify change owners",
            "Create lightweight and accessible change request mechanisms"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_req_add_chg_exception.html",
        related_best_practices=["OPS02-BP01", "OPS02-BP02", "OPS02-BP03"]
    ),
    "OPS02-BP06": BestPractice(
        id="OPS02-BP06",
        title="Responsibilities Between Teams Are Predefined or Negotiated",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Have defined agreements between teams describing how they work with and support each other",
        risk_level=RiskLevel.LOW,
        questions=[
            "Are inter-team working or support agreements documented?",
            "Do teams have defined communication channels and response expectations?",
            "Are service level agreements established between teams?",
            "Are responsibilities clear when teams share processes or procedures?"
        ],
        implementation_guidance=[
            "Develop formal agreements between teams based on processes and procedures",
            "Create runbooks for shared processes between teams",
            "Establish response SLAs for inter-team dependencies",
            "Document team responsibilities and communication channels"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ops_model_def_neg_team_agreements.html"
    ),
    "OPS03-BP01": BestPractice(
        id="OPS03-BP01",
        title="Executive Sponsorship",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Senior leadership clearly sets expectations for the organization and evaluates success",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Does senior leadership clearly set expectations for operational excellence?",
            "Are there defined success criteria and metrics for operational performance?",
            "Does leadership regularly evaluate and communicate operational success?",
            "Is there visible executive support for operational excellence initiatives?"
        ],
        implementation_guidance=[
            "Establish clear operational excellence expectations from senior leadership",
            "Define measurable success criteria and KPIs for operational performance",
            "Implement regular leadership reviews of operational metrics",
            "Communicate executive commitment to operational excellence across organization"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_executive_sponsor.html"
    ),
    "OPS03-BP02": BestPractice(
        id="OPS03-BP02",
        title="Team Members Are Empowered to Take Action",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Team members have the authority to take action when outcomes are at risk",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do team members have authority to take action when outcomes are at risk?",
            "Are decision-making boundaries clearly defined for team members?",
            "Do teams have the tools and permissions needed to respond to issues?",
            "Is there a culture that supports taking appropriate action without excessive approval?"
        ],
        implementation_guidance=[
            "Define clear decision-making authority and boundaries for team members",
            "Provide teams with necessary tools and permissions for incident response",
            "Establish guidelines for when escalation is required vs autonomous action",
            "Foster culture that encourages appropriate action-taking"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_emp_take_action.html"
    ),
    "OPS03-BP03": BestPractice(
        id="OPS03-BP03",
        title="Escalation Is Encouraged",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Team members know when and how to escalate to the appropriate level",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do team members know when escalation is appropriate?",
            "Are escalation paths clearly defined and documented?",
            "Is there a culture that encourages escalation when needed?",
            "Do escalation procedures include timelines and contact information?"
        ],
        implementation_guidance=[
            "Document clear escalation criteria and procedures",
            "Define escalation paths with contact information and timelines",
            "Train team members on when and how to escalate",
            "Create culture where escalation is viewed positively"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_escalation.html"
    ),
    "OPS03-BP04": BestPractice(
        id="OPS03-BP04",
        title="Communications Are Timely, Clear, and Actionable",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Mechanisms exist to provide timely, clear, and actionable communications",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are communication mechanisms timely and reach the right audience?",
            "Are communications clear and actionable?",
            "Do you have established communication channels for different scenarios?",
            "Are communication templates and procedures documented?"
        ],
        implementation_guidance=[
            "Establish communication channels for different types of information",
            "Create templates for common communication scenarios",
            "Define audience and timing requirements for different communications",
            "Implement mechanisms to ensure communications are actionable"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_effective_comms.html"
    ),
    "OPS03-BP05": BestPractice(
        id="OPS03-BP05",
        title="Experimentation Is Encouraged",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Experimentation is encouraged to accelerate learning and keep team members interested",
        risk_level=RiskLevel.LOW,
        questions=[
            "Is experimentation encouraged within appropriate boundaries?",
            "Do teams have time and resources allocated for experimentation?",
            "Are there mechanisms to share learnings from experiments?",
            "Is failure in experimentation treated as learning opportunity?"
        ],
        implementation_guidance=[
            "Allocate time and resources for team experimentation",
            "Define safe boundaries and guidelines for experimentation",
            "Create mechanisms to capture and share experimental learnings",
            "Foster culture where experimental failures are learning opportunities"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_experiment.html"
    ),
    "OPS03-BP06": BestPractice(
        id="OPS03-BP06",
        title="Learning Is Encouraged",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Learning is encouraged and supported to help team members develop skills",
        risk_level=RiskLevel.LOW,
        questions=[
            "Is learning actively encouraged and supported?",
            "Do team members have access to learning resources and opportunities?",
            "Is time allocated for learning and skill development?",
            "Are learning achievements recognized and celebrated?"
        ],
        implementation_guidance=[
            "Provide access to learning resources and training opportunities",
            "Allocate dedicated time for learning and skill development",
            "Create learning paths aligned with career development",
            "Recognize and celebrate learning achievements"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.html"
    ),
    "OPS03-BP07": BestPractice(
        id="OPS03-BP07",
        title="Team Members Are Encouraged to Maintain and Grow Their Skill Sets",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Team members are provided time and resources to maintain and grow their skills",
        risk_level=RiskLevel.LOW,
        questions=[
            "Are team members encouraged to maintain and grow their skill sets?",
            "Do you provide time and resources for skill development?",
            "Are there career development paths and mentoring programs?",
            "Do you support certification and continuing education?"
        ],
        implementation_guidance=[
            "Establish career development paths with skill requirements",
            "Provide time and budget for training and certification",
            "Implement mentoring and knowledge sharing programs",
            "Support attendance at conferences and learning events"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_res_appro.html"
    ),
    "OPS04-BP01": BestPractice(
        id="OPS04-BP01",
        title="Identify Key Performance Indicators",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Identify key performance indicators based on desired business and customer outcomes",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified KPIs based on desired business and customer outcomes?",
            "Do your metrics provide insight into workload health and performance?",
            "Are KPIs aligned with business objectives and customer experience?",
            "Do you have both technical and business metrics defined?"
        ],
        implementation_guidance=[
            "Define KPIs that align with business objectives and customer outcomes",
            "Implement both technical metrics (latency, errors) and business metrics (conversion, satisfaction)",
            "Use AWS CloudWatch and custom metrics to track KPIs",
            "Establish baselines and targets for each key performance indicator"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_identify_kpis.html"
    ),
    "OPS04-BP02": BestPractice(
        id="OPS04-BP02",
        title="Implement Application Telemetry",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Emit telemetry that provides insight into the state of your application",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you emitting telemetry that provides insight into application state?",
            "Do you have structured logging implemented?",
            "Are you collecting metrics for key application functions?",
            "Do you have distributed tracing for complex workflows?"
        ],
        implementation_guidance=[
            "Use AWS X-Ray for distributed tracing",
            "Implement structured logging with CloudWatch Logs",
            "Emit custom metrics using CloudWatch custom metrics",
            "Use AWS OpenTelemetry for comprehensive observability"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_application_telemetry.html"
    ),
    "OPS04-BP03": BestPractice(
        id="OPS04-BP03",
        title="Implement User Activity Telemetry",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Emit telemetry that provides insight into customer behavior and experience",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you collecting telemetry on customer behavior and experience?",
            "Do you track user journeys and conversion funnels?",
            "Are you monitoring customer satisfaction metrics?",
            "Do you have real user monitoring implemented?"
        ],
        implementation_guidance=[
            "Use AWS CloudWatch RUM for real user monitoring",
            "Implement customer journey tracking with custom metrics",
            "Use AWS Pinpoint for user engagement analytics",
            "Track conversion funnels and user experience metrics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_customer_telemetry.html"
    ),
    "OPS04-BP04": BestPractice(
        id="OPS04-BP04",
        title="Implement Dependency Telemetry",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Emit telemetry that provides insight into the state of services you depend on",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you monitoring the health and performance of your dependencies?",
            "Do you track response times and error rates for external services?",
            "Are you monitoring database and cache performance?",
            "Do you have alerts for dependency failures?"
        ],
        implementation_guidance=[
            "Monitor external API response times and error rates",
            "Use CloudWatch to track database and cache metrics",
            "Implement health checks for critical dependencies",
            "Set up alerts for dependency performance degradation"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_dependency_telemetry.html"
    ),
    "OPS04-BP05": BestPractice(
        id="OPS04-BP05",
        title="Implement Distributed Tracing",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Implement distributed tracing to understand request flows across services",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have distributed tracing implemented across your services?",
            "Can you trace requests end-to-end through your system?",
            "Are you using correlation IDs to track requests?",
            "Do you have visibility into service-to-service communication?"
        ],
        implementation_guidance=[
            "Use AWS X-Ray for distributed tracing",
            "Implement correlation IDs across all services",
            "Use AWS OpenTelemetry for standardized tracing",
            "Trace critical user journeys and business processes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_dist_trace.html"
    ),
    "OPS05-BP01": BestPractice(
        id="OPS05-BP01",
        title="Use Version Control",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use version control to enable tracking of changes and releases",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using version control for all code and configuration?",
            "Do you have branching strategies that support your development process?",
            "Are you tagging releases for traceability?",
            "Do you have proper commit message standards?"
        ],
        implementation_guidance=[
            "Use Git for version control with proper branching strategies",
            "Implement semantic versioning for releases",
            "Use AWS CodeCommit or GitHub for repository hosting",
            "Establish commit message and code review standards"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.html"
    ),
    "OPS05-BP02": BestPractice(
        id="OPS05-BP02",
        title="Test and Validate Changes",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Test and validate changes to help limit issues in production",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have comprehensive testing strategies (unit, integration, end-to-end)?",
            "Are you testing in environments that mirror production?",
            "Do you have automated testing in your CI/CD pipeline?",
            "Are you performing load and performance testing?"
        ],
        implementation_guidance=[
            "Implement unit, integration, and end-to-end testing",
            "Use AWS CodeBuild for automated testing in CI/CD",
            "Create test environments that mirror production",
            "Perform load testing with tools like AWS Load Testing solution"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_test_val_chg.html"
    ),
    "OPS05-BP03": BestPractice(
        id="OPS05-BP03",
        title="Use Configuration Management Systems",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use configuration management systems to make and track configuration changes",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using configuration management systems?",
            "Do you track configuration changes and their impact?",
            "Are configurations stored as code and version controlled?",
            "Do you have rollback capabilities for configuration changes?"
        ],
        implementation_guidance=[
            "Use AWS Systems Manager Parameter Store for configuration management",
            "Store configurations as code in version control",
            "Use AWS Config to track configuration changes",
            "Implement configuration validation and rollback procedures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_conf_mgmt_sys.html"
    ),
    "OPS05-BP04": BestPractice(
        id="OPS05-BP04",
        title="Use Build and Deployment Management Systems",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use build and deployment management systems to track and implement changes",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using automated build and deployment systems?",
            "Do you track builds and deployments?",
            "Are builds reproducible and consistent?",
            "Do you have deployment pipelines with proper gates?"
        ],
        implementation_guidance=[
            "Use AWS CodeBuild and CodeDeploy for automated builds and deployments",
            "Implement CI/CD pipelines with AWS CodePipeline",
            "Use container images or immutable artifacts for consistent deployments",
            "Implement deployment gates and approval processes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_build_mgmt_sys.html"
    ),
    "OPS05-BP05": BestPractice(
        id="OPS05-BP05",
        title="Perform Patch Management",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Perform patch management to gain features, address issues, and remain supported",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a patch management strategy for operating systems and applications?",
            "Are you regularly updating dependencies and libraries?",
            "Do you test patches before applying to production?",
            "Are you tracking security vulnerabilities and patches?"
        ],
        implementation_guidance=[
            "Use AWS Systems Manager Patch Manager for automated patching",
            "Implement dependency scanning and updates in CI/CD pipelines",
            "Test patches in non-production environments first",
            "Use AWS Inspector for vulnerability assessment"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_patch_mgmt.html"
    ),
    "OPS05-BP06": BestPractice(
        id="OPS05-BP06",
        title="Share Design Standards",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Share design standards to improve development efficiency and reduce errors",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have documented design standards and coding guidelines?",
            "Are design standards shared across development teams?",
            "Do you use templates and reusable components?",
            "Are design standards enforced through code reviews and tooling?"
        ],
        implementation_guidance=[
            "Document coding standards and architectural patterns",
            "Use AWS Service Catalog for standardized infrastructure templates",
            "Implement code linting and formatting tools",
            "Create reusable libraries and components"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_share_design_stds.html"
    ),
    "OPS05-BP07": BestPractice(
        id="OPS05-BP07",
        title="Implement Practices to Improve Code Quality",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Implement practices to improve code quality and minimize defects",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have code review processes in place?",
            "Are you using static code analysis tools?",
            "Do you have coding standards and style guides?",
            "Are you measuring and tracking code quality metrics?"
        ],
        implementation_guidance=[
            "Implement mandatory code reviews for all changes",
            "Use static analysis tools like Amazon CodeGuru Reviewer",
            "Enforce coding standards with automated linting",
            "Track code quality metrics and technical debt"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_code_quality.html"
    ),
    "OPS05-BP08": BestPractice(
        id="OPS05-BP08",
        title="Use Multiple Environments",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use multiple environments to experiment, develop, and test changes",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have separate environments for development, testing, and production?",
            "Are environments consistent and reproducible?",
            "Do you promote changes through environments systematically?",
            "Are environment configurations managed as code?"
        ],
        implementation_guidance=[
            "Create separate AWS accounts for different environments",
            "Use infrastructure as code for consistent environment provisioning",
            "Implement promotion pipelines between environments",
            "Use AWS Organizations for multi-account management"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_multi_env.html"
    ),
    "OPS05-BP09": BestPractice(
        id="OPS05-BP09",
        title="Make Frequent, Small, Reversible Changes",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Make frequent, small, reversible changes to reduce the scope of failure",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you making small, incremental changes rather than large releases?",
            "Can changes be easily reversed if issues occur?",
            "Do you have feature flags for controlling functionality?",
            "Are you practicing continuous integration and deployment?"
        ],
        implementation_guidance=[
            "Implement feature flags using AWS AppConfig",
            "Use blue-green or canary deployment strategies",
            "Practice continuous integration with frequent commits",
            "Design changes to be easily reversible"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_freq_sm_rev_chg.html"
    ),
    "OPS05-BP10": BestPractice(
        id="OPS05-BP10",
        title="Fully Automate Integration and Deployment",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Automate integration and deployment to reduce errors and enable rapid delivery",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are integration and deployment processes fully automated?",
            "Do you have automated testing in your deployment pipeline?",
            "Are deployments consistent and repeatable?",
            "Do you have rollback automation for failed deployments?"
        ],
        implementation_guidance=[
            "Use AWS CodePipeline for fully automated CI/CD",
            "Implement automated testing at multiple stages",
            "Use AWS CodeDeploy for consistent deployment strategies",
            "Automate rollback procedures for deployment failures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_auto_integ_deploy.html"
    ),
    "OPS06-BP01": BestPractice(
        id="OPS06-BP01",
        title="Plan for Unsuccessful Changes",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Plan to revert changes that do not have the desired outcome",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have rollback plans for all changes?",
            "Can you quickly revert changes if issues occur?",
            "Are rollback procedures tested and validated?",
            "Do you have monitoring to detect unsuccessful changes?"
        ],
        implementation_guidance=[
            "Implement automated rollback capabilities",
            "Use blue-green deployments for zero-downtime rollbacks",
            "Test rollback procedures regularly",
            "Monitor key metrics to detect deployment issues"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_plan_for_unsucessful_changes.html"
    ),
    "OPS06-BP02": BestPractice(
        id="OPS06-BP02",
        title="Test and Validate Changes",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Test changes and validate that they will operate as intended",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you test changes in production-like environments?",
            "Are you performing load and performance testing?",
            "Do you validate changes against acceptance criteria?",
            "Are you testing failure scenarios and edge cases?"
        ],
        implementation_guidance=[
            "Create production-like test environments",
            "Implement comprehensive testing strategies",
            "Use AWS Load Testing solution for performance validation",
            "Test failure scenarios and recovery procedures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_test_val_chg.html"
    ),
    "OPS06-BP03": BestPractice(
        id="OPS06-BP03",
        title="Use Deployment Management Systems",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use deployment management systems to track and control changes",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using deployment management systems?",
            "Do you track all deployments and their status?",
            "Can you control and coordinate deployments across environments?",
            "Do you have deployment approval and gate processes?"
        ],
        implementation_guidance=[
            "Use AWS CodeDeploy for managed deployments",
            "Implement deployment tracking and monitoring",
            "Use AWS Systems Manager Change Manager for change control",
            "Implement approval gates in deployment pipelines"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_deploy_mgmt_sys.html"
    ),
    "OPS06-BP04": BestPractice(
        id="OPS06-BP04",
        title="Automate Testing and Rollback",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Automate testing and rollback to reduce deployment risks",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are testing and rollback procedures automated?",
            "Do you have automated health checks after deployments?",
            "Can rollbacks be triggered automatically based on metrics?",
            "Are rollback procedures tested regularly?"
        ],
        implementation_guidance=[
            "Implement automated post-deployment testing",
            "Use CloudWatch alarms to trigger automatic rollbacks",
            "Automate health checks and validation procedures",
            "Test rollback automation regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_mit_deploy_risks_auto_testing_and_rollback.html"
    ),
    "OPS07-BP01": BestPractice(
        id="OPS07-BP01",
        title="Ensure Personnel Capability",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Have personnel with appropriate skills to support your workload",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have personnel with the skills needed to support your workload?",
            "Are there training programs to develop necessary capabilities?",
            "Do you have knowledge transfer and documentation processes?",
            "Are there backup personnel for critical roles?"
        ],
        implementation_guidance=[
            "Assess skill gaps and create training plans",
            "Implement knowledge sharing and documentation practices",
            "Cross-train team members on critical systems",
            "Use AWS Training and Certification programs"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_personnel_capability.html"
    ),
    "OPS07-BP02": BestPractice(
        id="OPS07-BP02",
        title="Ensure Consistent Review of Operational Readiness",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Consistently review operational readiness to identify and address gaps",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have regular operational readiness reviews?",
            "Are readiness criteria clearly defined and documented?",
            "Do you assess readiness before major releases or changes?",
            "Are operational readiness gaps tracked and addressed?"
        ],
        implementation_guidance=[
            "Establish operational readiness review processes",
            "Define clear readiness criteria and checklists",
            "Conduct pre-launch readiness assessments",
            "Track and remediate identified gaps"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_const_orr.html"
    ),
    "OPS07-BP03": BestPractice(
        id="OPS07-BP03",
        title="Use Runbooks for Procedures",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use runbooks to perform procedures consistently and efficiently",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have runbooks for operational procedures?",
            "Are runbooks kept up-to-date and accessible?",
            "Do runbooks include step-by-step instructions?",
            "Are runbooks tested and validated regularly?"
        ],
        implementation_guidance=[
            "Create comprehensive runbooks for all operational procedures",
            "Use AWS Systems Manager Documents for executable runbooks",
            "Keep runbooks version controlled and up-to-date",
            "Test runbooks regularly to ensure accuracy"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html"
    ),
    "OPS07-BP04": BestPractice(
        id="OPS07-BP04",
        title="Use Playbooks for Issue Investigation",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Use playbooks to investigate issues consistently and efficiently",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have playbooks for common issue investigation scenarios?",
            "Are playbooks accessible during incidents?",
            "Do playbooks include troubleshooting steps and escalation procedures?",
            "Are playbooks updated based on lessons learned?"
        ],
        implementation_guidance=[
            "Create playbooks for common incident scenarios",
            "Include diagnostic steps and escalation procedures",
            "Make playbooks easily accessible during incidents",
            "Update playbooks based on post-incident reviews"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_playbooks.html"
    ),
    "OPS07-BP05": BestPractice(
        id="OPS07-BP05",
        title="Make Informed Decisions to Deploy Systems and Changes",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Make informed decisions about when to deploy systems and changes",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have criteria for making deployment decisions?",
            "Are deployment decisions based on data and risk assessment?",
            "Do you consider business impact when scheduling deployments?",
            "Are there approval processes for high-risk deployments?"
        ],
        implementation_guidance=[
            "Define deployment decision criteria and processes",
            "Use data and metrics to inform deployment decisions",
            "Consider business impact and timing for deployments",
            "Implement approval processes for high-risk changes"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_informed_deploy_decisions.html"
    ),
    "OPS07-BP06": BestPractice(
        id="OPS07-BP06",
        title="Enable Support Plans",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Enable support plans appropriate for your business needs",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you have appropriate AWS support plans for your business needs?",
            "Are support contacts and escalation procedures documented?",
            "Do you leverage AWS support resources effectively?",
            "Are support requirements aligned with business criticality?"
        ],
        implementation_guidance=[
            "Select AWS support plans based on business requirements",
            "Document support contacts and escalation procedures",
            "Use AWS Trusted Advisor and support resources",
            "Align support levels with workload criticality"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_enable_support_plans.html"
    ),
    "OPS11-BP01": BestPractice(
        id="OPS11-BP01",
        title="Have a Process for Continuous Improvement",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Implement processes to drive continuous improvement of operations",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have a defined process for continuous improvement?",
            "Are improvement opportunities regularly identified and prioritized?",
            "Do you track the effectiveness of improvement initiatives?",
            "Are improvement processes integrated into regular operations?"
        ],
        implementation_guidance=[
            "Establish regular improvement review cycles",
            "Create processes to identify and prioritize improvement opportunities",
            "Track improvement initiatives and measure their impact",
            "Integrate improvement activities into operational workflows"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_process_cont_imp.html",
        related_best_practices=["OPS11-BP02", "OPS11-BP03", "OPS11-BP07"]
    ),
    "OPS11-BP02": BestPractice(
        id="OPS11-BP02",
        title="Perform Root Cause Analysis on Failures",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Perform root cause analysis on failures to identify improvement opportunities",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform root cause analysis on failures and incidents?",
            "Are RCA processes documented and consistently followed?",
            "Do you identify and implement corrective actions from RCA?",
            "Are RCA findings shared across teams for learning?"
        ],
        implementation_guidance=[
            "Establish formal root cause analysis processes",
            "Use structured RCA methodologies like 5 Whys or Fishbone diagrams",
            "Document findings and implement corrective actions",
            "Share RCA learnings across teams and organization"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_perform_rca_process.html",
        related_best_practices=["OPS11-BP01", "OPS11-BP03", "OPS11-BP08"]
    ),
    "OPS11-BP03": BestPractice(
        id="OPS11-BP03",
        title="Implement Feedback Loops",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Implement feedback loops to capture learnings and drive improvements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have feedback loops to capture operational learnings?",
            "Are feedback mechanisms accessible to all team members?",
            "Do you act on feedback to drive improvements?",
            "Are feedback loops integrated into operational processes?"
        ],
        implementation_guidance=[
            "Create multiple channels for collecting operational feedback",
            "Implement regular retrospectives and lessons learned sessions",
            "Act on feedback to implement operational improvements",
            "Integrate feedback collection into standard operational procedures"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_feedback_loops.html",
        related_best_practices=["OPS01-BP01", "OPS01-BP02", "OPS11-BP01", "OPS11-BP02"]
    ),
    "OPS11-BP04": BestPractice(
        id="OPS11-BP04",
        title="Perform Knowledge Management",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Perform knowledge management to preserve and share operational knowledge",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have knowledge management processes and systems?",
            "Is operational knowledge documented and accessible?",
            "Are knowledge sharing practices established?",
            "Do you preserve knowledge when team members leave?"
        ],
        implementation_guidance=[
            "Implement knowledge management systems and processes",
            "Document operational procedures and lessons learned",
            "Establish knowledge sharing practices and sessions",
            "Create knowledge transfer processes for role transitions"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.html",
        related_best_practices=["OPS02-BP02", "OPS02-BP03", "OPS11-BP08"]
    ),
    "OPS11-BP05": BestPractice(
        id="OPS11-BP05",
        title="Define Drivers for Improvement",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Define drivers for operational improvement based on business outcomes",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are improvement drivers clearly defined and aligned with business outcomes?",
            "Do you prioritize improvements based on business impact?",
            "Are improvement drivers communicated to all stakeholders?",
            "Do you regularly review and update improvement drivers?"
        ],
        implementation_guidance=[
            "Define improvement drivers based on business objectives",
            "Prioritize improvements based on business impact and value",
            "Communicate improvement drivers to all relevant stakeholders",
            "Regularly review and update drivers based on changing business needs"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_drivers_for_imp.html"
    ),
    "OPS11-BP06": BestPractice(
        id="OPS11-BP06",
        title="Validate Insights",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Validate insights from operations to ensure they drive effective improvements",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you validate operational insights before implementing changes?",
            "Are insights tested in controlled environments?",
            "Do you measure the impact of changes based on insights?",
            "Are validation processes documented and repeatable?"
        ],
        implementation_guidance=[
            "Establish processes to validate operational insights",
            "Test insights in controlled environments before full implementation",
            "Measure and track the impact of changes based on insights",
            "Document validation processes for consistency and repeatability"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_validate_insights.html"
    ),
    "OPS11-BP07": BestPractice(
        id="OPS11-BP07",
        title="Perform Operations Metrics Reviews",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Perform regular reviews of operations metrics to identify trends and improvements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you perform regular operations metrics reviews?",
            "Are metrics reviews structured and comprehensive?",
            "Do you identify trends and patterns from metrics reviews?",
            "Are action items from reviews tracked and implemented?"
        ],
        implementation_guidance=[
            "Establish regular operations metrics review meetings",
            "Create structured agendas and processes for metrics reviews",
            "Analyze trends and patterns to identify improvement opportunities",
            "Track and implement action items from metrics reviews"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_metrics_review.html"
    ),
    "OPS11-BP08": BestPractice(
        id="OPS11-BP08",
        title="Share Lessons Learned",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Share lessons learned across teams and organization to drive broader improvements",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you share lessons learned across teams and organization?",
            "Are there established channels for sharing operational knowledge?",
            "Do you document and preserve lessons learned?",
            "Are shared lessons acted upon by other teams?"
        ],
        implementation_guidance=[
            "Create channels and forums for sharing lessons learned",
            "Document lessons learned in accessible knowledge bases",
            "Establish regular knowledge sharing sessions",
            "Encourage teams to act on shared lessons and provide feedback"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_share_lessons_learned.html"
    ),
    "OPS11-BP09": BestPractice(
        id="OPS11-BP09",
        title="Allocate Time to Make Improvements",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Allocate time and resources to implement operational improvements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you allocate dedicated time for operational improvements?",
            "Are improvement activities prioritized alongside feature development?",
            "Do teams have capacity and resources for improvement work?",
            "Are improvement efforts tracked and measured?"
        ],
        implementation_guidance=[
            "Allocate dedicated time in team schedules for improvement work",
            "Balance improvement activities with feature development priorities",
            "Provide teams with necessary resources and capacity for improvements",
            "Track and measure the impact of improvement efforts"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_allocate_time_for_imp.html"
    ),
    "OPS08-BP01": BestPractice(
        id="OPS08-BP01",
        title="Analyze Workload Metrics",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Regularly review and analyze workload metrics to understand performance",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you regularly analyzing workload metrics?",
            "Do you have baseline metrics for normal operation?",
            "Are you tracking key performance indicators?",
            "Do you correlate metrics across different components?"
        ],
        implementation_guidance=[
            "Use CloudWatch to collect and analyze metrics",
            "Establish baselines for normal operational metrics",
            "Create custom metrics for business-specific KPIs",
            "Use CloudWatch Insights for metric correlation and analysis"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_metrics.html"
    ),
    "OPS08-BP02": BestPractice(
        id="OPS08-BP02",
        title="Analyze Workload Logs",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Regularly review and analyze workload logs to understand behavior",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you collecting and analyzing application and system logs?",
            "Do you have structured logging implemented?",
            "Are logs searchable and queryable?",
            "Do you correlate logs with metrics and traces?"
        ],
        implementation_guidance=[
            "Use CloudWatch Logs for centralized log collection",
            "Implement structured logging with JSON format",
            "Use CloudWatch Logs Insights for log analysis",
            "Correlate logs with metrics and distributed traces"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.html"
    ),
    "OPS08-BP03": BestPractice(
        id="OPS08-BP03",
        title="Analyze Workload Traces",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Regularly review and analyze workload traces to understand request flows",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you collecting and analyzing distributed traces?",
            "Can you trace requests end-to-end through your system?",
            "Do you analyze trace data for performance bottlenecks?",
            "Are traces correlated with metrics and logs?"
        ],
        implementation_guidance=[
            "Use AWS X-Ray for distributed tracing",
            "Analyze trace data to identify performance bottlenecks",
            "Use X-Ray service map to understand service dependencies",
            "Correlate traces with CloudWatch metrics and logs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_traces.html"
    ),
    "OPS08-BP04": BestPractice(
        id="OPS08-BP04",
        title="Create Actionable Alerts",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Create alerts that are actionable and provide clear next steps",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are your alerts actionable with clear next steps?",
            "Do alerts include sufficient context for troubleshooting?",
            "Are alert thresholds tuned to minimize false positives?",
            "Do you have different alert severities and escalation paths?"
        ],
        implementation_guidance=[
            "Use CloudWatch Alarms with appropriate thresholds",
            "Include context and runbook links in alert notifications",
            "Implement alert severity levels and escalation procedures",
            "Regularly review and tune alert thresholds"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_alerts.html"
    ),
    "OPS08-BP05": BestPractice(
        id="OPS08-BP05",
        title="Create Dashboards",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Create dashboards to provide visibility into workload health and performance",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have dashboards showing workload health and performance?",
            "Are dashboards accessible to relevant stakeholders?",
            "Do dashboards show both technical and business metrics?",
            "Are dashboards updated and maintained regularly?"
        ],
        implementation_guidance=[
            "Use CloudWatch Dashboards for operational visibility",
            "Create role-based dashboards for different audiences",
            "Include both technical metrics and business KPIs",
            "Use Amazon QuickSight for advanced business analytics"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_dashboards.html"
    ),
    "OPS09-BP01": BestPractice(
        id="OPS09-BP01",
        title="Measure Operations Goals and KPIs",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Measure operations goals and KPIs to understand operational health",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you measure operations goals and KPIs?",
            "Are operational metrics aligned with business objectives?",
            "Do you track both leading and lagging indicators?",
            "Are metrics reviewed regularly with stakeholders?"
        ],
        implementation_guidance=[
            "Define operational KPIs aligned with business goals",
            "Use CloudWatch custom metrics for operational measurements",
            "Track both technical and business operational metrics",
            "Establish regular review cycles for operational metrics"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_operations_health_measure_ops_goals_kpis.html"
    ),
    "OPS09-BP02": BestPractice(
        id="OPS09-BP02",
        title="Communicate Status and Trends",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Communicate operational status and trends to stakeholders",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you communicate operational status to stakeholders?",
            "Are status communications timely and relevant?",
            "Do you share operational trends and insights?",
            "Are communication channels appropriate for different audiences?"
        ],
        implementation_guidance=[
            "Create operational status reports and dashboards",
            "Use appropriate communication channels for different stakeholders",
            "Share trends and insights from operational data",
            "Establish regular communication cadences"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_operations_health_communicate_status_trends.html"
    ),
    "OPS09-BP03": BestPractice(
        id="OPS09-BP03",
        title="Review Operations Metrics and Prioritize Improvement",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Review operations metrics regularly and prioritize improvement opportunities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you regularly review operations metrics?",
            "Are improvement opportunities identified and prioritized?",
            "Do you track the effectiveness of operational improvements?",
            "Are reviews conducted with appropriate stakeholders?"
        ],
        implementation_guidance=[
            "Establish regular operational review meetings",
            "Use data to identify and prioritize improvement opportunities",
            "Track improvement initiatives and their impact",
            "Involve relevant stakeholders in operational reviews"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_operations_health_review_ops_metrics_prioritize_improvement.html"
    ),
    "OPS10-BP01": BestPractice(
        id="OPS10-BP01",
        title="Use a Process for Event, Incident, and Problem Management",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Have processes to address observed events, incidents, and problems",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have defined processes for event, incident, and problem management?",
            "Are roles and responsibilities clear for incident response?",
            "Do you have escalation procedures for different severity levels?",
            "Are processes documented and accessible during incidents?"
        ],
        implementation_guidance=[
            "Define incident management processes with clear roles",
            "Establish severity levels and escalation procedures",
            "Use incident management tools for tracking and coordination",
            "Document processes and make them accessible during incidents"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_event_incident_problem_process.html"
    ),
    "OPS10-BP02": BestPractice(
        id="OPS10-BP02",
        title="Have a Process Per Alert",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Have a well-defined response process for every alert",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Does every alert have a defined response process?",
            "Are response procedures documented and accessible?",
            "Do alerts include links to relevant runbooks or procedures?",
            "Are response processes tested and validated?"
        ],
        implementation_guidance=[
            "Create response procedures for each type of alert",
            "Include runbook links in alert notifications",
            "Document troubleshooting steps and escalation procedures",
            "Test and validate response procedures regularly"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_process_per_alert.html"
    ),
    "OPS10-BP03": BestPractice(
        id="OPS10-BP03",
        title="Prioritize Operational Events Based on Business Impact",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Prioritize operational events based on their business impact",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you prioritize events based on business impact?",
            "Are business impact criteria clearly defined?",
            "Do you have different response procedures for different priorities?",
            "Are priority decisions communicated to stakeholders?"
        ],
        implementation_guidance=[
            "Define business impact criteria for event prioritization",
            "Establish different response procedures based on priority",
            "Train teams on prioritization criteria and procedures",
            "Communicate priority decisions to relevant stakeholders"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_prioritize_events.html"
    ),
    "OPS10-BP04": BestPractice(
        id="OPS10-BP04",
        title="Define Escalation Paths",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Define escalation paths for operational events and incidents",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are escalation paths clearly defined and documented?",
            "Do escalation procedures include contact information and timelines?",
            "Are escalation paths tested and validated?",
            "Do team members know when and how to escalate?"
        ],
        implementation_guidance=[
            "Document clear escalation paths with contact information",
            "Define escalation criteria and timelines",
            "Test escalation procedures regularly",
            "Train team members on escalation processes"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_define_escalation_paths.html"
    ),
    "OPS10-BP05": BestPractice(
        id="OPS10-BP05",
        title="Define a Customer Communication Plan for Outages",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Have a plan to communicate with customers during outages",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a customer communication plan for outages?",
            "Are communication channels and procedures defined?",
            "Do you have templates for different types of communications?",
            "Are communication responsibilities clearly assigned?"
        ],
        implementation_guidance=[
            "Create customer communication plans for different outage scenarios",
            "Define communication channels and update procedures",
            "Prepare communication templates for common scenarios",
            "Assign clear responsibilities for customer communications"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_push_notify.html"
    ),
    "OPS10-BP06": BestPractice(
        id="OPS10-BP06",
        title="Communicate Status Through Dashboards",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Provide status visibility through dashboards during operational events",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you have dashboards to communicate operational status?",
            "Are dashboards accessible to relevant stakeholders during incidents?",
            "Do dashboards show real-time status and impact information?",
            "Are dashboards updated automatically during events?"
        ],
        implementation_guidance=[
            "Create operational status dashboards for incident communication",
            "Ensure dashboards are accessible during incidents",
            "Include real-time status and impact information",
            "Automate dashboard updates where possible"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_dashboards.html"
    ),
    "OPS10-BP07": BestPractice(
        id="OPS10-BP07",
        title="Automate Responses to Events",
        pillar=Pillar.OPERATIONAL_EXCELLENCE,
        description="Automate responses to well-understood operational events",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you automate responses to well-understood events?",
            "Are automated responses tested and validated?",
            "Do you have safeguards to prevent automated response failures?",
            "Are automated responses monitored and logged?"
        ],
        implementation_guidance=[
            "Use AWS Systems Manager Automation for event response",
            "Implement automated scaling and recovery procedures",
            "Test automated responses regularly",
            "Monitor and log all automated response actions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_event_response_auto_event_response.html"
    ),
    
    # Security
    "SEC01-BP01": BestPractice(
        id="SEC01-BP01",
        title="Separate Workloads Using Accounts",
        pillar=Pillar.SECURITY,
        description="Organize workloads in separate accounts and centralize identity management",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using separate AWS accounts for different workloads or environments?",
            "Do you have a multi-account strategy with AWS Organizations?",
            "Are accounts organized by business function, compliance, or risk profile?",
            "Do you centralize identity management across accounts?"
        ],
        implementation_guidance=[
            "Use AWS Organizations to manage multiple accounts",
            "Separate production, development, and testing environments into different accounts",
            "Organize accounts by business unit, application, or compliance requirements",
            "Use AWS SSO for centralized identity management across accounts"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_multi_accounts.html",
        related_best_practices=["SEC01-BP02"]
    ),
    "SEC01-BP02": BestPractice(
        id="SEC01-BP02",
        title="Secure Account Root User and Properties",
        pillar=Pillar.SECURITY,
        description="Secure the root user and configure account-level security properties",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Is the root user secured with MFA and strong password?",
            "Are root user access keys deleted or secured?",
            "Are account contact details configured?",
            "Are account-level security settings properly configured?"
        ],
        implementation_guidance=[
            "Enable MFA for root user and use strong, unique password",
            "Delete root user access keys or store them securely",
            "Configure alternate contacts for billing, operations, and security",
            "Enable AWS Config and CloudTrail at account level"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_aws_account.html",
        related_best_practices=["SEC01-BP01"]
    ),
    "SEC01-BP03": BestPractice(
        id="SEC01-BP03",
        title="Identify and Validate Control Objectives",
        pillar=Pillar.SECURITY,
        description="Identify and validate security control objectives based on compliance requirements",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified security control objectives for your workload?",
            "Are control objectives aligned with compliance requirements?",
            "Do you validate that controls meet their objectives?",
            "Are control objectives documented and communicated?"
        ],
        implementation_guidance=[
            "Define security control objectives based on business and compliance requirements",
            "Map controls to frameworks like SOC 2, PCI DSS, or NIST",
            "Implement validation processes to ensure controls meet objectives",
            "Document control objectives and communicate to stakeholders"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_control_objectives.html",
        related_best_practices=["OPS01-BP04", "SEC01-BP06", "SEC07-BP02", "SEC10-BP03"]
    ),
    "SEC01-BP04": BestPractice(
        id="SEC01-BP04",
        title="Stay Up to Date with Security Threats and Recommendations",
        pillar=Pillar.SECURITY,
        description="Stay informed about current security threats and AWS security recommendations",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you stay current with security threats and vulnerabilities?",
            "Are you subscribed to AWS security bulletins and advisories?",
            "Do you have processes to evaluate and respond to new threats?",
            "Are security recommendations implemented in a timely manner?"
        ],
        implementation_guidance=[
            "Subscribe to AWS Security Bulletins and security advisories",
            "Monitor threat intelligence sources and security research",
            "Establish processes to evaluate and respond to new security threats",
            "Regularly review and implement AWS security recommendations"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_updated_threats.html",
        related_best_practices=["SEC01-BP07", "SEC01-BP08"]
    ),
    "SEC01-BP05": BestPractice(
        id="SEC01-BP05",
        title="Reduce Security Management Scope",
        pillar=Pillar.SECURITY,
        description="Reduce security management scope by using managed services",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using AWS managed services to reduce security management overhead?",
            "Do you leverage managed services for security functions like patching?",
            "Are you using serverless architectures where appropriate?",
            "Do you minimize the attack surface through service selection?"
        ],
        implementation_guidance=[
            "Use managed services like RDS, ECS Fargate, and Lambda to reduce management overhead",
            "Leverage AWS managed security services like GuardDuty and Security Hub",
            "Choose serverless architectures to minimize infrastructure management",
            "Use managed services for patching, backup, and monitoring"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_reduce_management_scope.html",
        related_best_practices=["SEC01-BP06"]
    ),
    "SEC01-BP06": BestPractice(
        id="SEC01-BP06",
        title="Automate Testing and Validation of Security Controls",
        pillar=Pillar.SECURITY,
        description="Automate testing and validation of security controls in pipelines",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are security controls tested automatically in your deployment pipeline?",
            "Do you have automated security testing integrated into CI/CD?",
            "Are security validations performed before production deployment?",
            "Do you use infrastructure as code for consistent security configurations?"
        ],
        implementation_guidance=[
            "Integrate security testing tools into CI/CD pipelines",
            "Use AWS Config Rules to validate security configurations",
            "Implement automated security scanning with tools like Amazon Inspector",
            "Use infrastructure as code to ensure consistent security configurations"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_automate_security_controls.html",
        related_best_practices=["SEC01-BP03", "SEC01-BP05", "SEC07-BP02", "SEC10-BP03"]
    ),
    "SEC01-BP07": BestPractice(
        id="SEC01-BP07",
        title="Identify Threats and Prioritize Mitigations Using a Threat Model",
        pillar=Pillar.SECURITY,
        description="Perform threat modeling to identify and prioritize potential security threats",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform threat modeling for your workloads?",
            "Are threats identified and prioritized based on risk?",
            "Do you have mitigation strategies for identified threats?",
            "Is threat modeling updated as your architecture evolves?"
        ],
        implementation_guidance=[
            "Perform structured threat modeling using frameworks like STRIDE",
            "Identify and prioritize threats based on likelihood and impact",
            "Develop mitigation strategies for high-priority threats",
            "Update threat models as architecture and threat landscape evolve"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_threat_model.html",
        related_best_practices=["OPS01-BP05", "SEC01-BP04"]
    ),
    "SEC01-BP08": BestPractice(
        id="SEC01-BP08",
        title="Evaluate and Implement New Security Services and Features",
        pillar=Pillar.SECURITY,
        description="Regularly evaluate and implement new AWS security services and features",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you regularly evaluate new AWS security services and features?",
            "Are new security capabilities assessed for your workloads?",
            "Do you have a process for implementing beneficial security features?",
            "Are security service updates and new features tracked?"
        ],
        implementation_guidance=[
            "Regularly review AWS security service announcements and updates",
            "Evaluate new security features for applicability to your workloads",
            "Establish processes for testing and implementing new security capabilities",
            "Stay informed about security service roadmaps and upcoming features"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_implement_services_features.html",
        related_best_practices=["SEC01-BP04"]
    ),
    "SEC06-BP01": BestPractice(
        id="SEC06-BP01",
        title="Perform Application Security Testing",
        pillar=Pillar.SECURITY,
        description="Perform application security testing as part of the software development lifecycle",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you perform static application security testing (SAST)?",
            "Do you perform dynamic application security testing (DAST)?",
            "Are security tests integrated into your CI/CD pipeline?",
            "Do you perform dependency scanning for vulnerabilities?"
        ],
        implementation_guidance=[
            "Use Amazon CodeGuru Reviewer for static code analysis",
            "Implement DAST tools in your testing pipeline",
            "Use AWS Inspector for container and application vulnerability assessment",
            "Scan dependencies for known vulnerabilities in CI/CD"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_app_service_logging.html",
        related_best_practices=["SEC06-BP02", "SEC06-BP03"]
    ),
    "SEC06-BP02": BestPractice(
        id="SEC06-BP02",
        title="Configure Service and Application Logging",
        pillar=Pillar.SECURITY,
        description="Configure logging for services and applications to support security monitoring",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you logging security-relevant events from applications and services?",
            "Do logs include sufficient detail for security analysis?",
            "Are logs centrally collected and stored securely?",
            "Do you have log retention policies aligned with security requirements?"
        ],
        implementation_guidance=[
            "Use AWS CloudTrail for API logging",
            "Configure VPC Flow Logs for network monitoring",
            "Use AWS CloudWatch Logs for application logging",
            "Implement structured logging with security context"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_logs.html",
        related_best_practices=["SEC06-BP01", "SEC06-BP03"]
    ),
    "SEC06-BP03": BestPractice(
        id="SEC06-BP03",
        title="Analyze Logs Centrally",
        pillar=Pillar.SECURITY,
        description="Analyze security logs centrally to identify potential security events",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you centrally analyze logs for security events?",
            "Are you using automated tools for log analysis?",
            "Do you have correlation rules to identify security patterns?",
            "Are security events prioritized and escalated appropriately?"
        ],
        implementation_guidance=[
            "Use Amazon Security Lake for centralized security data",
            "Implement Amazon GuardDuty for threat detection",
            "Use AWS Security Hub for centralized security findings",
            "Create custom correlation rules for your environment"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html",
        related_best_practices=["SEC06-BP01", "SEC06-BP02", "SEC06-BP04"]
    ),
    "SEC06-BP04": BestPractice(
        id="SEC06-BP04",
        title="Implement Actionable Security Events",
        pillar=Pillar.SECURITY,
        description="Implement security events that trigger appropriate response actions",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do security events trigger automated responses where appropriate?",
            "Are security alerts actionable with clear next steps?",
            "Do you have escalation procedures for different event severities?",
            "Are security events integrated with incident response processes?"
        ],
        implementation_guidance=[
            "Use AWS Config Rules for compliance monitoring",
            "Implement automated remediation with AWS Systems Manager",
            "Create security event playbooks and runbooks",
            "Integrate with incident management systems"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_noncompliant_resources.html",
        related_best_practices=["SEC06-BP03"]
    ),
    "SEC05-BP01": BestPractice(
        id="SEC05-BP01",
        title="Create Network Layers",
        pillar=Pillar.SECURITY,
        description="Create network layers to segment resources based on security requirements",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use multiple network layers to segment resources?",
            "Are public and private resources properly separated?",
            "Do you use subnets to create security boundaries?",
            "Are network access controls implemented at multiple layers?"
        ],
        implementation_guidance=[
            "Use VPCs to create isolated network environments",
            "Implement public and private subnets appropriately",
            "Use security groups and NACLs for access control",
            "Consider AWS Transit Gateway for complex network topologies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html",
        related_best_practices=["SEC05-BP02"]
    ),
    "SEC05-BP02": BestPractice(
        id="SEC05-BP02",
        title="Control Traffic at All Layers",
        pillar=Pillar.SECURITY,
        description="Control network traffic at all layers with appropriate security controls",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you control traffic at the network, subnet, and instance levels?",
            "Are security groups configured with least privilege access?",
            "Do you use NACLs for additional network-level controls?",
            "Are you monitoring and logging network traffic?"
        ],
        implementation_guidance=[
            "Configure security groups with minimal required access",
            "Use NACLs for subnet-level traffic control",
            "Implement VPC Flow Logs for traffic monitoring",
            "Use AWS WAF for application-layer protection"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html",
        related_best_practices=["SEC05-BP01", "SEC05-BP03"]
    ),
    "SEC05-BP03": BestPractice(
        id="SEC05-BP03",
        title="Implement Inspection and Protection",
        pillar=Pillar.SECURITY,
        description="Implement network inspection and protection mechanisms",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you inspect network traffic for malicious activity?",
            "Are you using intrusion detection and prevention systems?",
            "Do you have DDoS protection implemented?",
            "Are you monitoring for unusual network patterns?"
        ],
        implementation_guidance=[
            "Use AWS Shield for DDoS protection",
            "Implement AWS WAF for web application protection",
            "Use Amazon GuardDuty for network threat detection",
            "Consider AWS Network Firewall for advanced inspection"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html",
        related_best_practices=["SEC05-BP02", "SEC05-BP04"]
    ),
    "SEC05-BP04": BestPractice(
        id="SEC05-BP04",
        title="Automate Network Protection",
        pillar=Pillar.SECURITY,
        description="Automate network protection to respond to threats quickly",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated responses to network security events?",
            "Are network security controls managed as code?",
            "Do you automatically update security rules based on threat intelligence?",
            "Are network security configurations validated automatically?"
        ],
        implementation_guidance=[
            "Use AWS Config Rules to validate network configurations",
            "Implement automated security group management",
            "Use AWS Lambda for automated threat response",
            "Integrate threat intelligence feeds for automatic rule updates"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_auto_protect.html",
        related_best_practices=["SEC05-BP03"]
    ),
    "SEC04-BP01": BestPractice(
        id="SEC04-BP01",
        title="Perform Vulnerability Management",
        pillar=Pillar.SECURITY,
        description="Perform regular vulnerability management for compute resources",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you regularly scan for vulnerabilities in your compute resources?",
            "Are vulnerabilities prioritized and remediated based on risk?",
            "Do you have a vulnerability management process?",
            "Are you tracking vulnerability remediation metrics?"
        ],
        implementation_guidance=[
            "Use Amazon Inspector for vulnerability assessment",
            "Implement regular vulnerability scanning schedules",
            "Prioritize vulnerabilities based on CVSS scores and business impact",
            "Track remediation metrics and SLAs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_vulnerability_management.html",
        related_best_practices=["SEC04-BP02", "SEC04-BP05"]
    ),
    "SEC04-BP02": BestPractice(
        id="SEC04-BP02",
        title="Use Hardened Images",
        pillar=Pillar.SECURITY,
        description="Use hardened images and reduce attack surface of compute resources",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use hardened base images for your compute resources?",
            "Are unnecessary services and packages removed from images?",
            "Do you regularly update and patch your base images?",
            "Are images scanned for vulnerabilities before deployment?"
        ],
        implementation_guidance=[
            "Use minimal base images like Amazon Linux or Alpine",
            "Remove unnecessary packages and services from images",
            "Implement image scanning in your CI/CD pipeline",
            "Use AWS ECR image scanning for container images"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_hardened_images.html",
        related_best_practices=["SEC04-BP01", "SEC04-BP04"]
    ),
    "SEC04-BP03": BestPractice(
        id="SEC04-BP03",
        title="Reduce Manual Management and Interactive Access",
        pillar=Pillar.SECURITY,
        description="Reduce manual management and interactive access to compute resources",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you minimize interactive access to compute resources?",
            "Are administrative tasks automated where possible?",
            "Do you use session management for necessary interactive access?",
            "Are privileged operations logged and monitored?"
        ],
        implementation_guidance=[
            "Use AWS Systems Manager Session Manager for secure access",
            "Automate administrative tasks with Systems Manager Automation",
            "Implement just-in-time access for privileged operations",
            "Log and monitor all privileged access activities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_reduce_manual_management.html",
        related_best_practices=["SEC04-BP05"]
    ),
    "SEC04-BP04": BestPractice(
        id="SEC04-BP04",
        title="Validate Software Integrity",
        pillar=Pillar.SECURITY,
        description="Validate the integrity of software and configurations",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you validate the integrity of software before deployment?",
            "Are software packages signed and verified?",
            "Do you use checksums or hashes to verify file integrity?",
            "Are configuration changes validated for integrity?"
        ],
        implementation_guidance=[
            "Use package signing and verification mechanisms",
            "Implement file integrity monitoring",
            "Use AWS Systems Manager for configuration compliance",
            "Verify checksums and digital signatures for software packages"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_validate_software_integrity.html",
        related_best_practices=["SEC04-BP02"]
    ),
    "SEC04-BP05": BestPractice(
        id="SEC04-BP05",
        title="Automate Compute Protection",
        pillar=Pillar.SECURITY,
        description="Automate compute protection to respond to security events",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have automated responses to compute security events?",
            "Are security configurations managed and enforced automatically?",
            "Do you automatically isolate compromised resources?",
            "Are security patches applied automatically where appropriate?"
        ],
        implementation_guidance=[
            "Use AWS Systems Manager Patch Manager for automated patching",
            "Implement automated incident response with AWS Lambda",
            "Use AWS Config for automated compliance enforcement",
            "Automate resource isolation during security incidents"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_auto_protection.html",
        related_best_practices=["SEC04-BP01", "SEC04-BP03"]
    ),
    "SEC07-BP01": BestPractice(
        id="SEC07-BP01",
        title="Identify the Data Within Your Workload",
        pillar=Pillar.SECURITY,
        description="Identify and understand the data within your workload and its sensitivity",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified all data within your workload?",
            "Do you understand the sensitivity and classification of your data?",
            "Are data flows and data stores documented?",
            "Do you know where sensitive data is processed and stored?"
        ],
        implementation_guidance=[
            "Conduct data discovery to identify all data within your workload",
            "Use AWS Macie for automated data discovery and classification",
            "Document data flows and create data maps",
            "Classify data based on sensitivity and regulatory requirements"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html",
        related_best_practices=["SEC07-BP02", "SEC07-BP03"]
    ),
    "SEC07-BP02": BestPractice(
        id="SEC07-BP02",
        title="Define Data Protection Controls",
        pillar=Pillar.SECURITY,
        description="Define data protection controls based on data classification",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you defined protection controls based on data classification?",
            "Are different protection levels applied to different data types?",
            "Do you have data handling procedures for each classification?",
            "Are protection controls aligned with regulatory requirements?"
        ],
        implementation_guidance=[
            "Define protection controls for each data classification level",
            "Implement appropriate encryption for different data types",
            "Create data handling procedures and access controls",
            "Align controls with compliance requirements like GDPR or HIPAA"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html",
        related_best_practices=["SEC07-BP01", "SEC08-BP01", "SEC09-BP01"]
    ),
    "SEC07-BP03": BestPractice(
        id="SEC07-BP03",
        title="Automate Data Classification",
        pillar=Pillar.SECURITY,
        description="Automate data classification to ensure consistent and scalable protection",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use automated tools for data classification?",
            "Are classification rules consistently applied across your workload?",
            "Do you have automated tagging based on data classification?",
            "Are classification changes automatically detected and handled?"
        ],
        implementation_guidance=[
            "Use AWS Macie for automated data classification",
            "Implement automated tagging based on classification results",
            "Create classification rules and policies",
            "Set up automated alerts for classification changes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_auto_classification.html",
        related_best_practices=["SEC07-BP01", "SEC07-BP04"]
    ),
    "SEC07-BP04": BestPractice(
        id="SEC07-BP04",
        title="Define Data Lifecycle Management",
        pillar=Pillar.SECURITY,
        description="Define data lifecycle management based on classification and requirements",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have defined data lifecycle policies?",
            "Are retention periods based on data classification and requirements?",
            "Do you have secure data disposal procedures?",
            "Are lifecycle policies automated where possible?"
        ],
        implementation_guidance=[
            "Define data retention policies based on classification",
            "Use S3 lifecycle policies for automated data management",
            "Implement secure data deletion procedures",
            "Automate lifecycle management where possible"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_lifecycle_management.html",
        related_best_practices=["SEC07-BP03"]
    ),
    "SEC08-BP01": BestPractice(
        id="SEC08-BP01",
        title="Implement Secure Key Management",
        pillar=Pillar.SECURITY,
        description="Implement secure key and certificate management for data at rest",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use a centralized key management system?",
            "Are encryption keys properly managed and rotated?",
            "Do you have separation of duties for key management?",
            "Are keys protected with appropriate access controls?"
        ],
        implementation_guidance=[
            "Use AWS KMS for centralized key management",
            "Implement automatic key rotation",
            "Use IAM policies for key access control",
            "Consider AWS CloudHSM for high-security requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html",
        related_best_practices=["SEC08-BP02", "SEC09-BP01"]
    ),
    "SEC08-BP02": BestPractice(
        id="SEC08-BP02",
        title="Enforce Encryption at Rest",
        pillar=Pillar.SECURITY,
        description="Enforce encryption at rest for all sensitive data",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Is all sensitive data encrypted at rest?",
            "Do you use strong encryption algorithms?",
            "Are encryption keys managed securely?",
            "Is encryption enforced through policies and controls?"
        ],
        implementation_guidance=[
            "Enable encryption for all AWS services storing data",
            "Use AES-256 or equivalent strong encryption",
            "Implement encryption policies and compliance checks",
            "Use AWS Config rules to enforce encryption requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html",
        related_best_practices=["SEC08-BP01", "SEC08-BP03"]
    ),
    "SEC08-BP03": BestPractice(
        id="SEC08-BP03",
        title="Automate Data at Rest Protection",
        pillar=Pillar.SECURITY,
        description="Automate data at rest protection to ensure consistent security",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you automatically apply encryption to new data stores?",
            "Are encryption policies enforced automatically?",
            "Do you have automated compliance checking for data protection?",
            "Are encryption violations automatically detected and remediated?"
        ],
        implementation_guidance=[
            "Use AWS Config rules for automated encryption compliance",
            "Implement automatic encryption for new resources",
            "Set up automated remediation for encryption violations",
            "Use AWS Security Hub for centralized compliance monitoring"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_automate_protection.html",
        related_best_practices=["SEC08-BP02", "SEC08-BP04"]
    ),
    "SEC08-BP04": BestPractice(
        id="SEC08-BP04",
        title="Enforce Access Control for Data at Rest",
        pillar=Pillar.SECURITY,
        description="Enforce access control for data at rest using authentication and authorization",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you enforce access control for data at rest?",
            "Are access permissions based on least privilege principles?",
            "Do you use strong authentication for data access?",
            "Are data access activities logged and monitored?"
        ],
        implementation_guidance=[
            "Use IAM policies for fine-grained access control",
            "Implement resource-based policies for data stores",
            "Enable access logging for all data stores",
            "Use AWS CloudTrail to monitor data access activities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_access_control.html",
        related_best_practices=["SEC08-BP03"]
    ),
    "SEC09-BP01": BestPractice(
        id="SEC09-BP01",
        title="Implement Secure Key and Certificate Management",
        pillar=Pillar.SECURITY,
        description="Implement secure key and certificate management for data in transit",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use secure key and certificate management for data in transit?",
            "Are TLS certificates properly managed and rotated?",
            "Do you use strong cryptographic protocols?",
            "Are certificates validated and trusted?"
        ],
        implementation_guidance=[
            "Use AWS Certificate Manager for TLS certificate management",
            "Implement automatic certificate renewal",
            "Use strong TLS versions (1.2 or higher)",
            "Validate certificate chains and revocation status"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html",
        related_best_practices=["SEC09-BP02", "SEC08-BP01"]
    ),
    "SEC09-BP02": BestPractice(
        id="SEC09-BP02",
        title="Enforce Encryption in Transit",
        pillar=Pillar.SECURITY,
        description="Enforce encryption in transit for all sensitive data",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Is all sensitive data encrypted in transit?",
            "Do you use strong encryption protocols?",
            "Are all communication channels secured?",
            "Do you enforce encryption policies?"
        ],
        implementation_guidance=[
            "Use TLS 1.2 or higher for all communications",
            "Implement HTTPS for all web traffic",
            "Use VPN or AWS PrivateLink for internal communications",
            "Enforce encryption policies through security groups and NACLs"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html",
        related_best_practices=["SEC09-BP01", "SEC09-BP03"]
    ),
    "SEC09-BP03": BestPractice(
        id="SEC09-BP03",
        title="Authenticate Network Communications",
        pillar=Pillar.SECURITY,
        description="Authenticate network communications to ensure data integrity and authenticity",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you authenticate network communications?",
            "Are communication endpoints verified?",
            "Do you use mutual authentication where appropriate?",
            "Are authentication mechanisms regularly updated?"
        ],
        implementation_guidance=[
            "Use mutual TLS (mTLS) for service-to-service communication",
            "Implement certificate-based authentication",
            "Use AWS App Mesh or service mesh for secure service communication",
            "Regularly rotate authentication credentials"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_authentication.html",
        related_best_practices=["SEC09-BP02"]
    ),

    
    # Reliability
    "REL01": BestPractice(
        id="REL01",
        title="Design for Failure",
        pillar=Pillar.RELIABILITY,
        description="Assume things will fail and design systems to handle failures gracefully",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using multiple Availability Zones?",
            "Do you have automated backup and recovery procedures?",
            "Are you implementing circuit breakers and retries?"
        ],
        implementation_guidance=[
            "Deploy across multiple AZs",
            "Implement automated backup strategies",
            "Use circuit breakers for external dependencies"
        ]
    ),
    "REL02": BestPractice(
        id="REL02",
        title="Implement Auto Scaling",
        pillar=Pillar.RELIABILITY,
        description="Automatically scale resources based on demand",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are you using Auto Scaling Groups?",
            "Do you have scaling policies based on metrics?",
            "Are you testing scaling scenarios?"
        ],
        implementation_guidance=[
            "Configure Auto Scaling Groups with appropriate policies",
            "Use CloudWatch metrics for scaling decisions",
            "Test scaling scenarios regularly"
        ]
    ),
    
    # Performance Efficiency
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
    ),
    
    # Cost Optimization
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
    ),
    
    # Sustainability
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


def get_best_practices_by_pillar(pillar: Pillar) -> List[BestPractice]:
    """Get all best practices for a specific pillar."""
    return [bp for bp in WELL_ARCHITECTED_BEST_PRACTICES.values() if bp.pillar == pillar]


def get_all_best_practices() -> List[BestPractice]:
    """Get all Well-Architected best practices."""
    return list(WELL_ARCHITECTED_BEST_PRACTICES.values())