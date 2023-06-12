import streamlit as st

def main():
    st.title("Navbar Example")

    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "About", "Contact"))

    # Render different pages based on user selection
    if page == "Home":
        render_home()
    elif page == "About":
        render_about()
    elif page == "Contact":
        render_contact()

def render_home():
    st.header("Home Page")
    st.write("Welcome to the home page!")

def render_about():
    st.header("About Page")
    st.write("This is the about page.")

def render_contact():
    st.header("Contact Page")
    st.write("You can reach us at contact@example.com.")

if __name__ == "__main__":
    main()