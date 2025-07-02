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

"""Security middleware for MCP server compliance."""

import time
from collections import defaultdict
from typing import Dict, Any
from loguru import logger

class SecurityMiddleware:
    """Security middleware for MCP server operations."""
    
    def __init__(self):
        self.request_counts = defaultdict(list)
        self.max_requests_per_minute = 60
        self.max_payload_size = 1024 * 1024  # 1MB
    
    def validate_request_size(self, payload: Dict[str, Any]) -> bool:
        """Validate request payload size."""
        payload_str = str(payload)
        if len(payload_str.encode('utf-8')) > self.max_payload_size:
            logger.warning(f"Request payload exceeds size limit: {len(payload_str)} bytes")
            return False
        return True
    
    def check_rate_limit(self, client_id: str = "default") -> bool:
        """Check if client is within rate limits."""
        now = time.time()
        minute_ago = now - 60
        
        # Clean old requests
        self.request_counts[client_id] = [
            req_time for req_time in self.request_counts[client_id]
            if req_time > minute_ago
        ]
        
        # Check current count
        if len(self.request_counts[client_id]) >= self.max_requests_per_minute:
            logger.warning(f"Rate limit exceeded for client: {client_id}")
            return False
        
        # Record this request
        self.request_counts[client_id].append(now)
        return True
    
    def log_security_event(self, event_type: str, details: Dict[str, Any]):
        """Log security-relevant events."""
        logger.info(f"Security Event: {event_type}", extra={"security_event": details})