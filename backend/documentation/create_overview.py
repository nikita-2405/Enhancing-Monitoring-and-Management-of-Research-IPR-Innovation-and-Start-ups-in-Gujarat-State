
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Page margins
section = doc.sections[0]
section.top_margin = Inches(0.8)
section.bottom_margin = Inches(0.8)
section.left_margin = Inches(1)
section.right_margin = Inches(1)

# Default font
style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(12)

# Title
title = doc.add_heading(
    "Enhancing Monitoring and Management of Research, IPR, Innovation, and Start-ups in Gujarat State",
    0
)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph(
    "Major Project Report – Project Overview",
    style="Subtitle"
)

doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "Research, Intellectual Property Rights (IPR), innovation, and start-ups "
    "play an important role in the development of a state's economy and "
    "technology ecosystem. Gujarat has several institutions, researchers, "
    "innovation centres, and start-up support organisations. However, "
    "information about these activities may be maintained across different "
    "platforms and organisations."
)
doc.add_paragraph(
    "This project proposes a centralized web-based system to manage and "
    "monitor research projects, IPR activities, innovations, and start-ups "
    "in Gujarat State. It provides role-based access, organized records, "
    "and an analytics dashboard."
)

doc.add_heading("2. Problem Statement", level=1)
doc.add_paragraph(
    "Information related to research projects, patents, innovations, and "
    "start-ups is often maintained in separate records or systems. This can "
    "make monitoring, tracking progress, accessing information, and preparing "
    "reports difficult. A centralized platform is needed to organize this "
    "information and provide authorized users with suitable access."
)

doc.add_heading("3. Objectives", level=1)
objectives = [
    "Develop a centralized platform for research, IPR, innovation, and start-up records.",
    "Provide role-based access to different categories of users.",
    "Allow authorized users to add, view, update, and delete records.",
    "Provide a common dashboard for monitoring available records.",
    "Support better organization, transparency, and information management."
]
for item in objectives:
    doc.add_paragraph(item, style="List Bullet")

doc.add_heading("4. Scope of the Project", level=1)
scope = [
    "Research Project Management",
    "Innovation Management",
    "Intellectual Property Rights (IPR) Management",
    "Start-up Management",
    "Role-based user authentication and authorization",
    "Dashboard and analytics"
]
for item in scope:
    doc.add_paragraph(item, style="List Bullet")

doc.add_heading("5. Proposed Solution", level=1)
doc.add_paragraph(
    "The proposed system is a web application developed using Python and "
    "Django, with MySQL as its database. It contains separate modules for "
    "research projects, innovations, IPR, and start-ups. Users log in with "
    "their assigned accounts and can access only the modules permitted by "
    "their roles. An analytics dashboard provides an overview of the "
    "information stored in the system."
)

doc.add_heading("6. Expected Outcome", level=1)
doc.add_paragraph(
    "The expected outcome is a centralized and structured web application "
    "that simplifies record management and supports monitoring of research, "
    "IPR, innovation, and start-up activities. It aims to improve information "
    "accessibility, organization, and administrative efficiency."
)

doc.add_heading("7. Technologies Used", level=1)
technologies = [
    "Frontend: HTML and CSS",
    "Backend: Python and Django",
    "Database: MySQL",
    "Development environment: Visual Studio Code / terminal",
    "Database management: MySQL Workbench"
]
for item in technologies:
    doc.add_paragraph(item, style="List Bullet")

doc.save("Project_Overview.docx")
print("Project Overview document created successfully!")
