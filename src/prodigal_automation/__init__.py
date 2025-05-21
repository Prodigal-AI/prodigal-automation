# src/prodigal_automation/__init__.py

__version__ = "0.1.1"

# re-export the core functions
from .tools import register_tool, call_tool
# import your OAuth, client, twitter, etc. so that they register their tools on import
import prodigal_automation.twitter    # noqa: F401
