import pytest

from test_data.posts_data import (
    CREATE_POST_PAYLOAD,
    PATCH_POST_PAYLOAD,
    UPDATE_POST_PAYLOAD,
)


# Verify that GET /posts returns a valid list of posts.
def test_get_posts_returns_successful_list_response(client):
    response = client.get("/posts")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) == 100

    for post in posts:
        assert isinstance(post["id"], int)
        assert isinstance(post["userId"], int)
        assert isinstance(post["title"], str) and post["title"].strip()
        assert isinstance(post["body"], str) and post["body"].strip()


# Verify that GET /posts/{id} returns the requested post.
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_single_post_returns_correct_id(client, post_id):
    response = client.get(f"/posts/{post_id}")

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert isinstance(post["title"], str) and post["title"].strip()
    assert isinstance(post["body"], str) and post["body"].strip()


# Verify that requesting a nonexistent post returns HTTP 404.
@pytest.mark.parametrize("post_id", [0, 101, 99999])
def test_get_nonexistent_post_returns_404(client, post_id):
    response = client.get(f"/posts/{post_id}")

    assert response.status_code == 404


# Verify that POST /posts creates a post and returns the submitted data.
def test_create_post_returns_201(client):
    payload = CREATE_POST_PAYLOAD.copy()

    response = client.post("/posts", payload)

    assert response.status_code == 201
    post = response.json()
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]
    assert "id" in post


# Verify that PUT /posts/1 returns the updated post data.
def test_update_post_returns_200(client):
    payload = UPDATE_POST_PAYLOAD.copy()

    response = client.put("/posts/1", payload)

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]


# Verify that PATCH /posts/1 updates the title of an existing post.
def test_patch_post_title_returns_200(client):
    payload = PATCH_POST_PAYLOAD.copy()

    response = client.patch("/posts/1", payload)

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["title"] == payload["title"]


# Verify that DELETE /posts/1 returns a successful deletion response.
def test_delete_post_returns_200(client):
    response = client.delete("/posts/1")

    assert response.status_code == 200
    assert response.json() == {}
