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

# Initialize Session State for Page Navigation
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'landing'  # 'landing' or 'dashboard'

# 2. Clean White Theme & Professional Studio CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .main {
        background-color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        color: #0f172a;
    }
    
    /* Left Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #21262d;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Studio Header */
    .studio-header {
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0;
        padding: 24px 32px;
        margin: -6rem -6rem 2rem -6rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .studio-header h1 {
        font-weight: 800;
        font-size: 28px;
        letter-spacing: -0.5px;
        margin: 0;
        color: #0f172a;
    }
    .studio-header p {
        color: #64748b;
        font-size: 13px;
        margin-top: 4px;
    }

    /* Hero Landing Styling */
    .hero-container {
        padding: 40px 20px;
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #0f172a;
        margin-bottom: 15px;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-size: 16px;
        color: #475569;
        margin-bottom: 30px;
        line-height: 1.6;
    }

    /* Colorful Feature Cards */
    .card-cyan {
        background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
        border: 1px solid #06b6d4;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .card-cyan * { color: #0e7490 !important; }

    .card-purple {
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
        border: 1px solid #8b5cf6;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .card-purple * { color: #6d28d9 !important; }

    .card-amber {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border: 1px solid #f59e0b;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .card-amber * { color: #b45309 !important; }

    /* Standard Dashboard Cards */
    .studio-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    /* Badges */
    .badge-critical {
        background-color: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fecaca;
        padding: 4px 12px;
        font-weight: 700;
        font-size: 11px;
        text-transform: uppercase;
        border-radius: 20px;
    }
    .badge-warning {
        background-color: #fef3c7;
        color: #b45309;
        border: 1px solid #fde68a;
        padding: 4px 12px;
        font-weight: 700;
        font-size: 11px;
        text-transform: uppercase;
        border-radius: 20px;
    }
    .badge-stable {
        background-color: #d1fae5;
        color: #047857;
        border: 1px solid #a7f3d0;
        padding: 4px 12px;
        font-weight: 700;
        font-size: 11px;
        text-transform: uppercase;
        border-radius: 20px;
    }

    /* Primary Action Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.4rem;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: LANDING PAGE (ABOUT & INTRO)
# =========================================================================
if st.session_state.app_state == 'landing':
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        st.markdown("📌 **Introduction**")
        st.markdown("📖 **Overview**")
        st.markdown("⚙️ **System Architecture**")

    st.markdown("""
        <div class="hero-container">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #4f46e5; text-transform: uppercase; margin-bottom: 10px;">
                Government of Rajasthan | Smart India Hackathon Initiative // SIH25102
            </div>
            <div class="hero-title">
                EduShield AI <span style="color: #64748b;">// STUDIO</span>
            </div>
            <div class="hero-subtitle">
                An advanced institutional early warning and predictive machine learning platform designed to proactively track student retention, compute vulnerability indexes, and coordinate administrative counseling across the State of Rajasthan.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns(3, gap="large")
    with col_h1:
        st.markdown("""
            <div class="card-cyan">
                <h3 style="margin-top:0; font-size: 18px;">01 // Neural Prediction</h3>
                <p style="font-size: 13px; margin:0;">Real-time vector calculations assessing individual student dropout risk using behavioral metrics.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
            <div class="card-purple">
                <h3 style="margin-top:0; font-size: 18px;">02 // Regional Intel</h3>
                <p style="font-size: 13px; margin:0;">Macro-level aggregation across participating districts, providing deep insight into institutional attendance.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h3:
        st.markdown("""
            <div class="card-amber">
                <h3 style="margin-top:0; font-size: 18px;">03 // Automated Hub</h3>
                <p style="font-size: 13px; margin:0;">Instantaneous emergency ticket dispatch and post-intervention score reassessment for counselors.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])
    with col_btn2:
        if st.button("🚀 Get Started // Enter Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: ACTUAL DASHBOARD FRONTEND
# =========================================================================
else:
    # Top Header Component
    st.markdown("""
        <div class="studio-header">
            <div>
                <h1>EduShield AI <span style="color: #64748b; font-weight: 400; font-size: 18px;">// STUDIO EDITION</span></h1>
                <p>Institutional Early Warning Systems & Architectural ML Telemetry</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Command Grid
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        if st.button("← Back to Overview", use_container_width=True):
            st.session_state.app_state = 'landing'
            st.rerun()
        st.markdown("---")
        st.markdown("**Architecture:** Microservice Node")
        st.markdown("**Security Standard:** TLS-AES-256")

    # Studio Navigation Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "01 // RISK PROFILER", 
        "02 // MASTER DATABASE", 
        "03 // REGIONAL INTEL",
        "04 // ALERT DISPATCH"
    ])

    # =========================================================================
    # TAB 1: AI RISK PROFILER
    # =========================================================================
    with tab1:
        st.markdown("<h3>Individual Student Vulnerability Assessment</h3>", unsafe_allow_html=True)
        
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
            with col_n1:
                school_support = st.selectbox("Extra School Support", options=["Yes", "No"])
            with col_n2:
                extra_paid_class = st.selectbox("Extra Paid Classes", options=["Yes", "No"])
            with col_n3:
                extra_curricular = st.selectbox("Extracurriculars", options=["Yes", "No"])
            with col_n4:
                absences = st.number_input("Absence Days", min_value=0, max_value=100, value=4)
                
            col_q1, col_q2 = st.columns(2)
            with col_q1:
                failures = st.number_input("Past Failures (Subjects)", min_value=0, max_value=10, value=0)
            with col_q2:
                final_grade = st.number_input("Final Grade / Score (0-100)", min_value=0.0, max_value=100.0, value=65.0)
            st.markdown('</div>', unsafe_allow_html=True)

            submit_eval = st.form_submit_button(label="EXECUTE NEURAL INFERENCE")

        if submit_eval:
            if not student_id.strip() or not school_name.strip():
                st.error("Mandatory fields missing: Student ID and Institution Name required.")
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
                    "School_Support": school_support,
                    "Extra_Paid_Class": extra_paid_class,
                    "Extra_Curricular_Activities": extra_curricular,
                    "Number_of_Absences": int(absences),
                    "Number_of_Failures": int(failures),
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
                        if "High" in str(tier):
                            badge_class = "badge-critical"
                        elif "Moderate" in str(tier):
                            badge_class = "badge-warning"

                        st.markdown("---")
                        st.markdown(f"### Assessment Output // `{student_id}`")
                        
                        st.markdown(f"""
                            <div class="studio-card">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div>
                                        <h2 style="margin:0; font-size: 38px; font-weight: 800; color: #0f172a;">{risk_score}%</h2>
                                        <p style="margin:4px 0 0 0; color: #64748b; font-size: 13px;">Dropout Vulnerability Index</p>
                                    </div>
                                    <div>
                                        <span class="{badge_class}">{tier}</span>
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

                        col_res1, col_res2 = st.columns(2, gap="large")
                        with col_res1:
                            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                            st.markdown("#### Primary Risk Vectors")
                            for factor in factors:
                                st.markdown(f"- {factor}")
                            st.markdown('</div>', unsafe_allow_html=True)
                        with col_res2:
                            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                            st.markdown("#### Prescribed Protocol")
                            if "High" in str(tier):
                                st.error("High Risk Protocol: Immediate counselor assignment required.")
                            elif "Moderate" in str(tier):
                                st.warning("Watchlist Protocol: Weekly attendance monitoring active.")
                            else:
                                st.success("Standard Status: Parameters within nominal limits.")
                            st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Backend processing error: Status {response.status_code}")
                except Exception as ex:
                    st.error(f"Connection failure: {ex}")

    # =========================================================================
    # TAB 2: MASTER STUDENT DATABASE
    # =========================================================================
    with tab2:
        st.markdown("<h3>Master Student Repository</h3>", unsafe_allow_html=True)
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("SYNC DATABASE RECORDS"):
            try:
                with st.spinner("Querying repository..."):
                    resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
                if resp.status_code == 200:
                    records = resp.json()
                    if records:
                        df_students = pd.DataFrame(records)
                        st.success(f"Loaded {len(df_students)} records.")
                        st.dataframe(df_students, use_container_width=True)
                    else:
                        st.info("Repository empty.")
                else:
                    st.error("Query failed.")
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================================
    # TAB 3: REGIONAL INTELLIGENCE
    # =========================================================================
    with tab3:
        st.markdown("<h3>Regional Analytics Matrix</h3>", unsafe_allow_html=True)
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("GENERATE TELEMETRY REPORT"):
            try:
                with st.spinner("Aggregating metrics..."):
                    resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
                if resp.status_code == 200:
                    analytics_data = resp.json()
                    summary = analytics_data.get("summary", {})
                    schools = analytics_data.get("school_metrics", [])
                    
                    k1, k2, k3, k4 = st.columns(4)
                    with k1:
                        st.metric("Total Monitored", summary.get("total_students_monitored", 0))
                    with k2:
                        st.metric("Historical Dropouts", summary.get("historical_dropouts", 0))
                    with k3:
                        st.metric("Unpaid Fee Issues", summary.get("students_with_unpaid_fees", 0))
                    with k4:
                        st.metric("Chronic Absences", summary.get("students_chronically_absent", 0))
                    
                    if schools:
                        df_schools = pd.DataFrame(schools)
                        st.dataframe(df_schools, use_container_width=True)
                else:
                    st.error("Failed to load metrics.")
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================================
    # TAB 4: INTERVENTION & ALERT HUB
    # =========================================================================
    with tab4:
        st.markdown("<h3>Emergency Intervention & Audit Hub</h3>", unsafe_allow_html=True)
        col_a1, col_a2 = st.columns(2, gap="large")
        
        with col_a1:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("#### Automated SMS & Ticket Dispatch")
            target_student_id = st.text_input("Target Student ID", placeholder="e.g., RJ-JP-2026-890", key="alert_id_input")
            if st.button("DISPATCH EMERGENCY TICKET"):
                if target_student_id:
                    try:
                        resp = requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_student_id}", timeout=10)
                        if resp.status_code == 200:
                            res_json = resp.json()
                            st.success(f"Ticket dispatched for **{target_student_id}**.")
                            st.markdown(f"- **Reference:** `{res_json.get('ticket_id', 'TICKET')}`")
                        else:
                            st.error("Dispatch failed.")
                    except Exception as err:
                        st.error(f"Error: {err}")
            st.markdown('</div>', unsafe_allow_html=True)
                    
        with col_a2:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("#### Post-Intervention Reassessment")
            reass_id = st.text_input("Target Student ID for Review", placeholder="e.g., RJ-JP-2026-890", key="reass_id_input")
            intervention_action = st.selectbox("Applied Protocol", options=["FEE_ASSISTANCE", "ATTENDANCE_COUNSELING", "ACADEMIC_REMEDIAL"])
            if st.button("PROCESS REASSESSMENT"):
                if reass_id:
                    try:
                        resp = requests.post(
                            f"{API_BASE_URL}/api/interventions/reassess/{reass_id}", 
                            params={"intervention_type": intervention_action}, 
                            timeout=10
                        )
                        if resp.status_code == 200:
                            res_json = resp.json()
                            st.success(f"Profile updated for **{reass_id}**.")
                            st.markdown(f"- **Revised Score:** `{res_json.get('risk_score', 'N/A')}%`")
                        else:
                            st.error("Reassessment failed.")
                    except Exception as err:
                        st.error(f"Error: {err}")
            st.markdown('</div>', unsafe_allow_html=True)
