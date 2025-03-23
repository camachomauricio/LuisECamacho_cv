import streamlit as st

# Set page config and custom theme
st.set_page_config(page_title="CV", page_icon=":briefcase:", layout="wide")


st.title("Luis Enrique Camacho Maya")

# Add a Download button for the PDF CV right below the title
with open("CV-Luis Enrique Camacho Maya (ENG & ESP).pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download CV (PDF)",
    data=PDFbyte,
    file_name="LuisCamacho_CV.pdf",
    mime="application/pdf"
)

st.subheader("Global IT Project Manager | Enterprise IT Specialist | Certified Scrum Master")

st.markdown("""
I am a Computer Systems Engineer with 10+ years of experience implementing and supporting IT solutions for global and local Pharma and F&B companies. I've led and managed projects across Network, IT Finance, and IT HR. I'm looking to grow in a global IT career where I can continue learning and applying new technologies.
""")
with st.expander("🔧 Skills"):
    st.markdown("""
- Python, Pandas, Scikit-learn, Streamlit
- SQL, Flask, Git, Power BI
- Data Visualization, Machine Learning, Statistics

- Project Management
  - SAP Project Management
  - Change Management
  - SAFe Scrum Master
  - Microsoft Azure DevOps
- Technical
  - Apptio/ATUM 2.0
  - Microsoft SQL
  - Oracle
  - VBA
  - Java (Elemental)
  - C/C++ (Elemental)
- Translation and Interpretation
  - English and Spanish
- Currently Learning
  - Gen AI (LLM)
""")

with st.expander("💼 Experience"):
    st.markdown("""
**Sector IT Associate Manager – Global HR IT Lead @ PepsiCo**  
*March 2023 – March 2025, Mexico City, Mexico*  
- Led requirements and IT project analysis for enterprise architecture and visual documentation.  
- Coordinated change management for IT solution deployments.  
- Acted as Business Relationship Manager supporting over 100 HR IT solutions (Learning, Talent Acquisition, etc.).  
  - Reduced recruitment process time from 40 to 20 days.  
  - Improved license provisioning process to reduce cost and enhance security.  
  - Oversaw InfoSec and data protection governance for HR platforms (SSO, risk assessments, file transfers).  
- SAP HCM Payroll project manager for Mexico and LATAM initiatives.  
  - Implemented employee payment capacity feature to prevent excessive deductions in Mexico.  
  - Built severance simulation reports for Peru and Ecuador.

**Sector IT Sr Analyst - TBM | Scrum Master @ PepsiCo**  
*January 2018 – February 2023, Mexico City, Mexico*  
- Analyzed and integrated financial (Opex, vendor) and CMDB data for IT cost transparency (up to $5M in savings).  
- Data modeling and dashboarding using Apptio (ATUM model) for financial and operational KPIs.  
- Worked with CMDB team to eliminate 95% of orphan servers and databases.  
- Supported application rationalization with KQI data.  
- Served as SAFe Scrum Master for TBM team and CGF LACE (Lean Agile Center of Excellence).

**Site Analyst & Application Developer @ Pfizer**  
*August 2014 – December 2017, Toluca, Mexico*  
- Managed IT infrastructure projects (optical fiber upgrades, security network setup).  
- Delivered IT onboarding sessions for new hires (10–20 people per session).  
- Built Excel-based desktop apps for financial analysis.  
- Provided service desk support and managed IT purchases and local inventory.
""")

with st.expander("🎓 Education"):
    st.markdown("""
**Bachelor of Science in Computer Systems Engineering**  
*ITESM Toluca, State of Mexico – May 2015*
""")

with st.expander("📜 Certifications"):
    st.markdown("""
- Japan Foundation’s In the Country Training Program for students of Asociación Japonesa de Estado de México (2024)  
- Develop Generative AI Solutions with Azure OpenAI Service (2024)  
- Microsoft Azure Fundamentals (AZ-900) (2023)  
- Certified SAFe® 5 DevOps Practitioner (2023)  
- SAFe Scrum Master (2021)  
- Recognized TBMA (2020)  
- Elite TBMA (2020)  
- SAFe Agilist (2019)
""")

with st.expander("🌍 Languages"):
    st.markdown("""
- **Mexican Spanish** – Native  
- **English** – Fluent  
  - IELTS 7.5 (2023)  
- **Japanese** – Conversational  
  - JLPT N4 (2024)
""")
    
st.markdown("""
---

👈 Check out the sidebar to see ML Projects and Dashboards!
""")