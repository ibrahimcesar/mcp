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

The server evaluates 12+ core best practices across all pillars:

### 🔧 Operational Excellence
- **OPS01-BP01**: Evaluate External Customer Needs *(requires user input)*
- **OPS01-BP02**: Evaluate Internal Customer Needs *(requires user input)*
- **OPS01-BP03**: Evaluate Governance Requirements *(requires user input)*
- **OPS01-BP04**: Evaluate Compliance Requirements *(requires user input)*
- **OPS01-BP05**: Evaluate Threat Landscape *(requires user input)*
- **OPS01-BP06**: Evaluate Tradeoffs While Managing Benefits and Risks *(requires user input)*
- **OPS02-BP01**: Resources Have Identified Owners *(requires user input)*
- **OPS02-BP02**: Processes and Procedures Have Identified Owners *(requires user input)*
- **OPS02-BP03**: Operations Activities Have Identified Owners *(requires user input)*
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
- **OPS11-BP01**: Have a Process for Continuous Improvement *(requires user input)*
- **OPS11-BP02**: Perform Root Cause Analysis on Failures *(requires user input)*
- **OPS11-BP03**: Implement Feedback Loops *(requires user input)*
- **OPS11-BP04**: Perform Knowledge Management *(requires user input)*
- **OPS11-BP05**: Define Drivers for Improvement *(requires user input)*
- **OPS11-BP06**: Validate Insights *(requires user input)*
- **OPS11-BP07**: Perform Operations Metrics Reviews *(requires user input)*
- **OPS11-BP08**: Share Lessons Learned *(requires user input)*
- **OPS11-BP09**: Allocate Time to Make Improvements *(requires user input)*
- **OPS01**: Infrastructure as Code
- **OPS02**: Comprehensive Monitoring

### 🔒 Security
- **SEC01**: Strong Identity Foundation
- **SEC02**: Security at All Layers

### 🛡️ Reliability
- **REL01**: Design for Failure
- **REL02**: Auto Scaling

### ⚡ Performance Efficiency
- **PERF01**: Appropriate Instance Types
- **PERF02**: Caching Strategies

### 💰 Cost Optimization
- **COST01**: Cost Monitoring
- **COST02**: Reserved Instances/Savings Plans

### 🌱 Sustainability
- **SUS01**: Resource Utilization Optimization
- **SUS02**: Managed Services Usage

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