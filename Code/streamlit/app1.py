"""
Author: Ei Tanaka, Cody Yu, Pon Swarnalaya Ravichandran
Date: December 11, 2023
Purpose: This file is used to run the streamlit app
References:
    https://github.com/blackary/st_pages?tab=readme-ov-file (streamlit pages)
"""

# ============================== imorts =======================================
import os
import streamlit as st
from st_pages import Page, show_pages, add_page_title

# ============================== Setup / constants ====================================
# Set up paths
OS_PATH = os.getcwd()
os.chdir("../../")
ROOT_PATH = os.getcwd()
IMAGE_PATH = os.path.join(OS_PATH, 'assets')
IMAGE_PATH1 = 'path/to/FIGURE01.png'
MODEL_PATH = os.path.join(ROOT_PATH, "Models")
ELECTRA_PATH = os.path.join(MODEL_PATH, "ELECTRA", "electra-finetuned-squadv2")
XLNET_PATH = ""
os.chdir(OS_PATH)

# Model Checkpoints
electra_checkpoint = "google/electra-base-discriminator"
electra_finetuned_checkpoint = "checkpoint-49410"
XLNET_checkpoint = ""
XLNET_finetuned_checkpoint = ""

# Specify what pages should be shown in the sidebar, and what their labels should be
show_pages(
    [
        Page("app.py", "Introduction"),
        Page("app_EDA.py", "Exploratory Data Analysis"),
        Page("app_Model.py", "Model"),
        Page("app_Results.py", "Results"),
        Page("app_demo.py", "Demo"),
    ]
)

# =============.================= Main Contents ====================================
st.title("Question Answering on SQuAD 2.0")

st.header("Introduction")

st.write("In the dynamic realm of Natural Language Processing (NLP), the advent of question-answering (QA) systems marks a significant stride in our ability to interact with and process digital information. "
         "This project is dedicated to developing a reading comprehension-based QA system inspired by the comprehensive insights in Speech and Language Processing by Daniel Jurafsky & James H. Martin (2023). "
         "We aim to create a system that can interpret and respond to questions posed in natural language, drawing answers from provided text passages.")

st.header("NLP Task - Question Answering")

st.header("Dataset")

st.write("SQuAD 2.0 stands as an innovative dataset strategically crafted to propel advancements in the domain of machine reading comprehension—an integral facet of natural language understanding. "
         "Distinguished from its predecessor, SQuAD 1.1, this dataset introduces a notable enhancement: the integration of 53,775 unanswerable questions meticulously generated by crowdworkers. "
         "These questions leverage the same passages employed in SQuAD 1.1 but are intentionally formulated to maintain relevance to the content while introducing plausible yet incorrect answers. "
         "This deliberate shift from the preceding version, which solely featured answerable questions with correct responses within the provided text, signifies a significant evolution. "
         "Below, we present two illustrative examples of this distinctive design.")

st.write("The principal objective underlying the conception of SQuAD 2.0 is to present a formidable challenge to and elevate the proficiency of machine learning models in discerning instances where a correct answer is absent within the provided text." 
         "This task introduces a heightened level of complexity compared to SQuAD 1.1, wherein models were tasked with identifying the text span most pertinent to the posed question." 
         "SQuAD 2.0 aspires to cultivate a deeper understanding and critical analysis, thereby pushing the boundaries of machine learning models' capabilities in comprehending and interpreting textual information."
        "The dataset has undergone meticulous testing, affirming its status as both a challenging and high-quality resource."
        "Evaluation with cutting-edge machine learning models reveals a markedly lower F1 score of 66.3% for SQuAD 2.0, contrasting with the human benchmark of 89.5% F1 score."
        "This discrepancy underscores the heightened difficulty of the dataset, as evidenced by the same model architecture achieving an 85.8% F1 score on SQuAD 1.1—reflecting a performance closer to human levels." 
         "Notably, the unanswerable questions within SQuAD 2.0 have demonstrated greater difficulty compared to those generated by alternative methods such as distant supervision or rule-based approaches.")