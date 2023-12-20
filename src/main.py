from retrive_satellite_imgae import fetch_satellite_image
from Predict import solar_panel_predict, image_predction
import json
import argparse


def get_args():
    parser = argparse.ArgumentParser("Main arguments")
    parser.add_argument("-k", "--api_key", help="API key", required=False)
    parser.add_argument("-a", "--address", help="Address for prediction", required=False, default=None)
    parser.add_argument("-z", "--zoom", help="Image Zoom (19 default).",
                        required=False, default=19)
    parser.add_argument("-i", "--image_dir", help="Image dir to apply the predictions.",
                        required=False, default=None)
    args = parser.parse_args()
    return args


def detector(address, api_key, zoom=18, size="640x640"):
    """
    Retrieves a satellite image of a given address and detects solar panels in it.

    Args:
    address (str): The address or geographic coordinates to fetch the satellite image for.
    api_key (str): Google Maps API key for accessing the satellite imagery service.
    zoom (int, optional): Zoom level for the satellite image. Defaults to 18.
    size (str, optional): Size of the satellite image to retrieve. Defaults to "640x640".

    Returns:
    tuple: A tuple containing the detection prediction and the processed image.
    """
    img_name = fetch_satellite_image(address, api_key, zoom=zoom, size=size)
    prediction, im = solar_panel_predict(img_name)
    im.show()
    print(prediction)
    return prediction, im


if __name__ == '__main__':
    # import api_key from json
    with open("../secret.json") as file:
        api_key = json.load(file)["google_maps_api_key"]

    args = get_args()
    if args.api_key is not None:
        api_key = args.api_key

    address = args.address
    image_path = args.image_dir

    if address is not None:
        if image_path is None:
            prediction, im = detector(address, api_key, zoom=args.zoom)
        else:
            print("Address and Image_path were provided, but i will predict the address!")
            prediction, im = detector(address, api_key, zoom=args.zoom)

    elif image_path is not None:
        image_predction(image_path)

    else:
        print("No valid info was provided, can't make predictions - Have a Sunny day 😎")
