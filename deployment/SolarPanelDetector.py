from ultralytics import YOLO
from PIL import Image
import requests
import random

model = YOLO('detector.pt')


def satellite_image_params(address, api_key, zoom, size):
    """
    Generate parameters for Google Maps API request based on given address, API key, zoom level, and image size.

    Parameters:
    address (str): The address to center the map on.
    api_key (str): Google Maps API key.
    zoom (int): Zoom level for the map.
    size (str): Size of the requested map image.

    Returns:
    dict: A dictionary of parameters for the API request.
    """
    params = {
        "center": address,
        "zoom": str(zoom),
        "size": size,
        "maptype": "satellite",
        "key": api_key
    }
    return params


def fetch_satellite_image(address, api_key, zoom=18, size="640x640"):
    """
    Fetches a satellite image from Google Maps API based on the given address, api_key, zoom level, and size.

    Parameters:
    address (str): The address for the satellite image.
    api_key (str): Google Maps API key.
    zoom (int): Zoom level for the satellite image.
    size (str): Size of the satellite image.

    Returns:
    str: File name of the saved satellite image or None if the request fails.
    """
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


def plot_results(im_array, save_image=False, img_path="results.jpg"):
    """
     Converts an image array to a PIL image and optionally saves it.

     Parameters:
     im_array (numpy.ndarray): The image array to be converted.
     save_image (bool): Whether to save the image.
     img_path (str): Path to save the image.

     Returns:
     PIL.Image: The converted PIL image.
     """
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    if save_image:
        im.save(img_path)  # save image
    return im


def solar_panel_predict(image, conf=0.45):
    """
    Analyzes an image to detect solar panels and returns an annotated image along with a relevant message.

    This function uses a model to detect solar panels in the given image. If solar panels are detected with confidence
    above the specified threshold, it selects a positive sentence; otherwise, it chooses a sentence encouraging
    solar panel installation. It also annotates the image with detection results.

    Parameters:
    image: The input image for solar panel detection.
    conf: Confidence threshold for detection, default is 0.5.

    Returns:
    Tuple of (annotated image, prediction message)
    """
    negative_setences = [
        "No solar panels yet?\nYour roof is a blank canvas waiting for a green masterpiece! 🎨🌱",
        "It's lonely up here without solar panels.\nImagine the sun-powered parties you're missing! 🌞🎉",
        "Your roof could be a superhero in disguise.\nJust needs its solar cape! 🦸‍♂️☀️",
        "Clear skies, empty roof.\nIt's the perfect opportunity to harness the sun! 🌤️🔋",
        "No panels detected – but don't worry,\nit's never too late to join the solar revolution and be a ray of hope! 🌍💡"]

    positive_sentences = [
        "Solar panels detected: You're not just saving money,\nyou're also charging up Mother Earth's good vibes! 🌍💚",
        "Roof status: Sunny side up!\nYour panels are turning rays into awesome days! ☀️😎",
        "You've got solar power!\nNow your roof is cooler than a polar bear in sunglasses. 🐻‍❄️🕶️",
        "Green alert: Your roof is now a climate hero's cape!\nSolar panels are saving the day, one ray at a time. 🦸‍♂️🌞",
        "Solar panels spotted: Your roof is now officially a member of the Renewable Energy Rockstars Club! ⭐🌱"]

    results = model(image, stream=True, conf=conf)
    for result in results:
        annotated_image = result.plot()
        im = plot_results(annotated_image)

        r = result.boxes
        confi = r.conf.numpy().tolist()
        if not confi:
            prediction = random.choice(negative_setences)
        else:
            prediction = random.choice(positive_sentences)
        return im, prediction


def detector(address, api_key, zoom=18, size="640x640"):
    """
    Detects solar panels in a satellite image fetched based on the given address.

    Parameters:
    address (str): The address to fetch the satellite image of.
    api_key (str): Google Maps API key.
    zoom (int): Zoom level for the image.
    size (str): Size of the image.

    Returns:
    tuple: Prediction text and detected image.
    """
    img_name = fetch_satellite_image(address, api_key, zoom=zoom, size=size)
    im, prediction = solar_panel_predict(img_name)
    return im, prediction
