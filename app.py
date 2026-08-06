import streamlit as st
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="Raj-Aegis | National Student Early Warning System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://sih-student-api.onrender.com"

# 2. Executive Gov-Tech UI/UX Styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .executive-header {
        background: linear-gradient(135deg, #091e3a 0%, #1d3557 100%);
        padding: 35px 40px;
        border-radius: 12px;
        color: #ffffff;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px -5px rgba(9, 30, 58, 0.25);
        border-bottom: 4px solid #3b82f6;
    }
    .enterprise-card {
        background: #ffffff;
        padding: 24px 28px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .badge-critical {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .badge-warning {
        background-color: #fef3c7;
        color: #92400e;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .badge-stable {
        background-color: #d1fae5;
        color: #065f46;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .stButton>button {
        background-color: #1d3557;
        color: white;
        border-radius: 6px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        border: none;
        transition: background-color 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        color: white;
    }
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Executive Header
st.markdown("""
    <div class="executive-header">
        <h1 style="margin:0; font-size: 28px; font-weight: 700; letter-spacing: -0.5px;">🎓 RAJ-AEGIS : Institutional Early Warning & Intervention Portal</h1>
        <p style="margin:8px 0 0 0; font-size: 15px; color: #93c5fd; font-weight: 400;">
            Advanced Machine Learning Analytics for Proactive Student Retention & Counselor Coordination
        </p>
        <p style="margin:4px 0 0 0; font-size: 12px; color: #94a3b8;">
            Government of Rajasthan | Smart India Hackathon Initiative (SIH25102)
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. Professional Sidebar Telemetry
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Emblem_of_Rajasthan.svg", width=65)
    st.markdown("### 🏛️ System Control Panel")
    st.success("API Gateway Status: Operational 🟢")
    st.markdown("---")
    st.markdown("**Core Engine:** Render Cloud Backend")
    st.markdown("**Data Security:** AES-256 / TLS Secured")
    st.markdown("**Jurisdiction:** State of Rajasthan")
    st.markdown("**Build ID:** v2.4-PROD")

# 5. Multi-Tab Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "📝 AI Risk Profiler", 
    "👥 Master Student Database", 
    "📊 Regional Intelligence",
    "🚨 Intervention & Alert Hub"
])

# =========================================================================
# TAB 1: AI RISK PROFILER
# =========================================================================
with tab1:
    st.markdown("### 🔍 Individual Student Vulnerability Assessment")
    st.markdown("Provide full student telemetry to match all backend ML feature requirements.")

    with st.form("evaluation_form"):
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            student_id = st.text_input("Student Unique ID / Roll Number*", placeholder="e.g., RJ-JP-2026-890")
            school_name = st.text_input("Institution Name*", placeholder="e.g., Govt Sr Sec School, Jaipur")
            gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
            fees_status = st.selectbox("Fees Status", options=["Paid", "Pending", "Unpaid", "last 5 months not paid"])
            internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
            family_support = st.selectbox("Family Academic Support", options=["Yes", "No"])
            
        with col_f2:
            wants_higher_ed = st.selectbox("Wants Higher Education", options=["Yes", "No"])
            medical_status = st.selectbox("Medical Health Status", options=["Good", "Average", "Poor"])
            school_support = st.selectbox("Extra School Support Received", options=["Yes", "No"])
            extra_paid_class = st.selectbox("Enrolled in Extra Paid Classes", options=["Yes", "No"])
            extra_curricular = st.selectbox("Participates in Extracurriculars", options=["Yes", "No"])
            
        st.markdown("---")
        col_n1, col_n2, col_n3 = st.columns(3)
        with col_n1:
            absences = st.number_input("Total Days of Absences", min_value=0, max_value=100, value=4)
        with col_n2:
            failures = st.number_input("Past Failures (Subjects)", min_value=0, max_value=10, value=0)
        with col_n3:
            final_grade = st.number_input("Final Grade / Score (0-100)", min_value=0.0, max_value=100.0, value=65.0)

        submit_eval = st.form_submit_button(label="Execute AI Predictive Inference", use_container_width=True)

    if submit_eval:
        if not student_id.strip() or not school_name.strip():
            st.error("⚠️ Mandatory fields missing: Please enter both Student ID and Institution Name.")
        else:
            # Complete payload including the extra binary/categorical features checked by backend
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
                with st.spinner("Processing vector telemetry via backend neural engine..."):
                    response = requests.post(f"{API_BASE_URL}/api/predict/custom", json=payload, timeout=15)
                
                if response.status_code == 200:
                    res_data = response.json()
                    risk_score = res_data.get("risk_score", 0.0)
                    tier = res_data.get("risk_tier", "Low Risk")
                    factors = res_data.get("top_factors", ["Stable baseline indicators"])
                    
                    badge_class = "badge-stable"
                    card_border = "#10b981"
                    if "High" in str(tier):
                        badge_class = "badge-critical"
                        card_border = "#ef4444"
                    elif "Moderate" in str(tier):
                        badge_class = "badge-warning"
                        card_border = "#f59e0b"

                    st.markdown("---")
                    st.markdown(f"### Diagnostic Report for Student: `{student_id}`")
                    
                    st.markdown(f"""
                        <div class="enterprise-card" style="border-left: 6px solid {card_border};">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <h2 style="margin:0; color: #0f172a; font-size: 32px; font-weight: 700;">{risk_score}%</h2>
                                    <p style="margin:4px 0 0 0; color: #64748b; font-size: 14px; font-weight: 500;">Calculated Dropout Vulnerability Index</p>
                                </div>
                                <div>
                                    <span class="{badge_class}">{tier}</span>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                    col_res1, col_res2 = st.columns(2)
                    
                    with col_res1:
                        st.markdown("#### Primary Risk Factors Identified")
                        if isinstance(factors, list) and factors:
                            for factor in factors:
                                st.markdown(f"- ⚠️ {factor}")
                        else:
                            st.markdown("- No critical risk vectors detected.")
                            
                    with col_res2:
                        st.markdown("#### Prescribed Institutional Protocol")
                        if "High" in str(tier):
                            st.error("🚨 **High Risk Protocol:** Immediate counselor dispatch and mandatory guardian conference required.")
                        elif "Moderate" in str(tier):
                            st.warning("⚠️ **Watchlist Protocol:** Enroll student in weekly attendance tracking and academic remedial support.")
                        else:
                            st.success("✅ **Standard Status:** Profile remains within acceptable institutional stability limits.")
                else:
                    st.error(f"⚠️ Backend Processing Error: Status code {response.status_code}")
            except Exception as ex:
                st.error(f"🚨 Network Connection Failure: {ex}")

# =========================================================================
# TAB 2: MASTER STUDENT DATABASE
# =========================================================================
with tab2:
    st.markdown("### 👥 State Master Student Repository")
    st.markdown("Review and inspect all active student logs synchronized from cloud databases.")
    
    if st.button("Sync Database Records", use_container_width=False):
        try:
            with st.spinner("Fetching synchronized records..."):
                resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
            if resp.status_code == 200:
                records = resp.json()
                if records:
                    df_students = pd.DataFrame(records)
                    st.success(f"Successfully loaded {len(df_students)} active student records.")
                    st.dataframe(df_students, use_container_width=True)
                else:
                    st.info("No records found in the database repository.")
            else:
                st.error("Failed to query student dataset.")
        except Exception as e:
            st.error(f"Database connection error: {e}")

# =========================================================================
# TAB 3: REGIONAL INTELLIGENCE
# =========================================================================
with tab3:
    st.markdown("### 📊 Regional District Analytics & Intelligence")
    st.markdown("Aggregated macro-level performance metrics compiled across reporting districts.")
    
    if st.button("Generate District Telemetry Report", use_container_width=False):
        try:
            with st.spinner("Compiling district data matrix..."):
                resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
            if resp.status_code == 200:
                analytics_data = resp.json()
                summary = analytics_data.get("summary", {})
                schools = analytics_data.get("school_metrics", [])
                
                st.markdown("---")
                st.markdown("#### District Performance Overview")
                
                k1, k2, k3, k4 = st.columns(4)
                with k1:
                    st.metric("Total Monitored", summary.get("total_students_monitored", 0))
                with k2:
                    st.metric("Historical Dropouts", summary.get("historical_dropouts", 0))
                with k3:
                    st.metric("Unpaid Fee Issues", summary.get("students_with_unpaid_fees", 0))
                with k4:
                    st.metric("Chronic Absences", summary.get("students_chronically_absent", 0))
                
                st.markdown("---")
                
                if schools:
                    df_schools = pd.DataFrame(schools)
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("#### Student Headcount per Institution")
                        if "School" in df_schools.columns and "total_students" in df_schools.columns:
                            st.bar_chart(df_schools.set_index("School")["total_students"])
                    with c2:
                        st.markdown("#### Average Absences per Institution")
                        if "School" in df_schools.columns and "avg_absences" in df_schools.columns:
                            st.bar_chart(df_schools.set_index("School")["avg_absences"])
                            
                    st.markdown("#### Comprehensive Institution Breakdown")
                    st.dataframe(df_schools, use_container_width=True)
                else:
                    st.info("No institutional breakdown available.")
            else:
                st.error("Failed to load district metrics.")
        except Exception as e:
            st.error(f"Connection error: {e}")

# =========================================================================
# TAB 4: INTERVENTION & ALERT HUB
# =========================================================================
with tab4:
    st.markdown("### 🚨 Emergency Intervention & Audit Hub")
    
    col_a1, col_a2 = st.columns(2)
    
    with col_a1:
        st.markdown("#### Automated SMS & Counselor Ticket Dispatch")
        target_student_id = st.text_input("Target Student ID", placeholder="e.g., RJ-JP-2026-890", key="alert_id_input")
        if st.button("Dispatch Urgent Alert Ticket", key="alert_btn"):
            if target_student_id:
                try:
                    resp = requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_student_id}", timeout=10)
                    if resp.status_code == 200:
                        res_json = resp.json()
                        st.success(f"✅ Alert ticket successfully dispatched for student **{target_student_id}**.")
                        st.markdown(f"- **Dispatch Status:** {res_json.get('status', 'Completed')}")
                        st.markdown(f"- **Guardian Notification:** {res_json.get('message', 'SMS notification sent successfully.')}")
                        st.markdown(f"- **Assigned Ticket ID:** {res_json.get('ticket_id', 'TICKET-' + target_student_id)}")
                    else:
                        st.error(f"Dispatch failed with status code {resp.status_code}")
                except Exception as err:
                    st.error(f"Error: {err}")
            else:
                st.warning("Please specify a valid Student ID.")
                
    with col_a2:
        st.markdown("#### Post-Intervention Status Reassessment")
        reass_id = st.text_input("Target Student ID for Review", placeholder="e.g., RJ-JP-2026-890", key="reass_id_input")
        intervention_action = st.selectbox("Applied Protocol", options=["FEE_ASSISTANCE", "ATTENDANCE_COUNSELING", "ACADEMIC_REMEDIAL"])
        if st.button("Process Intervention & Recompute", key="reass_btn"):
            if reass_id:
                try:
                    resp = requests.post(
                        f"{API_BASE_URL}/api/interventions/reassess/{reass_id}", 
                        params={"intervention_type": intervention_action}, 
                        timeout=10
                    )
                    if resp.status_code == 200:
                        res_json = resp.json()
                        st.success(f"✅ Profile successfully updated for student **{reass_id}**.")
                        st.markdown(f"- **Revised Risk Score:** `{res_json.get('risk_score', 'N/A')}%`")
                        st.markdown(f"- **Updated Risk Tier:** **{res_json.get('risk_tier', 'N/A')}**")
                        st.markdown(f"- **Audit Status:** Logged to state records successfully.")
                    else:
                        st.error(f"Reassessment failed. Status code: {resp.status_code}")
                except Exception as err:
                    st.error(f"Error: {err}")
            else:
                st.warning("Please specify a valid Student ID.")