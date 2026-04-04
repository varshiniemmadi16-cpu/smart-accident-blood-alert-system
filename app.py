import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import random
import os
import smtplib
from email.mime.text import MIMEText

# ---------------- EMAIL FUNCTION ----------------
def send_email_to_all(donor_emails, blood_needed, hospital, location, contact, patient_name):
    sender_email = "varshiniemmadi16@gmail.com"
    app_password = "roaxjvqiechfvjvm"

    subject = "🚨 Emergency Blood Requirement!"
    maps_link = f"https://www.google.com/maps/search/{location.replace(' ', '+')}"
    body = f"""
    🚑 URGENT ALERT!
    Blood Required: {blood_needed}
    🏥 Hospital: {hospital}
    📍 Location: {location}
    📞 Contact: {contact}
    📍 Directions: {maps_link}
    Please reach immediately if you can donate.
    🙏 Your help can save a life.
    """

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, app_password)

    for email in donor_emails:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email
        server.sendmail(sender_email, email, msg.as_string())

    server.quit()

# ---------------- FAKE ACCIDENT DETECTION ----------------
def fake_accident_detection(image_file):
    filename = os.path.basename(image_file.name).lower()
    if "accident" in filename:
        return True

    image = Image.open(image_file).convert("RGB")
    image_np = np.array(image)
    red_pixels = np.sum((image_np[:,:,0] > 180) & (image_np[:,:,1] < 100) & (image_np[:,:,2] < 100))
    total_pixels = image_np.shape[0] * image_np.shape[1]
    if red_pixels / total_pixels > 0.10:
        return True
    return False

# ---------------- UI ----------------
st.set_page_config(page_title="Smart Accident System", layout="wide")
st.sidebar.title("🚨 Smart System")
st.sidebar.info("Accident Detection + Blood Alert")

# ---------------- MULTI-LANGUAGE ----------------
languages = {"English": "en", "Telugu": "te", "Hindi": "hi"}
selected_lang = st.sidebar.selectbox("Select Language / భాష / भाषा", list(languages.keys()))
lang = languages[selected_lang]

translations = {
    "en": {
        "menu_home": "Home",
        "menu_detection": "Detection",
        "menu_donor_register": "Donor Register",
        "menu_search_donor": "Search Donor",
        "patient_name": "🧑‍🦽 Enter Patient Name",
        "hospital": "🏥 Enter Hospital Name",
        "location": "📍 Enter Location",
        "contact": "📞 Enter Contact Number",
        "send_alert": "🚨 Send Alert",
        "accident_detected": "🚨 Accident Detected by AI!",
        "no_accident": "✅ No accident detected by AI.",
        "blood_needed": "Select Required Blood",
        "available_donors": "🩸 Available Donors:",
        "fill_all": "⚠️ Please fill all emergency details!",
        "name": "Name",
        "email": "Email",
        "blood_group": "Blood Group",
        "register": "Register",
        "donor_registered": "✅ Donor Registered Successfully!",
        "no_donors": "No donors registered yet!",
        "upload_image": "Upload an image to detect accident."
    },
    "te": {
        "menu_home": "హోమ్",
        "menu_detection": "ప్రమాద గుర్తింపు",
        "menu_donor_register": "దాత నమోదు",
        "menu_search_donor": "దాతలు శోధించండి",
        "patient_name": "🧑‍🦽 రోగి పేరు నమోదు చేయండి",
        "hospital": "🏥 ఆసుపత్రి పేరు నమోదు చేయండి",
        "location": "📍 స్థానం నమోదు చేయండి",
        "contact": "📞 సంప్రదింపు సంఖ్య నమోదు చేయండి",
        "send_alert": "🚨 అలర్ట్ పంపండి",
        "accident_detected": "🚨 AI ద్వారా ప్రమాదం గుర్తించబడింది!",
        "no_accident": "✅ ప్రమాదం గుర్తించబడలేదు.",
        "blood_needed": "అవసరమైన రక్తాన్ని ఎంచుకోండి",
        "available_donors": "🩸 లభ్యమయ్యే దాతలు:",
        "fill_all": "⚠️ దయచేసి అన్ని అత్యవసర వివరాలను నమోదు చేయండి!",
        "name": "పేరు",
        "email": "ఇమెయిల్",
        "blood_group": "రక్త సమూహం",
        "register": "నమోదు చేయండి",
        "donor_registered": "✅ దాత విజయవంతంగా నమోదు అయ్యారు!",
        "no_donors": "ఏ దాతలు నమోదు కాలేదు!",
        "upload_image": "ప్రమాదం గుర్తించడానికి చిత్రం అప్లోడ్ చేయండి."
    },
    "hi": {
        "menu_home": "होम",
        "menu_detection": "दुर्घटना पहचान",
        "menu_donor_register": "दाता पंजीकरण",
        "menu_search_donor": "दाता खोजें",
        "patient_name": "🧑‍🦽 रोगी का नाम दर्ज करें",
        "hospital": "🏥 अस्पताल का नाम दर्ज करें",
        "location": "📍 स्थान दर्ज करें",
        "contact": "📞 संपर्क नंबर दर्ज करें",
        "send_alert": "🚨 अलर्ट भेजें",
        "accident_detected": "🚨 AI द्वारा दुर्घटना का पता चला!",
        "no_accident": "✅ कोई दुर्घटना नहीं मिली।",
        "blood_needed": "आवश्यक रक्त चुनें",
        "available_donors": "🩸 उपलब्ध दाता:",
        "fill_all": "⚠️ कृपया सभी आपातकालीन विवरण भरें!",
        "name": "नाम",
        "email": "ईमेल",
        "blood_group": "रक्त समूह",
        "register": "पंजीकरण करें",
        "donor_registered": "✅ दाता सफलतापूर्वक पंजीकृत!",
        "no_donors": "कोई दाता पंजीकृत नहीं है!",
        "upload_image": "दुर्घटना का पता लगाने के लिए चित्र अपलोड करें।"
    }
}
t = translations[lang]

# ---------------- MENU ----------------
menu = [
    t["menu_home"],
    t["menu_detection"],
    t["menu_donor_register"],
    t["menu_search_donor"]
]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- HOME ----------------
if choice == t["menu_home"]:
    st.markdown("# 🚨 Smart Accident Detection & Blood Alert System")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        ## 🚑 Emergency Response System
        This system helps in:
        - 🚗 Detecting accident emergencies  
        - 🩸 Connecting with blood donors  
        - ⚡ Sending quick alerts  
        👉 Built to save lives in critical situations
        """)
        st.success("✅ System Ready to Use")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966485.png")

# ---------------- DETECTION ----------------
elif choice == t["menu_detection"]:
    st.header("🚨 Emergency Blood Request")
    uploaded_file = st.file_uploader(t["upload_image"], type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Accident Image", use_column_width=True)
        accident_detected = fake_accident_detection(uploaded_file)
        if accident_detected:
            st.error(t["accident_detected"])
            if os.path.exists("donors.csv"):
                df = pd.read_csv("donors.csv")
                df = pd.read_csv("donors.csv")
                # ✅ ADD HERE (Step 1)
                df.columns = df.columns.str.strip()
                df = df.dropna(subset=["Email", "Blood"])
                df["Blood"] = df["Blood"].astype(str).str.strip().str.upper()
                df["Location"] = df["Location"].astype(str).str.strip().str.lower()
                blood_needed = st.selectbox(t["blood_needed"],["A+","A-","B+","B-","O+","O-","AB+","AB-"])
                patient_name = st.text_input(t["patient_name"])
                hospital = st.text_input(t["hospital"])
                location = st.text_input(t["location"])
                contact = st.text_input(t["contact"])
                result = df[(df["Blood"] == blood_needed.upper()) &(df["Location"].str.contains(location.lower(), na=False))]
                st.write(t["available_donors"])
                st.dataframe(result)
                if st.button(t["send_alert"]):
                    if not patient_name or not hospital or not location or not contact:
                        st.warning(t["fill_all"])
                    else:
                        if "Email" in result.columns:
                            donor_emails = result["Email"].dropna().astype(str).tolist()
                            st.write("📧 Emails being sent:", donor_emails)
                            if donor_emails:
                                send_email_to_all(donor_emails, blood_needed, hospital, location, contact, patient_name)
                                st.success("📲 Alert sent to ALL matching donors!")
                            else:
                                st.warning("No donor emails found!")
                        else:
                            st.error("⚠️ Email column missing!")
            else:
                st.warning(t["no_donors"])
        else:
            st.success(t["no_accident"])
    else:
        st.info(t["upload_image"])

# ---------------- DONOR REGISTER ----------------
elif choice == t["menu_donor_register"]:
    st.header("🩸 Donor Registration")
    name = st.text_input(t["name"])
    email = st.text_input(t["email"])
    blood = st.selectbox(t["blood_group"], ["A+","A-","B+","B-","O+","O-","AB+","AB-"])
    location = st.text_input(t["location"])
    if st.button(t["register"]):
        data = pd.DataFrame([[name,email,blood,location]], columns=["Name","Email","Blood","Location"])
        if os.path.exists("donors.csv"):
            data.to_csv("donors.csv", mode='a', header=False, index=False)
        else:
            data.to_csv("donors.csv", index=False)
        st.success(t["donor_registered"])

# ---------------- SEARCH DONOR ----------------
elif choice == t["menu_search_donor"]:
    st.header("🔍 Search Donors")
    blood_needed = st.selectbox(t["blood_needed"], ["A+","A-","B+","B-","O+","O-","AB+","AB-"])
    location_needed = st.text_input(t["location"])
    if os.path.exists("donors.csv"):
        df = pd.read_csv("donors.csv")
        result = df[(df["Blood"]==blood_needed) & (df["Location"].str.lower()==location_needed.lower())]
        st.dataframe(result)
    else:
        st.warning(t["no_donors"])
