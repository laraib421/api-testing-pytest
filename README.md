# 🔌 API Testing Suite — Pytest + Requests

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![CI](https://github.com/laraib421/api-testing-pytest/actions/workflows/api-tests.yml/badge.svg)

REST API test automation for [JSONPlaceholder](https://jsonplaceholder.typicode.com) covering **CRUD operations, JSON schema contract checks, negative cases and performance**.

## ✨ Highlights
- ♻️ Reusable `APIClient` wrapper with session & timeouts
- 📜 JSON Schema contract validation (`jsonschema`)
- 🧩 Parametrized, data-driven tests
- 🏷️ Markers: `smoke`, `negative`
- 📊 HTML report + weekly scheduled CI run

## 🚀 Run
```bash
pip install -r requirements.txt
pytest                 # all tests
pytest -m smoke        # smoke only
pytest --html=report.html --self-contained-html
```
Point at another environment: `API_BASE_URL=https://staging.example.com pytest`

## 📁 Structure
```
utils/api_client.py   HTTP client
utils/schemas.py      JSON schemas
tests/                test_posts.py, test_users.py
conftest.py           fixtures
```
