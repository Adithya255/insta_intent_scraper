import streamlit as st
import pandas as pd

# Define keyword categories
INTENT_KEYWORDS = {
    "Wants Instagram Growth": ["grow", "growth", "followers", "reach", "boost", "scale my page"],
    "Hiring Social Media Expert": ["hiring", "freelancer", "looking for", "social media expert", "need smm", "join our team"],
    "Needs Paid Ads Help": ["ads", "facebook ads", "run ads", "paid campaign", "ad expert", "need ads help"],
    "Open to Collaboration": ["collab", "collaboration", "dm for collab", "brand partner", "let's collab", "open for collab"],
    "Scaling Business": ["scale", "launch", "growing fast", "next level", "rebrand", "expanding"],
}

# Function to detect intent
def detect_intent(text):
    text = str(text).lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                return intent
    return "No clear intent"

# Streamlit UI
st.title("🧠 Instagram Lead Intent Detector")
st.write("Upload your CSV with bios, captions, or scraped text. We'll auto-detect buyer intent.")

uploaded_file = st.file_uploader("📤 Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    text_column = st.selectbox("📝 Select the column with Bio/Post text", df.columns)
    
    # Detect intent
    df["Detected Intent"] = df[text_column].apply(detect_intent)

    st.success("✅ Intent detection complete.")
    st.dataframe(df)

    # Download link
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download enriched CSV", csv, "intent_enriched_leads.csv", "text/csv")
