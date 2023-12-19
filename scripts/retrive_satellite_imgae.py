import requests


def satellite_image_params(address, api_key, zoom, size):
    params = {
        "center": address,
        "zoom": str(zoom),
        "size": size,
        "maptype": "satellite",
        "key": api_key
    }
    return params


def fetch_satellite_image(address, api_key, zoom=18, size="640x640"):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    params = satellite_image_params(address, api_key, zoom=zoom, size=size)
    try:
        response = requests.get(base_url, params=params)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    if response.status_code == 200:
        image_data = response.content
        img_name = f"{'_'.join(address.split()[-2:])}.jpg"
        with open(img_name, "wb") as file:
            file.write(image_data)
        print("Image was downloaded successfully")
        return img_name
