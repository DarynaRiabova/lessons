import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20,
}

asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = requests.get(search_url, params=search_params)
data = response.json()

items = data["collection"]["items"]

first_nasa_id = items[0]["data"][0]["nasa_id"]
second_nasa_id = items[1]["data"][0]["nasa_id"]

asset_url1 = asset_url_template.format(nasa_id=first_nasa_id)
asset_url2 = asset_url_template.format(nasa_id=second_nasa_id)

asset_response1 = requests.get(asset_url1)
asset_response2 = requests.get(asset_url2)

asset_data1 = asset_response1.json()
asset_data2 = asset_response2.json()

asset_items1 = asset_data1["collection"]["items"]
asset_items2 = asset_data2["collection"]["items"]

for item in asset_items1:
    file_url1 = item["href"]
    if file_url1.endswith(".jpg"):
        break
image_response1 = requests.get(file_url1)

with open("mars_photo1.jpg", "wb") as file:
    file.write(image_response1.content)

for item in asset_items2:
    file_url2 = item["href"]
    if file_url2.endswith(".jpg"):
        break

image_response2 = requests.get(file_url2)

with open("mars_photo2.jpg", "wb") as file:
    file.write(image_response2.content)
