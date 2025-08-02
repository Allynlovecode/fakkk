import streamlit as st
import smtplib
from email.message import EmailMessage

# ----- PAGE SETTINGS -----
st.set_page_config(page_title="Reflect & Apologize", layout="centered")

# ----- BACKGROUND MUSIC -----
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3">
Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)

# ----- CUSTOM STYLES -----
st.markdown("""
<style>
body {
    background-color: #4b227a;
}
.block-container {
    padding: 2rem 2rem 4rem;
    background-color: #4b227a;
    border-radius: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
h1 {
    text-align: center;
    color: #9e55f2;
}
textarea, input {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.title("**😔 Reflection time**")
st.markdown('<p style="font-size:20px; color:#f20f07;"><b>SAKITLA HATI KAU BUAT AKU CAMNI</b></p>', unsafe_allow_html=True)

# ----- QUESTIONS -----
what_happened = st.text_area("**💭 Apa salah kau ?**", height=120, placeholder="Apa kau rasa kau buat sampai aku marah")
what_i_felt = st.text_area("**🥺 Apa perasaan aku terhadap apa kau buat ?**", height=120, placeholder="Fikir perasaan aku, dasar nigger")
apology = st.text_area("**📝 Words to show youre sorry (no pendek allowed)**", height=200, placeholder="Taknak Sorry bocah")

# ----- OPEN-ENDED QUIZ -----
q1 = st.text_input("**🔎 Kau sedar tak kau buat salah**")
q2 = st.text_input("**📖 Apa je kau benda yang kau tau dan noted**")
q3 = st.text_input("**🚫 Nak buat lagi ke**")

# ----- SUBMIT -----
if st.button("📨 Submit & Send Apology"):
    email = EmailMessage()
    email['Subject'] = "💌 Apology Submission"
    email['From'] = "accforgenshin8@gmail.com"
    email['To'] = "accforgenshin8@gmail.com"

    content = f"""
Someone submitted a reflection:

💭 What they think they did:
{what_happened}

🥺 What they think you felt:
{what_i_felt}

📝 Their apology:
{apology}

🔎 Quiz Answers:
1. How it affected you: {q1}
2. Lesson learned: {q2}
3. Future actions: {q3}
"""

    email.set_content(content)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("accforgenshin8@gmail.com", "hxyp skpa gxuh hjrq")
            smtp.send_message(email)

        st.success("✅ Your answers have been sent.")

        # ----- DRAMATIC FINAL MESSAGE -----
        st.markdown("""
        <div style="text-align: center; margin-top: 3rem; font-size: 1.5rem; color: #991b1b;">
             <b>Your answers have been submitted.</b><br><br>
            The <i>Higher Authority</i> will now review<br>
            whether you are <b>worthy of forgiveness</b>.<br><br>
            <i>You will know… in time.</i>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Something went wrong: {e}")

