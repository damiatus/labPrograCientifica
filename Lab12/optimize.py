import pandas as pd
import optuna
import mlflow
import mlflow.xgboost
import xgboost as xgb
import pickle
import os
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from optuna.visualization.matplotlib import plot_optimization_history, plot_param_importances
import sys
import sklearn

file_path = ''
df = pd.read_csv(file_path + "./water_potability.csv")

X = df.drop(columns=["Potability"])
y = df["Potability"]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=20676305)

def get_best_model(experiment_id):
    runs = mlflow.search_runs(experiment_id)
    best_model_id = runs.sort_values("metrics.valid_f1")["run_id"].iloc[0]
    best_model = mlflow.sklearn.load_model("runs:/" + best_model_id + "/model")
    return best_model

def objective(trial):
    params = {
        'objective': 'binary:logistic',
        'eval_metric': 'logloss',
        'learning_rate': trial.suggest_loguniform('learning_rate', 0.01, 0.3),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'subsample': trial.suggest_uniform('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_uniform('colsample_bytree', 0.5, 1.0),
        'n_estimators': trial.suggest_int('n_estimators', 50, 300)
    }

    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)

    preds = model.predict(X_valid)
    valid_f1 = f1_score(y_valid, preds, average='macro')

    with mlflow.start_run(run_name=f"XGBoost con lr {params['learning_rate']}"):
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_param('learning_rate', params['learning_rate'])
        mlflow.log_param('max_depth', params['max_depth'])
        mlflow.log_param('subsample', params['subsample'])
        mlflow.log_param('colsample_bytree', params['colsample_bytree'])
        mlflow.log_param('n_estimators', params['n_estimators'])
        mlflow.log_metric('valid_f1', valid_f1)

    return valid_f1

def optimize_model():
    base_path = '/home/damiatus/labPrograCientifica/Lab12/'

    mlflow.set_experiment("XGBoost Optimization")

    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=30)

    def log_libraries_versions():
        with open(base_path + "/libs_versions.txt", 'w') as f:
            f.write(f"Python version: {sys.version}\n")
            f.write(f"optuna version: {optuna.__version__}\n")
            f.write(f"mlflow version: {mlflow.__version__}\n")
            f.write(f"xgboost version: {xgb.__version__}\n")
            f.write(f"scikit-learn version: {sklearn.__version__}\n")

        mlflow.set_tag("python_version", sys.version)
        mlflow.set_tag("optuna_version", optuna.__version__)
        mlflow.set_tag("mlflow_version", mlflow.__version__)
        mlflow.set_tag("xgboost_version", xgb.__version__)
        mlflow.set_tag("sklearn_version", sklearn.__version__)

    with mlflow.start_run():
        log_libraries_versions()
        best_model = get_best_model(mlflow.active_run().info.experiment_id)
        model_path = os.path.join(base_path, 'models', 'best_model.pkl')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, 'wb') as f:
            pickle.dump(best_model, f)

        os.makedirs(os.path.join(base_path, 'plots'), exist_ok=True)
        fig_optimization = plot_optimization_history(study)
        fig_optimization.figure.savefig(os.path.join(base_path, 'plots', 'optimization_history.png'))

        fig_importances = plot_param_importances(study)
        fig_importances.figure.savefig(os.path.join(base_path, 'plots', 'param_importances.png'))

        mlflow.log_artifact(os.path.join(base_path, 'plots', 'optimization_history.png'), artifact_path='plots')
        mlflow.log_artifact(os.path.join(base_path, 'plots', 'param_importances.png'), artifact_path='plots')

        fig, ax = plt.subplots()
        xgb.plot_importance(best_model, ax=ax)
        plt.savefig(os.path.join(base_path, 'plots', 'variable_importances.png'))
        mlflow.log_artifact(os.path.join(base_path, 'plots', 'variable_importances.png'), artifact_path='plots')

if __name__ == '__main__':
    optimize_model()

