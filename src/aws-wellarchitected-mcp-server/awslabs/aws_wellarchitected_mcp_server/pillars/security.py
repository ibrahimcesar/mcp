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

"""Security pillar best practices."""

from awslabs.aws_wellarchitected_mcp_server.models import Pillar, RiskLevel
from awslabs.aws_wellarchitected_mcp_server.well_architected_framework import BestPractice
from typing import Dict

SECURITY_BEST_PRACTICES: Dict[str, BestPractice] = {
   # Security
    "SEC01-BP01": BestPractice(
        id="SEC01-BP01",
        title="Separate Workloads Using Accounts",
        pillar=Pillar.SECURITY,
        area="AWS account management and separation",

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
        area="AWS account management and separation",

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
        area="Operating your workload securely",

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
        area="Operating your workload securely",

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
        area="Operating your workload securely",

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
        area="Operating your workload securely",

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
        area="Operating your workload securely",

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
        area="Operating your workload securely",

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
    "SEC02-BP01": BestPractice(
        id="SEC02-BP01",
        title="Use Strong Identity Foundation",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Implement strong identity foundation with centralized identity provider",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you use a centralized identity provider?",
            "Are you using strong authentication mechanisms?",
            "Do you implement least privilege access?"
        ],
        implementation_guidance=[
            "Use AWS IAM Identity Center for centralized identity",
            "Implement multi-factor authentication",
            "Apply principle of least privilege"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html"
    ),
    "SEC02-BP02": BestPractice(
        id="SEC02-BP02",
        title="Use Temporary Credentials",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Use temporary credentials instead of long-term access keys",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are you using temporary credentials?",
            "Do you avoid long-term access keys?",
            "Are credentials rotated regularly?"
        ],
        implementation_guidance=[
            "Use IAM roles instead of access keys",
            "Implement credential rotation",
            "Use AWS STS for temporary credentials"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_temp_credentials.html"
    ),
    "SEC02-BP03": BestPractice(
        id="SEC02-BP03",
        title="Store and Use Secrets Securely",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Store and use secrets securely using dedicated secret management services",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are secrets stored securely?",
            "Do you use dedicated secret management services?",
            "Are secrets rotated automatically?"
        ],
        implementation_guidance=[
            "Use AWS Secrets Manager for secret storage",
            "Implement automatic secret rotation",
            "Avoid hardcoding secrets in code"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_secrets.html"
    ),
    "SEC02-BP04": BestPractice(
        id="SEC02-BP04",
        title="Rely on Centralized Identity Provider",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Rely on centralized identity provider for human and machine identities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use centralized identity provider?",
            "Are identities managed consistently?",
            "Do you have identity federation?"
        ],
        implementation_guidance=[
            "Use AWS IAM Identity Center",
            "Implement SAML or OIDC federation",
            "Centralize identity management"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_centralized_identity.html"
    ),
    "SEC02-BP05": BestPractice(
        id="SEC02-BP05",
        title="Audit and Rotate Credentials Regularly",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Audit and rotate credentials regularly to maintain security",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you audit credentials regularly?",
            "Are credentials rotated on schedule?",
            "Do you track credential usage?"
        ],
        implementation_guidance=[
            "Use AWS Config for credential auditing",
            "Implement automated credential rotation",
            "Monitor credential usage with CloudTrail"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_audit_rotate.html"
    ),
    "SEC02-BP06": BestPractice(
        id="SEC02-BP06",
        title="Leverage User Groups and Attributes",
        pillar=Pillar.SECURITY,
        area="Identity management",

        description="Leverage user groups and attributes for access control",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you use user groups for access control?",
            "Are user attributes leveraged for authorization?",
            "Do you have attribute-based access control?"
        ],
        implementation_guidance=[
            "Use IAM groups for permission management",
            "Implement attribute-based access control",
            "Use tags for resource-based permissions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_user_groups_attributes.html"
    ),
    "SEC03-BP01": BestPractice(
        id="SEC03-BP01",
        title="Define Access Requirements",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Define access requirements based on least privilege principle",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Are access requirements clearly defined?",
            "Do you follow least privilege principle?",
            "Are permissions granted based on job function?"
        ],
        implementation_guidance=[
            "Define role-based access requirements",
            "Implement least privilege access",
            "Document access patterns and requirements"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define_requirements.html"
    ),
    "SEC03-BP02": BestPractice(
        id="SEC03-BP02",
        title="Grant Least Privilege Access",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Grant least privilege access to users and systems",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you grant minimum necessary permissions?",
            "Are permissions reviewed regularly?",
            "Do you use permission boundaries?"
        ],
        implementation_guidance=[
            "Use IAM permission boundaries",
            "Implement just-in-time access",
            "Regular permission reviews and cleanup"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privilege.html"
    ),
    "SEC03-BP03": BestPractice(
        id="SEC03-BP03",
        title="Establish Emergency Access Process",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Establish emergency access process for break-glass scenarios",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have emergency access procedures?",
            "Are break-glass processes documented?",
            "Is emergency access monitored and audited?"
        ],
        implementation_guidance=[
            "Create emergency access roles",
            "Document break-glass procedures",
            "Monitor and audit emergency access usage"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_emergency_access.html"
    ),
    "SEC03-BP04": BestPractice(
        id="SEC03-BP04",
        title="Reduce Permissions Continuously",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Continuously reduce permissions based on usage patterns",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you analyze permission usage?",
            "Are unused permissions removed?",
            "Do you have automated permission optimization?"
        ],
        implementation_guidance=[
            "Use AWS Access Analyzer",
            "Implement permission usage monitoring",
            "Automate permission cleanup processes"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_reduce_continuously.html"
    ),
    "SEC03-BP05": BestPractice(
        id="SEC03-BP05",
        title="Define Permission Guardrails for Your Organization",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Define permission guardrails to prevent privilege escalation",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have permission guardrails?",
            "Are privilege escalation paths blocked?",
            "Do you use service control policies?"
        ],
        implementation_guidance=[
            "Use AWS Organizations SCPs",
            "Implement permission boundaries",
            "Define organizational permission policies"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_guardrails.html"
    ),
    "SEC03-BP06": BestPractice(
        id="SEC03-BP06",
        title="Manage Access Based on Life Cycle",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Manage access based on user and resource life cycles",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you manage access based on life cycles?",
            "Are permissions updated when roles change?",
            "Do you have automated provisioning/deprovisioning?"
        ],
        implementation_guidance=[
            "Implement automated user provisioning",
            "Use identity lifecycle management",
            "Automate access reviews and updates"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_lifecycle.html"
    ),
    "SEC03-BP07": BestPractice(
        id="SEC03-BP07",
        title="Analyze Public and Cross-Account Access",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Analyze and monitor public and cross-account access",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you analyze public access?",
            "Are cross-account permissions monitored?",
            "Do you have visibility into external access?"
        ],
        implementation_guidance=[
            "Use AWS Access Analyzer",
            "Monitor cross-account access patterns",
            "Regular review of public access permissions"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html"
    ),
    "SEC03-BP08": BestPractice(
        id="SEC03-BP08",
        title="Share Resources Securely Within Your Organization",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Share resources securely within your organization",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you share resources securely?",
            "Are sharing mechanisms controlled?",
            "Do you monitor resource sharing?"
        ],
        implementation_guidance=[
            "Use AWS Resource Access Manager",
            "Implement secure sharing policies",
            "Monitor and audit resource sharing"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html"
    ),
    "SEC03-BP09": BestPractice(
        id="SEC03-BP09",
        title="Share Resources Securely with a Third Party",
        pillar=Pillar.SECURITY,
        area="Permissions management",

        description="Share resources securely with third parties when needed",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you share resources securely with third parties?",
            "Are third-party access controls in place?",
            "Do you monitor third-party access?"
        ],
        implementation_guidance=[
            "Use cross-account roles for third-party access",
            "Implement external ID for additional security",
            "Monitor and audit third-party access"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_third_party.html"
    ),
    "SEC06-BP01": BestPractice(
        id="SEC06-BP01",
        title="Perform Application Security Testing",
        pillar=Pillar.SECURITY,
        area="Detection",

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
        area="Detection",

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
        area="Detection",

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
        area="Detection",

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
        area="Protecting networks",

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
        area="Protecting networks",

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
        area="Protecting networks",

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
        area="Protecting networks",

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
        area="Protecting compute",

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
        area="Protecting compute",

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
        area="Protecting compute",

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
        area="Protecting compute",

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
        area="Protecting compute",

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
        area="Data classification",

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
        area="Data classification",

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
        area="Data classification",

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
        area="Data classification",

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
        area="Protecting data at rest",

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
        area="Protecting data at rest",

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
        area="Protecting data at rest",

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
        area="Protecting data at rest",

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
        area="Protecting data in transit",

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
        area="Protecting data in transit",

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
        area="Protecting data in transit",

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
    "SEC10-BP01": BestPractice(
        id="SEC10-BP01",
        title="Identify Key Personnel and External Resources",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Identify key personnel and external resources for incident response",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Have you identified key personnel for incident response?",
            "Do you have external resources and contacts identified?",
            "Are roles and responsibilities clearly defined?",
            "Do you have 24/7 contact information available?"
        ],
        implementation_guidance=[
            "Create incident response team with defined roles",
            "Establish relationships with external security experts",
            "Maintain updated contact lists and escalation procedures",
            "Define clear responsibilities for each team member"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_identify_personnel.html",
        related_best_practices=["SEC10-BP02", "SEC10-BP04"]
    ),
    "SEC10-BP02": BestPractice(
        id="SEC10-BP02",
        title="Develop Incident Management Plans",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Develop and maintain incident management plans and procedures",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have documented incident management plans?",
            "Are plans regularly updated and tested?",
            "Do plans cover different types of security incidents?",
            "Are communication procedures clearly defined?"
        ],
        implementation_guidance=[
            "Create comprehensive incident response plans",
            "Define incident classification and severity levels",
            "Establish communication and notification procedures",
            "Regularly review and update plans based on lessons learned"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_develop_management_plans.html",
        related_best_practices=["SEC10-BP01", "SEC10-BP03", "SEC10-BP04"]
    ),
    "SEC10-BP03": BestPractice(
        id="SEC10-BP03",
        title="Prepare Forensic Capabilities",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Prepare forensic capabilities to support incident investigation",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have forensic capabilities prepared?",
            "Are logs and evidence collection procedures defined?",
            "Do you have tools and expertise for forensic analysis?",
            "Are legal and compliance requirements considered?"
        ],
        implementation_guidance=[
            "Establish forensic investigation procedures",
            "Ensure comprehensive logging for forensic analysis",
            "Prepare forensic tools and analysis capabilities",
            "Consider legal and compliance requirements for evidence handling"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_prepare_forensic.html",
        related_best_practices=["SEC10-BP02", "SEC10-BP06"]
    ),
    "SEC10-BP04": BestPractice(
        id="SEC10-BP04",
        title="Develop and Test Security Incident Response Playbooks",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Develop and test security incident response playbooks",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have incident response playbooks for common scenarios?",
            "Are playbooks regularly tested and updated?",
            "Do playbooks include step-by-step procedures?",
            "Are playbooks accessible during incidents?"
        ],
        implementation_guidance=[
            "Create playbooks for common incident types",
            "Include detailed step-by-step response procedures",
            "Test playbooks through tabletop exercises",
            "Keep playbooks updated and easily accessible"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html",
        related_best_practices=["SEC10-BP01", "SEC10-BP02", "SEC10-BP07"]
    ),
    "SEC10-BP05": BestPractice(
        id="SEC10-BP05",
        title="Pre-provision Access",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Pre-provision access for incident response team members",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do incident responders have pre-provisioned access?",
            "Are access permissions appropriate for incident response?",
            "Is access regularly reviewed and updated?",
            "Are emergency access procedures defined?"
        ],
        implementation_guidance=[
            "Pre-provision appropriate access for incident response team",
            "Use break-glass access procedures for emergencies",
            "Regularly review and update access permissions",
            "Implement just-in-time access where possible"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_pre_provision_access.html",
        related_best_practices=["SEC10-BP06"]
    ),
    "SEC10-BP06": BestPractice(
        id="SEC10-BP06",
        title="Pre-deploy Tools",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Pre-deploy tools and resources for incident response",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Are incident response tools pre-deployed and ready?",
            "Do you have automated response capabilities?",
            "Are tools regularly tested and updated?",
            "Are backup tools and procedures available?"
        ],
        implementation_guidance=[
            "Pre-deploy incident response tools and automation",
            "Use AWS Systems Manager for automated response",
            "Regularly test and update response tools",
            "Maintain backup tools and manual procedures"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_pre_deploy_tools.html",
        related_best_practices=["SEC10-BP03", "SEC10-BP05"]
    ),
    "SEC10-BP07": BestPractice(
        id="SEC10-BP07",
        title="Run Game Days",
        pillar=Pillar.SECURITY,
        area="Preparation",

        description="Run game days to test incident response capabilities",
        risk_level=RiskLevel.LOW,
        questions=[
            "Do you regularly conduct incident response game days?",
            "Are different incident scenarios tested?",
            "Do you capture lessons learned from exercises?",
            "Are improvements implemented based on exercise results?"
        ],
        implementation_guidance=[
            "Conduct regular incident response exercises",
            "Test different incident scenarios and playbooks",
            "Capture lessons learned and improvement opportunities",
            "Update procedures based on exercise results"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_run_game_days.html",
        related_best_practices=["SEC10-BP04"]
    ),
    "SEC10-BP08": BestPractice(
        id="SEC10-BP08",
        title="Establish a Framework for Learning from Incidents",
        pillar=Pillar.SECURITY,
        area="Post-incident activity",

        description="Establish a framework for learning from security incidents",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you have a framework for learning from incidents?",
            "Are post-incident reviews conducted?",
            "Are lessons learned documented and shared?",
            "Are improvements implemented based on incident analysis?"
        ],
        implementation_guidance=[
            "Conduct post-incident reviews for all security incidents",
            "Document lessons learned and improvement opportunities",
            "Share learnings across teams and organization",
            "Implement improvements to prevent similar incidents"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_establish_incident_framework.html",
        related_best_practices=["SEC10-BP07"]
    ),
    "SEC11-BP01": BestPractice(
        id="SEC11-BP01",
        title="Train for Application Security",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Train development teams on application security best practices",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do development teams receive application security training?",
            "Is training regularly updated with current threats?",
            "Are secure coding practices taught and reinforced?",
            "Do you measure training effectiveness?"
        ],
        implementation_guidance=[
            "Provide regular application security training for developers",
            "Include secure coding practices and common vulnerabilities",
            "Update training content based on current threat landscape",
            "Measure and track training effectiveness"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_train_for_application_security.html",
        related_best_practices=["SEC11-BP08"]
    ),
    "SEC11-BP02": BestPractice(
        id="SEC11-BP02",
        title="Automate Testing Throughout the Development and Release Lifecycle",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Automate security testing throughout the development and release lifecycle",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you have automated security testing in your CI/CD pipeline?",
            "Are both static and dynamic security tests performed?",
            "Are security tests run at multiple stages of development?",
            "Are test results integrated into development workflows?"
        ],
        implementation_guidance=[
            "Integrate SAST and DAST tools into CI/CD pipelines",
            "Perform security testing at multiple development stages",
            "Use AWS CodeGuru and other automated security testing tools",
            "Fail builds on critical security findings"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_automate_testing_throughout_lifecycle.html",
        related_best_practices=["SEC11-BP03", "SEC11-BP04"]
    ),
    "SEC11-BP03": BestPractice(
        id="SEC11-BP03",
        title="Perform Regular Penetration Testing",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Perform regular penetration testing to identify security vulnerabilities",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you perform regular penetration testing?",
            "Are tests conducted by qualified security professionals?",
            "Do you test both applications and infrastructure?",
            "Are findings remediated in a timely manner?"
        ],
        implementation_guidance=[
            "Conduct regular penetration testing by qualified professionals",
            "Test both applications and underlying infrastructure",
            "Follow AWS penetration testing guidelines",
            "Remediate findings based on risk and severity"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_perform_regular_penetration_testing.html",
        related_best_practices=["SEC11-BP02"]
    ),
    "SEC11-BP04": BestPractice(
        id="SEC11-BP04",
        title="Perform Manual Code Reviews",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Perform manual code reviews to identify security issues",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you perform manual security-focused code reviews?",
            "Are reviewers trained in secure coding practices?",
            "Do reviews focus on security-critical code paths?",
            "Are review findings tracked and remediated?"
        ],
        implementation_guidance=[
            "Implement mandatory security-focused code reviews",
            "Train reviewers on secure coding practices and common vulnerabilities",
            "Focus reviews on security-critical code and high-risk changes",
            "Use code review tools to track findings and remediation"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_manual_code_reviews.html",
        related_best_practices=["SEC11-BP02"]
    ),
    "SEC11-BP05": BestPractice(
        id="SEC11-BP05",
        title="Centralize Services for Packages and Dependencies",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Centralize services for managing packages and dependencies",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you use centralized package and dependency management?",
            "Are packages scanned for vulnerabilities?",
            "Do you have approved package repositories?",
            "Are dependency updates managed centrally?"
        ],
        implementation_guidance=[
            "Use centralized package repositories and registries",
            "Implement vulnerability scanning for packages and dependencies",
            "Maintain approved package lists and versions",
            "Automate dependency updates and security patches"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_centralize_services_for_packages_and_dependencies.html",
        related_best_practices=["SEC11-BP06"]
    ),
    "SEC11-BP06": BestPractice(
        id="SEC11-BP06",
        title="Deploy Software Programmatically",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Deploy software programmatically to reduce security risks",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do you deploy software programmatically?",
            "Are deployments automated and repeatable?",
            "Do you use infrastructure as code for deployments?",
            "Are deployment processes secured and audited?"
        ],
        implementation_guidance=[
            "Use automated deployment pipelines",
            "Implement infrastructure as code for consistent deployments",
            "Secure deployment processes with appropriate access controls",
            "Audit and log all deployment activities"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_deploy_software_programmatically.html",
        related_best_practices=["SEC11-BP05", "SEC11-BP07"]
    ),
    "SEC11-BP07": BestPractice(
        id="SEC11-BP07",
        title="Regularly Assess Security Properties of the Deployment Pipeline",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Regularly assess security properties of the deployment pipeline",
        risk_level=RiskLevel.MEDIUM,
        questions=[
            "Do you regularly assess your deployment pipeline security?",
            "Are pipeline components secured and updated?",
            "Do you monitor pipeline for security events?",
            "Are pipeline access controls regularly reviewed?"
        ],
        implementation_guidance=[
            "Regularly assess deployment pipeline security",
            "Keep pipeline components updated and secured",
            "Monitor pipeline activities for security events",
            "Review and update pipeline access controls regularly"
        ],
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_regularly_assess_security_properties_of_pipelines.html",
        related_best_practices=["SEC11-BP06"]
    ),
    "SEC11-BP08": BestPractice(
        id="SEC11-BP08",
        title="Build a Program that Embeds Security Ownership in Workload Teams",
        pillar=Pillar.SECURITY,
        area="Application security",

        description="Build a program that embeds security ownership in workload teams",
        risk_level=RiskLevel.HIGH,
        questions=[
            "Do workload teams have embedded security ownership?",
            "Are security responsibilities clearly defined for each team?",
            "Do teams have security champions or liaisons?",
            "Is security integrated into team processes and culture?"
        ],
        implementation_guidance=[
            "Establish security champions within each workload team",
            "Define clear security responsibilities for team members",
            "Integrate security into team processes and workflows",
            "Provide teams with security tools and training"
        ],
        requires_user_input=True,
        url="https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_build_program_that_embeds_security_ownership_in_teams.html",
        related_best_practices=["SEC11-BP01"]
    ),
}