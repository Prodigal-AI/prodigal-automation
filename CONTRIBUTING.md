# 🤖✨ Contributing to Twitter Automation Project

Thank you for your interest in contributing to our **Twitter Automation** project! 🚀  
We welcome contributions from developers of all skill levels.  
This comprehensive guide will help you get started and ensure a smooth contribution process.

---

## 📋 Table of Contents

- [🤖✨ Contributing to Twitter Automation Project](#-contributing-to-twitter-automation-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [🤝 Code of Conduct](#-code-of-conduct)
    - [🌈 Our Standards](#-our-standards)
  - [🚀 Getting Started](#-getting-started)
    - [🧰 Prerequisites](#-prerequisites)
    - [⚡ Quick Start](#-quick-start)
    - [🌿 Branching and Forking Guide](#-branching-and-forking-guide)
      - [🍴 Forking the Repository](#-forking-the-repository)
      - [🌿 Creating and Using the `updates` Branch](#-creating-and-using-the-updates-branch)
  - [🛠️ Development Environment Setup](#️-development-environment-setup)
    - [🧪 Virtual Environment](#-virtual-environment)
    - [📦 Install Dependencies](#-install-dependencies)
    - [⚙️ Environment Configuration](#️-environment-configuration)
  - [📁 Project Structure](#-project-structure)
  - [🔄 Development Workflow](#-development-workflow)
  - [🧪 Testing Guidelines](#-testing-guidelines)
    - [🧬 Test Structure](#-test-structure)
    - [🖊️ Writing Tests](#️-writing-tests)
    - [📈 Test Coverage](#-test-coverage)
    - [🧪 Testing \& Linting Process](#-testing--linting-process)
      - [1. **Run Unit and Integration Tests**](#1-run-unit-and-integration-tests)
      - [2. **Check Code Formatting**](#2-check-code-formatting)
      - [3. **Lint the Codebase**](#3-lint-the-codebase)
      - [4. **Check Type Annotations**](#4-check-type-annotations)
      - [5. **(Optional) Run Example Scripts**](#5-optional-run-example-scripts)
  - [🔄 Pull Request Process](#-pull-request-process)
    - [📝 Before Submitting](#-before-submitting)
    - [🏷️ PR Title Format](#️-pr-title-format)
    - [📋 PR Description Template](#-pr-description-template)
    - [👀 Review Process](#-review-process)
  - [🐛 Issue Reporting](#-issue-reporting)
    - [🐞 Bug Reports](#-bug-reports)
    - [🌠 Feature Requests](#-feature-requests)
  - [🔒 Security Guidelines](#-security-guidelines)
    - [🐦 Twitter API Security](#-twitter-api-security)
    - [🛡️ Secure Coding Practices](#️-secure-coding-practices)
    - [🕵️ Reporting Security Issues](#️-reporting-security-issues)
  - [📖 Documentation](#-documentation)
    - [✍️ Docstring Format](#️-docstring-format)
    - [📝 README Updates](#-readme-updates)
  - [🌟 Community and Support](#-community-and-support)
    - [🆘 Getting Help](#-getting-help)
    - [🏅 Recognition](#-recognition)
  - [📋 Commit Message Format](#-commit-message-format)
    - [🏷️ Types](#️-types)
    - [💡 Examples](#-examples)
  - [🚀 Release Process](#-release-process)
  - [🙏 Thank You](#-thank-you)

---

## 🤝 Code of Conduct

We are committed to providing a **welcoming and inspiring community** for all.  
Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a respectful and collaborative environment for everyone.

### 🌈 Our Standards

- 🫶 **Be respectful**: Treat everyone with respect and kindness  
- 🤗 **Be inclusive**: Welcome newcomers and help them get started  
- 💡 **Be constructive**: Provide helpful feedback and suggestions  
- 🕰️ **Be patient**: Remember that we all have different experience levels  

---

## 🚀 Getting Started

### 🧰 Prerequisites

Before you begin, ensure you have the following installed:

- 🐍 **Python 3.8+** (Python 3.9+ recommended)
- 🌀 **Git** for version control
- 📦 **pip** for package management
- 🐦 A **Twitter Developer Account** (for API access)
- 🔑 **Gemini API Key** (for AI-powered content generation — [Get yours here](https://aistudio.google.com/app/apikey))

### ⚡ Quick Start

1. **Fork the repository** on GitHub  
2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/yourusername/twitter-automation.git
   cd twitter-automation
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/Prodigal-AI/prodigal-automation.git
   ```

---

### 🌿 Branching and Forking Guide

Proper branching and forking practices help us keep the project organized, review changes efficiently, and maintain a high-quality codebase. Here’s how you can contribute **the right way**:

#### 🍴 Forking the Repository

- Go to the GitHub page of this project.
- Click the **Fork** button (top right) to create your own copy of the repository.
- Work will be done on your fork, and then changes proposed to the main repo via a Pull Request (PR).

#### 🌿 Creating and Using the `updates` Branch

> **🚨 Important:**  
> **All new features, bug fixes, or updates MUST be submitted to the `updates` branch, NOT directly to `main`.**
>
> This helps us test and review changes before merging them into the production code.

**Why?**
- `main` branch = stable release  
- `updates` branch = new work in progress

**How to do this:**

1. **Sync your fork with the main repository:**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Check out the `updates` branch (create it if it doesn’t exist):**
   ```bash
   # If you don’t have 'updates' locally, create and track it:
   git checkout -b updates upstream/updates
   # Or, if you already have it:
   git checkout updates
   git pull upstream updates
   ```

3. **Create your own feature branch off `updates`:**
   ```bash
   git checkout updates
   git pull
   git checkout -b feature/your-feature-name
   # or for bug fixes
   git checkout -b fix/issue-number-description
   ```

4. **Make your changes on your feature branch.**

5. **Push your changes to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request:**
   - **Base branch:** `updates` (not `main`!)
   - **Compare branch:** `feature/your-feature-name` from your fork

**🔔 Summary Table**

| Purpose              | Branch      |
|----------------------|-------------|
| Stable Release       | `main`      |
| New Updates/Features | `updates`   |
| Your Work            | `feature/your-feature-name` or `fix/issue-description` (branched from `updates`) |

---

## 🛠️ Development Environment Setup

### 🧪 Virtual Environment

We strongly recommend using a virtual environment to avoid dependency conflicts:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/MacOS:
source venv/bin/activate

# Verify activation (you should see (venv) in your prompt)
which python  # Should point to your venv directory
```

### 📦 Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (MANDATORY for contributors)
pip install -r requirements_dev.txt

# Or install in development mode
pip install -e .
```

### ⚙️ Environment Configuration

1. **Copy the environment template**:
   ```bash
   cp .env.example .env
   ```
2. **Configure your environment variables**:
   ```bash
   # Twitter API Credentials
   TWITTER_API_KEY=your_api_key_here
   TWITTER_API_SECRET=your_api_secret_here
   TWITTER_ACCESS_TOKEN=your_access_token_here
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here

   # Gemini API Key (required for content generation)
   GEMINI_API_KEY=your_gemini_api_key_here

   # Application Settings
   DEBUG=True
   LOG_LEVEL=INFO
   ```
3. **Verify your setup**:
   ```bash
   python -c "import twitter_automation; print('✅ Setup successful!')"
   ```

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

## 🔄 Development Workflow

Before you begin any coding or feature work, **please follow these steps:**

1. **Check the CHANGELOG.md**  
   - Review recent updates and ongoing work to avoid duplicating existing or in-progress features/bugfixes.

2. **Install development dependencies**
   - Development and testing modules are required for contributions.  
   - Run:
     ```bash
     pip install -r requirements_dev.txt
     ```

3. **Create a Feature Branch**

   ```bash
   # Sync with upstream
   git fetch upstream
   git checkout updates
   git merge upstream/updates

   # Create a new branch from updates
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number-description
   ```

4. **Make Your Changes**
   - Write clean, readable code following our [coding standards](#-coding-standards)
   - Add tests for new functionality
   - Update documentation as needed
   - Follow the [conventional commit](#-commit-message-format) format

5. **Test Your Changes**

   ```bash
   # Run all tests
   python -m pytest

   # Run tests with coverage
   python -m pytest --cov=twitter_automation

   # Run specific test file
   python -m pytest tests/test_specific_module.py

   # Run linting
   flake8 src/ tests/
   black --check src/ tests/
   mypy src/
   ```

---

## 🧪 Testing Guidelines

### 🧬 Test Structure

- 💡 **Unit tests**: Test individual functions and classes in isolation
- 🔗 **Integration tests**: Test component interactions
- 🏃 **End-to-end tests**: Test complete workflows

### 🖊️ Writing Tests

```python
import pytest
from unittest.mock import Mock, patch

from twitter_automation.scheduler import TweetScheduler
from twitter_automation.exceptions import TwitterAPIError

class TestTweetScheduler:
    """Test suite for TweetScheduler class."""
    
    @pytest.fixture
    def mock_client(self):
        """Create a mock Twitter client."""
        return Mock()
    
    @pytest.fixture
    def scheduler(self, mock_client):
        """Create a TweetScheduler instance with mock client."""
        return TweetScheduler(mock_client)
    
    def test_schedule_tweet_success(self, scheduler, mock_client):
        """Test successful tweet scheduling."""
        content = "Test tweet content"
        mock_client.post_tweet.return_value = {"id": "123", "text": content}
        
        result = scheduler.schedule_tweet(content)
        
        assert result.id == "123"
        assert result.text == content
        mock_client.post_tweet.assert_called_once_with(content)
    
    def test_schedule_tweet_content_too_long(self, scheduler):
        """Test tweet content length validation."""
        long_content = "x" * 281
        
        with pytest.raises(ValueError, match="exceeds 280 character limit"):
            scheduler.schedule_tweet(long_content)
```

### 📈 Test Coverage

Maintain high test coverage (aim for **>90%**):

```bash
# Generate coverage report
python -m pytest --cov=twitter_automation --cov-report=html

# View coverage report
open htmlcov/index.html
```

---

### 🧪 Testing & Linting Process

For consistent and reliable code quality, **every PR must pass the following checks** before merging:

#### 1. **Run Unit and Integration Tests**
```bash
python -m pytest
```

#### 2. **Check Code Formatting**
```bash
black --check .
isort .
```

#### 3. **Lint the Codebase**
```bash
flake8 .
```

#### 4. **Check Type Annotations**
```bash
mypy src/
```

#### 5. **(Optional) Run Example Scripts**
You can test end-to-end tweet posting with an example script:
```bash
# Make sure your environment variables are set!
poetry run python src/prodigal_automation/examples/twitter_example.py
```
- 📝 This will prompt you for your Twitter credentials (unless set via environment variables).
- 🐦 Check your Twitter account to see if the tweet was posted.

---

## 🔄 Pull Request Process

### 📝 Before Submitting

- [ ] ✅ All tests pass locally
- [ ] 🎨 Code follows style guidelines
- [ ] 📖 Documentation is updated
- [ ] 📝 CHANGELOG.md is updated (if applicable)
- [ ] 🚫 No sensitive information in code

### 🏷️ PR Title Format

Use descriptive titles following [conventional commit](https://www.conventionalcommits.org/) format:

```
feat: add automated tweet scheduling
fix: resolve rate limiting issue in API client
docs: update installation instructions
test: add integration tests for tweet deletion
```

### 📋 PR Description Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or breaking changes documented)
```

### 👀 Review Process

1. 🤖 **Automated checks**: CI/CD pipeline runs tests and linting
2. 🧐 **Code review**: At least one maintainer reviews your PR
3. 🛠️ **Address feedback**: Make requested changes
4. ✅ **Approval**: PR is approved and merged

---

## 🐛 Issue Reporting

### 🐞 Bug Reports

Use the bug report template and include:

- 🏷️ **Clear title**: Describe the issue concisely
- 💻 **Environment**: Python version, OS, dependency versions
- 📝 **Steps to reproduce**: Detailed steps to reproduce the issue
- 🔮 **Expected behavior**: What should happen
- 💥 **Actual behavior**: What actually happens
- ⚠️ **Error messages**: Full error messages and stack traces
- 📸 **Screenshots**: If applicable

### 🌠 Feature Requests

- 🎯 **Use case**: Explain why this feature would be useful
- 💡 **Proposed solution**: Describe your ideal solution
- 🔄 **Alternatives**: Any alternative solutions considered
- 📝 **Additional context**: Screenshots, mockups, examples

---

## 🔒 Security Guidelines

### 🐦 Twitter API Security

- 🚫 **Never commit API credentials** to version control
- 🛡️ **Use environment variables** for all sensitive configuration
- ⏳ **Follow rate limiting** guidelines to avoid API restrictions
- ⚠️ **Implement proper error handling** for API failures

### 🛡️ Secure Coding Practices

```python
# ✅ Good: Use environment variables
import os
api_key = os.getenv('TWITTER_API_KEY')

# ❌ Bad: Hardcoded credentials
api_key = 'your_actual_api_key_here'
```

### 🕵️ Reporting Security Issues

Please report security vulnerabilities **privately** to [info@prodigalai.com](mailto:info@prodigalai.com) rather than opening public issues.

---

## 📖 Documentation

### ✍️ Docstring Format

Use **Google-style docstrings**:

```python
def create_tweet(content: str, media_ids: Optional[List[str]] = None) -> Tweet:
    """Create and post a new tweet.
    
    Args:
        content: The text content of the tweet.
        media_ids: Optional list of media IDs to attach.
        
    Returns:
        The created tweet object.
        
    Raises:
        TwitterAPIError: If the API request fails.
        ValueError: If content is invalid.
        
    Example:
        >>> tweet = create_tweet("Hello, world!")
        >>> print(tweet.id)
        '1234567890'
    """
```

### 📝 README Updates

When adding new features, update the main README.md with:

- 📖 Usage examples
- ⚙️ Configuration options
- 🔗 API documentation links

---

## 🌟 Community and Support

### 🆘 Getting Help

- 💬 **GitHub Issues**: For bug reports and feature requests
- 🗣️ **Discussions**: For questions and general discussion
- 🤝 **Discord/Slack**: [Join our community chat] (if available)
- 📚 **Documentation**: Check our [documentation site] (if available)

### 🏅 Recognition

We appreciate all contributions! Contributors are recognized in:

- `CONTRIBUTORS.md` file
- Release notes
- Project README

---

## 📋 Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 🏷️ Types

- `feat`: 🌟 New feature
- `fix`: 🐛 Bug fix
- `docs`: 📝 Documentation changes
- `style`: 🎨 Code style changes (formatting, etc.)
- `refactor`: 🔨 Code refactoring
- `test`: 🧪 Adding or updating tests
- `chore`: 🔧 Maintenance tasks

### 💡 Examples

```bash
feat: add tweet scheduling functionality
fix(api): resolve rate limiting error handling
docs: update installation instructions
test: add unit tests for tweet deletion
refactor: simplify authentication flow
```

---

## 🚀 Release Process

1. 🏷️ Update version in `pyproject.toml`
2. 📝 Update `CHANGELOG.md`
3. 🔄 Create a release PR
4. 🏷️ Tag the release after merge
5. 🚢 Automated deployment to PyPI

---

## 🙏 Thank You

Thank you for contributing to the **Twitter Automation** project!  
Your contributions help make this tool better for everyone.  
We appreciate your time and effort in improving the project.

For questions or clarification about this contributing guide, please [open an issue](https://github.com/Prodigal-AI/prodigal-automation/issues/new) or reach out to the maintainers.

**Happy coding!** 🚀🐦