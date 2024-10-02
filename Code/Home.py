import streamlit as st
from streamlit_lottie import st_lottie
from st_pages import Page, show_pages, add_page_title
import requests

st.set_page_config(page_title='Home', page_icon=':dna:', layout="wide",
                   initial_sidebar_state='auto')

show_pages(
    [
        Page("./Code/Home.py", "Home", "🏠"),
        Page("./Code/Web Server.py", "Web Server", ":mag_right:"),
        Page("./Code/User Guide.py", "User Guide", ":question:"),
        Page("./Code/Contact.py", "Contact", ":e-mail:"),
    ]
)

st.sidebar.success("Welcome to Catsoft_Kmalsite!")

st.markdown(f"""
    <style>
        .stApp {{
            background-color: #d6e3ef;
            font-family: 'Arial';
        }}
        ::-webkit-scrollbar {{
            display: none;
        }}
        .main {{
            width: 80%;
            margin:0 auto;
            color: black;
        }}
        h1 {{
            font-size: 5vw;
            color: #DFEEEF;
            text-align: center;
            font-weight: bold;
            margin-top: 2.53vw;
            padding: 2vw;
            background-color: #121549;
            position: fixed;
            height: 15vw;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1;
        }}
        h2 {{
            font-size: 2.67vw;
            margin-top: 12.5vw;
            margin-bottom: 0.83vw;
            text-align:center;
            color: #333333;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .navbar {{
            font-family: sans-serif;
            background-color: #a5bdcb;
            position: fixed;
            z-index: 1;  
            top: 17.5vw;
            left:0;
            border-radius: 0 0 0.83vw 0.83vw;
            width: 100%;
            padding: 0.4vw;
            border: none;
            text-align: center;
        }}
        .navbar a {{
            text-decoration: none;
            font-size: 1.25vw;
            cursor: pointer;
        }}
        .navbar a:hover {{
            color: #93BCE9;
            text-decoration: underline;
        }}
        .active {{
            background-color: transparent !important;
            color: #93BCE9 !important;
            text-decoration: underline;
        }}
        .navbar a:active, .navbar a:focus {{
            color: #93BCE9;
            text-decoration: underline;
            outline: none;
        }}
        .nav-links {{
            list-style-type: none;
            margin-top: 0;
            margin-bottom: 0;
            padding-left: 0;
            display: inline-flex;
        }}
        .nav-links li {{
            flex-grow: 1;
            text-align: center;
        }}
        .nav-links a {{
            display: block;
            color: #8da7cd;
            text-align: center;
            padding: 0.4vw;
            text-decoration: none;
            font-size: 1.3vw;
            cursor: pointer;
        }}
        .nav-links a:hover {{
            color: #144880;
            text-decoration: underline;
            transition: color .3s ease-in-out;
        }}
        .nav-links .active {{
            background-color: transparent !important;
            color: #303186 !important;
            text-decoration: underline;
        }}
        h5 {{
        color:black;
        text-align: justify;
        }}
        h3 {{
        color:black;
        }}
    </style>
""", unsafe_allow_html=True)


# 添加导航栏
st.markdown("""
    <h1>Welcome to Catsoft_Kmalsite! 👋<br>Here is a Kmal Sites Prediction Platform</h1>
    <nav class="navbar">
    <ul class="nav-links">
        <li><a class="button-link active" href="#Home">Home</a></li>
        <li><a class="button-link" href="#Web Server">Web Server</a></li>
        <li><a class="button-link" href="#User Guide">User Guide</a></li>
        <li><a class="button-link" href="#Contact">Contact</a></li>
    </ul>
    </nav>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
        .markdown-text-container {
            margin-top: 20%;
            margin-left: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("""<h2 style="margin-top: 13vw;">Introduction</h2>""", unsafe_allow_html=True)

st.markdown(
    """
    <h5 style="text-align:center">Welcome to <span style="color:red">Catsoft_Kmalsite</span> user interaction platform! <br> This is a user-friendly tool designed specifically for lysine malonylation site prediction using Catsoft_Kmalsite.</h5>
"""
, unsafe_allow_html=True)

from PIL import Image
image = Image.open("./Code/protein.png")
# 指定新的宽度和高度
new_width = 500
new_height = 300

# 调整图像大小
resized_image = image.resize((new_width, new_height))

# 显示调整大小后的图像
st.image(resized_image, use_column_width=True, output_format='auto')


st.markdown(
    """
    
    <div style="color:white;background-color:#0b2453;padding:1.67vw;width:100%">
    <h5 style="color:white;background-color:#0b2453;padding:1.67vw;width:100%"> On this platform, you can:</h5>
        <ul>
            <li>Quickly input protein sequences and structural information.</li>
            <li>Run the Catsoft_Kmalsite prediction model to obtain accurate and reliable predictions of protein acetylation sites.</li>
            <li>Easily browse and analyze the prediction results for further research and applications.</li>
        </ul>
    </div>
    """
    , unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .button {
      background-color: #46B3A8;
      border: none;
      border-radius: 1vw;
      color: white;
      padding: 1.25vw 2.67vw;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 1.5vw;

    }

    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="button">Start using our platform immediately!</div>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <p style="color:#D26A10;font-size: 2.08vw">**👈 To start predicting, please click on the sidebar.</p>
"""
, unsafe_allow_html=True)
