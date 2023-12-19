Solar-Panel-Detector 🛰️☀️
==============================
![](https://raw.githubusercontent.com/ArielDrabkin/Solar-Panel-Detector/master/deployment/examples/spd-demo.gif)

--------

## Overview
The Solar-Panel-Detector is an innovative AI-driven tool designed to identify solar panels in satellite imagery. 
Utilizing the state-of-the-art YOLOv8 object-detection model and various cutting-edge technologies, this project demonstrates how AI can be leveraged for environmental sustainability.

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

The Solar-Panel-Detector app analyzes satellite images to detect the presence of solar panels, serving both environmental research and the solar energy market. 
It provides insights into potential areas for solar panel installation and aids in understanding the spread of solar energy usage.

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
### Predicting an address
If you want to use the predictor to predict on an address you will need to get a Google Maps API key at https://developers.google.com/maps/documentation/maps-static/get-api-key.
Once you have the key you will need to replace the placeholder key and update it in the secret.json file.
then you can run the main.py file with the desired address.

### Predicting on a local image
If you want to use the predictor to predict on a local image you will need to run the Predict.py file with the desired image path.
```
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

--------
## References

--------
## Aknowledgements