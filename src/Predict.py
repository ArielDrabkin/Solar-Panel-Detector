from ultralytics import YOLO
from PIL import Image
import argparse
import random
def get_args():
    parser = argparse.ArgumentParser("Predict arguments")
    parser.add_argument("-i", "--Image_dir", help="image dir to apply the predictions.",
                        required=True)
    args = parser.parse_args()
    return args


# Load the model
model_path = '../models/final-mosaic-augmentation.pt'
model = YOLO(model_path)

def plot_results(im_array, save_image=False, img_path="results.jpg"):
    """
    Convert an image array to a PIL image, optionally save it, and return the image.

    Args:
    im_array (numpy.ndarray): The image array to be converted to a PIL image.
    save_image (bool): If True, saves the image to the specified path.
    img_path (str): Path where the image will be saved if save_image is True.

    Returns:
    PIL.Image.Image: The converted PIL image.
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
        return prediction, im

def image_predction(image_path, conf=0.5):
    """
    Loads an image from a specified path, performs solar panel prediction on it, and displays the results.

    This function opens an image from the given path, predicts the presence of solar panels using the
    solar_panel_predict function, and then displays the image along with the prediction result.

    Args:
    image_path (str): The file path of the image on which to perform the solar panel prediction.

    Note:
    The function currently has a hardcoded image path, which should be replaced with the 'image_path' argument
    for dynamic functionality.
    """
    image = Image.open(image_path)
    prediction, im = solar_panel_predict(image, conf=conf)
    im.show()
    print(prediction)

if __name__ == '__main__':
    args = get_args()
    image_path = args.image_dir
    image_predction(image_path)
