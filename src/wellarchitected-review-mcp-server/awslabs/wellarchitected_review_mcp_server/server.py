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

"""AWS Well-Architected Review MCP server implementation."""

import logging
from awslabs.wellarchitected_review_mcp_server.core import resources, tools
from mcp.server.fastmcp import FastMCP


# Set up logging
logger = logging.getLogger(__name__)

# Create MCP server
mcp = FastMCP(
    'AWS Well-Architected Review MCP Server',
    dependencies=[
        'pydantic',
        'boto3',
        'httpx',
    ],
)


# Register resources
mcp.resource('wellarchitected://pillars/{pillar_name}')(resources.get_pillar_details)
mcp.resource('wellarchitected://lens/{lens_name}')(resources.get_lens_details)
mcp.resource('wellarchitected://best-practices/{practice_id}')(resources.get_best_practice)


# Register tools
mcp.tool(name='GetWellArchitectedPillars')(tools.get_wellarchitected_pillars)
mcp.tool(name='GetWellArchitectedLens')(tools.get_wellarchitected_lens)
mcp.tool(name='ReviewArchitecture')(tools.review_architecture)
mcp.tool(name='GetWellArchitectedGuidance')(tools.get_wellarchitected_guidance)


def main():
    """Run the MCP server with CLI argument support."""
    mcp.run()


if __name__ == '__main__':
    main()
