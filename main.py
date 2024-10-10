# <==== Importing Dependencies ====>

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

# <==== Code starts here ====>

courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)

    return recommended_course_names

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
        background-size: cover;
    }
    .main {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 15px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center; color: blue; font-family: Arial, Helvetica, sans-serif;'>Coursera Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black; font-family: Arial, Helvetica, sans-serif;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)

course_list = courses_list['course_name'].values
selected_course = st.selectbox(
    "Type or select a course you like:",
    course_list,
    help="Start typing to search for a course, or select from the dropdown."
)

if st.button('Show Recommended Courses'):
    st.markdown("<h3 style='text-align: center; color: black; font-family: Arial, Helvetica, sans-serif;'>Recommended Courses</h3>", unsafe_allow_html=True)
    recommended_course_names = recommend(selected_course)
    for i, course in enumerate(recommended_course_names):
        st.markdown(f"<h5 style='text-align: center; color: green; font-family: Arial, Helvetica, sans-serif;'>{i+1}. {course}</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: red; font-family: Arial, Helvetica, sans-serif;'>Copyright reserved by Coursera and Respective Course Owners</h6>", unsafe_allow_html=True)
