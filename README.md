Solar-Panel-Detector 🛰️☀️
==============================
![](https://raw.githubusercontent.com/ArielDrabkin/Solar-Panel-Detector/master/deployment/examples/spd-demo.gif)

--------

## Overview

The Solar-Panel-Detector is an innovative AI-driven tool designed to identify solar panels in satellite imagery.
Utilizing the state-of-the-art YOLOv8 object-detection model and various cutting-edge technologies, this project
demonstrates how AI can be leveraged for environmental sustainability.

--------

## Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    ├── models             <- Trained and serialized models
    │   └── copy_paste-augmentation.pt     
    │   └── final-mosaic-augmentation.pt  
    │   └── mixup-augmentation.pt          
    │   └── mosaic-and-mixup-0.8-0.2-augmentation.pt     
    │   └── mosaic-augmentation.pt 
    │   └── NO-augmentation.pt
    ├── notebooks          <- Jupyter notebooks.
    │   └── Error Analysis.ipynb
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── final model training results        <- Generated graphics and figures to be used in reporting
    ├── src             <- Source code for various stages of the project
    │   └── retrive_satellite_imgae.py        <- Script for obtaining satellite image for a given address
    │   └── Predict.py                        <- Script for predicting with the trained model on a given image
    │   └── main.py                            <- Script for running the application
    ├── training            <- Training code for the several experiments made and the final model training.
    │   └── copy_paste-augmentation-training.ipynb
    │   └── final-mosaic-augmentation-training.ipynb
    │   └── mixup-augmentation-training.ipynb
    │   └── mosaic-and-mixup-0.8-0.2-augmentation-training.ipynb     
    │   └── mosaic-augmentation-training.ipynb
    │   └── NO-augmentation-training.ipynb
    ├── deployment               <- Deployment code for the application as it was dep;oyed on Hugging Face Spaces.
    │   └── examples       <- Examples of images for the application use.
    │   └── README.md          <- The HuggingFace Space built-in README for developers using this project.
    │   └── detector.pt        <- The trained model for the application.
    │   └── requirements.txt   <- The requirements file for deploying the application.
    │   └── SolarPanelDetector.py   <- The script that holds the functionality of the application.
    │   └── app.py   <- The script that runs the application.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── secret               <- Secterkeys for use in this project (No Keys present).

--------

## Key Technologies

**Roboflow** 🤖: For data organization and preprocessing.  
**Ultralytics** 🌊: Utilizing their open-source YOLOv8 model for accurate object detection.  
**Google Colab** ♾️: For model training and evaluation.  
**Lightning AI**⚡: Enhancing training efficiency.  
**ClearML** 📉: For training management and performance analysis.  
**Google Maps API** 🗺️: To acquire satellite imagery.  
**Gradio** 🎢: Creating a user-friendly GUI.  
**Hugging Face Spaces** 🤗: For deploying the application.

--------

## Application

* The Solar-Panel-Detector app analyzes satellite images to detect the presence of solar panels, serving both
  environmental research and the solar energy market.
* It provides insights into potential areas for solar panel installation and aids in understanding the spread of solar
  energy usage.
* The Predictions can be made on a specific address or a given image.

If you would like to use the app with the deployed GUI you can visit:
https://huggingface.co/spaces/ArielDrabkin/Solar-Panel-Detector

--------

## Usage

To run the solar panel detector locally:

1. clone the repository with the following command:

``` 
git clone https://github.com/ArielDrabkin/Solar-Panel-Detector.git
```

2. Install the required packages with the following command:

```
pip install -r requirements.txt
```

3. The script can be executed with several command-line arguments:

* -k, --api_key: (Optional) Your API key for mapping services.
* -a, --address: (Optional) Address for prediction.
* -z, --zoom: (Optional) Image Zoom level, default is 19.
* -i, --image_dir: (Optional) Directory of images for applying predictions.
  Once you are predicting on an address the predicted image will automatically be saved in the "src" folder.

4. To predict on an address, first If you will need to get a Google Maps API key
   at https://developers.google.com/maps/documentation/maps-static/get-api-key.

5. **Predicting Using Address Only:**  
   To get predictions based on an address, first update your Google Maps API key in the "secret.json" file
   Then use the -a or --address argument:

```
python main.py --address "1600 Pennsylvania Avenue NW, Washington, United States"
```

6. **Predicting Using a Custom API Key:**  
   Alternatively, if you have a custom API key and wish to use it instead of the one in ../secret.json, use the -k or
   --api_key argument:

```
python main.py --api_key "YOUR_CUSTOM_API_KEY" --address "1600 Pennsylvania Avenue NW, Washington, United States"
```

7. **Predicting with Image Analysis:**  
   To perform image analysis on a specific image, use the -i or --image_dir argument:

```
python main.py --image_dir "/path/to/image/directory"
```

Ensure that the specified directory contains the images you want to analyze.

8. Predict and Enjoy  
   ![](https://media2.giphy.com/media/l5D4Zr95KJdUd1E7jt/200.gif?cid=82a1493bvrrr37gb80ycpjqds92n6ybwud9ebiebre854ocw&ep=v1_gifs_related&rid=200.gif&ct=g)

--------

## Training

For using the data set for retraining a model you will need to get a secret key from roboflow where the data is stored
and then
update the secret.json file with the key and run the following code:

```
# Load the data sets from roboflow
with open("secret.json") as file:
    roboflow_api_key = json.load(file)["roboflow_api_key"]
rf = Roboflow(api_key=roboflow_api_key)
project = rf.workspace("ariel-drabkin-tifqg").project("solar-panel-detector-imvoh")
dataset = project.version(1).download("yolov8")
```

--------

## References

--------

## Aknowledgements

--------
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
