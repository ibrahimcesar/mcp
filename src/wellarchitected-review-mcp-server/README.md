# AWS Well-Architected Review MCP Server

An MCP server that provides access to AWS Well-Architected Framework resources and tools for performing architecture reviews.

## Overview

This MCP server integrates with the AWS Well-Architected Framework to help you evaluate your architecture designs against AWS best practices across multiple pillars:

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability

## Features

The server provides the following functionality:

- **Access to Well-Architected pillars**: Get detailed information about each pillar, including principles and best practices.
- **Access to Well-Architected lenses**: Get information about specialized lenses for different workload types (serverless, machine learning, etc.).
- **Architecture reviews**: Submit your architecture for review against Well-Architected best practices.
- **Guidance**: Get specific guidance based on AWS services, pillars, or specific best practices.

## Tools

### GetWellArchitectedPillars

Get a list of all Well-Architected Framework pillars and their details.

### GetWellArchitectedLens

Get details about a specific Well-Architected lens, including which pillars it covers.

### ReviewArchitecture

Submit an architecture description for review against Well-Architected Framework best practices.

Parameters:
- `architecture_description`: Description of the architecture to review
- `services`: List of AWS services used in the architecture
- `lens` (optional): Well-Architected lens to apply (default: "well-architected")
- `pillars` (optional): List of specific pillars to focus on

### GetWellArchitectedGuidance

Get Well-Architected guidance for specific services, pillars, or best practices.

Parameters:
- `service` (optional): AWS service to get guidance for
- `pillar` (optional): Well-Architected pillar to get guidance for
- `practice_id` (optional): Specific best practice ID to get guidance for

At least one parameter must be provided.

## Resources

### wellarchitected://pillars/{pillar_name}

Get details for a specific Well-Architected pillar.

### wellarchitected://lens/{lens_name}

Get details for a specific Well-Architected lens.

### wellarchitected://best-practices/{practice_id}

Get details for a specific Well-Architected best practice.

## Installation

To install, run:

```bash
pip install awslabs.wellarchitected-review-mcp-server
```

## Usage

To start the server:

```bash
python -m awslabs.wellarchitected_review_mcp_server.server
```

Or use the entry point:

```bash
awslabs.wellarchitected-review-mcp-server
```

## Development

To set up a development environment:

```bash
# Clone the repository
git clone https://github.com/awslabs/mcp.git
cd mcp/src/wellarchitected-review-mcp-server

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
