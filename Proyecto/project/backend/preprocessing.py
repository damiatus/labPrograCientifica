from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np

# Paso 1: Definir las transformaciones previas
categorical = ['borrow_block_number', 'wallet_address', 'market_ht_trendmode']
datetime_columns = ['borrow_timestamp', 'first_tx_timestamp', 'last_tx_timestamp',
                    'risky_first_tx_timestamp', 'risky_last_tx_timestamp']

datetime_columns_features = ['borrow_timestamp', 'first_tx_timestamp', 'last_tx_timestamp']

columnas_a_excluir = [
    'borrow_block_number', 'wallet_address', 'time_since_last_liquidated',
    'market_ht_trendmode', 'borrow_timestamp', 'first_tx_timestamp',
    'last_tx_timestamp', 'risky_first_tx_timestamp', 'risky_last_tx_timestamp',
    'risky_first_last_tx_timestamp_diff', 'time_since_first_deposit',
    'market_ppo', 'market_rocp', "market_rocr", 'target'
]

# Funciones de preprocesamiento
def convert_to_category(df):
    df[categorical] = df[categorical].astype('category')
    return df

def process_datetime_columns(df):
    df['risky_first_tx_timestamp'] = df['risky_first_tx_timestamp'].replace(999999999, pd.NA)
    df['risky_last_tx_timestamp'] = df['risky_last_tx_timestamp'].replace(999999999, pd.NA)
    for col in datetime_columns:
        df[col] = pd.to_datetime(df[col], unit='s', errors='coerce')
    return df

def extract_temporal_features(df):
    for col in datetime_columns_features:
        if col in df:
            df[f'{col}_year'] = df[col].dt.year
            df[f'{col}_month'] = df[col].dt.month
            df[f'{col}_day'] = df[col].dt.day
            df[f'{col}_weekday'] = df[col].dt.weekday
    return df

def normalize_columns(df):
    cols_a_normalizar = [col for col in df.select_dtypes(include=[np.number]).columns if col not in columnas_a_excluir]
    df_normalized = df.copy()
    for col in cols_a_normalizar:
        mean_val = df_normalized[col].mean()
        std_val = df_normalized[col].std()
        df_normalized[col] = (df_normalized[col] - mean_val) / std_val
    return df_normalized

def exclude_columns(df):
    df_excluded = df.drop(['borrow_block_number', 'wallet_address', "time_since_last_liquidated"], axis=1)
    return df_excluded

def one_hot_encode(df):
    ohe = OneHotEncoder(sparse_output=False)
    encoded = ohe.fit_transform(df[['market_ht_trendmode']])
    encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out(['market_ht_trendmode']))
    df = df.drop('market_ht_trendmode', axis=1).reset_index(drop=True)
    return pd.concat([df, encoded_df], axis=1)

def remove_datetime_columns(df):
    return df.select_dtypes(exclude=['datetime64[ns]'])

# Paso 2: Crear transformadores personalizados
categorical_transformer = FunctionTransformer(convert_to_category, validate=False)
datetime_transformer = FunctionTransformer(process_datetime_columns, validate=False)
temporal_feature_extractor = FunctionTransformer(extract_temporal_features, validate=False)
normalization_transformer = FunctionTransformer(normalize_columns, validate=False)
exclude_transformer = FunctionTransformer(exclude_columns, validate=False)
one_hot_transformer = FunctionTransformer(one_hot_encode, validate=False)
remove_datetime_transformer = FunctionTransformer(remove_datetime_columns, validate=False)

# Pipeline en el orden solicitado con extracción de características temporales
preprocessing_pipeline = Pipeline([
    ('categorical', categorical_transformer),              # Convertimos a categóricas si es necesario
    ('exclude_columns', exclude_transformer),              # Excluimos columnas específicas
    ('one_hot_encoding', one_hot_transformer),             # Aplicamos One-Hot Encoding
    ('datetime', datetime_transformer),                    # Convertimos las columnas datetime
    ('temporal_features', temporal_feature_extractor),     # Extraemos las características temporales
    ('datetime_exclusion', remove_datetime_transformer),   # Excluimos las columnas datetime originales
    ('normalization', normalization_transformer)           # Normalizamos las columnas numéricas
])



