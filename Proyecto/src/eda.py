import pandas as pd
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def eda(dataframe):
    """
    Realiza un análisis exploratorio de datos (EDA) en un DataFrame de pandas.
    
    Parámetros:
    - dataframe (pd.DataFrame): El DataFrame a analizar.

    Retorna:
    - None (imprime los resultados del análisis en consola).
    """
    try:
        # Configuración de pandas para la visualización
        pd.options.display.max_rows = 200
        pd.set_option('display.max_columns', None)

        # Dimensiones del DataFrame
        logging.info(f'1.- El DataFrame tiene {dataframe.shape[0]} filas y {dataframe.shape[1]} columnas\n')
        
        # Columnas del DataFrame
        logging.info(f'2.- Columnas del DataFrame: {list(dataframe.columns)}\n')
        
        # Ejemplos de filas
        logging.info('3.- Ejemplos de filas del DataFrame:\n')
        logging.info('Primeras 5 filas:')
        display(dataframe.head(5))
        logging.info('Últimas 5 filas:')
        display(dataframe.tail(5))
        logging.info('Muestreo aleatorio de 5 filas:')
        display(dataframe.sample(5, random_state=42))
        
        # Descripción numérica
        logging.info('4.- Descripción numérica del DataFrame:')
        display(dataframe.describe(include='all'))
        
        # Valores nulos
        logging.info('5.- Cantidad de valores nulos por columna:')
        display(dataframe.isna().sum())
        
        # Valores únicos
        logging.info('6.- Cantidad de valores únicos por columna:')
        unique_values = dataframe.nunique()
        display(unique_values)
        
        # Tipos de datos
        logging.info('7.- Tipos de datos por columna:')
        display(dataframe.dtypes)
        
        # Filas duplicadas
        logging.info('8.- Cantidad de filas duplicadas en el DataFrame:')
        logging.info(f'{dataframe.duplicated().sum()} filas duplicadas\n')
        
        # Variables categóricas con <= 6 categorías
        logging.info('9.- Distribución de variables categóricas con a lo más 6 categorías:')
        for column in dataframe.columns:
            if unique_values[column] <= 6:
                logging.info(f'\nColumna: {column}')
                display(dataframe[column].value_counts())
                display(dataframe[column].value_counts(normalize=True) * 100)

    except Exception as e:
        logging.error(f"Error durante el EDA: {e}")
