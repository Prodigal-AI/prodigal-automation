import typer
from typing_extensions import Annotated
from prodigal_automation.twitter.twitter import TwitterAutomator
from prodigal_automation.utils.tools import print_json
from prodigal_automation.core.errors import SocialMediaError

app = typer.Typer()

@app.command()
def post(
    content: Annotated[str, typer.Option(help="The content of the tweet to post.")]
):
    """
    Posts a new tweet to Twitter.
    """
    try:
        twitter_automator = TwitterAutomator()
        response = twitter_automator.post(content)
        typer.echo(f"Tweet posted successfully! ID: {response.id}")
        print_json(response)
    except SocialMediaError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

@app.command("timeline")
def get_timeline(
    count: Annotated[int, typer.Option(help="Number of tweets to fetch.")] = 20
):
    """
    Fetches the user's home timeline from Twitter.
    """
    try:
        twitter_automator = TwitterAutomator()
        timeline = twitter_automator.get_timeline(count=count)
        typer.echo(f"Fetched {timeline.count} tweets from timeline:")
        print_json(timeline)
    except SocialMediaError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"An unexpected error occurred: {e}", err=True)
        raise typer.Exit(code=1)

@app.callback()
def main():
    """
    Social Media Automation Tool
    """
    pass

if __name__ == "__main__":
    app()