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
    ├── notebooks          <- Jupyter notebooks.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── final model training results        <- Generated graphics and figures to be used in reporting
    │
    ├── scripts             <- Source code for various stages of the project
    ├── training            <- Training code for the several experiments made and the final model training.
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── secret               <- Source code for use in this project.

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
* The Predictions can be made on a specific address or a given image

If you would like to use the app with the deployed GUI you can visit:
https://huggingface.co/spaces/ArielDrabkin/Solar-Panel-Detector

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

4.  To predict on an address, first If you will need to get a Google Maps API key
at https://developers.google.com/maps/documentation/maps-static/get-api-key.

5. Predicting Using Address Only:
   To get predictions based on an address, first update your Google Maps API key in the "secret.json" file
   Then use the -a or --address argument:

```
python main.py --address "1600 Pennsylvania Avenue NW, Washington, United States"
```

5. Using a Custom API Key:
   Alternatively, if you have a custom API key and wish to use it instead of the one in ../secret.json, use the -k or
   --api_key argument:

```
python main.py --api_key "YOUR_CUSTOM_API_KEY" --address "1600 Pennsylvania Avenue NW, Washington, United States"
```

6. Predicting with Image Analysis:
   To perform image analysis on a directory of images, use the -i or --image_dir argument:

```
python main.py --image_dir "/path/to/image/directory"
```
Ensure that the specified directory contains the images you want to analyze.
7. Predict and Enjoy
![](https://media2.giphy.com/media/l5D4Zr95KJdUd1E7jt/200.gif?cid=82a1493bvrrr37gb80ycpjqds92n6ybwud9ebiebre854ocw&ep=v1_gifs_related&rid=200.gif&ct=g)
--------

## References

--------

## Aknowledgements

--------
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
