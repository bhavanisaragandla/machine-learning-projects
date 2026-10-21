# Flight Price Prediction

## Project Overview

A machine learning project that predicts flight ticket prices using flight-related features.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Docker

## Project Files

* `Flight Price Prediction.ipynb` — Model training and evaluation.
* `model.pkl` — Saved trained model.
* `app.py` — Prediction web application.
* `requirements.txt` — Python dependencies.
* `Dockerfile` — Docker deployment configuration.

## Run with Docker

Build the Docker image:

```bash
docker build -t flight-price-prediction .
```

Run the container:

```bash
docker run -p 8501:8501 flight-price-prediction
```

Open http://localhost:8501 in your browser.
