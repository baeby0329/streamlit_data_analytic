import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add a text input field
    name = st.text_input("Enter your name", "")
    
    # Add a button
    button_clicked = st.button("Submit")
    
    # Execute code when the button is clicked
    if button_clicked:
        if name:
            st.success(f"Hello, {name}!")
        else:
            st.warning("Please enter your name.")

if __name__ == "__main__":
    main()
