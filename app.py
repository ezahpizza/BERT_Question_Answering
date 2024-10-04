import streamlit as st
import numpy as np
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline
import torch

import warnings
warnings.filterwarnings('ignore')

@st.cache(allow_output_mutation=True)
def get_model():
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    model = AutoModelForQuestionAnswering.from_pretrained("ezahpizza/qa_model")
    return tokenizer,model


tokenizer,model = get_model()
question_answerer = pipeline("question-answering", model=model, tokenizer=tokenizer)

context = st.text_area('Enter text to Analyse')
question = st.text_area('Enter your question')
button = st.button("Answer")


if context and button and question :
    test_sample = tokenizer([context], padding=True, truncation=True, max_length=512,return_tensors='pt')
    # test_sample
    output = model(**test_sample)
    y_pred = question_answerer(question=question, context=context)
    st.write("Prediction: ",y_pred)