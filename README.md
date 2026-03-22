# Playwright Automation Framework

A professional end-to-end test automation framework built with **Playwright + Python + PyTest** using **Page Object Model (POM)** architecture, targeting [Automation Exercise](https://automationexercise.com) — a public e-commerce practice site.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Playwright | Browser automation |
| Python 3.11 | Programming language |
| PyTest | Test framework |
| Page Object Model | Architecture pattern |
| pytest-html | HTML test reports |
| GitHub Actions | CI/CD pipeline |

---

## Project Structure

```
playwright_framework/
├── pages/
│   ├── base_page.py       # Common reusable methods
│   ├── home_page.py       # Home page object
│   ├── login_page.py      # Login/Signup page object
│   ├── products_page.py   # Products page object
│   └── cart_page.py       # Cart page object
├── tests/
│   ├── test_home_page.py      # 6 test cases
│   ├── test_login_page.py     # 8 test cases
│   ├── test_products_page.py  # 9 test cases
│   └── test_cart_page.py      # 5 test cases
├── reports/               # HTML test reports (auto-generated)
├── .github/workflows/
│   └── playwright_tests.yml   # GitHub Actions CI/CD
├── conftest.py            # Fixtures and browser config
├── pytest.ini             # PyTest configuration
├── requirements.txt       # Dependencies
└── README.md
```

---

## Test Coverage

| Module | Test Cases | Types Covered |
|---|---|---|
| Home Page | 6 | Navigation, Logo, Title |
| Login Page | 8 | Valid, Invalid, Empty, Parametrize |
| Products Page | 9 | Search, Display, Keyword matching |
| Cart Page | 5 | Navigation, URL, Empty cart |
| **Total** | **28** | Functional, Regression, Parametrize |

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/MalaRamBabu/playwright-automation-framework.git
cd playwright-automation-framework
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers
```bash
playwright install
```

---

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific module
```bash
pytest tests/test_login_page.py
pytest tests/test_products_page.py
```

### Run on specific browser
```bash
pytest --browser-type=chromium
pytest --browser-type=firefox
pytest --browser-type=webkit
```

### Run in headed mode (see browser)
```bash
pytest --headless=false
```

### Run with HTML report
```bash
pytest --html=reports/test_report.html --self-contained-html
```

---

## CI/CD — GitHub Actions

Tests run automatically on every push to `main` branch.

- Trigger: Push or Pull Request to `main`
- Browser: Chromium (headless)
- Report: Uploaded as GitHub Actions artifact

---

## Author

**Mala Ram Babu**
Senior QA Automation Engineer | 4+ Years Experience
[LinkedIn](https://www.linkedin.com/in/mala-ram-babu) | [GitHub](https://github.com/MalaRamBabu)
