# src/prodigal_automation/examples/twitter-multi-tenant.py

#!/usr/bin/env python3
import os
from prodigal_automation.tools.manager import call_tool
from prodigal_automation.twitter_manager import register_twitter_credentials

def main():
    # 1) Register this tenant’s credentials up front
    register_twitter_credentials(
        tenant_id="agent-123",
        bearer_token=os.getenv("AGENT_123_TWITTER_BEARER"),
    )

    jwt = os.getenv("AGENT_123_JWT")  # orchestrator‐issued JWT

    # 2) Fetch timeline
    timeline = call_tool(
        "twitter.get_timeline",
        tenant_id="agent-123",
        username="jack",
        max_results=3,
        token=jwt,
    )
    print("Twitter timeline:", timeline)

    # 3) Fetch LinkedIn profile (if you also registered a LINKEDIN token)
    profile = call_tool(
        "linkedin.get_profile",
        tenant_id="agent-123",
        member_urn="urn:li:person:ABCDEFG",
        token=jwt,
    )
    print("LinkedIn profile:", profile)

if __name__ == "__main__":
    main()
