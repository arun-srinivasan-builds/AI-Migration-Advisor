import streamlit as st
import ollama

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Migration Advisor",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# PROFESSIONAL CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* GLOBAL PAGE */

    .stApp {
        background-color: #f5f5f7;
        color: #1d1d1f;
        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            Roboto,
            Helvetica,
            Arial,
            sans-serif;
    }

    .block-container {
        max-width: 1600px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* HEADINGS */

    h1 {
        color: #1d1d1f !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.04em;
        margin-bottom: 0.25rem !important;
    }

    h2 {
        color: #1d1d1f !important;
        font-size: 1.55rem !important;
        font-weight: 650 !important;
        letter-spacing: -0.02em;
        margin-top: 1rem !important;
    }

    h3 {
        color: #1d1d1f !important;
        font-size: 1.2rem !important;
        font-weight: 650 !important;
    }

    p, li, label, .stMarkdown {
        color: #1d1d1f;
    }

    /* HERO */

    .hero-subtitle {
        color: #6e6e73;
        font-size: 1.02rem;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }

    .intro-card {
        background: #ffffff;
        border: 1px solid #e5e5e7;
        border-radius: 14px;
        padding: 16px 20px;
        color: #424245;
        font-size: 0.96rem;
        margin-bottom: 1.7rem;
    }

    /* LABELS */

    .section-label {
        font-size: 0.78rem;
        font-weight: 650;
        color: #6e6e73;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        margin-bottom: 0.5rem;
    }

    /* INPUT */

    textarea {
        background-color: #ffffff !important;
        color: #1d1d1f !important;
        border: 1px solid #d2d2d7 !important;
        border-radius: 12px !important;
        font-size: 0.96rem !important;
        line-height: 1.5 !important;
    }

    textarea:focus {
        border-color: #0071e3 !important;
        box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.12) !important;
    }

    /* PRIMARY BUTTON */

    div.stButton > button {
        background-color: #0071e3 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 980px !important;
        min-height: 46px;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #0077ed !important;
        color: #ffffff !important;
        border: none !important;
        transform: translateY(-1px);
    }

    div.stButton > button p {
        color: #ffffff !important;
    }

    /* STATUS / ANALYZING BOX */

    /* Outer status container */
    [data-testid="stStatusWidget"] {
        background-color: #0071e3 !important;
        border: 1px solid #0071e3 !important;
        border-radius: 14px !important;
    }

    /* Inner details container */
    [data-testid="stStatusWidget"] > div {
        background-color: #0071e3 !important;
    }

    /* Status header */
    [data-testid="stStatusWidget"] summary {
        background-color: #0071e3 !important;
        color: #ffffff !important;
        border-radius: 14px !important;
    }

    /* Everything inside the status box */
    [data-testid="stStatusWidget"] p,
    [data-testid="stStatusWidget"] span,
    [data-testid="stStatusWidget"] svg {
        color: #ffffff !important;
    }

    /* Expanded status details */
    [data-testid="stStatusWidget"] [data-testid="stMarkdownContainer"] {
        background-color: #0071e3 !important;
    }

    [data-testid="stStatusWidget"] [data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
    }

    /* ASSESSMENT OUTPUT */

    [data-testid="stMarkdownContainer"] h2 {
        color: #1d1d1f !important;
        border-bottom: 1px solid #e5e5e7;
        padding-bottom: 8px;
        margin-top: 24px !important;
        margin-bottom: 12px !important;
        font-size: 1.28rem !important;
        font-weight: 700 !important;
    }

    [data-testid="stMarkdownContainer"] h3 {
        color: #0071e3 !important;
        font-size: 1.08rem !important;
        margin-top: 20px !important;
        margin-bottom: 8px !important;
        font-weight: 650 !important;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: #1d1d1f !important;
        font-weight: 700;
    }

    [data-testid="stMarkdownContainer"] li {
        line-height: 1.6;
        margin-bottom: 5px;
    }

    /* INFORMATION CARD */

    .info-box {
        background: #ffffff;
        border: 1px solid #e5e5e7;
        border-radius: 14px;
        padding: 16px 18px;
        margin-top: 1.4rem;
        font-size: 0.9rem;
    }

    .info-value {
        color: #1d1d1f;
        font-weight: 600;
    }

    .muted {
        color: #6e6e73;
        font-size: 0.88rem;
    }

    /* READY PANEL */

    .assessment-shell {
        background-color: #ffffff;
        border: 1px solid #e5e5e7;
        border-radius: 18px;
        padding: 24px 28px;
        min-height: 520px;
    }

    /* DISCLAIMER */

    .disclaimer {
        background: #fff8e8;
        border: 1px solid #f4dfad;
        border-radius: 12px;
        padding: 13px 16px;
        color: #5c4b21;
        font-size: 0.88rem;
        margin-top: 18px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("AI Migration Advisor")

st.markdown(
    '<div class="hero-subtitle">'
    'AI-assisted preliminary assessment for enterprise data and analytics migrations.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="intro-card">
    Describe a migration scenario in your own words.
    The advisor reviews migration complexity, key risks,
    assessment considerations, customer questions and recommended next steps.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# 30 / 70 LAYOUT
# ---------------------------------------------------------

input_col, assessment_col = st.columns(
    [3, 7],
    gap="large"
)

# ---------------------------------------------------------
# LEFT SIDE
# ---------------------------------------------------------

with input_col:

    st.markdown(
        '<div class="section-label">Migration Scenario</div>',
        unsafe_allow_html=True
    )

    st.subheader("Describe the environment")

    migration_details = st.text_area(
        "Include the source environment, target platform, workloads, "
        "dependencies, data volume, reporting, custom code and business expectations.",
        height=280,
        placeholder=(
            "Example:\n\n"
            "Current platform is Azure HDInsight and target platform is "
            "Microsoft Fabric. The environment contains Spark jobs, Hive tables, "
            "data pipelines, historical data and downstream Power BI reports..."
        )
    )

    analyze_clicked = st.button(
        "Analyze Migration",
        type="primary",
        use_container_width=True
    )

    st.markdown(
        """
        <div class="info-box">

        <div class="section-label">AI Engine</div>

        <div class="info-value">
        qwen3:0.6b via Ollama
        </div>

        <br>

        <div class="section-label">Deployment</div>

        <div class="muted">
        Local — AI model inference runs on this computer.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# RIGHT SIDE
# ---------------------------------------------------------

with assessment_col:

    st.markdown(
        '<div class="section-label">Assessment Workspace</div>',
        unsafe_allow_html=True
    )

    st.subheader("Preliminary AI Assessment")

    if analyze_clicked:

        if not migration_details.strip():

            st.warning(
                "Enter a migration scenario before running the assessment."
            )

        else:

            prompt = f"""
            You are an experienced Data Platform Migration Advisor.

            Analyse the following migration scenario:

            {migration_details}

            Produce a concise preliminary assessment.

            Use EXACTLY the following Markdown structure:

            ## Overall Migration Complexity
            State Low, Medium, or High and briefly explain why.

            ## Key Complexity Drivers
            Provide the major factors contributing to the complexity.

            ## Top 5 Migration Risks
            Provide a numbered list. Explain each risk briefly.

            ## Important Areas to Assess
            Provide a clear bullet list.

            ## Top 5 Questions for the Customer
            Provide a numbered list.

            ## Recommended Next Steps
            Provide a numbered list of practical next actions.

            ## Information Requiring Validation
            Clearly list information that cannot be determined from the
            supplied scenario.

            Important constraints:

            - Do not invent migration tools or utilities.
            - Do not invent timelines.
            - Do not invent SLAs.
            - Do not invent costs.
            - Do not invent technical capabilities.
            - Do not assume information that has not been supplied.
            - If a source-to-target migration appears inappropriate,
              incompatible or unclear, explicitly flag the concern.
            - Clearly distinguish known information from assumptions.
            - Keep recommendations preliminary and practical.
            """

            try:

                with st.status(
                    "Analyzing migration scenario...",
                    expanded=True
                ) as status:

                    st.write(
                        "Reviewing migration context and workloads..."
                    )

                    st.write(
                        "Assessing complexity and migration risks..."
                    )

                    st.write(
                        "Preparing preliminary recommendations..."
                    )

                    st.write(
                        "Local AI processing may take some time depending on the system."
                    )

                    response = ollama.chat(
                        model="qwen3:0.6b",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    assessment = response["message"]["content"]

                    status.update(
                        label="Assessment completed",
                        state="complete",
                        expanded=False
                    )

                st.markdown(assessment)

                st.markdown(
                    """
                    <div class="disclaimer">
                    <b>Human validation required.</b><br>
                    This is an AI-generated preliminary assessment.
                    Technical recommendations and migration decisions should
                    be validated by appropriate subject-matter experts.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as error:

                st.error(
                    f"Unable to generate the migration assessment: {error}"
                )

    else:

        st.markdown(
            """
            <div class="assessment-shell">

            <h3 style="color:#1d1d1f;">
            Ready for assessment
            </h3>

            <p style="color:#6e6e73; line-height:1.6;">
            Enter the migration scenario in the workspace on the left,
            then select <b>Analyze Migration</b>.
            </p>

            <br>

            <div class="section-label">Assessment will include</div>

            <p>
            • Overall migration complexity<br>
            • Complexity drivers<br>
            • Top migration risks<br>
            • Assessment areas<br>
            • Questions for the customer<br>
            • Recommended next steps<br>
            • Information requiring validation
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )
