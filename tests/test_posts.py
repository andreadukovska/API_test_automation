

# Verify that GET /posts returns status 200 and a list of posts.
def test_get_posts_returns_successful_list_response(client):
    response = client.get("/posts")

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)

# Verify that GET /posts/1 returns the requested post.
def test_get_single_post_returns_correct_id(client):
    response = client.get("/posts/1")

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert "title" in post
    assert isinstance(post["title"], str) and post["title"].strip()
    assert isinstance(post["body"], str) and post["body"].strip()


# Verify that requesting a nonexistent post returns HTTP 404.
def test_get_nonexistent_post_returns_404(client):
    response = client.get("/posts/99999")

    assert response.status_code == 404

# Verify that POST /posts creates a post and returns the submitted data.
def test_create_post_returns_201(client):

    payload = {
        "title": "API Automation Test",
        "body": "This is a test post.",
        "userId": 1
    }

    response = client.post("/posts", payload)

    assert response.status_code == 201
    post = response.json()
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]
    assert "id" in post

# Verify that PUT /posts/1 returns the updated post data.
def test_update_post_returns_200(client):

    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated post content.",
        "userId": 1
    }

    response = client.put("/posts/1", payload)

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["title"] == payload["title"]
    assert post["body"] == payload["body"]
    assert post["userId"] == payload["userId"]

# Verify that PATCH /posts/1 updates the title of an existing post.
def test_patch_post_title_returns_200(client):

    payload = {
        "title": "Partially updated title"
    }

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
    