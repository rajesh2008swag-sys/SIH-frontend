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
    st.session_state.app_state = 'landing'  # 'landing' or 'dashboard'

# 2. Jordan Studio White Theme CSS (Matching the provided reference layout)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .main {
        background-color: #f8fafc;
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

    /* Top Header */
    .studio-header {
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0;
        padding: 24px 32px;
        margin: -6rem -6rem 2rem -6rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Cards */
    .studio-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    /* Badges */
    .badge-high {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 11px;
        text-transform: uppercase;
    }

    /* Primary Action Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        border: none;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    
    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: LANDING / ABOUT PAGE (Default when website link opens)
# =========================================================================
if st.session_state.app_state == 'landing':
    # Sidebar navigation placeholder for landing
    with st.sidebar:
        st.markdown("### **EduShield AI**")
        st.markdown("---")
        st.markdown("📌 **Overview**")
        st.markdown("🚀 **System Introduction**")

    st.markdown("""
        <div style="max-width: 850px; margin: 40px auto; padding: 20px;">
            <div style="font-size: 12px; font-weight: 700; letter-spacing: 2px; color: #4f46e5; text-transform: uppercase; margin-bottom: 10px;">
                Government of Rajasthan | Smart India Hackathon
            </div>
            <h1 style="font-size: 44px; font-weight: 800; color: #0f172a; letter-spacing: -1px; margin-bottom: 20px;">
                Institutional Early Warning & Dropout Prediction System
            </h1>
            <p style="font-size: 17px; color: #475569; line-height: 1.6; margin-bottom: 35px;">
                EduShield AI is an enterprise-grade intelligence platform engineered to analyze student telemetry vectors, compute real-time dropout vulnerability risks, and coordinate proactive administrative interventions across educational institutions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.markdown("""
            <div class="studio-card">
                <h4>📊 Risk Profiler</h4>
                <p style="font-size: 13px; color: #64748b;">Instant predictive evaluations using advanced machine learning models.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="studio-card">
                <h4>👥 Student Repository</h4>
                <p style="font-size: 13px; color: #64748b;">Centralized database synchronization for live student records.</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="studio-card">
                <h4>🚨 Intervention Hub</h4>
                <p style="font-size: 13px; color: #64748b;">Automated alert dispatch and counselor ticket management.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c_btn1, c_btn2, c_btn3 = st.columns([2, 2, 2])
    with c_btn2:
        if st.button("🚀 Get Started // Open Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: ACTUAL DASHBOARD (Opened after clicking Get Started)
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
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("🚪 Logout / Overview", use_container_width=True):
            st.session_state.app_state = 'landing'
            st.rerun()

    # Top Header Bar
    st.markdown("""
        <div class="studio-header">
            <div style="font-weight: 600; font-size: 15px; color: #0f172a;">Government of Rajasthan</div>
            <div style="font-size: 13px; color: #64748b; font-weight: 500;">👤 Admin Portal</div>
        </div>
    """, unsafe_allow_html=True)

    # =========================================================================
    # 1. DASHBOARD VIEW
    # =========================================================================
    if selected_option == "🏠 Dashboard":
        st.markdown("<h2>Dashboard</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748b; margin-top: -10px; margin-bottom: 25px;'>Government of Rajasthan • AI-based Student Dropout Prediction System</p>", unsafe_allow_html=True)

        # Metric Summary Cards
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown("""
                <div class="studio-card">
                    <h1 style="margin:0; font-size: 36px; font-weight: 700;">5</h1>
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
        st.markdown("### High Risk Students")
        
        # High Risk Table Preview
        risk_data = {
            "Name": ["Rahul Sharma", "Priya Singh"],
            "Attendance": [54, 62],
            "CGPA": [5.8, 6.2],
            "Risk": ["High", "High"]
        }
        df_risk = pd.DataFrame(risk_data)
        st.dataframe(df_risk, use_container_width=True, hide_index=True)

    # =========================================================================
    # 2. STUDENTS REPOSITORY VIEW
    # =========================================================================
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
                else:
                    st.error("Failed to fetch records.")
            except Exception as e:
                st.error(f"Connection error: {e}")

    # =========================================================================
    # 3. AI PREDICTION VIEW (Risk Profiler Form)
    # =========================================================================
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

    # =========================================================================
    # 4. ANALYTICS VIEW
    # =========================================================================
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

    # =========================================================================
    # 5. COUNSELLING & REPORTS VIEW
    # =========================================================================
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
