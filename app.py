import streamlit as st
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="RAJ-AEGIS | National AI Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://sih-student-api.onrender.com"

# 2. Innovative Multi-Color Vibrant UI/UX Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap');
    
    .main {
        background-color: #0b0f19;
        font-family: 'Outfit', sans-serif;
        color: #f8fafc;
    }
    
    /* Executive Header with Neon Glow */
    .executive-header {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
        padding: 36px 40px;
        border-radius: 20px;
        color: #ffffff;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px -5px rgba(67, 56, 202, 0.4);
        border: 1px solid rgba(129, 140, 248, 0.3);
    }
    
    /* Unique Colorful Cards */
    .card-cyan {
        background: linear-gradient(135deg, rgba(14, 116, 144, 0.15) 0%, rgba(8, 51, 68, 0.4) 100%);
        border: 1px solid rgba(6, 182, 212, 0.4);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(6, 182, 212, 0.1);
    }
    .card-purple {
        background: linear-gradient(135deg, rgba(107, 33, 168, 0.15) 0%, rgba(59, 7, 100, 0.4) 100%);
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(168, 85, 247, 0.1);
    }
    .card-emerald {
        background: linear-gradient(135deg, rgba(6, 95, 70, 0.15) 0%, rgba(2, 44, 34, 0.4) 100%);
        border: 1px solid rgba(16, 185, 129, 0.4);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.1);
    }
    .card-amber {
        background: linear-gradient(135deg, rgba(146, 64, 14, 0.15) 0%, rgba(67, 20, 7, 0.4) 100%);
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(245, 158, 11, 0.1);
    }
    .card-rose {
        background: linear-gradient(135deg, rgba(159, 18, 57, 0.15) 0%, rgba(76, 5, 25, 0.4) 100%);
        border: 1px solid rgba(244, 63, 94, 0.4);
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(244, 63, 94, 0.1);
    }

    /* Vibrant Badges */
    .badge-critical {
        background: linear-gradient(135deg, #ef4444, #991b1b);
        color: white;
        padding: 6px 16px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
    }
    .badge-warning {
        background: linear-gradient(135deg, #f59e0b, #b45309);
        color: white;
        padding: 6px 16px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
    }
    .badge-stable {
        background: linear-gradient(135deg, #10b981, #047857);
        color: white;
        padding: 6px 16px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
    }

    /* Custom Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.4rem;
        border: 1px solid rgba(199, 210, 254, 0.3);
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
        transform: translateY(-2px);
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown("""
    <div class="executive-header">
        <h1 style="margin:0; font-size: 32px; font-weight: 800; letter-spacing: -0.5px;">⚡ RAJ-AEGIS : National AI Command & Intelligence</h1>
        <p style="margin:8px 0 0 0; font-size: 15px; color: #c7d2fe; font-weight: 500;">
            Next-Gen Predictive Risk Analytics & Automated Institutional Intervention Matrix
        </p>
        <p style="margin:4px 0 0 0; font-size: 12px; color: #94a3b8;">
            Government of Rajasthan | Smart India Hackathon Initiative (SIH25102)
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. Command Center Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Emblem_of_Rajasthan.svg", width=65)
    st.markdown("### 🎛️ Neural Telemetry Hub")
    st.success("Cloud Core: Active 🟢")
    st.markdown("---")
    st.markdown("**Engine:** Render Microservices")
    st.markdown("**Security:** Quantum-Grade TLS")
    st.markdown("**Region:** Jaipur Central")
    st.markdown("**Status:** Fully Operational")

# 5. Colorful Tabs
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
    st.markdown("### 🔍 Individual Student Vulnerability Profiler")
    
    with st.form("evaluation_form"):
        col_f1, col_f2 = st.columns(2, gap="large")
        
        with col_f1:
            st.markdown('<div class="card-cyan">', unsafe_allow_html=True)
            st.markdown("#### 📌 Administrative Profile")
            student_id = st.text_input("Student Unique ID / Roll Number*", placeholder="e.g., RJ-JP-2026-890")
            school_name = st.text_input("Institution Name*", placeholder="e.g., Govt Sr Sec School, Jaipur")
            gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
            fees_status = st.selectbox("Fees Status", options=["Paid", "Pending", "Unpaid", "last 5 months not paid"])
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_f2:
            st.markdown('<div class="card-purple">', unsafe_allow_html=True)
            st.markdown("#### 🌐 Environment & Aspirations")
            internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
            family_support = st.selectbox("Family Academic Support", options=["Yes", "No"])
            wants_higher_ed = st.selectbox("Wants Higher Education", options=["Yes", "No"])
            medical_status = st.selectbox("Medical Health Status", options=["Good", "Average", "Poor"])
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('<div class="card-amber">', unsafe_allow_html=True)
        st.markdown("#### 📈 Academic & Behavioral Telemetry Matrix")
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

        submit_eval = st.form_submit_button(label="🚀 Execute AI Neural Inference", use_container_width=True)

    if submit_eval:
        if not student_id.strip() or not school_name.strip():
            st.error("⚠️ Mandatory fields missing: Please enter both Student ID and Institution Name.")
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
                with st.spinner("Computing neural risk vectors across cloud cluster..."):
                    response = requests.post(f"{API_BASE_URL}/api/predict/custom", json=payload, timeout=15)
                
                if response.status_code == 200:
                    res_data = response.json()
                    risk_score = res_data.get("risk_score", 0.0)
                    tier = res_data.get("risk_tier", "Low Risk")
                    factors = res_data.get("top_factors", ["Stable baseline indicators"])
                    
                    badge_class = "badge-stable"
                    card_theme = "card-emerald"
                    if "High" in str(tier):
                        badge_class = "badge-critical"
                        card_theme = "card-rose"
                    elif "Moderate" in str(tier):
                        badge_class = "badge-warning"
                        card_theme = "card-amber"

                    st.markdown("---")
                    st.markdown(f"### 📊 Live Diagnostic Telemetry: `{student_id}`")
                    
                    st.markdown(f"""
                        <div class="{card_theme}">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <h1 style="margin:0; font-size: 42px; font-weight: 800; color: #ffffff;">{risk_score}%</h1>
                                    <p style="margin:4px 0 0 0; color: #cbd5e1; font-size: 15px; font-weight: 500;">Calculated Dropout Vulnerability Index</p>
                                </div>
                                <div>
                                    <span class="{badge_class}">{tier}</span>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                    col_res1, col_res2 = st.columns(2, gap="large")
                    
                    with col_res1:
                        st.markdown('<div class="card-purple">', unsafe_allow_html=True)
                        st.markdown("#### 🔍 Primary Risk Vectors Detected")
                        if isinstance(factors, list) and factors:
                            for factor in factors:
                                st.markdown(f"- 🔸 {factor}")
                        else:
                            st.markdown("- No critical flags detected.")
                        st.markdown('</div>', unsafe_allow_html=True)
                            
                    with col_res2:
                        st.markdown('<div class="card-cyan">', unsafe_allow_html=True)
                        st.markdown("#### 🛡️ Automated Prescribed Protocol")
                        if "High" in str(tier):
                            st.error("🚨 **High Risk Protocol:** Immediate counselor intervention and guardian notification triggered.")
                        elif "Moderate" in str(tier):
                            st.warning("⚠️ **Watchlist Protocol:** Enroll student in weekly remedial tracking.")
                        else:
                            st.success("✅ **Standard Status:** Profile stable within normative operational ranges.")
                        st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error(f"⚠️ Backend Telemetry Error: Status code {response.status_code}")
            except Exception as ex:
                st.error(f"🚨 Network Connection Failure: {ex}")

# =========================================================================
# TAB 2: MASTER STUDENT DATABASE
# =========================================================================
with tab2:
    st.markdown("### 👥 State Master Student Repository")
    
    st.markdown('<div class="card-cyan">', unsafe_allow_html=True)
    st.markdown("Synchronize and view live decentralized student records from the cloud database.")
    if st.button("🔄 Initialize Database Sync", use_container_width=False):
        try:
            with st.spinner("Fetching cloud repository records..."):
                resp = requests.get(f"{API_BASE_URL}/api/students", timeout=10)
            if resp.status_code == 200:
                records = resp.json()
                if records:
                    df_students = pd.DataFrame(records)
                    st.success(f"Successfully synchronized {len(df_students)} records.")
                    st.dataframe(df_students, use_container_width=True)
                else:
                    st.info("Repository currently empty.")
            else:
                st.error("Failed to query dataset.")
        except Exception as e:
            st.error(f"Connection error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# TAB 3: REGIONAL INTELLIGENCE
# =========================================================================
with tab3:
    st.markdown("### 📊 Regional District Intelligence Matrix")
    
    st.markdown('<div class="card-purple">', unsafe_allow_html=True)
    if st.button("📈 Generate District Telemetry Report", use_container_width=False):
        try:
            with st.spinner("Aggregating macro-level regional metrics..."):
                resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
            if resp.status_code == 200:
                analytics_data = resp.json()
                summary = analytics_data.get("summary", {})
                schools = analytics_data.get("school_metrics", [])
                
                st.markdown("---")
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
                    c1, c2 = st.columns(2, gap="large")
                    with c1:
                        st.markdown("#### Headcount per Institution")
                        st.bar_chart(df_schools.set_index("School")["total_students"])
                    with c2:
                        st.markdown("#### Average Absences per Institution")
                        st.bar_chart(df_schools.set_index("School")["avg_absences"])
                    st.dataframe(df_schools, use_container_width=True)
            else:
                st.error("Failed to compile metrics.")
        except Exception as e:
            st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================================
# TAB 4: INTERVENTION & ALERT HUB
# =========================================================================
with tab4:
    st.markdown("### 🚨 Emergency Intervention & Audit Hub")
    
    col_a1, col_a2 = st.columns(2, gap="large")
    
    with col_a1:
        st.markdown('<div class="card-rose">', unsafe_allow_html=True)
        st.markdown("#### 📤 Automated SMS & Ticket Dispatch")
        target_student_id = st.text_input("Target Student ID", placeholder="e.g., RJ-JP-2026-890", key="alert_id_input")
        if st.button("🚨 Dispatch Emergency Ticket", key="alert_btn"):
            if target_student_id:
                try:
                    resp = requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_student_id}", timeout=10)
                    if resp.status_code == 200:
                        res_json = resp.json()
                        st.success(f"✅ Alert dispatched for **{target_student_id}**.")
                        st.markdown(f"- **Status:** {res_json.get('status', 'Completed')}")
                        st.markdown(f"- **Ticket Ref:** `{res_json.get('ticket_id', 'TICKET-' + target_student_id)}`")
                    else:
                        st.error("Dispatch failed.")
                except Exception as err:
                    st.error(f"Error: {err}")
            else:
                st.warning("Enter valid Student ID.")
        st.markdown('</div>', unsafe_allow_html=True)
                
    with col_a2:
        st.markdown('<div class="card-amber">', unsafe_allow_html=True)
        st.markdown("#### 🔄 Post-Intervention Reassessment")
        reass_id = st.text_input("Target Student ID for Review", placeholder="e.g., RJ-JP-2026-890", key="reass_id_input")
        intervention_action = st.selectbox("Applied Protocol", options=["FEE_ASSISTANCE", "ATTENDANCE_COUNSELING", "ACADEMIC_REMEDIAL"])
        if st.button("⚖️ Process & Recompute", key="reass_btn"):
            if reass_id:
                try:
                    resp = requests.post(
                        f"{API_BASE_URL}/api/interventions/reassess/{reass_id}", 
                        params={"intervention_type": intervention_action}, 
                        timeout=10
                    )
                    if resp.status_code == 200:
                        res_json = resp.json()
                        st.success(f"✅ Profile updated for **{reass_id}**.")
                        st.markdown(f"- **Revised Score:** `{res_json.get('risk_score', 'N/A')}%`")
                        st.markdown(f"- **New Tier:** **{res_json.get('risk_tier', 'N/A')}**")
                    else:
                        st.error("Reassessment failed.")
                except Exception as err:
                    st.error(f"Error: {err}")
            else:
                st.warning("Enter valid Student ID.")
        st.markdown('</div>', unsafe_allow_html=True)
