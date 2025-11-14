# Adv Web Dev Activity 8 - DevOps Activity

## Overview

This project implements a minimal Flask API with automated testing, linting, coverage reporting, security scanning, and dependency updates using GitHub Actions. The API includes several endpoints with full test coverage. Screenshots of successful implementation of each step can be found in the `screenshots\` folder

## API Endpoints

### **GET `/hello`**
Returns a greeting message.
Example:
```
json output:
{ "message": "Hello, World!" }
```

### **POST `/echo`**
Accepts a JSON payload and returns it back with a `201 Created` status.
Example:
```
json:
{ "msg": "ping" }
```

### **PUT `/update`**
Accepts a JSON payload and returns it with an added `"updated": true` field.
Example:
```
json:
Input: { "item": "test" }
Output: { "updated": true, "item": "test" }
```

### **DELETE `/remove`**
Accepts a JSON payload and returns it with an added `"deleted": true` field.
Example:
```
json:
Input: { "item": "test" }
Output: { "deleted": true, "item": "test" }
```

## Tests
- All endpoints are covered with unit tests in `test_app.py` using pytest.
- Should return 4 successful pytests completed if run locally.
- CI workflow runs test automatically on push to GitHub and reports coverage using `pytest-cov` and Codecov.
- Test confirm a proper 200 status code and the appropriate JSON response as shown in examples within the endpoints.

## Issues Encountered
- **Dependabot File Note Found Issue**: Initially failed because it couldn't detect the `requirements.txt` file in the root folder. Was resolved by ensuring that the file existed on the main branch and publishing the `dependabot.yml` and `requirements.txt` file in the same commit.
- **GitHub Actions Matrix/Python Version Issue**: Specifying a matrix with python versions as `[3.10, 3.11, 3.12]` caused issues so the values where wrapped in quotes to make them valid strings: `["3.10", "3.11", "3.12"]`
- **CodeQL Security Scan Issue**: Using v1 actions led to errors indicating deprecation and some workflow runs failed due to insufficient permissions. Issues were fixed by updating to use v3 actions and ensuring proper permissions in the `codeql-analysis.yml` file.
- **General CI Setup Issues**: Needed to include all dependencies in `requirements.txt` before running GitHub workflow actions. Had to update `requirements.txt` with `pip freeze > requirements.txt` prior to committing code to GitHub at each step.