import gradio as gr
import os
from SolarPanelDetector import solar_panel_predict, detector

# Custom CSS for styling the app
custom_css = """
.feedback textarea {font-size: 20px !important;}
.centered-text {text-align: center; width: 100%;}
.center-image {display: flex; justify-content: center; align-items: center;}
"""
# URL for the logo image
logo_url = 'https://raw.githubusercontent.com/ArielDrabkin/Solar-Panel-Detector/master/deployment/examples/DALL-E.jpeg'

# Starting Gradio app configuration
with gr.Blocks(theme="HaleyCH/HaleyCH_Theme", title="Solar Panel Detector", css=custom_css) as app:
    # Main title for the app
    gr.Markdown("# **Solar Panel Detector 2.0** 🛰️☀️", elem_classes="centered-text")

    # Displaying the logo
    with gr.Row(elem_classes="center-image"):
        gr.Image(logo_url, scale=1, height=450, width=700, show_label=False, show_download_button=False,
                 show_share_button=False)

    # Description for using the app with address and Google Maps API
    gr.Markdown(
        "## This app provides the ability to detect solar panels in a given address or a given satellite image.")

    # Instructions for address-based detection
    gr.Markdown("### Using by address with google maps:\n1. Enter an address or geographic coordinates.\n"
                "2. Insert your Google maps api key which you can get from - "
                "https://developers.google.com/maps/documentation/maps-static/get-api-key .\n"
                "3. Choose the zoom level (19 is the default).")
    address = gr.Textbox(label="Address")
    api_key = gr.Textbox(label="Google maps api key", type="password")
    zoom = gr.Slider(minimum=18, maximum=22, step=1, value=19, label="zoom")
    btn = gr.Button(value="Submit")

    # Layout for displaying predictions for address-based detection
    with gr.Row():
        predicted_image_address = gr.Image(type="pil", show_label=False, scale=1)
        prediction_address = gr.Textbox(type="text", show_label=False, scale=1, elem_classes="feedback")
    btn.click(detector, inputs=[address, api_key, zoom], outputs=[predicted_image_address, prediction_address])

    # Description for image-based detection
    gr.Markdown("### Using by a given image:\nUpload an image or use the examples below.")
    with gr.Row():
        im = gr.Image(type="pil", show_label=False, scale=1)
        predicted_image = gr.Image(type="pil", show_label=False, scale=1)

    # Layout for displaying predictions for image-based detection
    prediction = gr.Textbox(type="text", show_label=False, elem_classes="feedback")
    btn = gr.Button(value="Submit")

    # Function call for image-based detection
    btn.click(solar_panel_predict, inputs=im, outputs=[predicted_image, prediction])

    # Providing example images for quick testing
    gr.Markdown("### Image Examples")
    gr.Examples(
        examples=[os.path.join(os.path.dirname(__file__), "examples/Gottingen.jpg"),
                  os.path.join(os.path.dirname(__file__), "examples/Tubingen.jpg"),
                  os.path.join(os.path.dirname(__file__), "examples/San-Diego.jpg"),
                  os.path.join(os.path.dirname(__file__), "examples/Ceske-Budejovice.jpg")],
        inputs=im,
        outputs=[predicted_image, prediction],
        fn=solar_panel_predict,
        cache_examples=False,
    )

if __name__ == "__main__":
    app.launch()
