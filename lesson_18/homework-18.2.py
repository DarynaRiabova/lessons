import requests

url = "http://127.0.0.1:8080/upload"

with open("lesson_18/cat1.jpg", "rb") as file:
    files = {"image": file}

    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
filename = "cat1.jpg"

url = f"http://127.0.0.1:8080/image/{filename}"

response = requests.get(url, headers={"Content-Type": "text"})

print(response.status_code)
print(response.json())

delete_url = f"http://127.0.0.1:8080/delete/{filename}"

delete_response = requests.delete(delete_url)

print(delete_response.status_code)
print(delete_response.json())
