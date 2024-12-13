import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from datetime import datetime

base_path = 'pathdags'

def create_folders(base_path):
    execution_date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_name = os.path.join(base_path, execution_date)

    os.makedirs(os.path.join(folder_name, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(folder_name, 'preprocessed'), exist_ok=True)
    os.makedirs(os.path.join(folder_name, 'splits'), exist_ok=True)
    os.makedirs(os.path.join(folder_name, 'models'), exist_ok=True)

    print(f"Carpetas creadas en: {folder_name}")
    return folder_name

def load_and_merge(folder_name):
    raw_folder = os.path.join(folder_name, 'raw')
    data_1_path = os.path.join(raw_folder, 'data_1.csv')
    data_2_path = os.path.join(raw_folder, 'data_2.csv')

    data_1 = pd.read_csv(data_1_path)
    if os.path.exists(data_2_path):
        data_2 = pd.read_csv(data_2_path)
        data = pd.concat([data_1, data_2], ignore_index=True)
    else:
        data = data_1

    preprocessed_path = os.path.join(folder_name, 'preprocessed', 'merged_data.csv')
    data.to_csv(preprocessed_path, index=False)
    print(f"Datos guardados en: {preprocessed_path}")
    return preprocessed_path

def split_data(folder_name):
    preprocessed_path = os.path.join(folder_name, 'preprocessed', 'merged_data.csv')
    data = pd.read_csv(preprocessed_path)

    X = data.drop(columns=['HiringDecision'])
    y = data['HiringDecision']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20676305, stratify=y)

    splits_folder = os.path.join(folder_name, 'splits')
    X_train.to_csv(os.path.join(splits_folder, 'X_train.csv'), index=False)
    X_test.to_csv(os.path.join(splits_folder, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(splits_folder, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(splits_folder, 'y_test.csv'), index=False)

    print(f"Conjuntos de datos guardados en: {splits_folder}")

def train_model(folder_name, model):
    splits_folder = os.path.join(folder_name, 'splits')

    X_train = pd.read_csv(os.path.join(splits_folder, 'X_train.csv'))
    y_train = pd.read_csv(os.path.join(splits_folder, 'y_train.csv'))

    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object']).columns

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])

    pipeline.fit(X_train, y_train.values.ravel())

    model_folder = os.path.join(folder_name, 'models')
    model_path = os.path.join(model_folder, f'{model.__class__.__name__}_model.joblib')
    joblib.dump(pipeline, model_path)
    print(f"Modelo guardado en: {model_path}")
    return model_path

def evaluate_models(folder_name):
    splits_folder = os.path.join(folder_name, 'splits')
    models_folder = os.path.join(folder_name, 'models')

    X_test = pd.read_csv(os.path.join(splits_folder, 'X_test.csv'))
    y_test = pd.read_csv(os.path.join(splits_folder, 'y_test.csv'))

    best_accuracy = 0
    best_model_name = None

    for model_file in os.listdir(models_folder):
        model_path = os.path.join(models_folder, model_file)
        model = joblib.load(model_path)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        print(f"Modelo: {model_file}, Accuracy: {accuracy}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model_name = model_file

    print(f"Mejor modelo: {best_model_name}, con Accuracy: {best_accuracy}")
    return best_model_name