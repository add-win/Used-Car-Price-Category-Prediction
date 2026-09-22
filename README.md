# Used Car Price Category Prediction

A lightweight machine learning web app that predicts the price category of a used car based on:

- Car age
- Kilometers driven

The app uses a trained scikit-learn model and a Gradio interface for an easy interactive prediction experience.

## Project Overview

This project is designed to estimate which price category a used car falls into using a simple machine learning pipeline. It is suitable for demonstration, learning, and quick deployment as a small web app.

## Features

- Predict price category from car age and mileage
- Simple Gradio user interface
- Easy local deployment
- Lightweight and fast to run

## Tech Stack

- Python
- Gradio
- pandas
- scikit-learn
- joblib

## Installation

1. Clone the repository.
2. Navigate to the project folder.
3. Create a virtual environment (optional but recommended).
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python app.py
```

Once the app starts, open the local URL shown in the terminal (usually http://localhost:7860).

## How It Works

The app loads a saved model file named `used_car_random_forest.pkl` and accepts two inputs:

- `Car_Age`
- `Kilometers_Driven`

It then predicts the car's price category and displays the result in the Gradio interface.

## Example Usage

- Car Age: 5
- Kilometers Driven: 45000

The model returns a predicted price category such as:

```text
Predicted Car Price Category: Low
```

## File Structure

```text
Used-Car-Price-Category-Prediction/
├── app.py
├── requirements.txt
├── used_car_random_forest.pkl
├── README.md
```

## Notes

- The model file must be present in the project directory for the app to run successfully.
- You can modify the app UI and input parameters in `app.py` if needed.

## License

This project is for educational and demonstration purposes.
