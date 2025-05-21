#!/usr/bin/env python3
"""
Run with:

  python -m prodigal_automation.examples.twitter_example

Make sure TWITTER_BEARER_TOKEN is exported in your shell.
"""

from prodigal_automation.tools import call_tool

def main():
    # 1) Fetch last 3 tweets by @jack
    timeline = call_tool("twitter_get_user_timeline", username="jack", max_results=3)
    print("Timeline:", timeline)

    # 2) If there’s at least one tweet, fetch it by ID
    if timeline:
        tid = timeline[0].id
        tweet = call_tool("twitter_get_tweet", tweet_id=tid)
        print("Single tweet:", tweet)

if __name__ == "__main__":
    main()
