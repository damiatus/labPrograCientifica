# Bosquejo del proyecto entero:

¡Perfecto! Gracias por el detalle del enunciado. Para la **Entrega 1**, nuestro objetivo principal será diseñar un modelo inicial basado en los datos disponibles y prepararnos para generar las predicciones que se subirán a CodaLab. Te guiaré paso a paso para lograr un enfoque sólido, eficiente y bien documentado. Aquí te detallo cómo proceder:

---

### **Paso 1: Configuración y Entorno de Trabajo**

1. **Entorno reproducible:**

   - Configura un entorno virtual con todas las librerías necesarias para el proyecto:
     ```bash
     python -m venv env
     source env/bin/activate
     pip install numpy pandas scikit-learn matplotlib seaborn jupyterlab
     ```
   - Mantén un archivo `requirements.txt` actualizado para facilitar la replicabilidad.
     ```bash
     pip freeze > requirements.txt
     ```

2. **Estructura del proyecto:**
   - **`notebooks/`**: Jupyter Notebooks con análisis, modelado e informe.
   - **`data/`**: Carpeta para los archivos `.parquet`.
   - **`src/`**: Funciones auxiliares reutilizables (ej. preprocesamiento, visualización, etc.).
   - **`outputs/`**: Carpeta para los archivos que se suben a CodaLab.

---

### **Paso 2: Análisis Exploratorio de Datos (EDA)**

El primer paso será entender los datos proporcionados:

1. **Carga de los archivos:**

   ```python
   import pandas as pd

   X_t0 = pd.read_parquet('data/X_t0.parquet')
   y_t0 = pd.read_parquet('data/y_t0.parquet')
   ```

   - **Verifica las primeras filas, tipos de datos y valores faltantes:**
     ```python
     print(X_t0.head())
     print(X_t0.info())
     print(X_t0.isnull().sum())
     print(y_t0.value_counts(normalize=True))  # Balance de clases
     ```

2. **Distribuciones y correlaciones:**

   - Visualiza las distribuciones de las variables y la relación con la variable objetivo (`y_t0`).
   - Identifica valores atípicos o inconsistencias.

3. **Observaciones clave del EDA:**
   - ¿Qué tipo de variables predominan (numéricas, categóricas)?
   - ¿Qué tan balanceadas están las clases? Si hay desbalance, considera métodos como **SMOTE** o **estratificación** al dividir datos.

---

### **Paso 3: Preprocesamiento Inicial**

Basado en el EDA, realiza transformaciones como:

1. **Tratamiento de valores faltantes:**

   - Imputación de medias/medianas para numéricas.
   - Categoría especial o moda para categóricas.

2. **Codificación de variables categóricas:**

   - Usa **One-Hot Encoding** o **Label Encoding**, dependiendo del modelo.

3. **Escalado de datos numéricos:**

   - Aplica escalado estándar o normalización, especialmente si utilizas modelos basados en distancias (ej. SVM, KNN).

4. **División del conjunto de datos:**

   ```python
   from sklearn.model_selection import train_test_split

   X_train, X_val, y_train, y_val = train_test_split(
       X_t0, y_t0, test_size=0.2, stratify=y_t0, random_state=42
   )
   ```

---

### **Paso 4: Modelado Inicial**

Para la entrega inicial, optaremos por modelos rápidos y sencillos:

1. **Modelos sugeridos:**

   - Árboles de decisión.
   - Regresión logística.
   - Random Forest (para establecer una línea base).

2. **Pipeline básico:**

   ```python
   from sklearn.ensemble import RandomForestClassifier
   from sklearn.metrics import classification_report, roc_auc_score

   model = RandomForestClassifier(random_state=42)
   model.fit(X_train, y_train)

   y_pred = model.predict(X_val)
   print(classification_report(y_val, y_pred))
   print("AUC:", roc_auc_score(y_val, model.predict_proba(X_val)[:, 1]))
   ```

---

### **Paso 5: Generación de Predicciones para CodaLab**

1. **Carga de `X_t1`:**

   ```python
   X_t1 = pd.read_parquet('data/X_t1.parquet')
   ```

2. **Generación de predicciones:**

   ```python
   y_pred_t1 = model.predict_proba(X_t1)[:, 1]  # Probabilidades de la clase positiva
   predictions = pd.DataFrame({'id': X_t1['id'], 'probability': y_pred_t1})
   ```

3. **Guardar archivo para entrega:**
   Usa la función `generateFiles` proporcionada:

   ```python
   from generateFiles import generateFiles

   generateFiles(predictions, output_path="outputs/predictions_t1.csv")
   ```

---

### **Paso 6: Documentación**

1. **Inicia un Notebook:**

   - **EDA**: Gráficos y observaciones.
   - **Preprocesamiento**: Justifica las decisiones tomadas.
   - **Modelo inicial**: Desempeño en validación, limitaciones, próximos pasos.

2. **Gráficos clave:**
   - Matriz de correlación.
   - Distribución de la probabilidad predicha para ambas clases.

---

### **Paso 7: Iteración y Ajustes**

1. Evalúa el desempeño inicial:
   - Si la métrica principal es **AUC**, optimiza para esta.
   - Revisa errores comunes y patrones en los datos mal clasificados.
2. Planea mejoras para la **Entrega 2**:
   - Incorporar selección de características.
   - Explorar técnicas avanzadas como Gradient Boosting (XGBoost, LightGBM).

---

### **Siguientes Pasos**

1. Completa el EDA y preprocesamiento.
2. Diseña y entrena un modelo base.
3. Genérame cualquier consulta técnica o sobre decisiones que desees ajustar.

Estoy aquí para guiarte en cada paso, ¡avancemos juntos! 🚀
