# API Security Testing Framework

## Overview about the project

This project is a Red Team focused API security testing framework designed to identify common vulnerabilities in REST APIs.

### It simulates real-world attack scenarios such as:

- Broken Object Level Authorization (BOLA)
- Rate Limiting Bypass
- API Key Exposure

### The framework includes:

- A vulnerable API (Flask-based)
- Automated attack scripts
- Security testing using industry tools

### Objectives
- Build a vulnerable API for testing
- Automate API vulnerability scanning
- Simulate real attacker behavior
- Generate security findings

## Project Structure
```
api-security-framework/
|__ main_scanner.py         # Automation engine
│
├── app/                # Vulnerable API
│   └── app.py
│
├── scanner/            # Attack modules
│   ├── bola_test.py
│   ├── rate_limit_test.py
│   └── api_key_test.py            
│  
│
├── reports/            # Scan results
│
├── requirements.txt

```
## Installation
**Clone the repo**
```jsx
git clone https://github.com/your-username/api-security-testing-framework.git
```
Move to the api-security Directory
```jsx
cd api-security-testing-framework
```
Create a environment 
```jsx
python3 -m venv venv
```
Activate the Environment
```jsx
source venv/bin/activate
```
Install all the requirement for building the site 
```jsx
pip install -r requirements.txt
```
## Usage
### Step 1: Run Vulnerable API
```jsx
python app/app.py
```
### Step 2: Run Scanner
```jsx
python scripts/main_scanner.py
```

### Vulnerabilities Tested
1. Broken Object Level Authorization (BOLA)
- Accessing unauthorized user data by modifying user IDs
2. Rate Limiting Bypass
- Sending multiple requests without restriction
3. API Key Exposure
- Sensitive API keys exposed in responses

## Tools Used
- Postman
- OWASP ZAP
- Burp Suite
- Python Requests Library
```jsx
flask
pyjwt
```

## Disclaimer

This project is created for educational and ethical testing purposes only.
Do not use this tool on systems without proper authorization.
