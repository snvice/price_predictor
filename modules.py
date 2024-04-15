frequency_encoding = {
    'itel': 43 / 1000,        # 43 occurrences out of 1000 total
    'Infinix': 90 / 1000,     # 90 occurrences out of 1000 total
    'Xiaomi': 260 / 1000,     # 260 occurrences out of 1000 total
    'Samsung': 218 / 1000,    # 218 occurrences out of 1000 total
    'Tecno': 125 / 1000,      # 125 occurrences out of 1000 total
    'Realme': 43 / 1000,      # 43 occurrences out of 1000 total
    'Huawei': 73 / 1000,      # 73 occurrences out of 1000 total
    'OPPO': 67 / 1000,        # 67 occurrences out of 1000 total
    'Nokia': 56 / 1000,       # 56 occurrences out of 1000 total
    'Apple': 55 / 1000,       # 55 occurrences out of 1000 total
    'Vivo': 51 / 1000,        # 51 occurrences out of 1000 total
    'Xtigi': 36 / 1000,       # 36 occurrences out of 1000 total
    'Ulefone': 33 / 1000,     # 33 occurrences out of 1000 total
    'Google Pixel': 18 / 1000,# 18 occurrences out of 1000 total
    'Asus': 17 / 1000,        # 17 occurrences out of 1000 total
    'ZTE': 15 / 1000,         # 15 occurrences out of 1000 total
    'HTC': 6 / 1000,          # 6 occurrences out of 1000 total
    'Nothing': 5 / 1000,      # 5 occurrences out of 1000 total
    'Lenovo': 4 / 1000,       # 4 occurrences out of 1000 total
    'Motorola': 3 / 1000,     # 3 occurrences out of 1000 total
    'Sony': 3 / 1000,         # 3 occurrences out of 1000 total
    'Neon ray': 2 / 1000,     # 2 occurrences out of 1000 total
    'Cubot': 2 / 1000,        # 2 occurrences out of 1000 total
    'Umidigi': 1 / 1000,      # 1 occurrence out of 1000 total
    'Alldocube': 1 / 1000     # 1 occurrence out of 1000 total
}


def predict_price(model, brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g):
    # Convert 5G option to binary (0 for No, 1 for Yes)
    has_5g = 1 if has_5g.lower() == 'yes' else 0
    
    # Convert brand to encoded value
    brand_encoded = frequency_encoding.get(brand, 0)  # Assume ordinal_mapping is defined

    input_data = [[brand_encoded, ram, internal_storage, battery, main_camera, front_camera, display, has_5g]]

    # Make prediction
    predicted_price = model.predict(input_data)
    # predicted_price = model.predict(brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g )

    return predicted_price[0]

def raw_values():
    brands = ['itel', 'Infinix', 'Xiaomi', 'Tecno', 'Realme', 'Samsung', 'Vivo',
       'OnePlus', 'Sony', 'ZTE', 'Apple', 'Huawei', 'OPPO', 'Xtigi',
       'Asus', 'Google Pixel', 'Motorola', 'Nokia', 'Lenovo', 'Nothing',
       'Ulefone', 'Umidigi', 'Neon ray', 'Cubot', 'HTC', 'Alldocube']
    rams = [1, 2, 3, 4, 6, 8, 10, 12, 15, 16, 18]
    internal_storages = [2, 8, 16, 31, 32, 64, 128, 164, 256, 265, 512]
    batteries = [2000, 3000, 4000, 4500, 5000, 6000]
    main_cameras = [2, 3, 5, 8, 12, 13, 16, 20, 25, 32, 40, 48, 50, 64, 100, 108, 200]
    front_cameras = [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 20, 24, 25, 32, 40, 44, 48, 50, 60]
    displays = [5.5, 6.0, 6.5, 7.0, 7.5]
    has_5g_options = ['Yes', 'No']

    return brands,rams,internal_storages,batteries,main_cameras,front_cameras,displays,has_5g_options

import streamlit as st
import pickle
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model