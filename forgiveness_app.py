import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- Email Sender Function ---
def send_email(answers):
    sender_email = "ainamalia@gmail.com"
    receiver_email = "ainamalia@gmail.com"
    app_password = "hxypskpagxuhhjrq"

    body = "Submission Received:\n\n"
    for question, answer in answers.items():
        body += f"{question}\n{answer}\n\n"

    message = MIMEText(body)
    message["Subject"] = "💌 Apology Submission Received"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Reflect & Apologize", layout="centered")

# --- BACKGROUND MUSIC ---
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
""", unsafe_allow_html=True)

# --- CUSTOM STYLES ---
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

# --- TITLE ---
st.title("**😔 Reflection time**")
st.markdown('<p style="font-size:20px; color:#f20f07;"><b>SAKITLA HATI KAU BUAT AKU CAMNI</b></p>', unsafe_allow_html=True)

# --- QUESTIONS ---
what_happened = st.text_area("**💭 Apa salah kau ?**", height=120, placeholder="Apa kau rasa kau buat sampai aku marah")
what_i_felt = st.text_area("**🥺 Apa perasaan aku terhadap apa kau buat ?**", height=120, placeholder="Fikir perasaan aku, dasar nigger")
apology = st.text_area("**📝 Words to show youre sorry (no pendek allowed)**", height=200, placeholder="Taknak Sorry bocah")

# --- OPEN-ENDED QUIZ ---
q1 = st.text_input("**🔎 Kau sedar tak kau buat salah**")
q2 = st.text_input("**📖 Apa je kau benda yang kau tau dan noted**")
q3 = st.text_input("**🚫 Nak buat lagi ke**")

# --- SUBMIT BUTTON ---
if st.button("📨 Submit & Send Apology"):
    if what_happened and what_i_felt and apology and q1 and q2 and q3:
        answers = {
            "💭 Apa salah dia?": what_happened,
            "🥺 Apa perasaan kau?": what_i_felt,
            "📝 Apology panjang": apology,
            "🔎 Kau sedar tak kau buat salah": q1,
            "📖 Apa kau noted": q2,
            "🚫 Nak buat lagi ke": q3
        }

        send_email(answers)
        st.success("✅ k, dah bla")

        st.markdown("""
        <div style="text-align: center; margin-top: 3rem; font-size: 1.5rem; color: #f20f07;">
            <b>Your damn reflection have been submitted.</b><br><br>
            The <i>Higher Authority</i> will now review<br>
            whether you are <b>worthy of forgiveness</b>.<br><br>
            <i>You will know… in time.</i>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("❌ ISI LAH SEMUA ADUHHH")
