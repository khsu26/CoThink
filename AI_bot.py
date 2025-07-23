import streamlit as st
import openai
import os

# set up openai api key
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

st.title("AI Study Assistant")
st.write("Upload or paste your notes below. Choose a learning tool to help you review!")

# upload file .txt
uploaded_file = st.file_uploader("Upload a study guide (.txt)", type=["txt"])
uploaded_text = ""
if uploaded_file is not None:
    uploaded_text = uploaded_file.read().decode("utf-8")
    st.success("File uploaded successfully!")

# study guide text area
study_text = st.text_area("Or paste your study guide here:", height=300)

# combine inputs for processing
full_input = uploaded_text + "\n" + study_text

# 3 buttons
col1, col2, col3 = st.columns(3)
response = ""

# flashcard generator
def generate_flashcards(text):
    prompt = f"Turn the following study guide into Q&A flashcards:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# summary generator
def summarize_notes(text):
    prompt = f"Summarize the following notes clearly and concisely in bullet points:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# practice problem generator
def generate_problem_with_steps(text):
    prompt = (
        f"Based on this study guide:\n\n{text}\n\n"
        "Create one thoughtful critical thinking or timeline-based question. Then walk the student through solving it step-by-step, "
        "encouraging reasoning and historical/contextual thinking. Do not give the final answer too early—guide instead."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# initialize chat history
if "practice_history" not in st.session_state:
    st.session_state.practice_history = []

# button logic
with col1:
    if st.button("📂 Generate Flashcards"):
        if full_input.strip():
            response = generate_flashcards(full_input)
        else:
            st.warning("Please paste or upload a study guide first.")

with col2:
    if st.button("📝 Summarize Notes"):
        if full_input.strip():
            response = summarize_notes(full_input)
        else:
            st.warning("Please paste or upload a study guide first.")

with col3:
    if st.button("🧠 Teach Problem-Solving"):
        if full_input.strip():
            new_response = generate_problem_with_steps(full_input)
            st.session_state.practice_history.append(new_response)
        else:
            st.warning("Please paste or upload a study guide first.")

# output display
if response:
    st.markdown("### 🔍 Output")
    st.markdown(response)

# problem-solving history
if st.session_state.practice_history:
    st.markdown("---")
    st.markdown("### 📘 Practice Walkthroughs")
    for i, entry in enumerate(st.session_state.practice_history, 1):
        st.markdown(f"**Practice {i}:**")
        st.markdown(entry)
        st.markdown("---")
