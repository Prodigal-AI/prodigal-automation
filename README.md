# 🚀 Prodigal Automation

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Twitter API](https://img.shields.io/badge/Twitter%20API-v2-1DA1F2.svg)](https://developer.twitter.com/en/docs/twitter-api)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-available-%23fbbc05.svg)](https://aistudio.google.com/app/apikey)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Primary repository for workflow automation and educational Twitter API integration**

A comprehensive Python-based automation tool designed for educational purposes, enabling users to learn Twitter API integration, data analysis, sentiment tracking, and automated content generation (using Google Gemini API) while adhering to platform policies.

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
  - [🔑 Gemini API Setup](#-gemini-api-setup)
    - [How to Get a Gemini API Key](#how-to-get-a-gemini-api-key)
  - [🚀 Running Your First Example](#-running-your-first-example)
    - [1. **Navigate to the Example Script**](#1-navigate-to-the-example-script)
    - [2. **Run the Example**](#2-run-the-example)
    - [3. **Enter Your Credentials at the Prompt**](#3-enter-your-credentials-at-the-prompt)
  - [💡 Usage Details](#-usage-details)
    - [**Sample Code Usage**](#sample-code-usage)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [👥 Contributors](#-contributors)
  - [📋 Changelog](#-changelog)

---

## ✨ Features

- 🐦 **Twitter API Integration** – Seamless connection with Twitter API v2
- 🤖 **Gemini API Integration** – Smart, AI-powered content generation with Google Gemini
- 📊 **Data Analysis** – Comprehensive tweet data collection and analysis
- 💭 **Sentiment Analysis** – Real-time sentiment tracking and monitoring
- 📈 **Trend Analysis** – Explore trending topics and user interactions
- 🔧 **Multi-tenant Support** – Handle multiple Twitter accounts
- 🛡️ **Security First** – Secure token management and authentication
- 📚 **Educational Focus** – Designed for learning and skill development

---

## 📁 Project Structure

```
prodigal-automation/
├── .github/                    # ⚙️ GitHub-specific configuration (CI/CD)
│   └── workflows/              # 🤖 GitHub Actions workflows
│       └── ci.yml              # 🧪 CI pipeline definition
├── src/
│   └── prodigal_automation/
│       ├── examples/           # 💡 Example scripts (see below)
│       │   ├── twitter_example.py        # 🐦 Single-account Twitter automation
│       │   └── twitter_multi_tenant.py   # 👥 Multi-account setup
│       ├── tool_modules/       # 🧩 Modular tool integrations (Twitter, LinkedIn, etc.)
│       ├── auth.py             # 🔐 Handles authentication
│       ├── client.py           # 🌐 API client interface
│       ├── oauth.py            # 🔄 OAuth flow handlers
│       ├── tools.py            # ✨ Content generation and validation
│       ├── twitter_manager.py  # 🕹️ High-level Twitter logic
│       └── twitter.py          # 🛠️ Twitter utilities and helpers
├── tests/                      # 🧪 Test suite (unit/integration tests)
├── .gitignore                  # 🚫 Files and folders to ignore in Git
├── CHANGELOG.md                # 📝 Project changelog/history
├── CODE_OF_CONDUCT.md          # 🤝 Contributor Code of Conduct
├── CONTRIBUTORS.md             # 👥 List of project contributors
├── CONTRIBUTING.md             # 🛤️ Contributing guidelines
├── LICENSE                     # 📜 Project license (MIT)
├── pyproject.toml              # ⚙️ Python project metadata/config
├── README.md                   # 📖 Project overview and instructions
├── requirements.txt            # 📦 Main dependencies
├── requirements_dev.txt        # 🧑‍💻 Dev/testing dependencies
└── TESTING.md                  # 🧪 Testing instructions and details
```

---
## 🔧 Prerequisites

- **Python**: Version **3.12** (mandatory — create your venv with this version)
- **Git**: For cloning the repository
- **Twitter Developer Account**: [Apply here](https://developer.x.com/en/portal/petition/essential/basic-info)
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

---

## 🚀 Running Your First Example

Once you have your Twitter API credentials, Gemini API key, and have set up your virtual environment with Python 3.12, follow these steps to run the sample script and automate your first tweet generation:

### 1. **Navigate to the Example Script**

- Go to:  
  `src/prodigal_automation/examples/`
- **Right-click** on `twitter_example.py` and select **"Open in Integrated Terminal"** in your code editor (e.g., VS Code).

  > **Note:**  
  > You are running `twitter_example.py` — **not** `twitter.py`.

### 2. **Run the Example**

From the integrated terminal, run:

```bash
python twitter_example.py
```

### 3. **Enter Your Credentials at the Prompt**

The script will interactively prompt you for the following, in order:

1. **Bearer Token**
2. **API Key**
3. **API Key Secret**
4. **Access Token**
5. **Access Token Secret**
6. **Gemini API Key**
7. **Topic** (for content generation)

Enter each credential as prompted. For "Topic", enter a subject you'd like to generate a tweet about (e.g., `AI and Machine Learning`).

---

## 💡 Usage Details

- The script will automatically generate tweet content up to Twitter's 280-character limit.
- The content is optimized for both brevity and quality using the Gemini API.
- You can modify or extend scripts in `src/prodigal_automation/examples/` for more advanced or multi-account use cases.

### **Sample Code Usage**

```python
from twitter_manager import TwitterManager

manager = TwitterManager(
    bearer_token="your_bearer_token",
    api_key="your_api_key",
    api_secret="your_api_secret",
    access_token="your_access_token",
    access_token_secret="your_access_token_secret",
    gemini_api_key="your_gemini_api_key"
)

result = manager.create_tweet(topic="AI and Machine Learning")
print(result)
```

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