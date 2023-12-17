from ultralytics import YOLO
from PIL import Image
model = YOLO('best.pt')


def plot_results(im_array, save_image=False, img_path="results.jpg"):
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    if save_image:
        im.save(img_path)  # save image
    return im


def solar_panel_predict(image, conf=0.5):
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

