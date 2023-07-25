# https://www.youtube.com/watch?v=VqgUkExPvLY
# Sven - Build a website in 12 minutes using python and streamlit

import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sonali's Webpage", page_icon = ":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#lottie_coding = load_lottieurl("https://lottie.host/?file=ad42b5ea-1aef-4dbd-9254-962192746370/5rKO2onOpb.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi, this is Sonali :wave:")
    st.title("A Data Scientist from Seattle")
    st.write("[Check out my meetup](https://www.meetup.com/destination-health-equity/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Community")
        st.write("##")
        st.write(
            """
            We have participants from diverse fields. They are wonderful!! """
        )
    with right_column:
        st_lottie(lottie_coding, height = 300, key = "coding")
