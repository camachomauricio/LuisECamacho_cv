import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Example")

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [23, 45, 12, 67]
}
df = pd.DataFrame(data)

st.subheader("Data Table")
st.dataframe(df)

st.subheader("Bar Chart")
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")
st.plotly_chart(fig)
