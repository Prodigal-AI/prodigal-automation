# src/prodigal_automation/examples/facebook_example.py

import os
import sys


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
        
        
if __name__ == "__main__":
    main()