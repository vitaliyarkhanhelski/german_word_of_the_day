import streamlit as st
from pathlib import Path
from main import get_german_word_of_the_day
import markdown

# Page configuration
st.set_page_config(
    page_title="German Word of the Day",
    page_icon="🇩🇪",
    layout="centered"
)

# Load CSS from external file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

css_file = Path(__file__).parent / "style.css"
load_css(css_file)

# Title
st.markdown("""
    <div class="title-container">
        <h2 class="main-title">🇩🇪 Słówko Dnia</h2>
        <p class="subtitle">Twoje codzienne słówko po niemiecku z listy Top 2000</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'word_result' not in st.session_state:
    st.session_state.word_result = None

# Center button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Losuj Słówko", use_container_width=True):
        with st.spinner("Generuję słówko..."):
            try:
                st.session_state.word_result = get_german_word_of_the_day()
                st.balloons()  # Show balloons effect on success
            except Exception as e:
                st.session_state.word_result = f"❌ Błąd: {str(e)}"

# Display result
if st.session_state.word_result:
    # Check if it's an error message
    if st.session_state.word_result.startswith("❌"):
        st.error(st.session_state.word_result)
    else:
        # Convert markdown to HTML and wrap in styled container
        html_content = markdown.markdown(st.session_state.word_result)
        wrapped_html = f'''
        <div class="result-box-wrapper">
            {html_content}
        </div>
        '''
        st.markdown(wrapped_html, unsafe_allow_html=True)

