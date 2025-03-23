import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Breast Cancer Classifier", layout="wide")
st.title("🧬 Breast Cancer Classification App")

st.write("This interactive tool uses a machine learning model to classify breast cancer as malignant or benign.")

# Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Sidebar input for selecting a data row
index = st.slider("Select a data sample index", 0, len(df)-1, 0)
user_input = df.iloc[index, :-1].values.reshape(1, -1)

# Train model
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df['target'], test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make prediction
prediction = model.predict(user_input)[0]
pred_label = data.target_names[prediction]

st.subheader("🔍 Model Prediction")
st.write(f"The model predicts this tumor is: **{pred_label.capitalize()}**")

# Accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
st.metric(label="Model Accuracy", value=f"{acc * 100:.2f}%")

# Radar chart
st.subheader("📊 Feature Radar Chart")

# Normalize input for radar plot (0 to 1 scale)
normalized = (df.iloc[index, :-1] - df.iloc[:, :-1].min()) / (df.iloc[:, :-1].max() - df.iloc[:, :-1].min())

# Select a subset of features to keep the chart readable
features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']
r_values = [normalized[feature] for feature in features]

fig = go.Figure(
    data=go.Scatterpolar(
        r=r_values,
        theta=features,
        fill='toself',
        name='Sample Features'
    )
)

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        )
    ),
    showlegend=False,
    title="Radar Chart of Selected Features"
)

st.plotly_chart(fig, use_container_width=True)

# Optional: Show data sample
with st.expander("📄 See Raw Data for Selected Sample"):
    st.write(df.iloc[[index]])