import streamlit as st
import base64
from io import BytesIO
from PIL import Image


st.set_page_config(page_title='User Guide', page_icon=':dna:', layout="wide",
                   initial_sidebar_state='auto')

st.sidebar.success("From this page, you may understand how to use our web server to start your prediction.")

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
            width: 58%;
            margin:0 auto;
            color: black;
        }}
        h1 {{
            font-size: 5vw;
            color: #DFEEEF;
            text-align: center;
            font-weight: bold;
            margin-top: 2.43vw;
            padding: 1.6vw;
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
            margin-top: 15vw;
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
            top: 17vw;
            left:0;
            border-radius: 0 0 0.83vw 0.83vw;
            width: 100%;
            padding: 0.4vw;
            border: none;
            text-align: center;
        }}
        .navbar a {{
            text-decoration: none;
            font-size: 1.2vw;
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
        .centered-text {{
            display: flex;
            justify-content: center;
        }}
        footer {{
            position: absolute;
            bottom: -6.67vw;
            width:100%;
            background-color: black;
            color: white;
            font-size: 1.17vw;
            text-align: center;
            line-height: 2.5vw;
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
        <li><a class="active" href="#User Guide">User Guide</a></li>
        <li><a href="#Contact">Contact</a></li>
    </ul>
    </nav>
""", unsafe_allow_html=True)

# 输入文本框和上传文件按钮
st.markdown("""<h2 style="margin-top: 13.5vw;">Tutorial(Q & A)</h2>""", unsafe_allow_html=True)

st.write(
    '<h5 style="width: 100%;background-color:yellow; display: inline-block; padding: 0.42vw;">Q<span style="color:red;">1. How to make your prediction?</span></h5>',
    unsafe_allow_html=True)

image1 = Image.open("./Code/t1.png")
image2 = Image.open("./Code/t2.png")
image3 = Image.open("./Code/t3.png")

caption = "A:"
caption1 = ("Firstly,  you should either copy/paste or upload a file containing the protein sequences with FASTA format into the input box, shown as 1-zone and 2-zone position in the figure above. ")
caption2 = ("Secondly, you should either copy/paste or upload a file containing the protein structure with DSSP format into the input box, shown as 3-zone and 4-zone position in the figure above. ")
caption3 = ("Finally, you can click the submit button in area 5 of the map and then wait for the result to appear.")

# 将图片转换为Base64编码
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# 创建HTML容器框并显示图片
st.markdown(
    """
        <div style='background-color: white; width: 100%;">
         <h5 style='padding: 0.42vw 0.17vw'>{}</h5>
         <div style='padding: 0 0.83vw; margin: 0 auto; text-align: center'>
            <div style='display: inline-block; width: 95%; padding: 0.42vw; box-sizing: border-box;'>
                <img src='data:image/png;base64,{}' style='max-width:100%; height:auto;'>
                 <p>{}</p>
            </div>
            <div style='display: inline-block; width: 95%; padding: 0.42vw; box-sizing: border-box;'>
                <img src='data:image/png;base64,{}' style='max-width:100%; height:auto;'>
                 <p>{}</p>
            </div>
            <div style='display: inline-block; width: 95%; padding: 0.42vw; box-sizing: border-box;'>
                <img src='data:image/png;base64,{}' style='max-width:100%; height:auto;'>
                 <p>{}</p>
            </div>
            <div style='clear:both;'></div>
            </div>
        </div>
    """.format(
        caption,
        image_to_base64(image1),caption1,
        image_to_base64(image2),caption2,
        image_to_base64(image3),caption3,

    ),
    unsafe_allow_html=True
)

st.write(
    '<h5 style="width: 100%;background-color:yellow; display: inline-block; padding: 0.42vw;">Q<span style="color:red;">2. The detailed explanation of the page of prediction results.</span></h5>',
    unsafe_allow_html=True
)
image4 = Image.open("./Code/t4.png")

caption4 = ('''The output part of the result contains five types of information: \n
 1. The name of the protein;
 2. Amino acids that have undergone modification; 
 3. The amino acid fragment sequence obtained by intercepting the upper and lower 16 amino acids at this position (total length 33 ); 
 4. Which position on the protein is lysine (K); 
 5. The score obtained by the model prediction (the closer the score is to 1, the more likely the selected modification will occur).\n
 Finally, you can click the button in area 6 and then wait for the predicted results to download.
''')

st.markdown(
    """
    <div style='background-color: white; width: 100%;">
     <h5 style='padding: 0.42vw 0.17vw'>{}</h5>
     <div style='padding: 0 0.83vw; margin: 0 auto; text-align: center'>
        <div style='display: inline-block; width: 95%; padding: 0.42vw; box-sizing: border-box;'>
            <img src='data:image/png;base64,{}' style='max-width:100%; height:auto;'>
             <p>{}</p>
        </div>
        <div style='clear:both;'></div>
        </div>
    </div>
""".format(
        caption,
        image_to_base64(image4), caption4,

    ),
    unsafe_allow_html=True
)
