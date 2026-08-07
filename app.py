import streamlit as st
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="RAJ-AEGIS | Dropout Prediction",
    page_icon="▪️",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_BASE_URL = "https://sih-student-api.onrender.com"

# Initialize Session State for Page Navigation
if 'app_state' not in st.session_state:
    st.session_state.app_state = 'landing'  # 'landing' or 'dashboard'

# 2. Complete Theme Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Syne:wght@600;700;800&display=swap');

    /* Force Full Page Background to Solid White */
    .stApp {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }

    /* Left Sidebar Styling (Only active in dashboard mode) */
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
        padding: 30px 20px;
        text-align: center;
        max-width: 950px;
        margin: 0 auto;
    }
    .landing-title {
        font-family: 'Syne', sans-serif;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1.5px;
        color: #0f172a;
        margin-bottom: 15px;
    }
    .landing-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #475569;
        margin-bottom: 30px;
        line-height: 1.6;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Landing Page Colorful Feature Cards */
    .card-cyan-box {
        background-color: #f0fdfa;
        border: 1px solid #2dd4bf;
        padding: 24px;
        border-radius: 12px;
        min-height: 150px;
    }
    .card-cyan-box h3 { font-family: 'Syne', sans-serif; color: #0f766e; font-size: 17px; margin-bottom: 8px; }
    .card-cyan-box p { color: #334155; font-size: 13px; margin: 0; line-height: 1.5; }

    .card-purple-box {
        background-color: #f5f3ff;
        border: 1px solid #a78bfa;
        padding: 24px;
        border-radius: 12px;
        min-height: 150px;
    }
    .card-purple-box h3 { font-family: 'Syne', sans-serif; color: #6d28d9; font-size: 17px; margin-bottom: 8px; }
    .card-purple-box p { color: #334155; font-size: 13px; margin: 0; line-height: 1.5; }

    .card-amber-box {
        background-color: #fffbeb;
        border: 1px solid #fcd34d;
        padding: 24px;
        border-radius: 12px;
        min-height: 150px;
    }
    .card-amber-box h3 { font-family: 'Syne', sans-serif; color: #b45309; font-size: 17px; margin-bottom: 8px; }
    .card-amber-box p { color: #334155; font-size: 13px; margin: 0; line-height: 1.5; }

    /* Team Members Grid Card */
    .team-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 12px;
        max-width: 800px;
        margin: 25px auto;
        text-align: left;
    }

    /* Dashboard Cards */
    .studio-card {
        background-color: #ffffff;
        border: 2px solid #e2e8f0;
        padding: 28px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .studio-card * {
        color: #0f172a !important;
    }

    /* Force Streamlit Input Fields */
    .stTextInput input, .stNumberInput input, div[data-baseweb="select"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        -webkit-text-fill-color: #0f172a !important;
    }
    div[data-baseweb="select"] * {
        color: #0f172a !important;
    }

    /* Force ALL Streamlit Buttons to be Bright Blue with Crisp White Text */
    div.stButton > button, button[kind="secondary"], button[kind="primary"], .stFormSubmitButton > button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
        border: none !important;
        opacity: 1 !important;
    }
    div.stButton > button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    div.stButton > button:hover, .stFormSubmitButton > button:hover {
        background-color: #1d4ed8 !important;
        color: #ffffff !important;
    }

    /* Badges */
    .badge-critical {
        background-color: #fee2e2; color: #b91c1c !important; border: 1px solid #fecaca;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase; border-radius: 20px;
    }
    .badge-warning {
        background-color: #fef3c7; color: #b45309 !important; border: 1px solid #fde68a;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase; border-radius: 20px;
    }
    .badge-stable {
        background-color: #d1fae5; color: #047857 !important; border: 1px solid #a7f3d0;
        padding: 6px 14px; font-weight: 700; font-size: 11px; text-transform: uppercase; border-radius: 20px;
    }

    #MainMenu {visibility: visible;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# STATE 1: LANDING PAGE
# =========================================================================
if st.session_state.app_state == 'landing':
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {display: none !important;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="landing-hero">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 2px; color: #4f46e5; text-transform: uppercase; margin-bottom: 8px;">
                Government of Rajasthan | Smart India Hackathon Initiative
            </div>
            <div class="landing-title">
                RAJ-AEGIS <span style="color: #64748b; font-weight: 400;">// Dropout Prediction</span>
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

    # Team Members & Institution Details Section
    st.markdown("""
        <div class="team-card">
            <h3 style="margin-top:0; color: #0f172a; font-family: 'Syne', sans-serif; font-size: 18px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
                Prepared by: SRM INSTITUTE OF SCIENCE AND TECHNOLOGY
            </h3>
            <ul style="color: #334155; font-size: 14px; line-height: 1.8; margin-bottom: 0; padding-left: 20px;">
                <li><b>RAJESH (FRONTEND)</b> — RA2511026020377</li>
                <li><b>FARID (BACKEND)</b> — RA2511026020353</li>
                <li><b>JASHWANTH (FRONTEND)</b> — RA2511026020355</li>
                <li><b>TARUNIKA (PPT)</b> — RA251102602068</li>
                <li><b>GAUTHAM (PPT)</b> — RA2511026020341</li>
                <li><b>VEDHANTHA (PROTOTYPE)</b> — RA2511026020366</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])
    with col_btn2:
        if st.button("Get Started // Enter Dashboard", use_container_width=True):
            st.session_state.app_state = 'dashboard'
            st.rerun()

# =========================================================================
# STATE 2: DASHBOARD VIEW (Connected via API Requests)
# =========================================================================
else:
    st.markdown("""
        <style>
        .stApp { background-color: #ffffff !important; color: #0f172a !important; }
        h1, h2, h3, h4, h5, h6, p, label, .stTextInput label, .stSelectbox label { color: #0f172a !important; }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("---")
        
        selected_option = st.radio(
            "Navigation",
            [
                "AI Prediction", 
                "Students", 
                "Analytics", 
                "Counselling", 
                "Reports"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("Logout", use_container_width=True):
            st.session_state.app_state = 'landing'
            st.rerun()

    # Top Header Bar
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 25px;">
            <div>
                <h1 style="margin:0; font-size: 28px; font-family: 'Syne', sans-serif; color: #0f172a !important;">Government of Rajasthan</h1>
                <p style="margin:4px 0 0 0; color: #64748b !important; font-size: 13px;">AI-based Student Dropout Prediction System</p>
            </div>
            <div style="color: #475569 !important; font-weight: 600;">Admin Portal</div>
        </div>
    """, unsafe_allow_html=True)

    # =========================================================================
    # 1. AI PREDICTION VIEW
    # =========================================================================
    if selected_option == "AI Prediction":
        st.markdown("<h2 style='color: #0f172a !important;'>Individual Student Vulnerability Assessment</h2>", unsafe_allow_html=True)
        
        with st.form("evaluation_form"):
            col_f1, col_f2 = st.columns(2, gap="large")
            
            with col_f1:
                st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                st.markdown("<h4 style='color: #0f172a !important;'>Administrative & Demographics</h4>", unsafe_allow_html=True)
                student_id = st.text_input("Student ID (e.g. STU1001)*", value="STU1001")
                student_name = st.text_input("Student Name*", value="Rahul Kumar")
                school_name = st.selectbox("Institution Name", options=["School_A", "School_B"])
                gender = st.selectbox("Gender", options=["M", "F"])
                cast_group = st.selectbox("Cast Category", options=["General", "OBC", "SC", "ST"])
                religion = st.selectbox("Religion", options=["Hindu", "Muslim", "Sikh"])
                address_type = st.selectbox("Area Type", options=["Urban", "Rural"])
                fees_status = st.selectbox("Fees Paid Status", options=["fully paid for the year", "last 5 months not paid"])
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_f2:
                st.markdown('<div class="studio-card">', unsafe_allow_html=True)
                st.markdown("<h4 style='color: #0f172a !important;'>Environmental & Family Parameters</h4>", unsafe_allow_html=True)
                age = st.number_input("Age", min_value=11, max_value=19, value=15)
                family_size = st.number_input("Family Size", min_value=2, max_value=9, value=4)
                parental_status = st.selectbox("Parental Status", options=["living together", "living apart"])
                mother_edu = st.selectbox("Mother Education", options=["Middle school", "High school", "University"])
                father_edu = st.selectbox("Father Education", options=["Middle school", "High school", "University"])
                mother_job = st.selectbox("Mother Job", options=["laborer", "farmer", "service", "housewife"])
                father_job = st.selectbox("Father Job", options=["laborer", "farmer", "service", "business"])
                guardian = st.selectbox("Guardian", options=["mother", "father"])
                travel_time = st.number_input("Travel Time (minutes)", min_value=5, max_value=60, value=15)
                st.markdown('</div>', unsafe_allow_html=True)
                
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #0f172a !important;'>Quantitative Behavioral & Academic Vectors</h4>", unsafe_allow_html=True)
            col_n1, col_n2, col_n3, col_n4 = st.columns(4)
            with col_n1: school_support = st.selectbox("School Support", options=["yes", "no"])
            with col_n2: family_support = st.selectbox("Family Support", options=["yes", "no"])
            with col_n3: internet_access = st.selectbox("Internet Access", options=["yes", "no"])
            with col_n4: medical_status = st.selectbox("Medical Status", options=["healthy", "poor"])
            
            col_b1, col_b2, col_b3 = st.columns(3)
            with col_b1: extra_paid_class = st.selectbox("Extra Paid Class", options=["no", "yes"])
            with col_b2: extra_curricular = st.selectbox("Extracurricular Activities", options=["no", "yes"])
            with col_b3: wants_higher_ed = st.selectbox("Wants Higher Education", options=["yes", "no"])

            col_q1, col_q2, col_q3, col_q4 = st.columns(4)
            with col_q1: absences = st.number_input("Absence Days", min_value=0, max_value=100, value=4)
            with col_q2: failures = st.number_input("Past Failures (Subjects)", min_value=0, max_value=10, value=0)
            with col_q3: final_grade = st.number_input("Final Grade (0.0 - 20.0)", min_value=0.0, max_value=20.0, value=12.0)
            with col_q4: parent_phone = st.text_input("Parent/Guardian Phone (+91)", value="8110025181")
            st.markdown('</div>', unsafe_allow_html=True)

            submit_eval = st.form_submit_button(label="EXECUTE NEURAL INFERENCE")

        if submit_eval:
            if not student_id.strip() or not student_name.strip():
                st.error("Mandatory fields missing: Student ID and Student Name required.")
            else:
                payload = {
                    "Student_ID": student_id,
                    "Name": student_name,
                    "School": school_name,
                    "Gender": gender,
                    "Cast": cast_group,
                    "Religion": religion,
                    "Age": int(age),
                    "Address": address_type,
                    "Family_Size": int(family_size),
                    "Parental_Status": parental_status,
                    "Mother_Education": mother_edu,
                    "Father_Education": father_edu,
                    "Mother_Job": mother_job,
                    "Father_Job": father_job,
                    "Fees_Paid_Status": fees_status,
                    "Guardian": guardian,
                    "Travel_Time": int(travel_time),
                    "Number_of_Failures": int(failures),
                    "School_Support": school_support,
                    "Family_Support": family_support,
                    "Extra_Paid_Class": extra_paid_class,
                    "Extra_Curricular_Activities": extra_curricular,
                    "Wants_Higher_Education": wants_higher_ed,
                    "Internet_Access": internet_access,
                    "Medical_Status": medical_status,
                    "Number_of_Absences": int(absences),
                    "Grade_1": float(final_grade),
                    "Grade_2": float(final_grade),
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

                        st.markdown(f"""
                            <div class="studio-card" style="background-color: #f8fafc;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <div>
                                        <h2 style="margin:0; font-size: 48px; font-weight: 800; color: #0f172a !important;">{risk_score}%</h2>
                                        <p style="margin:4px 0 0 0; color: #64748b !important; font-size: 13px;">Dropout Vulnerability Index</p>
                                    </div>
                                    <div><span class="{badge_class}">{tier}</span></div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Prediction API failed.")
                except Exception as ex:
                    st.error(f"Connection failure: {ex}")

    # =========================================================================
    # 2. STUDENTS REPOSITORY VIEW
    # =========================================================================
    elif selected_option == "Students":
        st.markdown("<h2 style='color: #0f172a !important;'>Master Student Repository</h2>", unsafe_allow_html=True)
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("SYNC DATABASE RECORDS"):
            try:
                with st.spinner("Querying repository via API..."):
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
                    st.error("API Query failed.")
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================================
    # 3. ANALYTICS VIEW
    # =========================================================================
    elif selected_option == "Analytics":
        st.markdown("<h2 style='color: #0f172a !important;'>Regional Analytics Matrix</h2>", unsafe_allow_html=True)
        st.markdown('<div class="studio-card">', unsafe_allow_html=True)
        if st.button("GENERATE TELEMETRY REPORT"):
            try:
                with st.spinner("Aggregating macro metrics via API..."):
                    resp = requests.get(f"{API_BASE_URL}/api/analytics/district", timeout=10)
                if resp.status_code == 200:
                    analytics_data = resp.json()
                    summary = analytics_data.get("summary", {})
                    schools = analytics_data.get("school_metrics", [])
                    
                    k1, k2, k3, k4 = st.columns(4)
                    with k1: st.metric("Total Monitored", summary.get("total_students_monitored", 0))
                    with k2: st.metric("Historical Dropouts", summary.get("historical_dropouts", 0))
                    with k3: st.metric("Unpaid Fee Issues", summary.get("students_with_unpaid_fees", 0))
                    with k4: st.metric("Chronic Absences", summary.get("students_chronically_absent", 0))
                    
                    if schools:
                        st.dataframe(pd.DataFrame(schools), use_container_width=True)
                else:
                    st.error("Failed to load telemetry metrics.")
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # =========================================================================
    # 4. COUNSELLING & REPORTS VIEWS
    # =========================================================================
    elif selected_option in ["Counselling", "Reports"]:
        st.markdown(f"<h2 style='color: #0f172a !important;'>{selected_option} Hub</h2>", unsafe_allow_html=True)
        col_a1, col_a2 = st.columns(2, gap="large")
        with col_a1:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #0f172a !important;'>Automated SMS & Ticket Dispatch</h4>", unsafe_allow_html=True)
            target_student_id = st.text_input("Target Student ID", placeholder="e.g., STU1000", key="alert_id_input")
            if st.button("DISPATCH EMERGENCY TICKET"):
                if target_student_id:
                    try:
                        resp = requests.post(f"{API_BASE_URL}/api/alerts/dispatch/{target_student_id}", timeout=10)
                        if resp.status_code == 200:
                            st.success(f"Ticket dispatched for student `{target_student_id}`.")
                        else:
                            st.error("Ticket dispatch failed.")
                    except Exception as err:
                        st.error(f"Error: {err}")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_a2:
            st.markdown('<div class="studio-card">', unsafe_allow_html=True)
            st.markdown("<h4 style='color: #0f172a !important;'>Post-Intervention Reassessment</h4>", unsafe_allow_html=True)
            reass_id = st.text_input("Target Student ID for Review", placeholder="e.g., STU1000", key="reass_id_input")
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
