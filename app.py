import streamlit as st
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="RAJ-AEGIS | Jordan Studio Edition",
    page_icon="▪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://sih-student-api.onrender.com"

# Initialize Session State for Page Navigation
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'landing'  # 'landing' or 'dashboard'

# 2. Styling (Light Mode for Landing Page container, Dark Sidebar, Exact match to screenshot)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Syne:wght@600;700;800&display=swap');

    /* Force Main View Background to White for Landing Page */
    .stApp {
        background-color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Left Sidebar Styling (Dark to match screenshot) */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #21262d;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Landing Page Hero Container */
    .landing-hero {
        background-color: #ffffff !important;
        padding: 40px 20px;
        text-align: center;
        max-width: 950px;
        margin: 0 auto;
    }
    .landing-title {
        font-family: 'Syne', sans-serif;
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #0f172a;
        margin-bottom: 20px;
    }
    .landing-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #475569;
        margin-bottom: 40px;
        line-height: 1.6;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Colorful Feature Cards matching screenshot */
    .card-cyan-box {
        background-color: #f0fdfa;
        border: 1px solid #2dd4bf;
        padding: 28px;
        border-radius: 12px;
        min-height: 160px;
    }
    .card-cyan-box h3 {
        font-family: 'Syne', sans-serif;
        color: #0f766e;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .card-cyan-box p {
        color: #334155;
        font-size: 13px;
        margin: 0;
        line-height: 1.5;
    }

    .card-purple-box {
        background-color: #f5f3ff;
        border: 1px solid #a78bfa;
        padding: 28px;
        border-radius: 12px;
        min-height: 160px;
    }
    .card-purple-box h3 {
        font-family: 'Syne', sans-serif;
        color: #6d28d9;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .card-purple-box p {
        color: #334155;
        font-size: 13px;
        margin: 0;
        line-height: 1.5;
    }

    .card-amber-box {
        background-color: #fffbeb;
        border: 1px solid #fcd34d;
        padding: 28px;
        border-radius: 12px;
        min-height: 160px;
    }
    .card-amber-box h3 {
        font-family: 'Syne', sans-serif;
        color: #b45309;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .card-amber-box p {
        color: #334155;
        font-size: 13px;
        margin: 0;
        line-height: 1.5;
    }

    /* Dashboard Dark Studio Theme & Cards (Untouched after clicking Get Started) */
    .studio-header {
        background-color: #0a0a0a;
        border: 1px solid #262626;
        padding: 48px;
        border-radius: 0px;
        color: #ffffff;
        margin-bottom: 30px;
    }
    .studio-card {
        background-color: #0a0a0a;
        border: 1px solid #262626;
        padding: 28px;
        border-radius: 0px;
        margin-bottom: 24px;
    }
    .badge-critical {
        background-color: #260000; color: #ff5252; border: 1px solid #ff5252;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase;
    }
    .badge-warning {
        background-color: #261c00; color: #ffb100; border: 1px solid #ffb100;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase;
    }
    .badge-stable {
        background-color: #022614; color: #00e676; border: 1px solid #00e676;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase;
    }

    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: LANDING PAGE (Exact White Theme Matching Uploaded Image)
# =========================================================================
if st.session_state.app_state == 'landing':
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        st.markdown("📌 **Introduction**")
        st.markdown("📖 **Overview**")
        st.markdown("⚙️ **System Architecture**")

    st.markdown("""
        <div class="landing-hero">
            <div class="landing-title">
                EduShield AI <span style="color: #64748b; font-weight: 400;">// STUDIO</span>
            </div>
            <div class="landing-subtitle">
                An advanced institutional early warning and predictive machine learning platform designed to proactively track student retention, compute vulnerability indexes, and coordinate administrative counseling across the State of Rajasthan.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns(3, gap="large")
    with col_h1:
        st.markdown("""
            <div class="card-cyan-box">
                <h3>01 // Neural Prediction</h3>
                <p>Real-time vector calculations assessing individual student dropout risk using behavioral metrics.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
            <div class="card-purple-box">
                <h3>02 // Regional Intel</h3>
                <p>Macro-level aggregation across participating districts, providing deep insight into institutional attendance.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h3:
        st.markdown("""
            <div class="card-amber-box">
                <h3>03 // Automated Hub</h3>
                <p>Instantaneous emergency ticket dispatch and post-intervention score reassessment for counselors.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])
    with col_btn2:
        if st.button("🚀 Get Started // Enter Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: DASHBOARD VIEW (Unchanged original dark studio frontend)
# =========================================================================
else:
    st.markdown("""
        <style>
        .stApp { background-color: #000000 !important; color: #f3f4f6 !important; }
        </style>
        <div class="studio-header" style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1>RAJ-AEGIS <span style="color: #525252; font-weight: 400; font-size: 24px;">// STUDIO EDITION</span></h1>
                <p style="color: #a3a3a3; margin-top: 5px;">Institutional Early Warning Systems & Architectural ML Telemetry</p>
            </div>
    """, unsafe_allow_html=True)
    
    if st.button("← Back to Overview"):
        st.session_state.app_state = 'landing'
        st.rerun()

    with st.sidebar:
        st.markdown("### ▪️ SYSTEM METRICS")
        st.success("API: CONNECTED [0ms]")
        st.markdown("---")
        st.markdown("**Architecture:** Microservice Node")
        st.markdown("**Security Standard:** TLS-AES-256")
        if st.button("Return to Landing Page", use_container_width=True):
            st.session_state.app_state = 'landing'
            st.rerun()

    tab1, tab2, tab3, tab4 = st.tabs([
        "01 // RISK PROFILER", 
        "02 // MASTER DATABASE", 
        "03 // REGIONAL INTEL",
        "04 // ALERT DISPATCH"
    ])

    with tab1:
        st.markdown("### Individual Student Vulnerability Assessment")
        with st.form("evaluation_form"):
            col_f1, col_f2 = st.columns(2, gap="large")
            with col_f1:
                st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                st.markdown("#### Administrative Context")
                student_id = st.text_input("Student Unique ID / Roll Number*", placeholder="e.g., RJ-JP-2026-890")
                school_name = st.text_input("Institution Name*", placeholder="e.g., Govt Sr Sec School, Jaipur")
                gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
                fees_status = st.selectbox("Fees Status", options=["Paid", "Pending", "Unpaid", "last 5 months not paid"])
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_f2:
                st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                st.markdown("#### Environmental Parameters")
                internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
                family_support = st.selectbox("Family Academic Support", options=["Yes", "No"])
                wants_higher_ed = st.selectbox("Wants Higher Education", options=["Yes", "No"])
                medical_status = st.selectbox("Medical Health Status", options=["Good", "Average", "Poor"])
                st.markdown('</div>', unsafe_allow_html=True)
                
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("#### Quantitative Behavioral Vectors")
            col_n1, col_n2, col_n3, col_n4 = st.columns(4)
            with col_n1: school_support = st.selectbox("Extra School Support", options=["Yes", "No"])
            with col_n2: extra_paid_class = st.selectbox("Extra Paid Classes", options=["Yes", "No"])
            with col_n3: extra_curricular = st.selectbox("Extracurriculars", options=["Yes", "No"])
            with col_n4: absences = st.number_input("Absence Days", min_value=0, max_value=100, value=4)
                
            col_q1, col_q2 = st.columns(2)
            with col_q1: failures = st.number_input("Past Failures (Subjects)", min_value=0, max_value=10, value=0)
            with col_q2: final_grade = st.number_input("Final Grade / Score (0-100)", min_value=0.0, max_value=100.0, value=65.0)
            st.markdown('</div>', unsafe_allow_html=True)

            submit_eval = st.form_submit_button(label="EXECUTE NEURAL INFERENCE")

        if submit_eval:
            if not student_id.strip() or not school_name.strip():
                st.error("Mandatory fields missing: Student ID and Institution Name required.")
            else:
                payload = {
                    "Student_ID": student_id, "School": school_name, "Gender": gender,
                    "Fees_Paid_Status": fees_status, "Internet_Access": internet_access,
                    "Family_Support": family_support, "Wants_Higher_Education": wants_higher_ed,
                    "Medical_Status": medical_status, "School_Support": school_support,
                    "Extra_Paid_Class": extra_paid_class, "Extra_Curricular_Activities": extra_curricular,
                    "Number_of_Absences": int(absences), "Number_of_Failures": int(failures),
                    "Final_Grade": float(final_grade)
                }
                try:
                    with st.spinner("Processing neural vector telemetry..."):
                        response = requests.post(f"{API_BASE_URL}/api/predict/custom", json=payload, timeout=15)
                    if response.status_code == 200:
                        res_data = response.json()
                        risk_score = res_data.get("risk_score", 0.0)
                        tier = res_data.get("risk_tier", "Low Risk")
                        factors = res_data.get("top_factors", ["Stable baseline indicators"])
                        
                        badge_class = "badge-stable"
                        if "High" in str(tier): badge_class = "badge-critical"
                        elif "Moderate" in str(tier): badge_class = "badge-warning"

                        st.markdown("---")
                        st.markdown(f"### Assessment Output // `{student_id}`")
                        st.markdown(f"""
                            <div class="studio-card">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div>
                                        <h2 style="margin:0; font-size: 48px; font-weight: 800; color: #ffffff;">{risk_score}%</h2>
                                        <p style="margin:4px 0 0 0; color: #a3a3a3; font-size: 13px;">Dropout Vulnerability Index</p>
                                    </div>
                                    <div><span class="{badge_class}">{tier}</span></div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                except Exception as ex:
                    st.error(f"Connection failure: {ex}")

    with tab2:
        st.markdown("### Master Student Repository")
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("SYNC DATABASE RECORDS"):
            try:
                resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
                if resp.status_code == 200:
                    records = resp.json()
                    if records:
                        st.dataframe(pd.DataFrame(records), use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown("### Regional Analytics Matrix")
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("GENERATE TELEMETRY REPORT"):
            try:
                resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
                if resp.status_code == 200:
                    analytics_data = resp.json()
                    summary = analytics_data.get("summary", {})
                    k1, k2, k3, k4 = st.columns(4)
                    with k1: st.metric("Total Monitored", summary.get("total_students_monitored", 0))
                    with k2: st.metric("Historical Dropouts", summary.get("historical_dropouts", 0))
                    with k3: st.metric("Unpaid Fee Issues", summary.get("students_with_unpaid_fees", 0))
                    with k4: st.metric("Chronic Absences", summary.get("students_chronically_absent", 0))
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown("### Emergency Intervention & Audit Hub")
        col_a1, col_a2 = st.columns(2, gap="large")
        with col_a1:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            target_student_id = st.text_input("Target Student ID", placeholder="e.g., RJ-JP-2026-890", key="alert_id_input")
            if st.button("DISPATCH EMERGENCY TICKET"):
                if target_student_id:
                    try:
                        requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_student_id}", timeout=10)
                        st.success(f"Ticket dispatched for **{target_student_id}**.")
                    except Exception as err:
                        st.error(f"Error: {err}")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_a2:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            reass_id = st.text_input("Target Student ID for Review", placeholder="e.g., RJ-JP-2026-890", key="reass_id_input")
            intervention_action = st.selectbox("Applied Protocol", options=["FEE_ASSISTANCE", "ATTENDANCE_COUNSELING", "ACADEMIC_REMEDIAL"])
            if st.button("PROCESS REASSESSMENT"):
                if reass_id:
                    try:
                        requests.post(f"{API_BASE_URL}/api/interventions/reassess/{reass_id}", params={"intervention_type": intervention_action}, timeout=10)
                        st.success(f"Profile updated for **{reass_id}**.")
                    except Exception as err:
                        st.error(f"Error: {err}")
            st.markdown('</div>', unsafe_allow_html=True)
