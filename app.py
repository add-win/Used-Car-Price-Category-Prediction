import gradio as gr
import joblib
import pandas as pd
import os

model = joblib.load("used_car_random_forest.pkl")


def predict_result(age, kilo):

    input_data = pd.DataFrame({
        "Car_Age": [age],
        "Kilometers_Driven": [kilo],
    })

    prediction = model.predict(input_poly)[0]

    return f"Predicted Car Price Category: {prediction}"


demo = gr.Interface(
    fn=predict_result,

    inputs=[
        gr.Number(label="Enter the Car Age", minimum=1, value=1),
        gr.Number(label="Enter the Kilometers Driven", minimum=1, value=1),
    ],

    outputs=gr.Textbox(label="Prediction"),

    title="Used Car Price Category Prediction",
    description="Predict car price category based on Car age and kilometers driven."
)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
