from ultralytics import YOLO
from PIL import Image
import sys

# Add models directory
sys.path.append('models')
model = YOLO('final-mosaic-augmentation.pt')


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


def solar_panel_predict(image, conf=0.5):
    """
    Predicts the presence of solar panels in an image and annotates them.

    Args:
    image (PIL.Image.Image): The image in which to detect solar panels.
    conf (float): Confidence threshold for the detection model.

    Returns:
    tuple: A tuple containing a prediction string and the annotated image.
           The string indicates whether solar panels were detected or not.
    """
    results = model(image, stream=True, conf=conf)
    for result in results:
        annotated_image = result.plot()
        im = plot_results(annotated_image)

        r = result.boxes
        confi = r.conf.numpy().tolist()
        if not confi:
            prediction = "NO SOLAR PANELS DETECTED"
        else:
            prediction = "SOLAR PANELS DETECTED"
        return prediction, im

