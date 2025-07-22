
import streamlit as st
import pandas as pd
from utils.recommender import get_user_recommendations

st.set_page_config(page_title="AI Recommender", layout="centered")

st.title("🎬 AI-Powered Movie Recommendation System")
st.markdown("Get personalized movie suggestions using collaborative filtering.")

user_id = st.number_input("Enter User ID (1–610):", min_value=1, max_value=610, step=1)

if st.button("Get Recommendations"):
    recommendations = get_user_recommendations(user_id)
    if not recommendations.empty:
        st.subheader("🎯 Top Recommended Movies:")
        st.dataframe(recommendations)
    else:
        st.warning("No recommendations found for this user.")

st.markdown("---")
st.caption("Powered by Python, Streamlit, and Surprise (SVD)")
