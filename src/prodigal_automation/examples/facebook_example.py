# src/prodigal_automation/examples/facebook_example.py

import os
import sys
import datetime
import time

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', 'src')))

from prodigal_automation.facebook import FacebookAutomation
from dotenv import load_dotenv
load_dotenv()

def main():
    """
    Example usage of Facebook Automation.
    """
    # Set your GEMINI_API_KEY as an environment variable
    # os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"

    # Set your FACEBOOK_ACCESS_TOKEN and FACEBOOK_PAGE_ID as environment variables
    # os.environ["FACEBOOK_ACCESS_TOKEN"] = "YOUR_FACEBOOK_PAGE_ACCESS_TOKEN"
    # os.environ["FACEBOOK_PAGE_ID"] = "YOUR_FACEBOOK_PAGE_ID"

    try:
        fb_automation = FacebookAutomation()
        fb_automation.run()
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    fb_automation = FacebookAutomation()
    fb_automation.run() # This handles basic text post

    print("\n--- Testing Image Post ---")
    image_topic = input("Enter topic for an image post: ")
    # In a real scenario, ContentGenerator might provide an image URL
    # For now, let's use a dummy URL or prompt the user for one
    image_url = input("Enter an image URL to post (e.g., https://example.com/image.jpg): ")
    if image_url:
        print("Generating image post content...")
        # You might want to get a separate caption for the image
        image_caption = fb_automation.content_generator.generate_simple_content(f"short caption for an image about {image_topic}")
        image_post_result = fb_automation.facebook_manager.post_image(image_caption, image_url)
        print(f"Image Post Result: {image_post_result}")
    else:
        print("Skipping image post.")

    print("\n--- Testing Video Post ---")
    video_topic = input("Enter topic for a video post: ")
    video_url = input("Enter a video URL to post (e.g., https://example.com/video.mp4): ")
    if video_url:
        print("Generating video post content...")
        video_caption = fb_automation.content_generator.generate_simple_content(f"short caption for a video about {video_topic}")
        video_post_result = fb_automation.facebook_manager.post_video(video_caption, video_url)
        print(f"Video Post Result: {video_post_result}")
    else:
        print("Skipping video post.")
        
    # Example of scheduling a post
    print("\n--- Testing Scheduled Post ---")
    schedule_choice = input("Do you want to schedule a post (yes/no)? ").lower()
    if schedule_choice == 'yes':
        future_time_str = input("Enter scheduling time (YYYY-MM-DD HH:MM:SS, e.g., 2025-06-25 10:00:00): ")
        try:
            dt_object = datetime.datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")
            # Ensure the scheduled time is in the future and within Facebook's limits (10 mins to 30 days)
            current_timestamp = int(time.time())
            scheduled_timestamp = int(dt_object.timestamp())

            if scheduled_timestamp < current_timestamp + 600: # 10 minutes
                print("Scheduled time must be at least 10 minutes in the future.")
            elif scheduled_timestamp > current_timestamp + (30 * 24 * 60 * 60): # 30 days
                print("Scheduled time cannot be more than 30 days in the future.")
            else:
                scheduled_post_topic = input("Enter topic for the scheduled post: ")
                scheduled_post_result = fb_automation.facebook_manager.create_post(scheduled_post_topic, scheduled_publish_time=scheduled_timestamp)
                print(f"Scheduled Post Result: {scheduled_post_result}")
        except ValueError as ve:
            print(f"Invalid date/time format or scheduling error: {ve}")
    else:
        print("Skipping scheduled post.")
        
    print("\n--- Testing Page Insights ---")
    insights_choice = input("Do you want to fetch page insights (yes/no)? ").lower()
    if insights_choice == 'yes':
        # Example metrics, refer to Facebook Graph API docs for full list
        metrics_to_fetch = ['page_impressions_unique', 'page_post_engagements']
        insights_result = fb_automation.facebook_manager.get_page_metrics(
            metrics=metrics_to_fetch,
            period='day',
            since=int((datetime.datetime.now() - datetime.timedelta(days=7)).timestamp()),
            until=int(datetime.datetime.now().timestamp())
        )
        print(f"Page Insights (last 7 days): {insights_result}")
    else:
        print("Skipping page insights.")

    print("\n--- Testing Post Insights (requires a post ID) ---")
    post_id_for_insights = input("Enter a Facebook Post ID to fetch insights (leave blank to skip): ")
    if post_id_for_insights:
        metrics_to_fetch = ['post_reactions_total', 'post_impressions']
        post_insights_result = fb_automation.facebook_manager.get_post_metrics(
            post_id=post_id_for_insights,
            metrics=metrics_to_fetch
        )
        print(f"Post Insights for {post_id_for_insights}: {post_insights_result}")
    else:
        print("Skipping post insights.")
        
if __name__ == "__main__":
    main()