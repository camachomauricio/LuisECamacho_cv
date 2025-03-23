import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import plotly.graph_objects as go

st.set_page_config(page_title="Breast Cancer Classifier", layout="wide")
st.title("🧬 Breast Cancer Classification App")

st.write("This interactive tool uses a machine learning model to classify breast cancer as malignant or benign.")

# Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Sidebar input for each feature
st.sidebar.header("Input Features")
user_input = []

for feature in df.columns[:-1]:
    min_val = float(df[feature].min())
    max_val = float(df[feature].max())
    mean_val = float(df[feature].mean())
    val = st.sidebar.slider(feature, min_val, max_val, mean_val)
    user_input.append(val)

user_input = np.array(user_input).reshape(1, -1)

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
min_vals = df.iloc[:, :-1].min()
max_vals = df.iloc[:, :-1].max()
normalized_input = (user_input[0] - min_vals) / (max_vals - min_vals)

# Select a subset of features to keep the chart readable
features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness']
r_values = [normalized_input[df.columns.get_loc(feature)] for feature in features]

fig = go.Figure(
    data=go.Scatterpolar(
        r=r_values,
        theta=features,
        fill='toself',
        name='User Input Features'
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

# Optional: Show input data
with st.expander("📄 See Your Input Data"):
    st.write(pd.DataFrame(user_input, columns=df.columns[:-1]))
