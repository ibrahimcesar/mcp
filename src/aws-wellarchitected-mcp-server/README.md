# AWS Well-Architected MCP Server

An AWS Labs Model Context Protocol (MCP) server that provides comprehensive AWS Well-Architected Framework reviews, generates Architecture Decision Records (ADRs), and offers implementation guidance.

> [!IMPORTANT]
> This MCP server helps you systematically review your AWS architecture against the 6 Well-Architected pillars and generates actionable ADRs for each best practice.

## ✨ Features

- **🔍 Comprehensive Reviews**: Analyze systems against all 6 Well-Architected pillars
- **📋 Best Practice Assessment**: Evaluate compliance with AWS best practices
- **📝 ADR Generation**: Create detailed Architecture Decision Records for each practice
- **⚠️ Risk Assessment**: Identify and prioritize risks (High/Medium/Low)
- **📚 Documentation Analysis**: Review and validate documentation currency
- **🛠️ Implementation Guidance**: Get specific recommendations and implementation steps
- **🎯 Priority Analysis**: Get top N recommendations based on risk and relationships
- **📊 Eisenhower Matrix**: Urgency vs importance prioritization framework
- **✅ SMART Solutions**: Structured implementation guidance with clear criteria
- **📋 Review Planning**: Three-phase methodology (Learn, Measure, Improve)

<details>
<summary>🏛️ Well-Architected Pillars Covered</summary>

1. **🔧 Operational Excellence** - Infrastructure as Code, Monitoring, Automation
2. **🔒 Security** - Identity, Data Protection, Infrastructure Security  
3. **🛡️ Reliability** - Fault Tolerance, Recovery, Scaling
4. **⚡ Performance Efficiency** - Resource Selection, Monitoring, Trade-offs
5. **💰 Cost Optimization** - Cost-Effective Resources, Matching Supply/Demand
6. **🌱 Sustainability** - Environmental Impact, Resource Efficiency

</details>

## 🚀 Installation

> [!TIP]
> We recommend using `uv` for faster dependency management and execution.

### Using uv (recommended)
```bash
cd src/aws-wellarchitected-mcp-server
uv sync
uv run awslabs.aws-wellarchitected-mcp-server
```

### Using pip
```bash
cd src/aws-wellarchitected-mcp-server
pip install -e .
```

<details>
<summary>⚙️ MCP Configuration</summary>

> [!IMPORTANT]
> Update the `cwd` path to match your actual installation directory.

Add to your MCP configuration file (`~/.config/mcp/mcp.json`):

**With uv:**
```json
{
  "mcpServers": {
    "aws-wellarchitected": {
      "command": "uv",
      "args": ["run", "awslabs.aws-wellarchitected-mcp-server"],
      "cwd": "/path/to/mcp/src/aws-wellarchitected-mcp-server"
    }
  }
}
```

**With pip:**
```json
{
  "mcpServers": {
    "aws-wellarchitected": {
      "command": "python",
      "args": ["-m", "awslabs.aws_wellarchitected_mcp_server.server"],
      "cwd": "/path/to/mcp/src/aws-wellarchitected-mcp-server"
    }
  }
}
```

</details>

## 💡 Usage

> [!NOTE]
> Provide detailed context about your architecture for better analysis results.

<details>
<summary>📋 Basic Review</summary>

```python
# Review all pillars
await review(
    context="E-commerce application with web tier, API tier, and database tier deployed on AWS",
    output_directory="./my-adrs"
)
```

</details>

<details>
<summary>🎯 Focused Review</summary>

> [!TIP]
> Focus on specific pillars for targeted improvements and faster reviews.

```python
# Review specific pillars
await review(
    context="Microservices architecture with containers",
    pillars=["SECURITY", "RELIABILITY"],
    documentation_paths=["./docs/architecture.md", "./README.md"],
    output_directory="./security-reliability-adrs"
)
```

</details>

<details>
<summary>🛠️ Get Implementation Guidance</summary>

```python
# Get specific implementation steps
await ask_implementation_fix(
    best_practice_id="SEC01",
    current_context="Currently using IAM users for applications",
    preferred_approach="Migrate to IAM roles"
)
```

</details>

<details>
<summary>🔧 Available Tools</summary>

### 🔍 `review`
Perform comprehensive Well-Architected Framework review
- **context**: Description of system/workload
- **pillars**: Optional list of specific pillars to review
- **documentation_paths**: Optional paths to documentation files
- **output_directory**: Directory to save ADR files

### 📋 `list_pillars`
List all available Well-Architected pillars with descriptions

### 📚 `get_best_practices`
Get best practices for specific pillar or all pillars
- **pillar**: Optional pillar name to filter practices

### 🛠️ `ask_implementation_fix`
Get detailed implementation guidance for specific best practice
- **best_practice_id**: ID of best practice (e.g., 'OPS01', 'SEC01')
- **current_context**: Current implementation description
- **preferred_approach**: Optional preferred implementation approach

### 📝 `collect_user_input`
Collect user input for best practices requiring human assessment
- **best_practice_id**: ID of best practice needing input (e.g., 'OPS01-BP01')
- **responses**: Dictionary of question-answer pairs for assessment

### 👥 `evaluate_customer_needs`
Specific tool for OPS01-BP01 customer needs assessment
- **stakeholder_engagement**: Current stakeholder engagement practices
- **customer_feedback_mechanisms**: Existing feedback collection methods
- **customer_outcome_focus**: How you prioritize based on customer outcomes
- **business_alignment**: How operations support business outcomes
- **support_data_review**: Use of historical support data
- **feature_validation**: Customer validation processes

### 🎯 `create_review_plan`
Generate structured review plan with three phases
- **workload_name**: Name of the workload to review
- **selected_pillars**: Optional list of pillars to focus on

### 📊 `get_priority_analysis`
Get top N priority recommendations based on risk and relationships
- **selected_pillars**: Optional list of pillars to analyze
- **count**: Number of top priorities to return (3, 5, or 10)

### 📊 `get_eisenhower_matrix`
Create urgency vs importance matrix for best practices
- **selected_pillars**: Optional list of pillars to analyze

### ✅ `get_smart_solutions`
Generate SMART solutions with implementation guidance
- **selected_pillars**: Optional list of pillars to analyze
- **focus_on_quick_wins**: Whether to focus on quick wins only

</details>

## 📊 Output

> [!NOTE]
> All generated files are saved in Markdown format for easy integration with documentation systems.

The server generates:

1. **📈 Review Results**: Comprehensive assessment with risk levels
2. **📝 ADR Files**: Markdown files for each best practice with:
   - Context and problem statement
   - Architectural decisions
   - Trade-offs and consequences
   - Implementation recommendations
3. **📋 Index File**: Summary of all ADRs with status indicators

<details>
<summary>📝 Example ADR Structure</summary>

```markdown
# ADR: Implement Infrastructure as Code

**Date:** 2024-01-15
**Status:** Proposed
**Best Practice ID:** OPS01
**Pillar:** OPERATIONAL_EXCELLENCE
**Risk Level:** HIGH

## Context
Well-Architected Framework OPERATIONAL_EXCELLENCE pillar requires...

## Decision
Need to implement Infrastructure as Code to meet Well-Architected standards

## Trade-offs
### Benefit
Improved system reliability and maintainability

### Cost
Initial implementation effort and potential complexity

## Implementation Notes
Priority: HIGH. Use AWS CloudFormation or CDK for infrastructure provisioning...
```

</details>

## ⚠️ Risk Levels

> [!CAUTION]
> Address HIGH risk items immediately to prevent potential system failures or security breaches.

- 🔴 **HIGH**: Critical issues requiring immediate attention
- 🟡 **MEDIUM**: Important improvements to plan and implement
- 🟢 **LOW**: Nice-to-have optimizations

<details>
<summary>📋 Best Practices Covered</summary>

## Summary
- **Total Best Practices**: 301
- **Operational Excellence**: 68 practices
- **Security**: 63 practices  
- **Reliability**: 59 practices
- **Performance Efficiency**: 32 practices
- **Cost Optimization**: 50 practices
- **Sustainability**: 29 practices

### 🔧 Operational Excellence
- **OPS01-BP01**: Evaluate External Customer Needs *(requires user input)*
- **OPS01-BP02**: Evaluate Internal Customer Needs *(requires user input)*
- **OPS01-BP03**: Evaluate Governance Requirements *(requires user input)*
- **OPS01-BP04**: Evaluate Compliance Requirements *(requires user input)*
- **OPS01-BP05**: Evaluate Threat Landscape *(requires user input)*
- **OPS01-BP06**: Evaluate Tradeoffs While Managing Benefits and Risks *(requires user input)*
- **OPS02-BP01**: Resources Have Identified Owners *(requires user input)*
- **OPS02-BP02**: Processes and Procedures Have Identified Owners *(requires user input)*
- **OPS02-BP03**: Operations Activities Have Identified Owners Responsible for Their Performance *(requires user input)*
- **OPS02-BP04**: Mechanisms Exist to Manage Responsibilities and Ownership *(requires user input)*
- **OPS02-BP05**: Mechanisms Exist to Request Additions, Changes, and Exceptions *(requires user input)*
- **OPS02-BP06**: Responsibilities Between Teams Are Predefined or Negotiated *(requires user input)*
- **OPS03-BP01**: Executive Sponsorship *(requires user input)*
- **OPS03-BP02**: Team Members Are Empowered to Take Action *(requires user input)*
- **OPS03-BP03**: Escalation Is Encouraged *(requires user input)*
- **OPS03-BP04**: Communications Are Timely, Clear, and Actionable *(requires user input)*
- **OPS03-BP05**: Experimentation Is Encouraged *(requires user input)*
- **OPS03-BP06**: Learning Is Encouraged *(requires user input)*
- **OPS03-BP07**: Team Members Are Encouraged to Maintain and Grow Their Skill Sets *(requires user input)*
- **OPS04-BP01**: Identify Key Performance Indicators *(requires user input)*
- **OPS04-BP02**: Implement Application Telemetry
- **OPS04-BP03**: Implement User Activity Telemetry
- **OPS04-BP04**: Implement Dependency Telemetry
- **OPS04-BP05**: Implement Distributed Tracing
- **OPS05-BP01**: Use Version Control
- **OPS05-BP02**: Test and Validate Changes
- **OPS05-BP03**: Use Configuration Management Systems
- **OPS05-BP04**: Use Build and Deployment Management Systems
- **OPS05-BP05**: Perform Patch Management
- **OPS05-BP06**: Share Design Standards *(requires user input)*
- **OPS05-BP07**: Implement Practices to Improve Code Quality
- **OPS05-BP08**: Use Multiple Environments
- **OPS05-BP09**: Make Frequent, Small, Reversible Changes
- **OPS05-BP10**: Fully Automate Integration and Deployment
- **OPS06-BP01**: Plan for Unsuccessful Changes
- **OPS06-BP02**: Test and Validate Changes
- **OPS06-BP03**: Use Deployment Management Systems
- **OPS06-BP04**: Automate Testing and Rollback
- **OPS07-BP01**: Ensure Personnel Capability *(requires user input)*
- **OPS07-BP02**: Ensure Consistent Review of Operational Readiness *(requires user input)*
- **OPS07-BP03**: Use Runbooks for Procedures *(requires user input)*
- **OPS07-BP04**: Use Playbooks for Issue Investigation *(requires user input)*
- **OPS07-BP05**: Make Informed Decisions to Deploy Systems and Changes *(requires user input)*
- **OPS07-BP06**: Enable Support Plans *(requires user input)*
- **OPS07-BP07**: Automate Responses to Events
- **OPS08-BP01**: Analyze Workload Metrics
- **OPS08-BP02**: Analyze Workload Logs
- **OPS08-BP03**: Analyze Workload Traces
- **OPS08-BP04**: Create Actionable Alerts
- **OPS08-BP05**: Create Dashboards
- **OPS09-BP01**: Measure Operations Goals and KPIs *(requires user input)*
- **OPS09-BP02**: Communicate Status and Trends *(requires user input)*
- **OPS09-BP03**: Review Operations Metrics and Prioritize Improvement *(requires user input)*
- **OPS10-BP01**: Use a Process for Event, Incident, and Problem Management *(requires user input)*
- **OPS10-BP02**: Have a Process Per Alert *(requires user input)*
- **OPS10-BP03**: Prioritize Operational Events Based on Business Impact *(requires user input)*
- **OPS10-BP04**: Define Escalation Paths *(requires user input)*
- **OPS10-BP05**: Define a Customer Communication Plan for Outages *(requires user input)*
- **OPS10-BP06**: Communicate Status Through Dashboards
- **OPS11-BP01**: Have a Process for Continuous Improvement *(requires user input)*
- **OPS11-BP02**: Perform Root Cause Analysis on Failures *(requires user input)*
- **OPS11-BP03**: Implement Feedback Loops *(requires user input)*
- **OPS11-BP04**: Perform Knowledge Management *(requires user input)*
- **OPS11-BP05**: Define Drivers for Improvement *(requires user input)*
- **OPS11-BP06**: Validate Insights *(requires user input)*
- **OPS11-BP07**: Perform Operations Metrics Reviews *(requires user input)*
- **OPS11-BP08**: Share Lessons Learned *(requires user input)*
- **OPS11-BP09**: Allocate Time to Make Improvements *(requires user input)*

### 🔒 Security
- **SEC01-BP01**: Separate Workloads Using Accounts
- **SEC01-BP02**: Secure Account Root User and Properties
- **SEC01-BP03**: Identify and Validate Control Objectives *(requires user input)*
- **SEC01-BP04**: Stay Up to Date with Security Threats and Recommendations *(requires user input)*
- **SEC01-BP05**: Reduce Security Management Scope
- **SEC01-BP06**: Automate Testing and Validation of Security Controls
- **SEC01-BP07**: Identify Threats and Prioritize Mitigations Using a Threat Model *(requires user input)*
- **SEC01-BP08**: Evaluate and Implement New Security Services and Features *(requires user input)*
- **SEC02-BP01**: Use Strong Identity Foundation
- **SEC02-BP02**: Use Temporary Credentials
- **SEC02-BP03**: Store and Use Secrets Securely
- **SEC02-BP04**: Rely on Centralized Identity Provider
- **SEC02-BP05**: Audit and Rotate Credentials Regularly
- **SEC02-BP06**: Leverage User Groups and Attributes
- **SEC03-BP01**: Define Access Requirements
- **SEC03-BP02**: Grant Least Privilege Access
- **SEC03-BP03**: Establish Emergency Access Process
- **SEC03-BP04**: Reduce Permissions Continuously
- **SEC03-BP05**: Define Permission Guardrails for Your Organization
- **SEC03-BP06**: Manage Access Based on Life Cycle
- **SEC03-BP07**: Analyze Public and Cross-Account Access
- **SEC03-BP08**: Share Resources Securely Within Your Organization
- **SEC03-BP09**: Share Resources Securely with a Third Party
- **SEC04-BP01**: Perform Vulnerability Management
- **SEC04-BP02**: Use Hardened Images
- **SEC04-BP03**: Reduce Manual Management and Interactive Access
- **SEC04-BP04**: Validate Software Integrity
- **SEC04-BP05**: Automate Compute Protection
- **SEC05-BP01**: Create Network Layers
- **SEC05-BP02**: Control Traffic at All Layers
- **SEC05-BP03**: Implement Inspection and Protection
- **SEC05-BP04**: Automate Network Protection
- **SEC06-BP01**: Perform Application Security Testing
- **SEC06-BP02**: Configure Service and Application Logging
- **SEC06-BP03**: Analyze Logs Centrally
- **SEC06-BP04**: Implement Actionable Security Events
- **SEC07-BP01**: Identify the Data Within Your Workload *(requires user input)*
- **SEC07-BP02**: Define Data Protection Controls *(requires user input)*
- **SEC07-BP03**: Automate Data Classification
- **SEC07-BP04**: Define Data Lifecycle Management *(requires user input)*
- **SEC08-BP01**: Implement Secure Key Management
- **SEC08-BP02**: Enforce Encryption at Rest
- **SEC08-BP03**: Automate Data at Rest Protection
- **SEC08-BP04**: Enforce Access Control for Data at Rest
- **SEC09-BP01**: Implement Secure Key and Certificate Management
- **SEC09-BP02**: Enforce Encryption in Transit
- **SEC09-BP03**: Authenticate Network Communications
- **SEC10-BP01**: Identify Key Personnel and External Resources *(requires user input)*
- **SEC10-BP02**: Develop Incident Management Plans *(requires user input)*
- **SEC10-BP03**: Prepare Forensic Capabilities *(requires user input)*
- **SEC10-BP04**: Develop and Test Security Incident Response Playbooks *(requires user input)*
- **SEC10-BP05**: Pre-provision Access *(requires 

user input)*
- **SEC10-BP06**: Pre-deploy Tools
- **SEC10-BP07**: Run Game Days *(requires user input)*
- **SEC10-BP08**: Establish a Framework for Learning from Incidents *(requires user input)*
- **SEC11-BP01**: Train for Application Security *(requires user input)*
- **SEC11-BP02**: Automate Testing Throughout the Development and Release Lifecycle
- **SEC11-BP03**: Perform Regular Penetration Testing *(requires user input)*
- **SEC11-BP04**: Perform Manual Code Reviews *(requires user input)*
- **SEC11-BP05**: Centralize Services for Packages and Dependencies
- **SEC11-BP06**: Deploy Software Programmatically
- **SEC11-BP07**: Regularly Assess Security Properties of the Deployment Pipeline
- **SEC11-BP08**: Build a Program that Embeds Security Ownership in Workload Teams *(requires user input)*

### 🛡️ Reliability
- **REL01-BP01**: Become Aware of Service Quotas and Constraints
- **REL01-BP02**: Manage Service Quotas Across Accounts and Regions
- **REL01-BP03**: Accommodate Fixed Service Quotas and Constraints
- **REL01-BP04**: Monitor and Manage Quotas
- **REL01-BP05**: Automate Quota Monitoring
- **REL01-BP06**: Ensure Sufficient Buffer for Quotas
- **REL02-BP01**: Ensure Highly Available Network Connectivity for Users
- **REL02-BP02**: Ensure Highly Available Network Connectivity Between Systems
- **REL02-BP03**: Ensure IP Subnet Allocation Accounts for Expansion and Availability
- **REL02-BP04**: Prefer Hub-and-Spoke Topologies over Many-to-Many Mesh
- **REL02-BP05**: Enforce Non-overlapping Private IP Address Ranges
- **REL03-BP01**: Choose How to Segment Your Workload *(requires user input)*
- **REL03-BP02**: Build Services Focused on Specific Business Domains *(requires user input)*
- **REL03-BP03**: Provide Service Contracts per API
- **REL04-BP01**: Identify Which Kind of Distributed System Failure to Protect Against *(requires user input)*
- **REL04-BP02**: Implement Loosely Coupled Dependencies
- **REL04-BP03**: Do Constant Work
- **REL04-BP04**: Make All Responses Idempotent
- **REL05-BP01**: Implement Graceful Degradation
- **REL05-BP02**: Throttle Requests
- **REL05-BP03**: Control and Limit Retry Calls
- **REL05-BP04**: Fail Fast and Limit Queues
- **REL05-BP05**: Set Client Timeouts
- **REL05-BP06**: Make Services Stateless Where Possible
- **REL05-BP07**: Implement Emergency Levers *(requires user input)*
- **REL06-BP01**: Monitor All Components for the Workload
- **REL06-BP02**: Define and Calculate Metrics
- **REL06-BP03**: Send Notifications Based on Monitoring
- **REL06-BP04**: Automate Responses to Events
- **REL07-BP01**: Use Auto Scaling or Other Scaling Policies
- **REL07-BP04**: Load Test Your Workload
- **REL08-BP01**: Use Runbooks for Standard Activities *(requires user input)*
- **REL08-BP03**: Integrate Resiliency Testing as Part of Your Deployment
- **REL08-BP04**: Deploy Using Immutable Infrastructure
- **REL08-BP05**: Deploy Changes with Automation
- **REL09-BP01**: Identify and Back Up All Data That Needs to Be Backed Up
- **REL09-BP02**: Secure and Encrypt Backups
- **REL09-BP03**: Perform Data Backup Automatically
- **REL09-BP04**: Perform Periodic Recovery of the Data to Verify Backup Integrity and Processes
- **REL10-BP01**: Deploy the Workload to Multiple Locations
- **REL10-BP02**: Select the Appropriate Locations for Your Multi-Location Deployment
- **REL10-BP03**: Use Bulkhead Architectures to Limit Scope of Impact
- **REL11-BP01**: Monitor All Components of the Workload to Detect Failures
- **REL11-BP02**: Fail Over to Healthy Resources
- **REL11-BP03**: Automate Healing on All Layers
- **REL11-BP04**: Rely on the Data Plane and Not the Control Plane During Recovery
- **REL11-BP05**: Use Static Stability to Prevent Bimodal Behavior
- **REL11-BP06**: Send Notifications When Events Impact Availability
- **REL11-BP07**: Architect Your Product to Meet Availability Targets and Uptime Service Level Agreements (SLAs)
- **REL12-BP01**: Use Playbooks to Investigate Failures
- **REL12-BP02**: Perform Post-Incident Analysis
- **REL12-BP03**: Test Functional Requirements and Include Resiliency Testing
- **REL12-BP04**: Use Chaos Engineering
- **REL12-BP05**: Conduct Game Days Regularly
- **REL13-BP01**: Define Recovery Objectives for Downtime and Data Loss
- **REL13-BP02**: Use Defined Recovery Strategies to Meet the Recovery Objectives
- **REL13-BP03**: Test Disaster Recovery Implementation to Validate the Implementation
- **REL13-BP04**: Manage Configuration Drift at the DR Site or Region
- **REL13-BP05**: Automate Recovery

### ⚡ Performance Efficiency
- **PERF01-BP01**: Learn About and Understand Available Cloud Services and Features *(requires user input)*
- **PERF01-BP02**: Use Guidance from Your Cloud Provider or an Appropriate Partner *(requires user input)*
- **PERF01-BP03**: Factor Cost Requirements into Decisions *(requires user input)*
- **PERF01-BP04**: Evaluate the Available Options and Trade-offs *(requires user input)*
- **PERF01-BP05**: Use Policies and Reference Architectures *(requires user input)*
- **PERF01-BP06**: Use Benchmarking to Drive Architectural Decisions
- **PERF01-BP07**: Use a Data-Driven Approach for Architectural Choices
- **PERF02-BP01**: Select the Best Compute Options for Your Workload
- **PERF02-BP02**: Understand the Available Compute Configuration and Features
- **PERF02-BP03**: Collect Compute-Related Metrics
- **PERF02-BP04**: Configure and Right-Size Compute Resources
- **PERF02-BP05**: Use Dynamic Scaling
- **PERF02-BP06**: Use Hardware-Based Compute Accelerators
- **PERF03-BP01**: Use Purpose-Built Data Stores
- **PERF03-BP02**: Evaluate Available Configuration Options
- **PERF03-BP03**: Collect and Record Performance Metrics
- **PERF03-BP04**: Implement Strategies to Improve Query Performance
- **PERF03-BP05**: Implement Data Access Patterns That Utilize Caching
- **PERF04-BP01**: Understand How Networking Impacts Performance
- **PERF04-BP02**: Evaluate Available Networking Features
- **PERF04-BP03**: Choose Appropriate Dedicated Connectivity or VPN
- **PERF04-BP04**: Use Load Balancing to Distribute Traffic
- **PERF04-BP05**: Choose Network Protocols to Improve Performance
- **PERF04-BP06**: Choose Your Workload's Location Based on Network Requirements
- **PERF04-BP07**: Optimize Network Configuration Based on Metrics
- **PERF05-BP01**: Establish Key Performance Indicators (KPIs) to Measure Workload Performance
- **PERF05-BP02**: Use Monitoring Solutions to Understand the Areas Where Performance Can Be Improved
- **PERF05-BP03**: Define a Process to Improve Workload Performance *(requires user input)*
- **PERF05-BP04**: Load Test Your Workload
- **PERF05-BP05**: Use Automation to Proactively Remediate Performance Issues
- **PERF05-BP06**: Keep Your Workload, the Underlying System, and All Service Components Up to Date *(requires user input)*
- **PERF05-BP07**: Review Metrics at Regular Intervals *(requires user input)*

### 💰 Cost Optimization
- **COST01-BP01**: Establish a Cloud Financial Management Function *(requires user input)*
- **COST01-BP02**: Establish a Partnership Between Finance and Technology *(requires user input)*
- **COST01-BP03**: Establish Cloud Budgets and Forecasts *(requires user input)*
- **COST01-BP04**: Implement Cost Awareness in Your Organizational Processes *(requires user input)*
- **COST01-BP05**: Report and Notify on Cost Optimization *(requires user input)*
- **COST01-BP06**: Monitor Cost Proactively
- **COST01-BP07**: Keep Up-to-Date with New Service Releases *(requires user input)*
- **COST01-BP08**: Create a Cost-Aware Culture *(requires user input)*
- **COST01-BP09**: Quantify Business Value from Cost Optimization *(requires user input)*
- **COST02-BP01**: Develop Policies Based on Your Organization Requirements *(requires user input)*
- **COST02-BP02**: Implement Goals and Targets *(requires user input)*
- **COST02-BP03**: Implement an Account Structure
- **COST02-BP04**: Implement Groups and Roles *(requires user input)*
- **COST02-BP05**: Implement Cost Controls
- **COST02-BP06**: Track Project Lifecycle *(requires user input)*
- **COST03-BP01**: Configure Detailed Information Sources
- **COST03-BP02**: Ident

ify Cost Attribution Categories *(requires user input)*
- **COST03-BP03**: Establish Organization Metrics *(requires user input)*
- **COST03-BP04**: Configure Billing and Cost Management Tools
- **COST03-BP05**: Add Organization Information to Cost and Usage
- **COST03-BP06**: Allocate Costs Based on Workload Metrics *(requires user input)*
- **COST04-BP01**: Track Resources Over Their Lifetime
- **COST04-BP02**: Implement a Decommissioning Process *(requires user input)*
- **COST04-BP03**: Decommission Resources
- **COST04-BP04**: Decommission Resources Automatically
- **COST04-BP05**: Enforce Data Retention Policies
- **COST05-BP01**: Perform Cost Analysis for Different Usage Over Time
- **COST05-BP02**: Select Service Components to Optimize Cost in Line with Organization Priorities *(requires user input)*
- **COST05-BP03**: Perform a Thorough Analysis of Each Component *(requires user input)*
- **COST05-BP04**: Select Software with Cost-Effective Licensing *(requires user input)*
- **COST05-BP05**: Select Services for This Workload to Optimize Cost *(requires user input)*
- **COST05-BP06**: Perform Cost Analysis for Different Usage Over Time *(requires user input)*
- **COST06-BP01**: Perform Cost Modeling *(requires user input)*
- **COST06-BP02**: Select Resource Type and Size Based on Data
- **COST06-BP03**: Select Resource Type and Size Based on Metrics
- **COST06-BP04**: Use Shared Resources *(requires user input)*
- **COST07-BP01**: Perform Pricing Model Analysis *(requires user input)*
- **COST07-BP02**: Choose Regions Based on Cost *(requires user input)*
- **COST07-BP03**: Select Third-Party Agreements with Cost-Efficient Terms *(requires user input)*
- **COST07-BP04**: Implement Pricing Models for All Components
- **COST07-BP05**: Perform Regular Analysis of Pricing Options *(requires user input)*
- **COST08-BP01**: Implement Data Transfer Cost Modeling
- **COST08-BP02**: Select Components to Optimize Data Transfer Costs
- **COST08-BP03**: Implement Services to Reduce Data Transfer Costs
- **COST09-BP01**: Perform Analysis on the Workload Demand *(requires user input)*
- **COST09-BP02**: Implement a Buffer or Throttle to Manage Demand
- **COST09-BP03**: Supply Resources Dynamically
- **COST10-BP01**: Develop a Workload Review Process *(requires user input)*
- **COST10-BP02**: Review and Analyze This Workload Regularly *(requires user input)*
- **COST11-BP01**: Perform Automation for Operations *(requires user input)*

### 🌱 Sustainability
- **SUS01-BP01**: Choose Region Based on Both Business Requirements and Sustainability Goals *(requires user input)*
- **SUS02-BP01**: Scale Infrastructure with User Load
- **SUS02-BP02**: Align SLA with Sustainability Goals *(requires user input)*
- **SUS02-BP03**: Stop the Creation and Maintenance of Unused Assets
- **SUS02-BP04**: Optimize Areas of Code That Consume the Most Time or Resources
- **SUS02-BP05**: Optimize Impact on Customer Devices and Equipment *(requires user input)*
- **SUS02-BP06**: Use Efficient Protocols and Minimize Data Transfer
- **SUS03-BP01**: Optimize Software and Architecture for Asynchronous and Scheduled Jobs
- **SUS03-BP02**: Remove or Refactor Workload Components with Low or No Use
- **SUS03-BP03**: Optimize Areas of Code That Consume the Most Time or Resources
- **SUS03-BP04**: Optimize Impact on Customer Devices and Equipment *(requires user input)*
- **SUS03-BP05**: Use Programming Languages and Frameworks That Support Sustainability Goals *(requires user input)*
- **SUS04-BP01**: Implement a Data Classification Policy *(requires user input)*
- **SUS04-BP02**: Use Technologies That Support Data Access and Storage Patterns
- **SUS04-BP03**: Use Lifecycle Policies to Delete Unnecessary Data
- **SUS04-BP04**: Minimize Data Movement Across Networks
- **SUS04-BP05**: Back Up Data Only When Difficult to Recreate *(requires user input)*
- **SUS04-BP06**: Use Shared File Systems or Object Storage to Access Common Data
- **SUS04-BP07**: Minimize Data Production *(requires user input)*
- **SUS04-BP08**: Use Compression and Deduplication
- **SUS05-BP01**: Use the Minimum Amount of Hardware to Meet Your Needs
- **SUS05-BP02**: Use Instance Types with the Least Impact
- **SUS05-BP03**: Use Managed Services
- **SUS05-BP04**: Optimize Your Use of Hardware-Based Compute Accelerators
- **SUS06-BP01**: Adopt Methods That Can Rapidly Introduce Sustainability Improvements *(requires user input)*
- **SUS06-BP02**: Keep Your Workload Up-to-Date
- **SUS06-BP03**: Increase Utilization of Build Environments
- **SUS06-BP04**: Use Managed Device Farms for Testing
- **SUS06-BP05**: Use Automation to Reduce the Environmental Impact of Development and Test

</details>

## ⚙️ Configuration

> [!TIP]
> While AWS credentials are not required for basic reviews, they can enhance analysis when available.

Set AWS credentials and region:

```bash
export AWS_REGION=us-east-1
export AWS_PROFILE=your-profile
```

<details>
<summary>🎯 Usage with Amazon Q CLI</summary>

```bash
# Basic review
q "Review my 3-tier web application architecture"

# Security-focused review
q "Perform Well-Architected security review of my EKS cluster"

# Get implementation help
q "How do I implement Infrastructure as Code (OPS01)?"
```

</details>

## 📄 License

Apache License 2.0 - see LICENSE file for details.

---

> [!NOTE]
> This MCP server is part of the AWS Labs MCP collection. For more AWS MCP servers, visit the [main repository](https://github.com/awslabs/mcp).