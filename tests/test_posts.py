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