import streamlit as st
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from CTDC import CTDC_Descriptor
from EAAC import EAAC_Descriptor
from EGAAC import EGAAC_Descriptor
from sliding_slice_fasta import sliding_slice_fasta
from sliding_slice_dssp import sliding_slice_dssp
import io
import base64
import uuid

st.set_page_config(page_title='Web Server', page_icon=':dna:', layout="wide",
                   initial_sidebar_state='auto')

st.sidebar.success(" Start predicting!")

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
            width: 70%;
            margin:0 auto;
            color: black;
        }}
        h1 {{
            font-size: 5vw;
            color: #DFEEEF;
            text-align: center;
            font-weight: bold;
            margin-top: 2.43vw;
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
        <li><a class="active" href="#Web Server">Web Server</a></li>
        <li><a href="#User Guide">User Guide</a></li>
        <li><a href="#Contact">Contact</a></li>
    </ul>
    </nav>
""", unsafe_allow_html=True)

# 输入文本框和上传文件按钮
st.markdown("""<h2 style="margin-top: 13.5vw;">Enter Your Protein Information</h2>""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .streamlit-expanderHeader {
            justify-content: center !important;
            font-size: 1.5vw !important;
            font-weight: bold !important;
            color: black !important;
            background-color: white !important;
            border-radius: 0.25vw !important;
            border: 0.25vw solid #374673 !important;
            padding: 0.1vw !important;
            width: 6vw;
            margin-left: 50vw !important;
        }
        .streamlit-expanderContent {
            border: none;
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

st.write(
    '<h5>1.Input your protein sequence here. The sequence should be in <span style="color:red;">FASTA</span> format.</h5>',
    unsafe_allow_html=True)
with st.expander('**Example** ', expanded=True):
    st.write("<span style='color: #374673;'>Here is an example protein sequence in FASTA format:</span>",
             unsafe_allow_html=True)
    st.code(">sp|Q12345|PROTEIN_X\nGALMQDPASKTECFFIAKNEGVLRGTRKFLAWDAEALEKFIKNEGVFKGTYEVIRGWCDGRYLVFEAKENGEITRTVKVLG\n")

st.markdown("""
    <style>
    .stTextArea>label{
        color: black !important;
        margin: auto;
    }
     .stTextArea textarea {
        color: black !important;
        caret-color: black; 
        border-radius: 0.42vw;
        font-size: 1.67vw;
        box-shadow: 0.17vw 0.17vw 0.33vw #c9c9c9;
        border-left: 0.08vw solid black; 
        background-color: #FFFFFF !important;
        border: 0.17vw solid #121549 !important;
        margin-bottom:0;
        margin: auto;
        resize: none;
    }
    </style>
    """, unsafe_allow_html=True)

protein_seq = st.text_area(label='Please enter the correct protein sequence in FASTA format: ', height=200,
                           key='protein-sequence')


button_style = """
    <style>
        .stButton>button{
            background-color: #054D69;
            color: #FFFFFF;
            font-size: 1.5vw;
            border-radius: 0.42vw;
            padding: 0.83vw 1.67vw;
            cursor: pointer;
            font-weight: bold;
            box-shadow: none;
            outline: none !important;
            border:none;
            margin-left:12vw;
            margin-top:1vw;
        }

        .stButton:hover>button{
            background-color: #07498E;
            transition: color 0.1ms linear;
        }

    </style>
"""

st.write(button_style, unsafe_allow_html=True)

browse_files_button = st.file_uploader("Or select a file to upload:", type=["txt", "fasta"])

st.write("-----------")
st.write(
    '<h5 style="margin:0.83vw auto 0 auto;">2.Input your protein structure here. The structure should be in <span style="color:red;">DSSP</span> format.</h5>',
    unsafe_allow_html=True)

with st.expander('**Example** ', expanded=True):
    st.write("<span style='color: #374673;'>Here is an example protein structure in DSSP format:</span>",
             unsafe_allow_html=True)
    st.code(''' #  RESIDUE  AA  STRUCTURE  BP1  BP2  ACC  N-H-->O  O-->H-N  N-H-->O  O-->H-N  TCO  KAPPA  ALPHA  PHI  PSI  X-CA  Y-CA  Z-CA
1      1    A     M         0    0   245   0, 0.0   2,-0.4   0, 0.0   0, 0.0   0.000 360.0  360.0 360.0 57.9  32.7  34.6 -33.8
2      2    A     L         -    0   173   0, 0.0   0, 0.0   0, 0.0   0, 0.0  -0.972 360.0  -86.4 -138.3 116.5 30.7  32.5 -31.3
3      3    A     S         -    0   105  -2,-0.4   3,-0.2   1,-0.1   0, 0.0   0.178 28.8  -176.0 -20.1  116.7 31.9  29.0 -30.2
''')

protein_struc = st.text_area(label='Please enter the correct protein structure in DSSP format: ', height=200,
                           key='protein-structure')


structure_files_button = st.file_uploader(label='Or select a file to upload:', type="dssp")

st.write("-----------")
st.write('<h5 style="margin:0.83vw auto 0 auto;">3.Console:<span style="color:red;"> Click</span> the button below to make a prediction or clear the prediction.</h5>',unsafe_allow_html=True)
# 点击按钮开始预测
col1, col2 = st.columns(2)
submit_button = col1.button(label='Submit', key='predict-button')
if submit_button:
    st.write("-----------")
    with st.spinner("Please wait a moment, we will show the results soon! Thanks for your patience!"):
        st.markdown("<h3 style='text-align: center;'>Predicton Result</h3>", unsafe_allow_html=True)

        file1 = ''
        if browse_files_button:
            file1 = browse_files_button.read().decode("utf-8")
        fasta_contents = protein_seq + file1
        if fasta_contents == '':
            st.write("Please enter the correct protein sequence!")

        file2 = ''
        dssp_contents = ''

        if structure_files_button:
            file2 = structure_files_button.getvalue().decode("utf-8")
            file2 = io.StringIO(file2)
            file2 = ''.join(file2.readlines()[28:])
            dssp_contents = ''.join(protein_struc.split("\n",1)[1:]) + '\n' + file2 if protein_struc else file2
        elif protein_struc:
            dssp_contents = ''.join(protein_struc.split("\n",1)[1:])

        if all(var is not None and var != '' for var in [fasta_contents, dssp_contents]):

            data, slices, k_index = sliding_slice_fasta(fasta_contents)

            M = {'sliding_window': 5}  # 默认编码滑动窗口
            CTDC_seq = CTDC_Descriptor(data, M)
            CTDC_seq.Protein_CTDC()
            CTDC_df = pd.DataFrame(CTDC_seq.encoding_array)

            EAAC_seq = EAAC_Descriptor(data, M)
            EAAC_seq.Protein_EAAC()
            EAAC_df = pd.DataFrame(EAAC_seq.encoding_array)

            EGAAC_seq = EGAAC_Descriptor(data, M)
            EGAAC_seq.Protein_EGAAC()
            EGAAC_df = pd.DataFrame(EGAAC_seq.encoding_array)

            data1 = CTDC_df.to_numpy()
            data2 = EAAC_df.to_numpy()
            data3 = EGAAC_df.to_numpy()
            data123 = np.hstack((data1, data2, data3))

            data4 = sliding_slice_dssp(dssp_contents)

            model1 = CatBoostClassifier()
            model1.load_model("model1")
            model2 = CatBoostClassifier()
            model2.load_model("model2")

            # 进行模型预测
            preds1 = model1.predict_proba(data123)[:, 1]
            preds2 = model2.predict_proba(data4)[:, 1]

            pred1 = model1.predict(data123)
            pred2 = model2.predict(data4)

            weight = [0.4538986914845343, 0.5461013085154657]

            soft_preds = preds1 * weight[0] + preds2 * weight[1]
            soft_pred = np.round(soft_preds >= 0.5).astype(int)

            class_1 = np.where(soft_pred == 1)[0]
            num_1 = len(class_1)

            # st.write(f"The predicton result has {num_1} items!")
            st.markdown(
                f"""<div class="centered-text">The prediction result has {num_1} items!</div>""",
                unsafe_allow_html=True
            )
            # 存在丙二酰化修饰的K
            id = [slices[i][0][1] for j in class_1 for i in range(len(slices)) if j == i]
            Peptide_seq = [slices[i][1] for j in class_1 for i in range(len(slices)) if j == i]
            Position = [slices[i][2]+1 for j in class_1 for i in range(len(slices)) if j == i]

            # 将含有 "K" 的位置标红
            Peptide_seq_formatted = []
            for seq in Peptide_seq:
                k_indices = [i for i, char in enumerate(seq) if char == "K"]
                formatted_seq = ""
                if len(k_indices) > 0:
                    mid_index = len(seq) // 2
                    if mid_index in k_indices:
                        formatted_seq = seq[
                                        :mid_index] + f'<span style="color:red; font-weight:bold">{seq[mid_index]}</span>' + seq[
                                                                                                                             mid_index + 1:]

                    else:
                        formatted_seq = seq
                else:
                    formatted_seq = seq
                Peptide_seq_formatted.append(formatted_seq)

            dt = {'ID': id,
                  'Code': ['K'] * num_1,
                  'Peptide': Peptide_seq_formatted,
                  'Position': Position,
                  'Score': [soft_preds[i] for i in class_1]}
            df = pd.DataFrame(dt)


            def draw_table(df):
                df_sorted = df.sort_values(df.columns[-1], ascending=False)
                columns = df_sorted.columns
                thead1 = """<thead><th scope="col"></th>"""
                thead_temp = []
                for k in range(len(list(columns))):
                    thead_temp.append(
                        """<th scope="col" class="text-white " style="color:black;vertical-align: middle; text-align: center;width:16%">""" + str(
                            list(columns)[k]) + """</th>""")
                header = thead1 + "".join(thead_temp) + """</tr></thead>"""
                rows = []
                rows_temp = []
                for i in range(df_sorted.shape[0]):
                    rows.append(
                        """<th scope="row" style="color:black;vertical-align: middle; text-align: center;width:16%">""" + str(
                            i + 1) + """</th>""")
                    rows_temp.append(df_sorted.iloc[i].values.tolist())
                td_temp = []
                for j in range(len(rows_temp)):
                    for m in range(len(rows_temp[j])):
                        td_temp.append(
                            """<td class="text-white" style="color:black;vertical-align: middle; text-align: center;width:16%">""" +
                            str(rows_temp[j][m]) + """</td>""")
                td_temp2 = []
                for n in range(len(td_temp)):
                    td_temp2.append(td_temp[n:n + df_sorted.shape[1]])
                td_temp3 = []
                for x in range(len(td_temp2)):
                    if int(x % (df_sorted.shape[1])) == 0:
                        td_temp3.append(td_temp2[x])
                td_temp4 = []
                for xx in range(len(td_temp3)):
                    td_temp4.append("".join(td_temp3[xx]))
                td_temp5 = []
                for v in range(len(td_temp4)):
                    td_temp5.append(
                        """<tr><th scope="row" class="text-white" style="color:black;vertical-align: middle; text-align: center;width:12%">""" + str(
                            v + 1) + """</th>""" +
                        str(td_temp4[v]) + """</tr>""")
                table_html = """<table class="table text-center table-bordered" style="width: 100%;background-color: white;" border="2">""" + \
                             header + """<tbody>""" + "".join(td_temp5) + """</tbody></table>"""

                return table_html


            styled_table = draw_table(df)
            df_sorted = df.sort_values(by=df.columns[-1], ascending=False)
            csv = df_sorted.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # 转换成base64编码
            # 创建下载按钮
            button_label = "Download CSV File"
            button_uuid = str(uuid.uuid4()).replace("-", "")
            button_id = f"download_button_{button_uuid}"
            button_code = f"""
                <div style="display: flex; justify-content: flex-end;">
                    <a download="{id[0]}.csv" id="{button_id}" href="data:file/csv;base64,{b64}">
                        <button class="streamlit-button small-button primary-button" 
                                style="padding: .375rem .75rem;margin-top:0.42vw;font-size: 1.17vw;background-color:#616f93;color:#fff">
                            {button_label}
                        </button>
                    </a>
                 </div>
                <script>
                    document.getElementById('{button_id}').addEventListener('click', function() {{
                        this.disabled = true;
                        this.innerText = 'Downloading...';
                    }});
                </script>
            """

            # 在应用程序中显示表格和下载链接
            st.markdown(f"""<div class="centered-text;">{styled_table}</div>""", unsafe_allow_html=True)
            st.markdown(button_code, unsafe_allow_html=True)

# 添加清除按钮
if col2.button('Clear', key='clear-button'):
    protein_seq = ""
    browse_files_button = None
    structure_files_button = None

st.markdown("<footer>Copyright © 2024 - Created by Xuzhou Medical University</footer>", unsafe_allow_html=True)
