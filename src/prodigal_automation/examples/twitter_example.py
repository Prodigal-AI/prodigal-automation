# src/prodigal_automation/examples/twitter_example.py
#!/usr/bin/env python3

"""
Twitter Automation Example

Run with:
  python -m prodigal_automation.examples.twitter_example
"""

# src/prodigal_automation/examples/twitter_example.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to Python path
current_dir = Path(__file__).parent
src_dir = current_dir.parent.parent  # points to src/
sys.path.insert(0, str(src_dir))

try:
    from prodigal_automation.twitter import TwitterAutomation
except ImportError as e:
    print(f"Error: {e}")
    print("Try running with: python -m prodigal_automation.examples.twitter_example")
    sys.exit(1)

def main():
    env_path = current_dir / ".env.example"
    if env_path.exists():
        load_dotenv(env_path)
    
    automation = TwitterAutomation()
    automation.run()

if __name__ == "__main__":
    main()