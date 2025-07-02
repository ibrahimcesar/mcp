# AWS Well-Architected Framework Rules

## Context
This project implements an MCP server for AWS Well-Architected Framework reviews and analysis.

## Code Standards
- Follow AWS Well-Architected best practices in all implementations
- Use type hints for all function parameters and return values
- Include comprehensive docstrings for all public functions
- Handle errors gracefully with appropriate logging

## Architecture Principles
- Implement the six Well-Architected pillars: 🔧 Operational Excellence, 🔒 Security, 🛡️ Reliability, ⚡ Performance Efficiency, 💰 Cost Optimization, 🌱 Sustainability
- Use SMART criteria for all solution recommendations
- Prioritize simple over complex solutions
- Ensure all solutions are two-way door (reversible) when possible

## Display Standards
- Always use emojis for risk levels: 🔴 HIGH, 🟡 MEDIUM, 🟢 LOW
- Always use emojis for pillars: 🔧 Operational Excellence, 🔒 Security, 🛡️ Reliability, ⚡ Performance Efficiency, 💰 Cost Optimization, 🌱 Sustainability
- Include risk level emojis in all user-facing outputs and responses
- Include pillar emojis when referencing specific pillars

## MCP Server Guidelines
- All tools should return structured JSON responses
- Include comprehensive error handling
- Provide clear descriptions for all tool parameters
- Follow FastMCP patterns and conventions

## Testing Requirements
- Test all MCP tools before deployment
- Validate JSON schema compliance
- Ensure proper error handling for invalid inputs
- Test with various pillar combinations