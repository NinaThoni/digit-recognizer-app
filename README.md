# Digit Recognizer

A web-based digit recognition app built with **PyTorch**, **Streamlit**, and **PostgreSQL**, deployed using **Docker Compose**. Users can draw digits in the browser, receive predictions, and log them to a local database with their true label for tracking model performance.

---

##  Features

-  Trained PyTorch CNN model for digit classification (MNIST)
-  Streamlit UI with a drawable canvas for digit input
-  Logging predictions & user-provided true labels to PostgreSQL
-  Fully containerized with Docker + Docker Compose
-  Auto table creation on startup (robust deployment)
-  Persistent volume storage for PostgreSQL

---

##  Tech Stack

| Layer           | Tool/Tech          |
|------------------|---------------------|
| Frontend / UI     | [Streamlit](https://streamlit.io) |
| Model Inference   | [PyTorch](https://pytorch.org) |
| Image Processing  | [Torchvision](https://pytorch.org/vision/) |
| Database          | [PostgreSQL](https://www.postgresql.org/) |
| Canvas Input      | [streamlit-drawable-canvas](https://github.com/andfanilo/streamlit-drawable-canvas) |
| Containerization  | Docker & Docker Compose |

---

##  Demo

![image](https://github.com/user-attachments/assets/afbce585-1727-401c-86db-454d5d5359f9)


---

##  How It Works

1. Users draw a digit on the canvas
2. The image is preprocessed and passed to a pre-trained CNN model
3. The predicted digit and user-provided true label are logged to the database
4. A history of recent predictions is displayed below the app

---

##  Local Setup

### Prerequisites

- Docker
- Docker Compose

### File Structure

<pre> ```none digit-recognizer/ │ ├── model/ # Saved PyTorch model (.pth) │ ├── model.py │ └── train.py │ ├── database/ │ └── db.py # PostgreSQL connection and logging logic │ ├── frontend/ │ └── app.py # Streamlit app │ ├── Dockerfile # Dockerfile for the app container ├── docker-compose.yml # Multi-container setup (App + DB) ├── requirements.txt # Python dependencies └── .env # Environment variables (not committed) ``` </pre>
