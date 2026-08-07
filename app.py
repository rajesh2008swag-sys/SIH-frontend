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
    st.session_state.app_state = 'introduction'

# 2. Clean Streamlit Light Theme Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .main {
        background-color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Colorful Feature Cards */
    .card-cyan {
        background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
        border: 1px solid #06b6d4;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #0e7490;
    }
    .card-purple {
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
        border: 1px solid #8b5cf6;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #6d28d9;
    }
    .card-amber {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border: 1px solid #f59e0b;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        color: #b45309;
    }

    .studio-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: INTRODUCTION PAGE
# =========================================================================
if st.session_state.app_state == 'introduction':
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        st.markdown("📌 **Introduction**")
        st.markdown("📖 **Overview**")
        st.markdown("⚙️ **System Architecture**")

    st.markdown("""
        <div style="max-width: 900px; margin: 30px auto; padding: 20px;">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #4f46e5; text-transform: uppercase; margin-bottom: 8px;">
                Government of Rajasthan | Smart India Hackathon Initiative
            </div>
            <h1 style="font-size: 42px; font-weight: 800; color: #0f172a; letter-spacing: -1px; margin-bottom: 15px;">
                EduShield AI — Institutional Early Warning & Prediction System
            </h1>
            <p style="font-size: 16px; color: #475569; line-height: 1.6; margin-bottom: 30px;">
                Welcome to the official state-level intelligence platform. EduShield AI analyzes student data vectors in real time, flags dropout risks, and automates emergency administrative interventions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.markdown("""
            <div class="card-cyan">
                <h4 style="color: #0e7490; margin-top:0;">📊 Risk Profiler</h4>
                <p style="font-size: 13px; color: #155e75; margin-bottom:0;">Instant predictive evaluations using advanced machine learning models.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-purple">
                <h4 style="color: #6d28d9; margin-top:0;">👥 Student Repository</h4>
                <p style="font-size: 13px; color: #5b21b6; margin-bottom:0;">Centralized database synchronization for live student records.</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="card-amber">
                <h4 style="color: #b45309; margin-top:0;">🚨 Intervention Hub</h4>
                <p style="font-size: 13px; color: #92400e; margin-bottom:0;">Automated alert dispatch and counselor ticket management.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c_btn1, c_btn2, c_btn3 = st.columns([2, 2, 2])
    with c_btn2:
        if st.button("🚀 Get Started // Enter Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: DASHBOARD VIEW
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
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.app_state = 'introduction'
            st.rerun()

    if selected_option == "🏠 Dashboard":
        st.markdown("<h2>Dashboard</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b; margin-top: -10px; margin-bottom: 25px;'>Government of Rajasthan • AI-based Student Dropout Prediction System</p>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 34px; font-weight: 700; color: #0f172a;">5</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">Students</p>
                </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 34px; font-weight: 700; color: #dc2626;">2</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">High Risk</p>
                </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 34px; font-weight: 700; color: #d97706;">1</h1>
                    <p style="margin:5px 0 0 0; color: #64748b; font-size: 13px;">Medium Risk</p>
                </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 34px; font-weight: 700; color: #16a34a;">2</h1>
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
        if st.button("🔄 Sync Database Records"):
            try:
                resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
                if resp.status_code == 200:
                    records = resp.json()
                    if records:
                        st.dataframe(pd.DataFrame(records), use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")

    elif selected_option == "⚡ AI Prediction":
        st.markdown("<h2>AI Vulnerability Prediction</h2>", unsafe_allow_html=True)
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
                st.error("Please fill in Student ID and Institution Name.")
            else:
                payload = {
                    "Student_ID": student_id, "School": school_name, "Gender": gender,
                    "Fees_Paid_Status": fees_status, "Internet_Access": internet_access,
                    "Family_Support": family_support, "Wants_Higher_Education": wants_higher_ed,
                    "Medical_Status": medical_status, "School_Support": "Yes",
                    "Extra_Paid_Class": "No", "Extra_Curricular_Activities": "Yes",
                    "Number_of_Absences": int(absences), "Number_of_Failures": int(failures),
                    "Final_Grade": float(final_grade)
                }
                try:
                    res = requests.post(f"{API_BASE_URL}/api/predict/custom", json=payload, timeout=15)
                    if res.status_code == 200:
                        data = res.json()
                        st.success(f"Risk Score Calculated: **{data.get('risk_score')}%** ({data.get('risk_tier')})")
                except Exception as err:
                    st.error(f"Error: {err}")

    elif selected_option == "📊 Analytics":
        st.markdown("<h2>Regional Intelligence & Analytics</h2>", unsafe_allow_html=True)
        if st.button("Generate District Telemetry"):
            try:
                resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
                if resp.status_code == 200:
                    res_data = resp.json()
                    summary = res_data.get("summary", {})
                    k1, k2, k3, k4 = st.columns(4)
                    with k1: st.metric("Monitored", summary.get("total_students_monitored", 0))
                    with k2: st.metric("Dropouts", summary.get("historical_dropouts", 0))
                    with k3: st.metric("Unpaid Fees", summary.get("students_with_unpaid_fees", 0))
                    with k4: st.metric("Absences", summary.get("students_chronically_absent", 0))
            except Exception as ex:
                st.error(f"Error: {ex}")

    elif selected_option in ["💬 Counselling", "📋 Reports"]:
        st.markdown(f"<h2>{selected_option} Hub</h2>", unsafe_allow_html=True)
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
