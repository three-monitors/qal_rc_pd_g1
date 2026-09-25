import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Частина 1. Базові запити

# Завдання 1: Отримати всі posts
def task1_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    posts = response.json()
    print(f"Кількість записів: {len(posts)}")
    assert len(posts) == 100
    return posts

# Завдання 2: Отримати post по id=10
def task2_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/10")
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    post = response.json()
    print(f"ID: {post['id']}")
    assert post['id'] == 10
    assert 'userId' in post
    assert 'title' in post
    assert 'body' in post
    return post

# Завдання 3: Отримати todos користувача 2
def task3_get_user_todos():
    response = requests.get(f"{BASE_URL}/todos", params={"userId": 2})
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    todos = response.json()
    for todo in todos:
        assert todo['userId'] == 2
    print(f"Кількість todos: {len(todos)}")
    return todos

# Частина 2. CRUD

# Завдання 4: Create (POST)
def task4_create_post():
    payload = {
        "title": "my title",
        "body": "my body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print(f"Status code: {response.status_code}")
    assert response.status_code == 201
    post = response.json()
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
    assert post['title'] == "my title"
    assert post['body'] == "my body"
    return post

# Завдання 5: Update через PUT
def task5_update_post():
    payload = {
        "id": 5,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/5", json=payload)
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    post = response.json()
    print(f"Updated title: {post['title']}")
    assert post['title'] == "updated title"
    return post

# Завдання 6: Partial Update через PATCH
def task6_patch_post():
    payload = {
        "title": "patched title"
    }
    response = requests.patch(f"{BASE_URL}/posts/5", json=payload)
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    post = response.json()
    print(f"Patched title: {post['title']}")
    assert post['title'] == "patched title"
    return post

# Завдання 7: Delete
def task7_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/5")
    print(f"Status code: {response.status_code}")
    assert response.status_code in [200, 204]
    print("Post deleted")

# Частина 3. Негативні сценарії

# Завдання 8: Отримати неіснуючий post
def task8_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")
    print(f"Status code: {response.status_code}")
    assert response.status_code == 404

# Завдання 9: Відправити POST без required полів
def task9_post_without_required_fields():
    payload = {}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

# Частина 4. Робота з headers

# Завдання 10: Custom headers
def task10_custom_headers():
    headers = {
        "User-Agent": "QA Student"
    }
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200
    print("Request with custom headers successful")

# Bonus: Універсальна функція
def make_request(method, endpoint, **kwargs):
    if method == "GET":
        return requests.get(f"{BASE_URL}{endpoint}", **kwargs)
    elif method == "POST":
        return requests.post(f"{BASE_URL}{endpoint}", **kwargs)
    elif method == "PUT":
        return requests.put(f"{BASE_URL}{endpoint}", **kwargs)
    elif method == "PATCH":
        return requests.patch(f"{BASE_URL}{endpoint}", **kwargs)
    elif method == "DELETE":
        return requests.delete(f"{BASE_URL}{endpoint}", **kwargs)
    else:
        raise ValueError(f"Unsupported method: {method}")


def main():
    """Виконання всіх завдань"""
    print("=== Частина 1: Базові запити ===")
    task1_get_all_posts()
    task2_get_post_by_id()
    task3_get_user_todos()

    print("\n=== Частина 2: CRUD ===")
    task4_create_post()
    task5_update_post()
    task6_patch_post()
    task7_delete_post()

    print("\n=== Частина 3: Негативні сценарії ===")
    task8_get_nonexistent_post()
    task9_post_without_required_fields()

    print("\n=== Частина 4: Headers ===")
    task10_custom_headers()

    print("\n=== Bonus: Універсальна функція ===")
    print("GET all posts:")
    make_request("GET", "/posts")
    print("POST new post:")
    make_request("POST", "/posts",
                 json={"title": "test", "body": "test", "userId": 1})


if __name__ == "__main__":
    main()
