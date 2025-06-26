# 🚀 Prodigal Automation

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Twitter API](https://img.shields.io/badge/Twitter%20API-v2-1DA1F2.svg)](https://developer.twitter.com/en/docs/twitter-api)
[![Facebook Graph API](https://img.shields.io/badge/Facebook%20Graph%20API-v19.0-blue.svg)](https://developers.facebook.com/docs/graph-api/)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-available-%23fbbc05.svg)](https://aistudio.google.com/app/apikey)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Primary repository for workflow automation and educational Twitter & Facebook API integration**

A comprehensive Python-based automation tool designed for educational purposes, enabling users to learn Twitter and Facebook API integration, data analysis, sentiment tracking, and automated content generation (using Google Gemini API) while adhering to platform policies.

---

## 📋 Table of Contents

- [🚀 Prodigal Automation](#-prodigal-automation)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [📁 Project Structure](#-project-structure)
  - [🔧 Prerequisites](#-prerequisites)
  - [📦 Installation Guide](#-installation-guide)
  - [🐦 Twitter API Setup](#-twitter-api-setup)
    - [Step 1: Create Your Twitter Developer Account](#step-1-create-your-twitter-developer-account)
    - [Step 2: Describe Your Use Case](#step-2-describe-your-use-case)
    - [Step 3: Create Your Twitter App](#step-3-create-your-twitter-app)
    - [Step 4: Configure Authentication](#step-4-configure-authentication)
    - [Step 5: Generate API Keys](#step-5-generate-api-keys)
  - [📘 Facebook Graph API Setup](#-facebook-graph-api-setup)
    - [Step 1: Create a Facebook Developer Account](#step-1-create-a-facebook-developer-account)
    - [Step 2: Create a Facebook App](#step-2-create-a-facebook-app)
    - [Step 3: Get a Page Access Token and Page ID](#step-3-get-a-page-access-token-and-page-id)
    - [Add Products](#add-products)
    - [Use Graph API Explorer](#use-graph-api-explorer)
    - [Store these:](#store-these)
  - [Required Permissions](#required-permissions)
    - [For posting content (text, image, video):](#for-posting-content-text-image-video)
    - [For fetching insights:](#for-fetching-insights)
  - [🔑 Gemini API Setup](#-gemini-api-setup)
    - [How to Get a Gemini API Key](#how-to-get-a-gemini-api-key)
- [🚀 Running Your First Example](#-running-your-first-example)
  - [1. Navigate to the Example Script](#1-navigate-to-the-example-script)
  - [2. Run the Example](#2-run-the-example)
  - [3. Enter Your Credentials at the Prompt](#3-enter-your-credentials-at-the-prompt)
    - [For `twitter_example.py`:](#for-twitter_examplepy)
    - [For `facebook_example.py`:](#for-facebook_examplepy)
  - [💡 Usage Details](#-usage-details)
  - [📄 Sample Code Usage (Twitter)](#-sample-code-usage-twitter)
  - [📄 Sample Code Usage (Facebook)](#-sample-code-usage-facebook)
  - [🧪 Running Tests](#-running-tests)
    - [Navigate to the project root directory:](#navigate-to-the-project-root-directory)
    - [Ensure development dependencies are installed:](#ensure-development-dependencies-are-installed)
    - [Run all tests:](#run-all-tests)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [👥 Contributors](#-contributors)
  - [📋 Changelog](#-changelog)

---

## ✨ Features

- 🐦 **Twitter API Integration** – Seamless connection with Twitter API v2
- 📘 **Facebook Graph API Integration** – Post text, images, videos, and retrieve insights
- 🤖 **Gemini API Integration** – Smart, AI-powered content generation with Google Gemini
- 📊 **Data Analysis** – Comprehensive tweet/post data collection and analysis
- 💭 **Sentiment Analysis** – Real-time sentiment tracking and monitoring
- 📈 **Trend Analysis** – Explore trending topics and user interactions
- 📅 **Post Scheduling** – Schedule content for future publication on Facebook
- 🔧 **Multi-tenant Support** – Handle multiple social media accounts
- 🛡️ **Security First** – Secure token management and authentication
- 📚 **Educational Focus** – Designed for learning and skill development

---

## 📁 Project Structure
```bash
prodigal-automation/
├── .github/              # ⚙️ GitHub-specific configuration (CI/CD)
│   └── workflows/        # 🤖 GitHub Actions workflows
│       └── ci.yml        # 🧪 CI pipeline definition
├── src/
│   └── prodigal_automation/
│       ├── examples/     # 💡 Example scripts (see below)
│       │   ├── twitter_example.py        # 🐦 Single-account Twitter automation
│       │   ├── twitter_multi_tenant.py   # 👥 Multi-account setup
│       │   └── facebook_example.py       # 📘 Facebook automation examples
│       ├── tool_modules/ # 🧩 Modular tool integrations (Twitter, LinkedIn, etc.)
│       ├── auth.py       # 🔐 Handles authentication
│       ├── client.py     # 🌐 API client interface for Twitter & Facebook
│       ├── facebook.py   # 📘 High-level Facebook automation logic
│       ├── facebook_manager.py # 🕹️ Facebook API interactions and content management
│       ├── oauth.py      # 🔄 OAuth flow handlers
│       ├── tools.py      # ✨ Content generation and validation
│       ├── twitter_manager.py # 🕹️ High-level Twitter logic
│       └── twitter.py    # 🛠️ Twitter utilities and helpers
├── tests/                # 🧪 Test suite (unit/integration tests)
│   ├── test_client.py    # Tests for client.py (including FacebookClient)
│   └── test_facebook_manager.py # Tests for facebook_manager.py
├── .gitignore            # 🚫 Files and folders to ignore in Git
├── CHANGELOG.md          # 📝 Project changelog/history
├── https://www.google.com/search?q=CODE_OF_CONDUCT.md    # 🤝 Contributor Code of Conduct
├── CONTRIBUTORS.md       # 👥 List of project contributors
├── https://www.google.com/search?q=CONTRIBUTING.md       # 🛤️ Contributing guidelines
├── https://www.google.com/search?q=LICENSE               # 📜 Project license (MIT)
├── pyproject.toml        # ⚙️ Python project metadata/config
├── README.md             # 📖 Project overview and instructions
├── requirements.txt      # 📦 Main dependencies
├── requirements_dev.txt  # 🧑‍💻 Dev/testing dependencies
└── TESTING.md            # 🧪 Testing instructions and details
```

---
## 🔧 Prerequisites

- **Python**: Version **3.12** (mandatory — create your venv with this version)
- **Git**: For cloning the repository
- **Twitter Developer Account**: [Apply here](https://developer.x.com/en/portal/petition/essential/basic-info)
- **Facebook Developer Account**: [Apply here](https://developers.facebook.com/)
- **Gemini API Key**: For AI-powered content generation (see below)

---

## 📦 Installation Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Prodigal-AI/prodigal-automation.git
   cd prodigal-automation
   ```

2. **Create a Python 3.12 Virtual Environment**

   > **IMPORTANT:** The virtual environment **must** use Python 3.12.  
   > If you have multiple Python versions, specify 3.12 when creating the venv.

   ```bash
   python3.12 -m venv prodigal_env
   source prodigal_env/bin/activate  # On Windows: prodigal_env\Scripts\activate
   ```

   To check the Python version in your venv:
   ```bash
   python --version
   # Should print: Python 3.12.x
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Copy the example `.env` file and edit it with your Twitter API credentials (instructions for getting these are below).  
   **Note:**  
   In addition to Twitter API keys, you should also add your **Gemini API key** in the `.env.example` file and your actual `.env`. This is required for Gemini-based features.

   ```bash
   cp src/prodigal_automation/examples/.env.example src/prodigal_automation/examples/.env
   # Edit src/prodigal_automation/examples/.env with your credentials
   # Add your Gemini API key as GEMINI_API_KEY=your_gemini_api_key
   ```

---

## 🐦 Twitter API Setup

### Step 1: Create Your Twitter Developer Account

- Go to the [Twitter Developer Portal](https://developer.x.com/en/portal/petition/essential/basic-info)
- Click **"Sign up for Free Account"**
- Accept the Developer Agreement & Policy

### Step 2: Describe Your Use Case

When prompted, paste this use-case description:

```
I plan to use the Twitter API strictly for educational purposes. My goal is to learn how to collect and analyze tweet data, perform sentiment analysis, explore trends, build small data science and NLP projects, and develop simple Twitter bots. This will help me gain hands-on experience in data analysis, machine learning, and API integration for academic and personal growth. I do not intend to use the data for commercial purposes or to violate Twitter's policies. The focus is on skill-building, research, and exploring real-time social media data to better understand user interactions, public sentiment, and event trends.
```

### Step 3: Create Your Twitter App

- Go to **Projects & Apps** → Select your project
- Click **Edit** and configure:
  - **App Name:** `Prodigal Automation Testing` (or your preferred name)
  - **Description:** `Educational use of Twitter API for data analysis, sentiment tracking, and building small NLP and bot projects to enhance programming and machine learning skills.`
- Click **Save**

### Step 4: Configure Authentication

- Go to **User Authentication Settings** → **Set up**
- Set permissions:
  - ✅ **Read and Write**
  - **Type:** `Web App, Automated App or Bot`
  - **Callback URI:** `https://www.prodigalai.com/`
  - **Website URL:** `https://www.prodigalai.com/`
- Click **Save** → **Yes**

### Step 5: Generate API Keys

- **Keys and Tokens** → **Consumer Keys** → **Regenerate**
- **Authentication Tokens** → **Bearer Token** → **Regenerate**
- **Access Token and Secret** → **Regenerate**

> **Store all credentials securely!**  
> You’ll need them for the next step.

---
## 📘 Facebook Graph API Setup

To enable Facebook automation, you'll need a Facebook Developer account, a Facebook App, and a Page Access Token with sufficient permissions for the Facebook Page you want to manage.

---

### Step 1: Create a Facebook Developer Account

- Go to the [Facebook for Developers Portal](https://developers.facebook.com/)
- If you don't have one, click **"Get Started"** to create a new developer account.
- You'll need to verify your account.

---

### Step 2: Create a Facebook App

- In the Facebook for Developers dashboard, click **"Create App"**.
- Choose the app type (e.g., **"Business"** or **"None"** if you're just experimenting for learning).
- Provide an App Name (e.g., _"Prodigal Automation App"_).
- Click **"Create App"**.

---

### Step 3: Get a Page Access Token and Page ID

This is the most critical part for posting to a Page.

### Add Products

- From your App Dashboard, under **"Add a Product"**, find **"Marketing API"** or **"Graph API"** and click **"Set Up"**.
- For simpler posting, you might not need the full Marketing API. Setting up a **"Basic Display"** or **"Business"** app and navigating to the **Graph API Explorer** is a common path.

### Use Graph API Explorer

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Select your newly created app from the **Application** dropdown.
3. Click **"Get Token"** → **"Get User Access Token"**.
4. Select the required permissions (see **Required Permissions** below). This gives you a **User Access Token**.
5. With the User Access Token selected, click **"Get Token"** again → **"Get Page Access Token"**.
6. Select the Facebook Page you manage and wish to post to. This will generate a **Page Access Token**.

**Important:**  
- Copy this **Page Access Token** — it’s usually long-lived.
- While in the Graph API Explorer, you can also find your **Facebook Page ID**:
  - Select the Page Access Token.
  - In the dropdown for objects, select your page name.
  - The ID will appear in the URL or response.

### Store these:

```env
FACEBOOK_ACCESS_TOKEN=your_page_access_token
FACEBOOK_PAGE_ID=your_page_id
```

---

## Required Permissions

### For posting content (text, image, video):

- `pages_show_list`
- `pages_read_engagement`
- `pages_manage_posts`
- `pages_manage_ads` *(sometimes needed for advanced scenarios)*

### For fetching insights:

- `read_insights`
- `pages_read_engagement`

> You need to select these permissions when generating your **User Access Token** in the **Graph API Explorer**, before exchanging it for a **Page Access Token**.
>
> ⚠️ Some permissions may require **App Review** for production use, but for development and learning, they’re typically accessible.

## 🔑 Gemini API Setup

**Gemini** is Google's new generative AI platform.  
You need a valid Gemini API key to enable automated content generation in this project.

### How to Get a Gemini API Key

1. **Go to the Google AI Studio**  
   [Google AI Studio](https://aistudio.google.com/app/apikey)

2. **Sign in with your Google account**  
   - Use a personal or educational Google account.

3. **Create a New API Key**
   - Click on **"Create API Key"**
   - Assign a name (e.g., "Prodigal Automation")
   - Click **Create**

4. **Copy Your API Key**
   - Once generated, click the copy button.

5. **Add Your API Key to the Project**
   - Open your `.env` file (see Installation Guide above)
   - Add the key:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     ```

6. **Keep Your Key Secure!**
   - **Never share or commit your API key** to public repositories.

> 📚 [More info about Gemini API](https://aistudio.google.com/app/apikey)
> 
---
# 🚀 Running Your First Example

Once you have your Twitter API credentials, Facebook API credentials, Gemini API key, and have set up your virtual environment with Python 3.12, follow these steps to run the sample script and automate content generation:

---

## 1. Navigate to the Example Script

- Go to: `src/prodigal_automation/examples/`
- Right-click on `twitter_example.py` or `facebook_example.py` and select **"Open in Integrated Terminal"** in your code editor (e.g., VS Code).

> **Note:**  
> You are running `*_example.py` — not `*.py` (e.g., `twitter.py` or `facebook.py`).

---

## 2. Run the Example

From the integrated terminal, run:

```bash
python twitter_example.py
# or for Facebook:
python facebook_example.py
```

---

## 3. Enter Your Credentials at the Prompt

The script will interactively prompt you for the necessary credentials.  
For **"Topic"**, enter a subject you'd like to generate content about (e.g., _AI and Machine Learning_).

### For `twitter_example.py`:

- Bearer Token  
- API Key  
- API Key Secret  
- Access Token  
- Access Token Secret  
- Gemini API Key  
- Topic (for content generation)  

### For `facebook_example.py`:

- Gemini API Key  
- Facebook Page Access Token  
- Facebook Page ID  
- Facebook App ID (optional)  
- Facebook App Secret (optional)  
- Facebook post topic (for content generation)  

Prompts for image/video URLs, scheduling, insights, or deletion are based on the script's interactive flow.

---

## 💡 Usage Details

- The scripts will automatically generate content up to platform-specific limits (e.g., Twitter's 280-character limit).
- The content is optimized for both brevity and quality using the Gemini API.
- You can modify or extend scripts in `src/prodigal_automation/examples/` for more advanced or multi-account use cases, including posting images/videos, scheduling posts, and retrieving insights on Facebook.

---

## 📄 Sample Code Usage (Twitter)

```python
from prodigal_automation.twitter_manager import TwitterManager
import os

# It's recommended to load credentials from environment variables or a .env file
# For example, using python-dotenv:
# from dotenv import load_dotenv
# load_dotenv()

manager = TwitterManager(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    api_key=os.getenv("TWITTER_API_KEY"),
    api_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    gemini_api_key=os.getenv("GEMINI_API_KEY")
)

result = manager.create_tweet(topic="AI and Machine Learning")
print(result)
```

---

## 📄 Sample Code Usage (Facebook)

```python
from prodigal_automation.facebook import FacebookAutomation
import os

# It's recommended to load credentials from environment variables or a .env file
# For example, using python-dotenv:
# from dotenv import load_dotenv
# load_dotenv()

# FacebookAutomation can initialize directly from environment variables
# if they are set (FACEBOOK_ACCESS_TOKEN, FACEBOOK_PAGE_ID, GEMINI_API_KEY)
fb_automation = FacebookAutomation()

# Example: Create a text post
post_result = fb_automation.facebook_manager.create_post(topic="Sustainable AI practices")
print(f"Text Post Result: {post_result}")

# Example: Post an image (requires an image URL)
image_url = "https://picsum.photos/1200/630"  # Replace with a real image URL
image_post_result = fb_automation.facebook_manager.post_image(
    message="Check out this beautiful image!",
    image_url=image_url
)
print(f"Image Post Result: {image_post_result}")

# Example: Schedule a post for 1 hour from now
import time
scheduled_time = int(time.time()) + 3600  # 1 hour from now
scheduled_post_result = fb_automation.facebook_manager.create_post(
    topic="The future of renewable energy",
    scheduled_publish_time=scheduled_time
)
print(f"Scheduled Post Result: {scheduled_post_result}")

# Example: Get Page Insights (requires read_insights permission)
insights_result = fb_automation.facebook_manager.get_page_metrics(
    metrics=['page_impressions_unique', 'page_post_engagements'],
    period='week'
)
print(f"Page Insights: {insights_result}")
```

---

## 🧪 Running Tests

To ensure the stability and correctness of the project, especially after making changes, it's highly recommended to run the test suite.

### Navigate to the project root directory:

```bash
cd prodigal-automation
```

### Ensure development dependencies are installed:

```bash
pip install -r requirements_dev.txt
```

### Run all tests:

```bash
poetry run pytest
```

> This command will discover and run all test files (e.g., `test_client.py`, `test_facebook_manager.py`) within the `tests/` directory.  
> You will see output indicating the number of tests run and whether they passed or failed.
---
## 🤝 Contributing

We welcome contributions from everyone!  
If you want to become a contributor, **please make sure to read and follow:**

- [CONTRIBUTORS.md](CONTRIBUTORS.md):  
  Meet the people behind this project and see how you can join the list!
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md):  
  **Strictly follow** our Code of Conduct to maintain a welcoming, respectful, and inclusive community.
- [CONTRIBUTING.md](CONTRIBUTING.md):  
  Step-by-step guide for setting up your development environment, submitting PRs, reporting issues, and all collaboration rules.

> **New members must strictly follow the guidelines and steps outlined in `CONTRIBUTING.md` and adhere to our `CODE_OF_CONDUCT.md` at all times.**

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👥 Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for the full list, or meet a few of our awesome contributors below!

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Pavansai20054">
        <img src="https://github.com/Pavansai20054.png" width="100px;" alt="RANGDAL PAVANSAI"/>
        <br />
        <sub><b>RANGDAL PAVANSAI</b></sub>
      </a>
      <br />
      <a href="mailto:psai49779@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/rangdal-pavansai">💼</a>
    </td>
    <td align="center">
      <a href="https://github.com/wagmare-sanjana">
        <img src="https://github.com/wagmare-sanjana.png" width="100px;" alt="WAGMARE SANJANA"/>
        <br />
        <sub><b>WAGMARE SANJANA</b></sub>
      </a>
      <br />
      <a href="mailto:wagmaresanjana5@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/wagmare-sanjana/">💼</a>
    </td>
    <td align="center">
      <a href="https://github.com/ankith">
        <img src="https://github.com/ankith.png" width="100px;" alt="Ankith"/>
        <br />
        <sub><b>Ankith</b></sub>
      </a>
      <br />
      <a href="mailto:ankith@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/ankith/">💼</a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/Ali-Beg/">
        <img src="https://github.com/Ali-Beg.png" width="100px;" alt="Ali Beg"/>
        <br />
        <sub><b>Ali Beg</b></sub>
      </a>
      <br />
      <a href="mailto:mbeg937@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/ali-beg">💼</a>
    </td>
    <td align="center">
      <a href="https://github.com/michael-rodriguez">
        <img src="https://github.com/michael-rodriguez.png" width="100px;" alt="Michael Rodriguez"/>
        <br />
        <sub><b>Raj mishra</b></sub>
      </a>
      <br />
      <a href="mailto:m.rodriguez.tech@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/michael-rodriguez-tech">💼</a>
    </td>
    <td align="center">
      <a href="https://github.com/priya-sharma">
        <img src="https://github.com/priya-sharma.png" width="100px;" alt="Priya Sharma"/>
        <br />
        <sub><b>Aditya</b></sub>
      </a>
      <br />
      <a href="mailto:priya.sharma.ai@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/priya-sharma-ai">💼</a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/david-kim">
        <img src="https://github.com/david-kim.png" width="100px;" alt="David Kim"/>
        <br />
        <sub><b>David Kim</b></sub>
      </a>
      <br />
      <a href="mailto:david.kim.ml@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/david-kim-ml">💼</a>
    </td>
    <td align="center">
      <a href="https://github.com/alexandra-petrov">
        <img src="https://github.com/alexandra-petrov.png" width="100px;" alt="Alexandra Petrov"/>
        <br />
        <sub><b>Alexandra Petrov</b></sub>
      </a>
      <br />
      <a href="mailto:alexandra.petrov.data@gmail.com">📧</a>
      <a href="https://www.linkedin.com/in/alexandra-petrov-data">💼</a>
    </td>
    <td align="center">
      <!-- Placeholder for future contributors -->
      <a href="#">
        <img src="https://via.placeholder.com/100x100?text=You%3F" width="100px;" alt="Future Contributor"/>
        <br />
        <sub><b>Your Name Here</b></sub>
      </a>
      <br />
      <a href="CONTRIBUTING.md">🤝 Join Us!</a>
    </td>
  </tr>
</table>

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and updates.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

[Report Bug](https://github.com/Prodigal-AI/prodigal-automation/issues) • [Request Feature](https://github.com/Prodigal-AI/prodigal-automation/issues) • [Documentation](https://github.com/Prodigal-AI/prodigal-automation/wiki)

</div>

---

<p align="center">
  <i>Built with ❤️ for educational purposes and the developer community</i>
</p>