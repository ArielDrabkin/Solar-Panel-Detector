from ultralytics import YOLO
from PIL import Image

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

def image_predction(image_path):
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
    image_path = "H:\My Drive\my computer\Data Science\solar-panel-detector2\deployment\examples\Ceske-Budejovice.jpg"
    image = Image.open(image_path)
    prediction,im =  solar_panel_predict(image, conf=0.5)
    im.show()
    print(prediction)

if __name__ == '__main__':
    image_path = "H:\My Drive\my computer\Data Science\solar-panel-detector2\deployment\examples\Ceske-Budejovice.jpg"
    image_predction(image_path)
