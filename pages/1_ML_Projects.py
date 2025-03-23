import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

st.title("🌱 ML Demo: Iris Flower Classifier")

st.write("This is a basic classification app using scikit-learn and Streamlit.")

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

st.subheader("Input Features")
sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 4.35)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 1.3)

X = df
y = iris.target
model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
predicted_species = iris.target_names[prediction][0]

st.success(f"🌼 Predicted Iris Species: **{predicted_species}**")
