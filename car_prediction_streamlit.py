import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("car_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)
st.title("Car Prediction Model")

# Define the label mapping
label_mapping_model = {0: "Audi A1", 1: "Audi A2", 2: "Audi A3", 3: "Opel Astra", 4: "Opel Corsa", 5: "Opel Insignia", 6: "Renault Clio", 7: "Renault Duster", 8: "Renault Espace"}
label_mapping_bodytype = {0: "Compact", 1: "Convertible", 2: "Coupe", 3: "Off-Road", 4: "Other", 5: "Sedans", 6: "Station wagon", 7: "Transporter", 8: "Van"}
label_mapping_painttype = {0: "Metallic", 1: "Perl effect", 2: "Uni/basic",3:"nan"}
label_mapping_gearingtype = {0: "Automatic", 1: "Manual", 2: "Semi-automatic"}
label_mapping_drivechain = {0: "4WD", 1: "FRONT", 2: "REAR",3:"nan"}
label_mapping_upholsterytype = {0: "Beige", 1: "Black", 2: "Blue", 3: "Brown", 4: "Cloth", 5: "Full leather", 6: "Grey", 7: "Other", 8: "Part leather",9:"Velour",10:"White",11:"alcantara",12:"nan"}
label_mapping_fuel = {0: "BENZINE", 1: "DIESEL", 2: "ELECTRIC",3:"LPG",4:"OTHERS"}


# Reverse the label mapping to create a new dictionary
reverse_label_mapping_model = {v: k for k, v in label_mapping_model.items()}
reverse_label_mapping_bodytype = {v: k for k, v in label_mapping_bodytype.items()}
reverse_label_mapping_painttype = {v: k for k, v in label_mapping_painttype.items()}
reverse_label_mapping_gearingtype = {v: k for k, v in label_mapping_gearingtype.items()}
reverse_label_mapping_drivechain = {v: k for k, v in label_mapping_drivechain.items()}
reverse_label_mapping_upholsterytype = {v: k for k, v in label_mapping_upholsterytype.items()}
reverse_label_mapping_fuel = {v: k for k, v in label_mapping_fuel.items()}


# Create sliders for the features
Model = st.selectbox("Model", list(label_mapping_model.values()))
body_type = st.selectbox("body_type", list(label_mapping_bodytype.values()))
km = st.slider("km", 0, 500000)
registration = st.slider("registration", 2016, 2019)
prev_owner = st.slider("prev_owner",1,4)
hp = st.slider("hp", 50, 300)
#Paint_Type = st.selectbox("Paint Type",list(label_mapping_painttype.values()))
Nr_of_Doors = st.slider("Nr. of Doors", 2, 7)
#Nr_of_Seats = st.slider("Nr. of Seats", 2, 7)
Gearing_Type = st.selectbox("Gearing Type", list(label_mapping_gearingtype.values()))
#Weight = st.slider("Weight", 500, 2500)
Drive_chain = st.selectbox("Drive chain", list(label_mapping_drivechain.values()))
#CO2_Emission = st.slider("CO2 Emission", 0, 1000)
Gears = st.slider("Gears", 4,8)
Upholstery_Type = st.selectbox("Upholstery_Type", list(label_mapping_upholsterytype.values()))
EnginePowerCC = st.slider("EnginePowerCC", 800, 3000)
FUEL = st.selectbox("FUEL", list(label_mapping_fuel.values()))
Consumption_City = st.slider("Consumption_City", 3, 20)

# Create the DataFrame with the selected feature values
df = pd.DataFrame(
    [
        {
            "Model": reverse_label_mapping_model[Model],
            "body_type": reverse_label_mapping_bodytype[body_type],
            "km": km,
            "registration": registration,
            "prev_owner": prev_owner,
            "hp": hp,
            "Paint_Type": "Paint Type",
            "Nr_of_Doors": Nr_of_Doors,
            "Nr_of_Seats": "Nr. of Seats",
            "Gearing_Type": reverse_label_mapping_gearingtype[Gearing_Type],
            "Weight": "Weight",
            "Drive_chain": reverse_label_mapping_drivechain[Drive_chain],
            "CO2_Emission": "CO2 Emission",
            "Gears": Gears,
            "Upholstery_Type": reverse_label_mapping_upholsterytype[Upholstery_Type],
            "EnginePowerCC": EnginePowerCC,
            "FUEL": reverse_label_mapping_fuel[FUEL],
            "Consumption_City": Consumption_City,
        }
    ]
)

prediction = model.predict(df)

st.success(f"Price: {prediction}")
