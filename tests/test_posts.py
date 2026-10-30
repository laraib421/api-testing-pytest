import pytest
from jsonschema import validate
from utils.schemas import POST_SCHEMA


@pytest.mark.smoke
def test_get_all_posts_returns_100(api):
    r = api.get("/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_single_post_matches_schema(api, post_id):
    r = api.get(f"/posts/{post_id}")
    assert r.status_code == 200
    data = r.json()
    validate(instance=data, schema=POST_SCHEMA)
    assert data["id"] == post_id


def test_filter_posts_by_user(api):
    r = api.get("/posts", params={"userId": 1})
    assert r.status_code == 200
    assert all(p["userId"] == 1 for p in r.json())


@pytest.mark.smoke
def test_create_post(api):
    payload = {"title": "QA rocks", "body": "Automated with pytest", "userId": 7}
    r = api.post("/posts", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


def test_update_post_put(api):
    payload = {"id": 1, "title": "updated", "body": "new body", "userId": 1}
    r = api.put("/posts/1", json=payload)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"


def test_partial_update_patch(api):
    r = api.patch("/posts/1", json={"title": "patched"})
    assert r.status_code == 200
    assert r.json()["title"] == "patched"


def test_delete_post(api):
    r = api.delete("/posts/1")
    assert r.status_code == 200


@pytest.mark.negative
def test_nonexistent_post_returns_404(api):
    r = api.get("/posts/99999")
    assert r.status_code == 404


def test_response_time_under_2s(api):
    r = api.get("/posts/1")
    assert r.elapsed.total_seconds() < 2
