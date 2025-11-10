import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAqJw3GMzGUiSH8XmofqdEKDX34oLlIaLE")  # Replace with your Gemini API key

# Load the model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="AI Debug Buddy", page_icon="🧠")
st.title("🧠 AI Debug Buddy")
st.write("Paste your failing **stacktrace or error log** below to get AI-guided debugging steps.")

# Input box for stacktrace only
stacktrace = st.text_area("Paste your stacktrace here:", height=250, placeholder="Example: Traceback (most recent call last): ...")

if st.button("🔍 Analyze Error"):
    if stacktrace.strip() == "":
        st.warning("Please paste a stacktrace before analyzing.")
    else:
        with st.spinner("Analyzing your error using AI..."):
            prompt = f"""
            You are an expert Python debugger. Analyze the following stacktrace and explain:
            1. The root cause of the error.
            2. What part of the code might be responsible.
            3. Step-by-step debugging or fix suggestions.
            
            Stacktrace:
            {stacktrace}
            """

            response = model.generate_content(prompt)
            st.success("✅ AI Debugging Steps:")
            st.markdown(response.text)
