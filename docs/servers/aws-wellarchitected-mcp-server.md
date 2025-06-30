# AWS Well-Architected MCP Server

The AWS Well-Architected MCP Server provides comprehensive AWS Well-Architected Framework reviews, generates Architecture Decision Records (ADRs), and offers implementation guidance for improving your cloud architecture.

## Overview

This MCP server helps you:
- Perform systematic Well-Architected Framework reviews
- Generate detailed Architecture Decision Records (ADRs) for each best practice
- Assess risk levels and prioritize improvements
- Get specific implementation guidance and steps
- Validate documentation currency and completeness

## Installation

```bash
cd src/aws-wellarchitected-mcp-server
pip install -e .
```

## Configuration

The server requires no special AWS permissions for basic reviews, but can benefit from read access to analyze existing resources.

```bash
export AWS_REGION=us-east-1
export AWS_PROFILE=your-profile
```

## Available Tools

### `review`
Performs a comprehensive Well-Architected Framework review of your architecture.

**Parameters:**
- `context` (required): Description of the system/workload to review
- `pillars` (optional): List of specific pillars to review (default: all pillars)
- `documentation_paths` (optional): Paths to documentation files to analyze
- `output_directory` (optional): Directory to save ADR files (default: "./well-architected-adrs")

**Example:**
```python
await review(
    context="E-commerce platform with microservices architecture, using EKS, RDS, and ElastiCache",
    pillars=["SECURITY", "RELIABILITY", "COST_OPTIMIZATION"],
    documentation_paths=["./docs/architecture.md", "./README.md"],
    output_directory="./my-wa-review"
)
```

### `list_pillars`
Lists all AWS Well-Architected Framework pillars with descriptions.

**Example:**
```python
await list_pillars()
```

### `get_best_practices`
Retrieves best practices for a specific pillar or all pillars.

**Parameters:**
- `pillar` (optional): Specific pillar name to filter practices

**Example:**
```python
await get_best_practices(pillar="SECURITY")
```

### `ask_implementation_fix`
Provides detailed implementation guidance for a specific best practice.

**Parameters:**
- `best_practice_id` (required): ID of the best practice (e.g., 'OPS01', 'SEC01')
- `current_context` (required): Description of current implementation
- `preferred_approach` (optional): Preferred implementation approach

**Example:**
```python
await ask_implementation_fix(
    best_practice_id="SEC01",
    current_context="Currently using IAM users for application access",
    preferred_approach="Migrate to IAM roles with OIDC"
)
```

## Well-Architected Pillars

### 1. Operational Excellence
Focus on running and monitoring systems, and continually improving processes and procedures.

**Key Areas:**
- Infrastructure as Code
- Monitoring and Observability
- Automation and CI/CD
- Incident Response

### 2. Security
Protect data, systems, and assets while delivering business value through risk assessments and mitigation strategies.

**Key Areas:**
- Identity and Access Management
- Data Protection
- Infrastructure Protection
- Incident Response

### 3. Reliability
Ensure a workload performs its intended function correctly and consistently when expected.

**Key Areas:**
- Fault Tolerance
- Recovery Planning
- Scaling and Elasticity
- Change Management

### 4. Performance Efficiency
Use computing resources efficiently to meet system requirements and maintain efficiency as demand changes.

**Key Areas:**
- Resource Selection
- Monitoring and Analysis
- Performance Optimization
- Trade-off Analysis

### 5. Cost Optimization
Run systems to deliver business value at the lowest price point.

**Key Areas:**
- Cost-Effective Resources
- Matching Supply and Demand
- Expenditure Awareness
- Optimizing Over Time

### 6. Sustainability
Minimize environmental impacts of running cloud workloads.

**Key Areas:**
- Resource Efficiency
- Demand Management
- Software and Architecture
- Data Management

## Best Practices Covered

The server evaluates key best practices across all pillars:

| ID | Title | Pillar | Risk Level |
|----|-------|--------|------------|
| OPS01 | Infrastructure as Code | Operational Excellence | HIGH |
| OPS02 | Comprehensive Monitoring | Operational Excellence | HIGH |
| SEC01 | Strong Identity Foundation | Security | HIGH |
| SEC02 | Security at All Layers | Security | HIGH |
| REL01 | Design for Failure | Reliability | HIGH |
| REL02 | Auto Scaling | Reliability | MEDIUM |
| PERF01 | Appropriate Instance Types | Performance Efficiency | MEDIUM |
| PERF02 | Caching Strategies | Performance Efficiency | MEDIUM |
| COST01 | Cost Monitoring | Cost Optimization | MEDIUM |
| COST02 | Reserved Instances/Savings Plans | Cost Optimization | LOW |
| SUS01 | Resource Utilization | Sustainability | MEDIUM |
| SUS02 | Managed Services | Sustainability | LOW |

## Generated ADRs

The server generates comprehensive Architecture Decision Records (ADRs) for each best practice:

### ADR Structure
- **Context**: Problem statement and current situation
- **Decision**: Recommended architectural decision
- **Consequences**: Positive and negative outcomes
- **Trade-offs**: Benefits vs. costs analysis
- **Alternatives**: Other approaches considered
- **Implementation Notes**: Specific guidance and steps

### Example ADR Output
```markdown
# ADR: Implement Infrastructure as Code

**Date:** 2024-01-15
**Status:** Proposed
**Best Practice ID:** OPS01
**Pillar:** OPERATIONAL_EXCELLENCE
**Risk Level:** HIGH

## Context
Well-Architected Framework OPERATIONAL_EXCELLENCE pillar requires consistent and repeatable infrastructure provisioning...

## Decision
Implement Infrastructure as Code using AWS CloudFormation or CDK...

## Trade-offs
### Benefit
- Improved system reliability and maintainability
- Version-controlled infrastructure changes
- Reduced manual errors

### Cost
- Initial implementation effort
- Learning curve for team
- Ongoing maintenance overhead
```

## Risk Assessment

The server categorizes findings by risk level:

- 🔴 **HIGH RISK**: Critical issues requiring immediate attention
- 🟡 **MEDIUM RISK**: Important improvements to plan and implement  
- 🟢 **LOW RISK**: Nice-to-have optimizations

## Implementation Guidance

For each non-compliant best practice, the server provides:

1. **Specific Steps**: Detailed implementation steps
2. **Prerequisites**: Required setup and permissions
3. **Success Criteria**: How to validate implementation
4. **Monitoring**: Ongoing monitoring recommendations
5. **Effort Estimation**: Time and resource requirements

## Use Cases

### Architecture Review
Perform comprehensive reviews of existing architectures to identify improvement opportunities.

### Pre-Production Validation
Validate new architectures against Well-Architected principles before deployment.

### Compliance Documentation
Generate ADRs for compliance and audit purposes.

### Team Education
Use generated reports to educate teams on AWS best practices.

### Continuous Improvement
Regular reviews to maintain architectural excellence over time.

## Best Practices for Usage

1. **Provide Detailed Context**: Include comprehensive system descriptions for better analysis
2. **Include Documentation**: Reference existing documentation for completeness validation
3. **Focus Reviews**: Use pillar-specific reviews for targeted improvements
4. **Regular Reviews**: Perform reviews regularly as systems evolve
5. **Act on Findings**: Prioritize high-risk items for immediate attention

## Limitations

- Analysis is based on provided context and documentation
- Cannot directly inspect AWS resources (requires separate tooling)
- Recommendations are general and may need customization
- Best practices coverage focuses on core areas (not exhaustive)

## Integration Examples

### CI/CD Pipeline
```yaml
- name: Well-Architected Review
  run: |
    python -c "
    import asyncio
    from awslabs.aws_wellarchitected_mcp_server.server import review
    
    result = asyncio.run(review(
        context='${{ env.SYSTEM_DESCRIPTION }}',
        output_directory='./wa-review'
    ))
    print(f'Review completed: {result}')
    "
```

### Documentation Generation
Use the server to automatically generate architecture documentation and decision records as part of your documentation pipeline.

## Support

For issues and feature requests, please use the [GitHub Issues](https://github.com/awslabs/mcp/issues) page.