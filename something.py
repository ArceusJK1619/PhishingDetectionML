import streamlit as st
import requests

def check_url_safety(url):
    # Implement your safety check logic here
    # This is just a placeholder, you might use a library or service for actual URL safety checks
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def main():
    st.markdown(
        """
        <style>
        div.st-ae st-af st-ag st-ah st-ai st-aj st-ak st-al st-am st-an st-ao st-ap st-aq st-ar st-as st-at st-au st-av st-aw st-ax st-ay st-az st-b0 st-b1 st-b2 st-b3 st-b4 st-b5 st-b6 st-b7 st-b8 st-b9 {
        border-radius: 40px;        
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("URL Safety Checker")
    url = st.text_input("Enter URL:")
    if st.button("Check Safety"):
        if url:
            is_safe = check_url_safety(url)
            if is_safe:
                st.success("The URL is safe.")
            else:
                st.error("The URL is not safe.")
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()