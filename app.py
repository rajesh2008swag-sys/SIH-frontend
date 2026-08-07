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

# 2. Clean White Studio Minimalist Aesthetic CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Syne:wght@600;700;800&display=swap');

    .main {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
        color: #0f172a;
    }
    
    /* Top Header */
    .studio-header {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 36px 40px;
        border-radius: 0px;
        color: #0f172a;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
    }
    .studio-header h1 {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 32px;
        letter-spacing: -1px;
        margin: 0;
        color: #0f172a;
    }
    .studio-header p {
        font-family: 'Inter', sans-serif;
        color: #64748b;
        font-size: 14px;
        margin-top: 8px;
    }

    /* Landing / Overview Hero Styling */
    .hero-container {
        padding: 20px 0px;
        max-width: 900px;
    }
    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: 44px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #0f172a;
        margin-bottom: 16px;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        color: #475569;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    .feature-box {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        text-align: left;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .feature-box h3 {
        font-family: 'Syne', sans-serif;
        color: #0f172a;
        font-size: 18px;
        margin-bottom: 8px;
    }
    .feature-box p {
        color: #64748b;
        font-size: 13px;
        margin: 0;
    }

    /* Cards */
    .studio-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 0px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* Badges */
    .badge-critical {
        background-color: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fecaca;
        padding: 6px 14px;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .badge-warning {
        background-color: #fef3c7;
        color: #b45309;
        border: 1px solid #fde68a;
        padding: 6px 14px;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .badge-stable {
        background-color: #d1fae5;
        color: #047857;
        border: 1px solid #a7f3d0;
        padding: 6px 14px;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 11px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Buttons */
    .stButton>button {
        background-color: #0f172a;
        color: #ffffff;
        border-radius: 0px;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
        padding: 0.7rem 1.5rem;
        border: 1px solid #0f172a;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        color: #0f172a;
        border: 1px solid #0f172a;
    }

    /* Input Fields Override */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 0px !important;
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation Menu (Introduction is placed as the first option)
with st.sidebar:
    st.markdown("### 🏛️ RAJ-AEGIS NAVIGATION")
    st.markdown("Select a module below:")
    
    selected_option = st.radio(
        "Modules",
        [
            "ℹ️ Introduction & Overview",
            "📝 AI Risk Profiler", 
            "👥 Master Student Database", 
            "📊 Regional Intelligence", 
            "🚨 Alert & Intervention Hub"
        ],
        label_visibility="collapsed"
    )

# 4. Dynamic Top Header based on selection
if selected_option == "ℹ️ Introduction & Overview":
    header_title = "RAJ-AEGIS <span style='color: #64748b; font-weight: 400; font-size: 20px;'>// SYSTEM OVERVIEW</span>"
    header_desc = "Smart India Hackathon Initiative (SIH25102) — Proactive Student Retention & Early Warning Platform"
else:
    header_title = "RAJ-AEGIS <span style='color: #64748b; font-weight: 400; font-size: 20px;'>// WHITE STUDIO EDITION</span>"
    header_desc = "Institutional Early Warning Systems & Architectural ML Telemetry"

st.markdown(f"""
    <div class="studio-header">
        <h1>{header_title}</h1>
        <p>{header_desc}</p>
    </div>
""", unsafe_allow_html=True)

# =========================================================================
# MODULE 0: INTRODUCTION & OVERVIEW (DEFAULT LANDING)
# =========================================================================
if selected_option == "ℹ️ Introduction & Overview":
    st.markdown("""
        <div class="hero-container">
            <div style="font-family: 'Syne', sans-serif; font-size: 11px; letter-spacing: 2px; color: #64748b; margin-bottom: 12px; text-transform: uppercase;">
                Government of Rajasthan // SIH25102
            </div>
            <div class="hero-title">
                Institutional Early Warning & Intervention Portal
            </div>
            <div class="hero-subtitle">
                An advanced predictive machine learning platform designed to proactively track student retention, compute vulnerability indexes, and coordinate administrative counseling across educational institutions in Rajasthan.
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_h1, col_h2, col_h3 = st.columns(3, gap="large")
    with col_h1:
        st.markdown("""
            <div class="feature-box">
                <h3>01 // Neural Prediction</h3>
                <p>Real-time vector calculations assessing individual student dropout risk using behavioral and academic metrics.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
            <div class="feature-box">
                <h3>02 // Regional Intel</h3>
                <p>Macro-level aggregation across participating districts, providing deep insight into institutional attendance and fee statuses.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_h3:
        st.markdown("""
            <div class="feature-box">
                <h3>03 // Automated Hub</h3>
                <p>Instantaneous emergency ticket dispatch and post-intervention score reassessment for school counselors.</p>
            </div>
        """, unsafe_allow_html=True)

# =========================================================================
# MODULE 1: AI RISK PROFILER
# =========================================================================
elif selected_option == "📝 AI Risk Profiler":
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
                                    <h2 style="margin:0; font-family: 'Syne', sans-serif; font-size: 44px; font-weight: 800; color: #0f172a;">{risk_score}%</h2>
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
# MODULE 2: MASTER STUDENT DATABASE
# =========================================================================
elif selected_option == "👥 Master Student Database":
    st.markdown("### Master Student Repository")
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
# MODULE 3: REGIONAL INTELLIGENCE
# =========================================================================
elif selected_option == "📊 Regional Intelligence":
    st.markdown("### Regional Analytics Matrix")
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
# MODULE 4: ALERT & INTERVENTION HUB
# =========================================================================
elif selected_option == "🚨 Alert & Intervention Hub":
    st.markdown("### Emergency Intervention & Audit Hub")
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
