import pickle
import pandas as pd
import streamlit as st

@st.cache_resource
def load():
    model = pickle.load(open("models/animal_species_model.pkl","rb"))
    cols = pickle.load(open("models/model_columns.pkl","rb"))
    return model, cols

model, cols = load()

st.title("🐾 Fast Animal Species Predictor")

weight = st.number_input("Weight",0.1,300.0,20.0)
length = st.number_input("Length",10.0,300.0,50.0)
legs = st.selectbox("Legs",[0,2,4])
fur = st.checkbox("Fur")
wings = st.checkbox("Wings")
eggs = st.checkbox("Eggs")
tail = st.checkbox("Tail")
aquatic = st.checkbox("Aquatic")
warm = st.checkbox("Warm Blooded")

if st.button("Predict"):
    df = pd.DataFrame([{
        "weight_kg":weight,
        "body_length_cm":length,
        "legs":legs,
        "has_wings":int(wings),
        "has_tail":int(tail),
        "has_fur":int(fur),
        "lays_eggs":int(eggs),
        "aquatic":int(aquatic),
        "warm_blooded":int(warm)
    }])[cols]

    pred = model.predict(df)[0]
    st.success(f"Prediction: {pred}")
