import streamlit as st

st.set_page_config(page_title='Contact', page_icon=':dna:', layout="wide",
                   initial_sidebar_state='auto')

st.sidebar.success("Please contact us if you have any questions!")

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
            width: 50%;
            margin:0 auto;
            color: black;
        }}
        h1 {{
            font-size: 60px;
            color: #DFEEEF;
            text-align: center;
            font-weight: bold;
            margin-top: 40px;
            margin-bottom: 50px;
            padding: 20px;
            background-color: #121549;
            position: fixed;
            height:180px;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1;
        }}
        h2 {{
        font-size: 32px;
        margin-top: 180px;
        margin-bottom: 10px;
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
            top: 220px;
            left:0;
            border-radius: 0 0 10px 10px;
            width: 100%;
            padding: 5px;
            border: none;
            text-align: center;
        }}
        .navbar a {{
            text-decoration: none;
            font-size: 15px;
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
            padding: 12px 16px;
            text-decoration: none;
            font-size: 18px;
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
        h5{{
        color:black;
        text-align: justify;
        }}
        h3{{
        color:black;
        }}
        .centered-text {{
        display: flex;
        justify-content: center;
        }}
        footer {{
            position: absolute;
            bottom: -80px;
            width:100%;
            background-color: black;
            color: white;
            font-size: 14px;
            text-align: center;
            line-height: 30px;
        }}
    </style>
""", unsafe_allow_html=True)

# 添加导航栏
st.markdown("""
    <h1>Catsoft_Kmalsite<br>Kmal Sites Prediction Platform</h1>
    <nav class="navbar">
    <ul class="nav-links">
        <li><a href="#Home">Home</a></li>
        <li><a href="#Web Server">Web Server</a></li>
        <li><a href="#User Guide">User Guide</a></li>
        <li><a class="active" href="#Contact">Contact</a></li>
    </ul>
    </nav>
""", unsafe_allow_html=True)

st.markdown("<h2>Email</h2>", unsafe_allow_html=True)

st.markdown("Feel free to contact us if you nedd any help: flyinsky6@189.cn", unsafe_allow_html=True)