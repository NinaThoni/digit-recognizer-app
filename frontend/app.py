import sys 
sys.path.append("./")

import streamlit as st
import torch
import numpy as np
import torchvision.transforms as transforms
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from model.model import DigitClassifier
from database.db import insert_prediction, fetch_predictions, init_db

init_db() 

# Load model
MODEL_PATH = "model/mnist_cnn.pth"
model = DigitClassifier()
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Streamlit UI
st.title("Digit Recognizer 🖌️")
st.write("Draw a digit below, enter the correct digit, and get a prediction!")

# Create drawing canvas
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    height=200,
    width=200,
    drawing_mode="freedraw",
    key="canvas"
)

# Always show the true label input field
true_label = st.text_input("Enter the correct digit (required):", "")

# Disable "Predict" button if true label is empty
predict_button_disabled = true_label.strip() == "" or not true_label.isdigit() or not (0 <= int(true_label) <= 9)

# Predict button (only enabled when true label is valid)
predict_button = st.button("Predict", disabled=predict_button_disabled)

if predict_button:
    if canvas_result.image_data is not None:
        img_array = (canvas_result.image_data[:, :, :3] * 255).astype("uint8")  
        img = Image.fromarray(img_array).convert("L") 
        img = transform(img)
        img = img.unsqueeze(0)

        with torch.no_grad():
            output = model(img)
            prediction = torch.argmax(output, dim=1).item()
            confidence = torch.nn.functional.softmax(output, dim=1)[0][prediction].item() * 100

        st.write(f"Prediction: **{prediction}**")
        st.write(f"Confidence: **{confidence:.2f}%**")

        # Insert into database
        insert_prediction(prediction, int(true_label))
        st.success("Prediction and true label logged successfully!")

# **Display past predictions**
st.subheader("Prediction History 📜")
history_data = fetch_predictions()

if history_data:
    st.dataframe(history_data)  # Display as a table
else:
    st.write("No previous predictions recorded.")


