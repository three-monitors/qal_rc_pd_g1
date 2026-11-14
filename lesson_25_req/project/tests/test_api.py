import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 100


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/10")
    assert response.status_code == 200
    post = response.json()
    assert post['id'] == 10
    assert 'userId' in post
    assert 'title' in post
    assert 'body' in post


def test_get_user_todos():
    response = requests.get(f"{BASE_URL}/todos", params={"userId": 2})
    assert response.status_code == 200
    todos = response.json()
    for todo in todos:
        assert todo['userId'] == 2


def test_create_post():
    payload = {
        "title": "my title",
        "body": "my body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    post = response.json()
    assert post['title'] == "my title"
    assert post['body'] == "my body"


def test_update_post():
    payload = {
        "id": 5,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/5", json=payload)
    assert response.status_code == 200
    post = response.json()
    assert post['title'] == "updated title"


def test_patch_post():
    payload = {
        "title": "patched title"
    }
    response = requests.patch(f"{BASE_URL}/posts/5", json=payload)
    assert response.status_code == 200
    post = response.json()
    assert post['title'] == "patched title"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/5")
    assert response.status_code in [200, 204]


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404


def test_custom_headers():
    headers = {
        "User": "Student"
    }
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code == 200
