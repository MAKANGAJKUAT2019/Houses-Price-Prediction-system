import streamlit as st
from PIL import Image
from Inputs import take_inputs
# This code sets the configuration for a Streamlit page
st.set_page_config(page_title="apartment price", page_icon=":home:", layout="wide", initial_sidebar_state="auto")




# It also hides the footer
st.markdown("<style>footer{display:none;}</style>", unsafe_allow_html=True)


# Creates a heading in HTML and CSS AND Display it using the streamlit Library

st.markdown('<p class="font">Apartment House Price Prediction System</p>', unsafe_allow_html=True)
st.markdown("""<style> .font
    { font-size:55px ; font-family:'Cooper Black'; color:#FF9633;
    }</style>""", unsafe_allow_html=True)

# This code modifies the font style of a markdown element
st.markdown("""<style> .font1
                        { font-size:40px ; font-family:'Open Sans', fantasy; color:#00A8E8;
                        }</style>""", unsafe_allow_html=True)


# This code creates a sidebar menu with two options, "Predict" and "About".
# The user can select one of the options and it is stored in the variable "choice".
menu = ["Predict", "About"]
choice = st.sidebar.selectbox("Menu", menu)



# This code creates two sections in the sidebar of the Streamlit app.
st.sidebar.title("Contributions")
st.sidebar.info(
    """
    This is an Open Source project and you are Welcomed to make any impactfull additions whatsoever.

    [GitHub Account](https://github.com/) | [Source code](https://github.com/)
    """
)

st.sidebar.title("Contact Developer")
st.sidebar.info(
    """
    **Moses Makanga Sidibu**: 

    [GitHub](https://github.com/) 
    """
)


def predict_page():
    st.markdown('<p class="font1">Apartment Prediction Page</p>', unsafe_allow_html=True)
    st.info("Make sure to fill in all the Variables indicated below....\
            If the Distance to CBD is 0 or Less than 0, then there will be an error.")


    take_inputs()

# The above code is a function that creates an about page for a project recommender system.
# It displays text that provides information about the project, as well as links to the project's social media accounts.

def about_page():
    st.markdown('<p class="font1">About Page</p>', unsafe_allow_html=True)
    # Load an image from file
    image = Image.open('./apartment.jpeg')

    # Display the image using the `image` function
    st.image(image, use_column_width=True)
    st.markdown("""
            <div style="background-color:#F0F8FF;padding 10px; font-family:sans-serif; font-size:16px;>"
            <p>Welcome to our about page! We are excited to share with you our project on Nairobi Apartment Rental Price prediction. 

In the bustling city of Nairobi, finding an ideal apartment with affordable rent can be a daunting task. That's where our project comes in. We have developed a state-of-the-art machine learning model that can predict the rental prices of apartments in Nairobi, helping both tenants and landlords make informed decisions.

By considering different factors, such as location, size, amenities, and historical rental trends, our model has been trained to accurately estimate the rental prices.

Not only does our project empower potential tenants to estimate the expected cost of renting an apartment, but it also helps landlords set competitive rental prices. By providing valuable insights and predictions, we aim to streamline the apartment rental process, making it more transparent and convenient for all parties involved.

We believe that our project can revolutionize the way apartment rentals are approached in Nairobi. Our goal is to provide users with a reliable tool that takes the guesswork out of rental pricing and allows them to make informed decisions. 

Thank you for visiting our about page, and we hope that our project on Nairobi Apartment Rental Price prediction proves to be helpful and valuable to you.</p>
            
            
            """, unsafe_allow_html=True)


# This code checks the value of the variable "choice" and takes an action accordingly.
# If the value is "About", it calls the function about_page(), otherwise it calls the function predict_page()

if choice == 'About':
    about_page()

else:
    predict_page()
