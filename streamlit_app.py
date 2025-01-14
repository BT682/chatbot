import streamlit as st
import openai
import os

# Set your OpenAI API key securely
# Option 1: Use environment variables (recommended)
openai.api_key = os.getenv("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")

# Option 2: Use Streamlit's secrets management
# Uncomment the line below and set your API key in .streamlit/secrets.toml
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to correct grammar
def correct_grammar(text):
    prompt = f"Please correct the grammar, spelling, and punctuation of the following text:\n\n{text}\n\nCorrected text:"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use 'gpt-4' if you have access
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,  # For consistent results
        )
        corrected_text = response.choices[0].message.content.strip()
        return corrected_text
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app interface
def main():
    st.title("English Grammar Checker")
    st.write("Enter your text below and click 'Correct Grammar' to see the corrected version.")

    # Text input
    user_input = st.text_area("Your Text:", height=200)

    if st.button("Correct Grammar"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Correcting..."):
                corrected_text = correct_grammar(user_input)
            st.subheader("Corrected Text:")
            st.write(corrected_text)

if __name__ == "__main__":
    main()
