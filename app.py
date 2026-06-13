import streamlit as st
import random

st.set_page_config(
    page_title="Who is the Duffer?",
    page_icon="😎",
    layout="wide"
)

# -----------------------
# Chocolate Background
# -----------------------
st.markdown("""
<style>
.stApp{
    background-color:#7B3F00;
}

.main-title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
    margin-top:100px;
}

.question{
    text-align:center;
    color:white;
    font-size:36px;
    font-weight:bold;
}

.center{
    display:flex;
    justify-content:center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Session State
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = 1

# -----------------------
# PAGE 1
# -----------------------
if st.session_state.page == 1:

    st.markdown(
        "<div class='main-title'>Are you MAX??</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    c1, c2, c3 = st.columns([2,1,1])

    with c2:
        if st.button("YES", use_container_width=True):
            st.session_state.page = 2
            st.rerun()

    with c3:
        st.button("NO", use_container_width=True)

# -----------------------
# PAGE 2
# -----------------------
elif st.session_state.page == 2:

    st.markdown(
        "<div class='question'>Choose the correct answer:<br>Who is the DUFFER?</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    image_col1, image_col2 = st.columns(2)

    with image_col1:
        st.image("max.jpg", width=250)

    with image_col2:
        st.image("sakshi.jpg", width=250)

    st.write("")

    # Randomize Sakshi position
    sakshi_position = random.randint(0, 4)

    cols = st.columns(5)

    # Max button always visible
    with cols[2]:
        if st.button("MAX", use_container_width=True):
            st.session_state.page = 3
            st.rerun()

    # Sakshi button appears randomly
    with cols[sakshi_position]:
        if st.button("SAKSHI", use_container_width=True):
            st.success("Nice try 😏")
            st.rerun()

# -----------------------
# PAGE 3
# -----------------------
elif st.session_state.page == 3:

    st.markdown(
        "<div class='question'>Correct Answer: MAX 😂</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.video("video.mp4")