import typer
from typing_extensions import Annotated
from prodigal_automation.twitter.twitter import TwitterAutomator
from prodigal_automation.facebook.facebook import FacebookAutomator 
from prodigal_automation.utils.tools import print_json
from prodigal_automation.core.errors import SocialMediaError

app = typer.Typer()

@app.command("twitter-post")
def twitter_post(
    content: Annotated[str, typer.Option(help="The content of the tweet to post.")]
):
    """
    Posts a new tweet to Twitter.
    """
    try:
        twitter_automator = TwitterAutomator()
        response = twitter_automator.post(content)
        typer.echo(f"Twitter post successful! ID: {response.id}")
        print_json(response)
    except SocialMediaError as e:
        typer.echo(f"Error posting to Twitter: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

@app.command("twitter-timeline")
def twitter_timeline(
    count: Annotated[int, typer.Option(help="Number of tweets to fetch.")] = 20
):
    """
    Fetches the user's home timeline from Twitter.
    """
    try:
        twitter_automator = TwitterAutomator()
        timeline = twitter_automator.get_timeline(count=count)
        typer.echo(f"Fetched {timeline.count} tweets from Twitter timeline:")
        print_json(timeline)
    except SocialMediaError as e:
        typer.echo(f"Error fetching Twitter timeline: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

@app.command("facebook-post")
def facebook_post(
    content: Annotated[str, typer.Option(help="The content of the post for Facebook.")]
):
    """
    Posts new content to Facebook.
    """
    try:
        facebook_automator = FacebookAutomator()
        response = facebook_automator.post(content)
        typer.echo(f"Facebook post successful! Post ID: {response.post_id}")
        print_json(response)
    except SocialMediaError as e:
        typer.echo(f"Error posting to Facebook: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

# @app.command("facebook-feed")
# def facebook_feed(
#     count: Annotated[int, typer.Option(help="Number of posts to fetch.")] = 25
# ):
#     """
#     Fetches the user's or page's feed from Facebook.
#     """
#     try:
#         facebook_automator = FacebookAutomator()
#         feed = facebook_automator.get_feed(count=count)
#         typer.echo(f"Fetched {len(feed)} posts from Facebook feed:")
#         print_json(feed)
#     except SocialMediaError as e:
#         typer.echo(f"Error fetching Facebook feed: {e}", err=True)
#         raise typer.Exit(code=1)
#     except Exception as e:
#         typer.echo(f"An unexpected error occurred: {e}", err=True)
#         raise typer.Exit(code=1)


@app.callback()
def main():
    """
    Social Media Automation Tool
    """
    pass

if __name__ == "__main__":
    app()