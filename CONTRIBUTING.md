# 🌟 Contributing to Prodigal-Automation

Welcome! 🎉 We're thrilled you're considering contributing to **Prodigal-Automation** – a modular, scalable tool for automating social media interactions. This guide will help you get started with development, understand the project structure, and walk you through how to add new features or fix bugs.

---

## 📚 Table of Contents

- [🌟 Contributing to Prodigal-Automation](#-contributing-to-prodigal-automation)
  - [📚 Table of Contents](#-table-of-contents)
  - [1. 🚀 Getting Started](#1--getting-started)
    - [📌 Fork and Clone](#-fork-and-clone)
    - [📦 Install Dependencies](#-install-dependencies)
    - [⚙️ Configure Environment Variables](#️-configure-environment-variables)
  - [2. 🧱 Project Structure](#2--project-structure)
  - [3. ➕ Adding a New Social Media Platform](#3--adding-a-new-social-media-platform)
    - [🛠 Steps:](#-steps)
  - [4. 🧑‍💻 General Contribution Guidelines](#4--general-contribution-guidelines)
    - [💡 Code Style](#-code-style)
    - [⚠️ Error Handling](#️-error-handling)
    - [✅ Testing](#-testing)
    - [🔀 Submitting a Pull Request](#-submitting-a-pull-request)
  - [5. 🐛 Reporting Issues](#5--reporting-issues)
  - [6. 🤝 Code of Conduct](#6--code-of-conduct)
  - [🙏 Thank You](#-thank-you)

---

## 1. 🚀 Getting Started

Before contributing, make sure to set up your development environment properly.

### 📌 Fork and Clone

1. Fork the repository via GitHub.  
2. Clone your forked repo:
   ```bash
   git clone https://github.com/your-username/prodigal-automation.git
   cd prodigal-automation
   ```

### 📦 Install Dependencies

We use [Poetry](https://python-poetry.org/) for dependency management:

```bash
pip install poetry
poetry install
```

### ⚙️ Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your API credentials:

    ```env
    TWITTER_CONSUMER_KEY="your_twitter_consumer_key"
    TWITTER_CONSUMER_SECRET="your_twitter_consumer_secret"
    TWITTER_ACCESS_TOKEN="your_twitter_access_token"
    TWITTER_ACCESS_TOKEN_SECRET="your_twitter_access_token_secret"

    FACEBOOK_ACCESS_TOKEN="your_facebook_access_token"
    FACEBOOK_PAGE_ID="your_facebook_page_id_optional"
    ```

    > 🚫 **Note**: Never commit your `.env` file to version control.

---

## 2. 🧱 Project Structure

The project follows a modular design for scalability and maintainability.

```
social-media-automator/
├── .env.example
├── poetry.lock
├── pyproject.toml
├── README.md
├── src/
│   ├── core/              # Core components: base classes, models, errors, authentication
│   ├── twitter/           # Twitter implementation
│   ├── facebook/          # Facebook implementation
│   ├── utils/             # Shared utility functions
│   └── cli.py             # Typer-based CLI
├── tests/                 # Unit & integration tests
└── .gitignore
```

---

## 3. ➕ Adding a New Social Media Platform

Adding a new platform (e.g., LinkedIn, Instagram) is straightforward thanks to the modular architecture.

### 🛠 Steps:

1. **Create a Platform Module**  
   Create a new directory under `src/` (e.g., `src/linkedin/`).

2. **Add Environment Variables**  
   Update `.env.example` and document new variables (e.g., `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`).

3. **Extend Authentication**  
   In `src/core/auth.py`, add a method like `get_linkedin_credentials()` that uses a Pydantic model (`LinkedInAuthCredentials`).

4. **Define Models**  
   In `src/core/models.py`, create:
   - `LinkedInAuthCredentials`
   - Any relevant response models (e.g., `LinkedInPostResponse`)

5. **Implement Platform Client**  
   Create `linkedin_client.py` with a `LinkedInClient` class inheriting from `BaseSocialMediaClient`.

6. **Build Manager Logic**  
   Create `linkedin_manager.py` with a `LinkedInManager` to handle business logic like:
   ```python
   def post_to_linkedin(post_data: Dict[str, Any]) -> LinkedInPostResponse:
   ```

7. **Create Platform Automator**  
   In `linkedin.py`, build a `LinkedInAutomator` to orchestrate the authentication, client, and manager layers.

8. **Integrate with CLI**  
   In `src/cli.py`:
   - Import the new automator.
   - Add CLI commands using `@app.command()` (e.g., `linkedin-post`, `linkedin-profile`).

9. **Update Dependencies**  
   Add the SDK to `pyproject.toml`, e.g.:
   ```toml
   linkedin-api = "^1.0.0"
   ```

10. **Write Tests**  
    Add a file `test_linkedin.py` and use `unittest.mock` for API simulations.

---

## 4. 🧑‍💻 General Contribution Guidelines

### 💡 Code Style

- Follow **PEP 8** standards.
- Use **type hints** everywhere.
- Include **docstrings** for all modules, classes, and methods.
- Write **readable** code with meaningful variable names.

### ⚠️ Error Handling

- Use custom exceptions from `src/core/errors.py`.

### ✅ Testing

- Write unit tests for all new features or bug fixes.
- Run all tests before submitting:
  ```bash
  poetry run pytest tests/
  ```
- Aim for high test coverage.

### 🔀 Submitting a Pull Request

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   or
   ```bash
   git checkout -b bugfix/your-bug-fix-name
   ```

2. **Make your changes**, adhering to the coding standards.

3. **Commit clearly**:
   ```bash
   git commit -m "feat: Add LinkedIn integration for posting"
   ```

4. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**:
   - Use a clear title and detailed description.
   - Reference related issues if applicable.

---

## 5. 🐛 Reporting Issues

Have a bug or feature idea? Open an issue on [GitHub Issues](https://github.com/Prodigal-AI/prodigal-automation/issues).

- **For bugs**, include:
  - Steps to reproduce
  - Expected vs actual behavior
  - Error messages or logs

- **For features**, include:
  - What you want to see
  - Why it’s useful
  - Ideas for implementation (if any)

---

## 6. 🤝 Code of Conduct

We follow a [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating, you’re expected to uphold these values in all project spaces.

> 💬 Be respectful.  
> 👐 Be inclusive.  
> 🧠 Be thoughtful.

---

## 🙏 Thank You

Your contributions make **Prodigal-Automation** better for everyone. Whether it's a bug fix, new feature, or suggestion — we appreciate your help! 💙