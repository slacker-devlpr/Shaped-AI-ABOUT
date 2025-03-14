import streamlit as st
# Page config:
st.set_page_config(
    page_title="ShapedAI, old",
    page_icon=r"Anka (7).png"
)



# Hide all unneeded parts of streamlit:
hide_streamlit_style = """
<style>
.css-hi6a2p {padding-top: 0rem;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
hide_streamlit_style = """
<style>
div[data-testid="stToolbar"] {
visibility: hidden;
height: 0%;
position: fixed;
}
div[data-testid="stDecoration"] {
visibility: hidden;
height: 0%;
position: fixed;
}
div[data-testid="stStatusWidget"] {
visibility: hidden;
height: 0%;
position: fixed;
}
#MainMenu {
visibility: hidden;
height: 0%;
}
header {
visibility: hidden;
height: 0%;
}
footer {
visibility: hidden;
height: 0%;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown('''
<style>
.stApp [data-testid="stToolbar"]{
    display:none;
}
</style>
''', unsafe_allow_html=True)
enable_scroll = """
<style>
.main {
    overflow: auto;
}
</style>
"""
st.markdown(enable_scroll, unsafe_allow_html=True)
st.title("Renaming to AnkaAI!")
st.write("Due to trademark reasons, we have rebranded from Shaped AI to Anka AI. While our name has changed, our mission and commitment to innovation remain the same. Thank you for your support as we continue to grow under our new identity!")

st.link_button("Go to AnkaAI", "https://anka-ai.streamlit.app", use_container_width=True)
