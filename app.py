import streamlit as st
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="EduShield AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://sih-student-api.onrender.com"

# Initialize Session State
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'landing'

# 2. Forced Pure White Theme & Colorful Card CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Force Entire App Background to Pure White */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Force All Main Content Containers to White */
    [data-testid="stMain"], .main, .block-container {
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Force All Text Elements to Dark Slate */
    h1, h2, h3, h4, h5, h6, span, p, label, div {
        color: #0f172a;
    }

    /* Left Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #21262d;
        padding-top: 20px;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Colorful Feature Boxes for Landing Page */
    .landing-card-cyan {
        background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%) !important;
        border: 2px solid #06b6d4 !important;
        padding: 28px !important;
        border-radius: 12px !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(6, 182, 212, 0.1);
    }
    .landing-card-cyan h3, .landing-card-cyan p {
        color: #0e7490 !important;
    }

    .landing-card-purple {
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%) !important;
        border: 2px solid #8b5cf6 !important;
        padding: 28px !important;
        border-radius: 12px !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(139, 92, 246, 0.1);
    }
    .landing-card-purple h3, .landing-card-purple p {
        color: #6d28d9 !important;
    }

    .landing-card-amber {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%) !important;
        border: 2px solid #f59e0b !important;
        padding: 28px !important;
        border-radius: 12px !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(245, 158, 11, 0.1);
    }
    .landing-card-amber h3, .landing-card-amber p {
        color: #b45309 !important;
    }

    /* Standard Dashboard Cards */
    .studio-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }

    /* Primary Action Buttons */
    .stButton>button {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.4rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: LANDING PAGE (Pure White with Colorful Cards)
# =========================================================================
if st.session_state.app_state == 'landing':
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        st.markdown("📌 **Introduction**")
        st.markdown("📖 **Overview**")
        st.markdown("⚙️ **System Architecture**")

    st.markdown("""
        <div style="max-width: 900px; margin: 40px auto; padding: 20px; text-align: center;">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #4f46e5; text-transform: uppercase; margin-bottom: 10px;">
                Government of Rajasthan | Smart India Hackathon Initiative // SIH25102
            </div>
            <h1 style="font-size: 46px; font-weight: 800; color: #0f172a; letter-spacing: -1.5px; margin-bottom: 15px;">
                EduShield AI <span style="color: #64748b; font-weight: 400;">// STUDIO</span>
            </h1>
            <p style="font-size: 16px; color: #475569; line-height: 1.6; margin-bottom: 40px;">
                An advanced institutional early warning and predictive machine learning platform designed to proactively track student retention, compute vulnerability indexes, and coordinate administrative counseling across the State of Rajasthan.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns(3, gap="large")
    with col_h1:
        st.markdown("""
            <div class="landing-card-cyan">
                <h3 style="margin-top:0; font-size: 18px; font-weight: 700;">01 // Neural Prediction</h3>
                <p style="font-size: 13px; margin:0; line-height: 1.5;">Real-time vector calculations assessing individual student dropout risk using behavioral metrics.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
            <div class="landing-card-purple">
                <h3 style="margin-top:0; font-size: 18px; font-weight: 700;">02 // Regional Intel</h3>
                <p style="font-size: 13px; margin:0; line-height: 1.5;">Macro-level aggregation across participating districts, providing deep insight into institutional attendance.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h3:
        st.markdown("""
            <div class="landing-card-amber">
                <h3 style="margin-top:0; font-size: 18px; font-weight: 700;">03 // Automated Hub</h3>
                <p style="font-size: 13px; margin:0; line-height: 1.5;">Instantaneous emergency ticket dispatch and post-intervention score reassessment for counselors.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])
    with col_btn2:
        if st.button("🚀 Get Started // Enter Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: ACTUAL DASHBOARD VIEW
# =========================================================================
else:
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        
        selected_option = st.radio(
            "Navigation",
            [
                "🏠 Dashboard", 
                "👥 Students", 
                "⚡ AI Prediction", 
                "📊 Analytics", 
                "💬 Counselling", 
                "📋 Reports"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("🚪 Logout / Overview", use_container_width=True):
            st.session_state.app_state = 'landing'
            st.rerun()

    st.markdown("""
        <div style="background-color: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 20px 32px; margin: -6rem -6rem 2rem -6rem; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-weight: 600; font-size: 15px; color: #0f172a;">Government of Rajasthan</div>
            <div style="font-size: 13px; color: #64748b; font-weight: 500;">👤 Admin Portal</div>
        </div>
    """, unsafe_allow_html=True)

    if selected_option == "🏠 Dashboard":
        st.markdown("<h2>Dashboard</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b; margin-top: -10px; margin-bottom: 25px;'>Government of Rajasthan • AI-based Student Dropout Prediction System</p>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 36px; font-weight: 700; color: #0f172a;">5</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">Students</p>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 36px; font-weight: 700; color: #dc2626;">2</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">High Risk</p>
                </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 36px; font-weight: 700; color: #d97706;">1</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">Medium Risk</p>
                </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 36px; font-weight: 700; color: #16a34a;">2</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">Low Risk</p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3>High Risk Students</h3>", unsafe_allow_html=True)
        risk_data = {
            "Name": ["Rahul Sharma", "Priya Singh"],
            "Attendance": [54, 62],
            "CGPA": [5.8, 6.2],
            "Risk": ["High", "High"]
        }
        st.dataframe(pd.DataFrame(risk_data), use_container_width=True, hide_index=True)

    elif selected_option == "👥 Students":
        st.markdown("<h2>Master Student Repository</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b;'>Synchronized records from cloud database.</p>", unsafe_allow_html=True)
        if st.button("🔄 Sync Database Records"):
            try:
                with st.spinner("Fetching cloud records..."):
                    resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
                if resp.status_code == 200:
                    records = resp.json()
                    if records:
                        st.dataframe(pd.DataFrame(records), use_container_width=True)
                    else:
                        st.info("No records found in repository.")
            except Exception as e:
                st.error(f"Connection error: {e}")

    elif selected_option == "⚡ AI Prediction":
        st.markdown("<h2>AI Vulnerability Prediction</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b;'>Provide student institutional telemetry to calculate risk vectors.</p>", unsafe_allow_html=True)

        with st.form("prediction_form"):
            col_f1, col_f2 = st.columns(2, gap="large")
            with col_f1:
                student_id = st.text_input("Student Unique ID / Roll Number*", placeholder="e.g., RJ-JP-2026-890")
                school_name = st.text_input("Institution Name*", placeholder="e.g., Govt Sr Sec School, Jaipur")
                gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
                fees_status = st.selectbox("Fees Status", options=["Paid", "Pending", "Unpaid"])
            with col_f2:
                internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
                family_support = st.selectbox("Family Academic Support", options=["Yes", "No"])
                wants_higher_ed = st.selectbox("Wants Higher Education", options=["Yes", "No"])
                medical_status = st.selectbox("Medical Health Status", options=["Good", "Average", "Poor"])

            col_n1, col_n2, col_n3 = st.columns(3)
            with col_n1:
                absences = st.number_input("Absences", min_value=0, max_value=100, value=4)
            with col_n2:
                failures = st.number_input("Past Failures", min_value=0, max_value=10, value=0)
            with col_n3:
                final_grade = st.number_input("Final Grade (0-100)", min_value=0.0, max_value=100.0, value=65.0)

            submit_pred = st.form_submit_button("🚀 Run AI Predictive Inference", use_container_width=True)

        if submit_pred:
            if not student_id.strip() or not school_name.strip():
                st.error("Please fill in both Student ID and Institution Name.")
            else:
                payload = {
                    "Student_ID": student_id,
                    "School": school_name,
                    "Gender": gender,
                    "Fees_Paid_Status": fees_status,
                    "Internet_Access": internet_access,
                    "Family_Support": family_support,
                    "Wants_Higher_Education": wants_higher_ed,
                    "Medical_Status": medical_status,
                    "School_Support": "Yes",
                    "Extra_Paid_Class": "No",
                    "Extra_Curricular_Activities": "Yes",
                    "Number_of_Absences": int(absences),
                    "Number_of_Failures": int(failures),
                    "Final_Grade": float(final_grade)
                }
                try:
                    with st.spinner("Computing neural risk vectors..."):
                        res = requests.post(f"{API_BASE_URL}/api/predict/custom", json=payload, timeout=15)
                    if res.status_code == 200:
                        data = res.json()
                        st.success(f"Risk Score Calculated: **{data.get('risk_score')}%** ({data.get('risk_tier')})")
                    else:
                        st.error("Prediction failed.")
                except Exception as err:
                    st.error(f"Error: {err}")

    elif selected_option == "📊 Analytics":
        st.markdown("<h2>Regional Intelligence & Analytics</h2>", unsafe_allow_html=True)
        if st.button("Generate District Telemetry"):
            try:
                with st.spinner("Aggregating macro metrics..."):
                    resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
                if resp.status_code == 200:
                    res_data = resp.json()
                    summary = res_data.get("summary", {})
                    
                    k1, k2, k3, k4 = st.columns(4)
                    with k1:
                        st.metric("Monitored", summary.get("total_students_monitored", 0))
                    with k2:
                        st.metric("Dropouts", summary.get("historical_dropouts", 0))
                    with k3:
                        st.metric("Unpaid Fees", summary.get("students_with_unpaid_fees", 0))
                    with k4:
                        st.metric("Absences", summary.get("students_chronically_absent", 0))
                    
                    schools = res_data.get("school_metrics", [])
                    if schools:
                        st.dataframe(pd.DataFrame(schools), use_container_width=True)
            except Exception as ex:
                st.error(f"Error: {ex}")

    elif selected_option in ["💬 Counselling", "📋 Reports"]:
        st.markdown(f"<h2>{selected_option} Hub</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b;'>Manage emergency tickets, counseling sessions, and compliance reports.</p>", unsafe_allow_html=True)
        
        target_id = st.text_input("Enter Student ID for Action", placeholder="e.g., RJ-JP-2026-890")
        if st.button("🚨 Dispatch Emergency Intervention Ticket"):
            if target_id:
                try:
                    r = requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_id}", timeout=10)
                    if r.status_code == 200:
                        st.success(f"Emergency ticket successfully dispatched for student `{target_id}`.")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter a valid Student ID.")
