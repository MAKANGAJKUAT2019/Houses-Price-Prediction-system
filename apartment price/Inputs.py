import streamlit as st
import time
import pandas as pd
import pickle
import xgboost as xgb

def take_inputs():

    # Load Model
    model = pickle.load(open("xgboost_model.pkl", "rb"))

    all_location = ["Ruaka", "Utawala", "Kileleshwa", "Lavington", "Westlands", "Ruiru",
                    "Juja", "Syokimau", "Muthaiga", "Kilimani"]
    all_amenities = ["garbage collection", "parking", "garden", "swimming pool", "gym"]

    location_map = {
        "Ruaka": 0, "Utawala": 1, "Kileleshwa": 2, "Lavington": 3, "Westlands": 4,
        "Ruiru": 5, "Juja": 6, "Syokimau": 7, "Muthaiga": 8, "Kilimani": 9
    }


    location = st.selectbox("Location", all_location, key="3")

    distancetoCBD = st.number_input("Distance to CBD (km)", step=0.1)
    if distancetoCBD <= 0:
        st.error("Enter a valid positive number")
    else:
        var = []

        # Assign numerical value to Location
        location_code = location_map[location]


        bedrooms = st.selectbox("Bedrooms", range(1, 5), key='0')
        bathrooms = st.selectbox("Bathrooms", range(1, 5), key='1')
        floorsize = st.number_input("Floor Size (sqM)", step=0.1, key='2')

        if floorsize <= 0:
            st.error("Enter a valid positive number")
        else:
            var.append((location_code, distancetoCBD, bedrooms, bathrooms, floorsize))

            # Assigning values to Amenities
            amenities = st.multiselect("Available Amenities", all_amenities, default=[])
            amenity_values = []
            for amenity in all_amenities:
                if amenity in amenities:
                    amenity_values.append(1)
                else:
                    amenity_values.append(0)

            var.extend(amenity_values)
    merged_list = [item for sublist in var if isinstance(sublist, tuple) for item in sublist] + \
                  [item for item in var if not isinstance(item,tuple)]


    # Create a dictionary from user input and convert it to DataFrame
    input_dict = dict(zip(model.feature_names, merged_list))
    input_df = pd.DataFrame([input_dict])

    print(merged_list)

    if st.button("Predict"):
        @st.cache_resource
        def predict(data):
            # Load Model
            model = pickle.load(open("xgboost_model.pkl", "rb"))
            dinput = xgb.DMatrix(data)
            pred = model.predict(dinput)
            return st.write(f"The House Price is Ksh.{round(pred[0],2)}")

        with st.spinner("Predicting..."):
            time.sleep(3)
        st.success("Prediction Done", icon="✅")
        predict(input_df)

