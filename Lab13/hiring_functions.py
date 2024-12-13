
from datetime import datetime
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, f1_score
import joblib
import gradio as gr

def create_folders():
    execution_date = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = f"pathdags/{execution_date}"
    os.makedirs(os.path.join(base_path, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'splits'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'models'), exist_ok=True)
    return base_path

def split_data(base_path):
    data = pd.read_csv('pathdags/raw/data_1.csv')
    train, test = train_test_split(data, test_size=0.2, stratify=data['HiringDecision'], random_state=20676305)

    train.to_csv(os.path.join(base_path, 'splits', 'train.csv'), index=False)
    test.to_csv(os.path.join(base_path, 'splits', 'test.csv'), index=False)
    print(f"Datos divididos y guardados en {base_path}/splits")

def preprocess_and_train(base_path):
    train_data = pd.read_csv(os.path.join(base_path, 'splits', 'train.csv'))
    test_data = pd.read_csv(os.path.join(base_path, 'splits', 'test.csv'))

    X_train = train_data.drop(columns=['HiringDecision'])
    y_train = train_data['HiringDecision']
    X_test = test_data.drop(columns=['HiringDecision'])
    y_test = test_data['HiringDecision']

    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(), categorical_features)
        ])

    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', RandomForestClassifier(random_state=20676305))])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"F1 Score (Contratado): {f1}")

    model_path = os.path.join(base_path, 'models', 'hiring_pipeline.joblib')
    joblib.dump(pipeline, model_path)

    return model_path


def predict(file,model_path):

    pipeline = joblib.load(model_path)
    input_data = pd.read_json(file)
    predictions = pipeline.predict(input_data)
    print(f'La prediccion es: {predictions}')
    labels = ["No contratado" if pred == 0 else "Contratado" for pred in predictions]

    return {'Predicción': labels[0]}


def gradio_interface():
    model_path = "pathdags/models/hiring_pipeline.joblib"
    interface = gr.Interface(
        fn=lambda file: predict(file, model_path),
        inputs=gr.File(label="Sube un archivo JSON"),
        outputs="json",
        title="Hiring Decision Prediction",
        description="Sube un archivo JSON con las características de entrada para predecir si una persona será contratada o no."
    )
    interface.launch(share=True)