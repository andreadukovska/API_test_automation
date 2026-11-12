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