# Import Libraries
import spacy
import pandas as pd
import fitz
from tqdm import tqdm
# nlp = spacy.blank('en')


# Load Model
def load_model(model_name):
    nlp_model = spacy.load(model_name)
    return nlp_model


# Prediction Model
def prediction(nlp_model, resume_path):
    fname = resume_path
    doc = fitz.open(fname)
    text = ""
    for page in doc:
        text = text + str(page.get_text())
    tx = " ".join(text.split("\n"))
    doc = nlp_model(tx)
    cols = []
    data = []
    for ent in doc.ents:
        print(f"{ent.label_.upper():{30}}-{ent.text}")
        cols.append(ent.label_.upper())
        data.append(ent.text)
    em_df = pd.DataFrame(data, index=cols)
    return em_df.to_dict()


# Main Model
def main(pred_text):
    # path = "train_data.pkl"
    model_path = "Result1"
    nlp_model = load_model(model_path)
    final_data = prediction(nlp_model, pred_text)
    return final_data
