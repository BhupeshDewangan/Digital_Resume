from pathlib import Path

import streamlit as st
from PIL import Image

# --------PATH SETTINGS------------

curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = curr_dir / "style" / "main.css"
resume_file = curr_dir / "assets" / "resume.pdf"
profile_pic = curr_dir / "assets" / "pic.jpg"

# ----------GENERAL SETTINGS------------

PAGE_TITLE = "Digital Resume | Bhupesh Dewangan"
PAGE_ICON = ":wave:"
NAME = 'Bhupesh Dewangan'
DESC = """ 
I am pursuing my B. Tech degree, exploring some advanced level technology like - Artificial Intelligence, Machine Learning, Data Visualization, And Data Science. I love making web pages and designing UI/UX.
""" 

EMAIL = "bhupesh.dew.careers@gmail.com"

SOCIAL_MEDIA = {

    "Linkedin" : "https://github.com/BhupeshDewangan/Sorting_Visualization",
    "Github" : "https://github.com/BhupeshDewangan/Sorting_Visualization",
    "Leetcode" : "https://github.com/BhupeshDewangan/Sorting_Visualization",
    "Code Studio" : "https://github.com/BhupeshDewangan/Sorting_Visualization",
}

PROJECTS = {

    "😁 qjiwhids" : "udiuhidiud",
    "😁 sjhss" : "udiuhidiud",
    "😁 qjqoiqdd" : "udiuhidiud",
    "😁 snkdkhd" : "udiuhidiud",

  
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# -------LOAD CSS, PDF AND PROFILE PIC---------

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# -------- HERO SECTION -----------

col1, col2 = st.columns(2, gap = "small")

with col1:
    st.image(profile_pic, width = 230)

with col2:
    st.title(NAME)
    st.write(DESC)
    st.download_button(
        label = "📃 Download Resume",
        data = PDFbyte,
        file_name = "Bhupesh_Dewangan_Resume.pdf",
        mime = "application/octet-stream",
    )
    st.write("😁", EMAIL)

# -------- SOCIAL LINKS -------------

st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ---------EXPERIENCE AND QULIFICATION-------------

st.write('\n')
st.subheader("Experience and Qualifications")

# --------SKILLS -------------

st.write("\n")
st.subheader("Hard Skills")

st.write(
    """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """
)


# ------- PROJECTS and ACCOMPLISHMENTS

st.write('\n')
st.subheader("Projects and Accomplishments")

st.write("-----------")
for projects, links in PROJECTS.items():
    st.write(f"[{projects}]({link})")

