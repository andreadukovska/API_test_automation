 #Verify that the GET /posts endpoint responds successfully with HTTP status code 200.

import requests

def test_get_posts_returns_successful_list_response():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout = 10
    )

    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)

# Verify that GET /posts/1 returns the requested post.

def test_get_single_post_returns_correct_id():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    post = response.json()
    assert post["id"] == 1
    assert "title" in post
    assert isinstance(post["title"], str) and post["title"].strip()
    assert isinstance(post["body"], str) and post["body"].strip()


# Verify that requesting a nonexistent post returns HTTP 404.
def test_get_nonexistent_post_returns_404():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/99999",
        timeout=10
    )

    assert response.status_code == 404

# Verify that POST /posts creates a post and returns the submitted data.
def test_create_post_returns_201():
    payload = {
        "title": "API Automation Test",
        "body": "This is a test post.",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    post = response.json()
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]
    assert "id" in post

# Verify that PUT /posts/1 returns the updated post data.
def test_update_post_returns_200():
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated post content.",
        "userId": 1
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    post = response.json()
    assert post["id"] == 1
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]

# Verify that PATCH /posts/1 updates the title of an existing post.
def test_patch_post_title_returns_200():
    payload = {
        "title": "Partially updated title"
    }

    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    post = response.json()
    assert post["id"] == 1
    assert post["title"] == payload["title"]

# Verify that DELETE /posts/1 returns a successful deletion response.
def test_delete_post_returns_200():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    assert response.status_code == 200
    assert response.json() == {}