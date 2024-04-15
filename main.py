import streamlit as st

# This must be the first Streamlit command used on an app page
# Configures the default settings of the page

st.set_page_config(
    page_title="Cool App", # The page title, shown in the browser tab
    page_icon="random",
    layout="wide", # constrains the elements into a centered column of fixed width
    initial_sidebar_state="expanded", # How the sidebar should start out
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Display text in header formatting
st.subheader(':iphone: Phone price predictor')
st.subheader(' ', anchor= 'header1', divider='rainbow')
st.subheader(':rainbow[Enter phone specifications]')

from modules import raw_values, load_model, predict_price


with st.form("form", clear_on_submit=False):
    brands,rams,internal_storages,batteries,main_cameras,front_cameras,displays,has_5g_options = raw_values()

    brand = st.radio('brand', brands, horizontal=True, index=None)
    ram = st.radio('ram', rams, horizontal=True, index=None)
    internal_storage = st.radio('internal storage', internal_storages, horizontal=True, index=None)
    battery = st.radio('batteries', batteries, horizontal=True, index=None)
    main_camera = st.radio('main_cameras', main_cameras, horizontal=True, index=None)
    front_camera = st.radio('front_cameras', front_cameras, horizontal=True, index=None)
    display = st.radio('displays', displays, horizontal=True, index=None)
    has_5g = st.radio('5G', has_5g_options, horizontal=True, index=None)

    submitted = st.form_submit_button("Submit")
    if submitted:
        if not all([brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g]):
            st.warning("Please select options for all categories.")
        else:
            rf = load_model()
            price = predict_price(rf, brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g)            
            st.write("price:", price)