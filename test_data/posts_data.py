# Payload for creating a new post.
CREATE_POST_PAYLOAD = {
    "title": "API Automation Test",
    "body": "This is a test post.",
    "userId": 1
}

# Payload for replacing an existing post.
UPDATE_POST_PAYLOAD = {
    "id": 1,
    "title": "Updated title",
    "body": "Updated post content.",
    "userId": 1
}

# Payload for partially updating an existing post.
PATCH_POST_PAYLOAD = {
    "title": "Partially updated title"
}