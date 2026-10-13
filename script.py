import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Hello, what's your name?")

name = st.text_input("")

if name:
    st.markdown(
        """
        <div style="text-align: center; font-size: 35px;">
            💗 💕 💗 💕 💗
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h2 style='text-align: center;'> {name} ДУРА!</h2>",
        unsafe_allow_html=True
    )
    st.image(r"dog.jpg",
        width=350)
    st.balloons()
