import pytest
from jsonschema import validate
from utils.schemas import USER_SCHEMA


@pytest.mark.smoke
def test_users_list_matches_schema(api):
    r = api.get("/users")
    assert r.status_code == 200
    users = r.json()
    assert len(users) == 10
    for user in users:
        validate(instance=user, schema=USER_SCHEMA)


def test_user_emails_are_unique(api):
    emails = [u["email"] for u in api.get("/users").json()]
    assert len(emails) == len(set(emails))


def test_content_type_header_is_json(api):
    r = api.get("/users/1")
    assert "application/json" in r.headers["Content-Type"]


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_user_has_posts(api, user_id):
    r = api.get(f"/users/{user_id}/posts")
    assert r.status_code == 200
    assert len(r.json()) > 0


@pytest.mark.negative
def test_unknown_user_returns_404(api):
    assert api.get("/users/0").status_code == 404
