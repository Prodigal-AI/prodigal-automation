![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
[![License](https://img.shields.io/github/license/Nivesh03/package-twitter.svg)](LICENSE)
[![Twitter API](https://img.shields.io/badge/Twitter%20API-v2-1DA1F2.svg)](https://developer.twitter.com/en/docs/twitter-api)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# Prodigal-Automation

A Python project for automating social media interactions, starting with Twitter.

## Features

* **Modular Design:** Easily extendable to other social media platforms.
* **Twitter Automation:** Post tweets and fetch timelines.
* **Secure Credentials:** Uses `python-dotenv` for managing API keys.
* **Data Validation:** Leverages `pydantic` for robust data validation.
* **Command-Line Interface (CLI):** Interact with the automation tool directly from your terminal.
* **Poetry:** Modern dependency management and project packaging.

## Setup

1.  **Clone the repository:**
   Clone the [Prodigal-automation](https://github.com/Prodigal-AI/prodigal-automation.git) repo
    ```bash
    git clone https://github.com/Prodigal-AI/prodigal-automation.git
    cd prodigal-automation
    ```

2.  **Install Poetry (if you haven't already):**
    ```bash
    pip install poetry
    ```

3.  **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```

4.  **Configure environment variables:**
    Rename `.env.example` to `.env` and fill in your Twitter API credentials. You'll need to create a Twitter Developer account and an app to get these.

    ```
    # .env
    TWITTER_CONSUMER_KEY="your_consumer_key_here"
    TWITTER_CONSUMER_SECRET="your_consumer_secret_here"
    TWITTER_ACCESS_TOKEN="your_access_token_here"
    TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret_here"
    ```

## Usage

You can run the CLI commands using `poetry run sma` or, after `poetry install`, `sma`.

### Post a Tweet

```bash
poetry run sma post --content "Hello from my automated Twitter bot using Poetry and Tweepy! #PythonAutomation"