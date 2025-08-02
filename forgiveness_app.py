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
    background-color: #8e2fc4;
    font-family: 'Sora', sans-serif;
}
.block-container {
    padding: 2rem 2rem 4rem;
    background-color: #8e2fc4;
    border-radius: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
textarea, input {
    border-radius: 10px !important;
}
h1 {
    text-align: center;
    color: #ffddf4;
}
label[data-testid="stMarkdownContainer"] > div {
    font-size: 20px;
    color: #ffd2f0;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title("**⋆˙⟡😾 Reflect otak mung⋆˙⟡**")
st.markdown('<p style="font-size:20px; color:#f20f07;"><b>SAKITLA HATI KAU BUAT AKU CAMNI</b></p>', unsafe_allow_html=True)

# --- QUESTIONS ---
what_happened = st.text_area("😿 Apa salah kau ?", height=120, placeholder="Apa kau rasa kau buat sampai aku marah")
what_i_felt = st.text_area("😾 Apa perasaan aku terhadap apa kau buat ?", height=120, placeholder="Fikir perasaan aku, dasar nigger")
apology = st.text_area("📄 Words to show you're sorry (no pendek allowed)", height=200, placeholder="Taknak Sorry bocah")

# --- OPEN-ENDED QUIZ ---
q1 = st.text_input("❓ Kau sedar tak kau buat salah")
q2 = st.text_input("✏️ Apa je benda yang kau tau dan noted")
q3 = st.text_input("❗ Nak buat lagi ke")

# --- SUBMIT BUTTON ---
if st.button("📨 Bagi aku baca"):
    if what_happened and what_i_felt and apology and q1 and q2 and q3:
        answers = {
            "💭 Apa salah dia?": what_happened,
            "🥺 Apa perasaan kau?": what_i_felt,
            "📝 Apology panjang": apology,
            "🔎 Kau sedar tak kau buat salah": q1,
            "📖 Apa kau noted": q2,
            "🚫 Nak buat lagi ke": q3
        }

        try:
            send_email(answers)

            # --- Show POPUP + Blur BG ---
            st.markdown("""
            <style>
            /* Blur background */
            .main {
                filter: blur(10px);
                pointer-events: none;
            }
            /* Overlay */
            #overlay-blur {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background-color: rgba(0, 0, 0, 0.4);
                z-index: 998;
            }
            /* Popup Box */
            .submission-box {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: #4a1a66;
                color: #a67ebd;
                padding: 2rem;
                border-radius: 25px;
                text-align: center;
                box-shadow: 0 8px 24px rgba(0,0,0,0.3);
                font-size: 20px;
                z-index: 999;
                animation: fadeIn 1.0s ease-in-out;
            }
            @keyframes fadeIn {
                0% { opacity: 0; transform: translate(-50%, -60%); }
                100% { opacity: 1; transform: translate(-50%, -50%); }
            }
            </style>

            <div id="overlay-blur"></div>
            <div class="submission-box">
                <b>₊˚⊹ ᰔ Your damn reflection has been submitted ₊˚⊹ ᰔ</b><br><br>
                So nanti <i>ayat manis kau</i>aku baca<br>
                Whether you are <b>worthy of forgiveness</b>.<br><br>
                <i>Hmph</i> 
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
    else:
        st.error("❌ JAWAB LA SEMUA SHIBAL")

