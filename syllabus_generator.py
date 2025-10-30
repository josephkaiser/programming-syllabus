"""
Improved Programming Syllabus Generator
For engineering graduates with mathematical background but limited programming experience
More realistic pacing, better progression, and clearer learning objectives
"""

from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

# Configuration
TOTAL_WEEKS = 72  # More realistic: 1.5 years instead of 1 year
DAYS_PER_WEEK = 3  # 3 days/week for sustainability
OUTPUT_PATH = "Programming_Syllabus_72Weeks_Realistic.pdf"

# Track global day counter
day_counter = 1

def add_page_footer(canvas, doc):
    """Add footer to each page"""
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.grey)
    page_num = canvas.getPageNumber()
    text = f"Page {page_num}"
    canvas.drawCentredString(5.5*inch, 0.5*inch, text)
    canvas.restoreState()

# Create document
doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=landscape(LETTER),
                        leftMargin=36, rightMargin=36, topMargin=48, bottomMargin=48)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontSize=22, leading=26, spaceAfter=12, 
                         alignment=TA_CENTER, textColor=colors.HexColor('#1A237E'), bold=True))
styles.add(ParagraphStyle(name='SubtitleCustom', fontSize=12, leading=14, spaceAfter=18, 
                         alignment=TA_CENTER, textColor=colors.HexColor('#424242'), italic=True))
styles.add(ParagraphStyle(name='SectionHeader', fontSize=13, leading=16, spaceAfter=8, 
                         textColor=colors.HexColor('#1976D2'), bold=True))
styles.add(ParagraphStyle(name='WeekHeader', fontSize=11, leading=14, spaceAfter=6, 
                         textColor=colors.HexColor('#2E7D32'), bold=True))
styles.add(ParagraphStyle(name='BodyJustify', fontSize=10, leading=13, spaceAfter=8, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='QuoteStyle', fontSize=10, leading=13, spaceAfter=8, 
                         alignment=TA_CENTER, italic=True, textColor=colors.HexColor('#37474F')))
styles.add(ParagraphStyle(name='HeaderCell', fontSize=7.5, leading=9, bold=True, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='PhaseHeader', fontSize=14, leading=18, spaceAfter=10,
                         textColor=colors.HexColor('#D32F2F'), bold=True))
styles.add(ParagraphStyle(name='BulletList', fontSize=9.5, leading=12, spaceAfter=4, leftIndent=15))

content = []

# ========== TITLE PAGE ==========
content.append(Paragraph("Programming Mastery: A Structured Path", styles['TitleCustom']))
content.append(Paragraph("72-Week Curriculum for Engineering Graduates", styles['SubtitleCustom']))
content.append(Spacer(1, 20))

content.append(Paragraph("🎯 Philosophy", styles['SectionHeader']))
content.append(Paragraph(
    "This curriculum is designed for engineering graduates with strong mathematical foundations but limited "
    "programming experience. Rather than rushing through topics, we prioritize <b>deep understanding</b> over "
    "broad coverage. Each concept builds naturally on previous knowledge, with time to practice and internalize "
    "before moving forward.",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

content.append(Paragraph("⏱️ Time Commitment", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Duration:</b> 72 weeks (approximately 18 months)<br/>"
    "<b>Schedule:</b> 3 days per week, 3-4 hours per session<br/>"
    "<b>Total Hours:</b> ~650-850 hours of focused study<br/>"
    "<b>Pace:</b> Designed to be sustainable alongside full-time work or other commitments",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

content.append(Paragraph("📚 Learning Approach", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Foundation First:</b> Master Python thoroughly (Months 1-4) before introducing other languages<br/>"
    "<b>Spiral Learning:</b> Revisit concepts with increasing depth as your understanding grows<br/>"
    "<b>Project-Based:</b> Build real projects that demonstrate understanding, not just toy examples<br/>"
    "<b>Theory + Practice:</b> Understand the 'why' behind algorithms, not just the 'how'<br/>"
    "<b>Spaced Repetition:</b> Regular review of previous topics to ensure retention",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

content.append(Paragraph("🛠️ What You'll Need", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Required:</b><br/>"
    "• A laptop (macOS, Linux, or Windows with WSL2)<br/>"
    "• VS Code or PyCharm Community Edition<br/>"
    "• GitHub account for version control<br/>"
    "• 10-20 GB free disk space<br/><br/>"
    "<b>Recommended:</b><br/>"
    "• Dual monitors or large display (makes coding much easier)<br/>"
    "• LeetCode Premium subscription (optional, for additional practice)<br/>"
    "• Notebook for sketching algorithms and taking notes",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== CORE TEXTS ==========
content.append(Paragraph("📖 Core Textbooks", styles['TitleCustom']))
content.append(Spacer(1, 12))

content.append(Paragraph(
    "These books are carefully selected to match your background as an engineering graduate. "
    "You'll start with accessible texts and gradually progress to more advanced material.",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

# Phase 1 books
content.append(Paragraph("Phase 1: Foundations (Weeks 1-24)", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Primary:</b><br/>"
    "• <i>Python Crash Course</i> by Eric Matthes (more beginner-friendly than Automate)<br/>"
    "• <i>Think Python</i> by Allen Downey (free, excellent for programmers)<br/>"
    "• <i>Grokking Algorithms</i> by Aditya Bhargava (visual, intuitive algorithm introduction)<br/><br/>"
    "<b>Reference:</b><br/>"
    "• Python official documentation (docs.python.org)<br/>"
    "• <i>Effective Python</i> by Brett Slatkin (learn Python idioms)",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Phase 2 books
content.append(Paragraph("Phase 2: Algorithms & Data Structures (Weeks 25-40)", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Primary:</b><br/>"
    "• <i>Introduction to Algorithms</i> (CLRS) - Selected chapters only, with guidance<br/>"
    "• <i>Algorithm Design Manual</i> by Skiena (more practical than CLRS)<br/>"
    "• <i>Problem Solving with Algorithms and Data Structures using Python</i> by Miller & Ranum (free)<br/><br/>"
    "<b>Practice:</b><br/>"
    "• <i>Elements of Programming Interviews in Python</i> by Aziz, Lee, and Prakash",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Phase 3 books
content.append(Paragraph("Phase 3: Systems Programming (Weeks 41-56)", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Primary:</b><br/>"
    "• <i>The C Programming Language</i> by Kernighan & Ritchie (K&R)<br/>"
    "• <i>Computer Systems: A Programmer's Perspective</i> (CSAPP) - Selected chapters<br/>"
    "• <i>Operating Systems: Three Easy Pieces</i> (OSTEP) - Free online, very readable<br/><br/>"
    "<b>Network Programming:</b><br/>"
    "• <i>Beej's Guide to Network Programming</i> (free online)",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Phase 4 books
content.append(Paragraph("Phase 4: Advanced Topics (Weeks 57-72)", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Specialization (Choose Your Path):</b><br/>"
    "• <i>Designing Data-Intensive Applications</i> by Kleppmann (backend/systems)<br/>"
    "• <i>Hands-On Machine Learning</i> by Géron (ML/AI)<br/>"
    "• <i>High Performance Python</i> by Gorelick (optimization)<br/>"
    "• <i>Flask Web Development</i> or <i>FastAPI</i> docs (web development)<br/><br/>"
    "<b>Theory (Optional but Valuable):</b><br/>"
    "• <i>Introduction to the Theory of Computation</i> by Sipser",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== CURRICULUM OVERVIEW ==========
content.append(Paragraph("📋 Curriculum Structure", styles['TitleCustom']))
content.append(Spacer(1, 12))

phases = [
    ("PHASE 1: PYTHON FOUNDATIONS (Weeks 1-24, 6 months)", [
        "Weeks 1-8: Python Basics - Syntax, data types, control flow, functions, basic I/O",
        "Weeks 9-12: Core Data Structures - Lists, dicts, sets, tuples; file handling",
        "Weeks 13-16: Object-Oriented Programming - Classes, inheritance, polymorphism",
        "Weeks 17-20: Intermediate Python - Exceptions, modules, testing, debugging",
        "Weeks 21-24: First Real Projects - CLI tools, data processing scripts, APIs",
        "",
        "<b>Key Milestone:</b> Build 3-5 substantial Python projects for your portfolio"
    ]),
    ("PHASE 2: ALGORITHMS & DATA STRUCTURES (Weeks 25-40, 4 months)", [
        "Weeks 25-28: Algorithm Analysis - Big-O, recursion, problem-solving strategies",
        "Weeks 29-32: Fundamental DS - Stacks, queues, linked lists, trees",
        "Weeks 33-36: Sorting & Searching - All major algorithms with complexity analysis",
        "Weeks 37-40: Graphs & Advanced DS - Graph algorithms, heaps, hash tables",
        "",
        "<b>Key Milestone:</b> Solve 75-100 LeetCode problems (Easy & Medium)"
    ]),
    ("PHASE 3: SYSTEMS PROGRAMMING (Weeks 41-56, 4 months)", [
        "Weeks 41-46: C Fundamentals - Types, pointers, memory, structs",
        "Weeks 47-50: Computer Systems - Memory hierarchy, processes, virtual memory",
        "Weeks 51-54: Operating Systems - Concurrency, file systems, I/O",
        "Weeks 55-56: Network Programming - Sockets, protocols, client-server",
        "",
        "<b>Key Milestone:</b> Build C programs demonstrating systems concepts"
    ]),
    ("PHASE 4: SPECIALIZATION & MASTERY (Weeks 57-72, 4 months)", [
        "Weeks 57-60: Dynamic Programming - Systematic approach to complex problems",
        "Weeks 61-64: Choose Your Path - Backend, ML, systems, or web development",
        "Weeks 65-68: Advanced Topics - Design patterns, architecture, performance",
        "Weeks 69-72: Capstone Project - Comprehensive project combining all skills",
        "",
        "<b>Key Milestone:</b> Portfolio-worthy capstone demonstrating mastery"
    ])
]

for phase_title, phase_items in phases:
    content.append(Paragraph(phase_title, styles['PhaseHeader']))
    for item in phase_items:
        if item:
            content.append(Paragraph(f"• {item}", styles['BulletList']))
    content.append(Spacer(1, 12))

content.append(PageBreak())

# ========== DETAILED WEEKLY BREAKDOWN ==========
content.append(Paragraph("📅 Detailed Week-by-Week Breakdown", styles['TitleCustom']))
content.append(Spacer(1, 12))

def create_week_table(week_num, week_title, days_data):
    """Create a table for a single week"""
    global day_counter
    
    # Header row
    table_data = [['Day', 'Topic', 'Reading', 'Practice Problems', 'Project']]
    
    for day_topic, reading, problems, project in days_data:
        table_data.append([
            str(day_counter),
            day_topic,
            reading,
            problems,
            project
        ])
        day_counter += 1
    
    table = Table(table_data, colWidths=[0.5*inch, 2*inch, 1.8*inch, 1.7*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1976D2')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8),
        ('FONTSIZE', (0,1), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('TOPPADDING', (0,1), (-1,-1), 6),
        ('BOTTOMPADDING', (0,1), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F5F5F5')])
    ]))
    
    return table

# ========== PHASE 1: PYTHON FOUNDATIONS ==========
content.append(Paragraph("■ PHASE 1: PYTHON FOUNDATIONS (Weeks 1-24)", styles['PhaseHeader']))
content.append(Spacer(1, 8))

# Week 1
content.append(Paragraph("Week 1: Python Basics - Getting Started", styles['WeekHeader']))
week1_days = [
    ("Setup & First Programs", "Python Crash Course Ch.1",
     "None - focus on setup", "Print patterns, simple calculator"),
    ("Variables & Data Types", "Python Crash Course Ch.2",
     "Complete setup exercises", "Temperature converter with validation"),
    ("Control Flow: if/else", "Python Crash Course Ch.3",
     "Basic type exercises", "Rock-paper-scissors game")
]
content.append(create_week_table(1, "Python Basics", week1_days))
content.append(Spacer(1, 10))

# Week 2
content.append(Paragraph("Week 2: Loops and Problem Solving", styles['WeekHeader']))
week2_days = [
    ("While & For Loops", "Python Crash Course Ch.4",
     "Loop exercises", "Number guessing game with hints"),
    ("Loop Patterns & Nested Loops", "Think Python Ch.7",
     "Pattern printing", "Multiplication table generator"),
    ("Lists Introduction", "Python Crash Course Ch.5",
     "LC: Two Sum (with hints)", "Todo list (basic version)")
]
content.append(create_week_table(2, "Loops", week2_days))
content.append(Spacer(1, 10))

# Week 3
content.append(Paragraph("Week 3: Lists and Collections", styles['WeekHeader']))
week3_days = [
    ("List Operations & Methods", "Python Crash Course Ch.5",
     "List manipulation", "Contact manager (list-based)"),
    ("List Comprehensions", "Effective Python Item 27-30",
     "LC: Remove Duplicates", "Data filtering tool"),
    ("Tuples & List vs Tuple", "Think Python Ch.12",
     "LC: Valid Palindrome", "Coordinate geometry calculator")
]
content.append(create_week_table(3, "Lists", week3_days))
content.append(Spacer(1, 10))

# Week 4
content.append(Paragraph("Week 4: Functions - Building Blocks", styles['WeekHeader']))
week4_days = [
    ("Function Basics", "Python Crash Course Ch.6",
     "Function exercises", "Math library (GCD, primes, factorial)"),
    ("Parameters & Returns", "Think Python Ch.3, 6",
     "LC: Fizz Buzz", "String utility library"),
    ("Scope & Documentation", "Python docs: Functions",
     "LC: Reverse Integer", "Unit converter with docstrings")
]
content.append(create_week_table(4, "Functions", week4_days))
content.append(Spacer(1, 10))

# Week 5
content.append(Paragraph("Week 5: Dictionaries - Key-Value Magic", styles['WeekHeader']))
week5_days = [
    ("Dictionary Basics", "Python Crash Course Ch.7",
     "Dict manipulation", "Word frequency counter"),
    ("Dict Methods & Patterns", "Effective Python Item 16-18",
     "LC: Contains Duplicate", "English-Spanish translator"),
    ("Sets & When to Use Them", "Think Python Ch.19",
     "LC: Single Number", "Remove duplicates from large file")
]
content.append(create_week_table(5, "Dictionaries", week5_days))
content.append(Spacer(1, 10))

# Week 6
content.append(Paragraph("Week 6: Strings - Text Processing", styles['WeekHeader']))
week6_days = [
    ("String Methods", "Python Crash Course Ch.8",
     "String exercises", "Text formatter (line wrapping, case)"),
    ("String Formatting", "Effective Python Item 4",
     "LC: Valid Anagram", "CSV generator from data"),
    ("Regular Expressions Intro", "Python docs: re module",
     "LC: Implement strStr()", "Email validator")
]
content.append(create_week_table(6, "Strings", week6_days))
content.append(Spacer(1, 10))

# Week 7
content.append(Paragraph("Week 7: File I/O - Working with Data", styles['WeekHeader']))
week7_days = [
    ("Reading Files", "Python Crash Course Ch.9",
     "File reading exercises", "Log file analyzer"),
    ("Writing Files", "Think Python Ch.14",
     "File writing exercises", "Markdown to HTML converter"),
    ("File Paths & JSON", "Python docs: pathlib, json",
     "LC: Valid Parentheses", "Configuration file manager")
]
content.append(create_week_table(7, "File I/O", week7_days))
content.append(Spacer(1, 10))

# Week 8
content.append(Paragraph("Week 8: Review & First Real Project", styles['WeekHeader']))
week8_days = [
    ("Review Week - Solidify Basics", "Review previous chapters",
     "Mixed LC Easy problems", "Refactor previous projects"),
    ("Project Planning", "None - plan project",
     "Continue LC practice", "Design expense tracker app"),
    ("Project Day 1", "None",
     "Debug previous solutions", "Build expense tracker (CLI)")
]
content.append(create_week_table(8, "Review", week8_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 9
content.append(Paragraph("Week 9: Exception Handling", styles['WeekHeader']))
week9_days = [
    ("Try-Except Basics", "Python Crash Course Ch.10",
     "Exception exercises", "Robust file reader"),
    ("Custom Exceptions", "Effective Python Item 81-82",
     "LC: Min Stack", "Input validator library"),
    ("Context Managers", "Python docs: contextlib",
     "LC: Valid Parentheses II", "Resource manager (with/as)")
]
content.append(create_week_table(9, "Exceptions", week9_days))
content.append(Spacer(1, 10))

# Week 10
content.append(Paragraph("Week 10: Debugging & Testing", styles['WeekHeader']))
week10_days = [
    ("Debugging Techniques", "Python Crash Course Ch.11",
     "Debug buggy code", "Debug mystery programs"),
    ("Unit Testing Intro", "Python docs: unittest",
     "Write tests for previous code", "Test-driven calculator"),
    ("pytest Basics", "pytest documentation",
     "LC: Add Two Numbers", "Build & test string library")
]
content.append(create_week_table(10, "Testing", week10_days))
content.append(Spacer(1, 10))

# Week 11
content.append(Paragraph("Week 11: Modules & Packages", styles['WeekHeader']))
week11_days = [
    ("Import System", "Python Crash Course Ch.12",
     "Module exercises", "Multi-file project structure"),
    ("Creating Packages", "Python packaging guide",
     "LC: Palindrome Number", "Installable utility package"),
    ("Virtual Environments", "venv documentation",
     "Setup project envs", "Manage project dependencies")
]
content.append(create_week_table(11, "Modules", week11_days))
content.append(Spacer(1, 10))

# Week 12
content.append(Paragraph("Week 12: Command Line Tools", styles['WeekHeader']))
week12_days = [
    ("sys.argv & argparse", "Python docs: argparse",
     "CLI exercises", "Command-line calculator"),
    ("Environment Variables", "Python docs: os module",
     "LC: Reverse String", "Config-driven CLI tool"),
    ("Build Complete CLI App", "Real Python: CLI tutorial",
     "LC: Roman to Integer", "File organizer (by type/date)")
]
content.append(create_week_table(12, "CLI", week12_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 13: OOP Introduction
content.append(Paragraph("Week 13: Object-Oriented Programming - Classes", styles['WeekHeader']))
week13_days = [
    ("Class Basics", "Python Crash Course Ch.13",
     "Class exercises", "Create BankAccount class"),
    ("Methods & self", "Think Python Ch.15-16",
     "LC: Design HashSet", "Student class with grades"),
    ("__init__ & Attributes", "Effective Python Item 37-40",
     "LC: Design HashMap", "Playing card deck (Card class)")
]
content.append(create_week_table(13, "OOP Basics", week13_days))
content.append(Spacer(1, 10))

# Week 14
content.append(Paragraph("Week 14: OOP - Inheritance", styles['WeekHeader']))
week14_days = [
    ("Inheritance Basics", "Python Crash Course Ch.14",
     "Inheritance exercises", "Vehicle hierarchy"),
    ("Method Overriding", "Think Python Ch.17",
     "LC: Min Stack", "Shape classes (area/perimeter)"),
    ("super() & MRO", "Effective Python Item 40",
     "LC: Max Stack", "Employee management system")
]
content.append(create_week_table(14, "Inheritance", week14_days))
content.append(Spacer(1, 10))

# Week 15
content.append(Paragraph("Week 15: OOP - Polymorphism & Magic Methods", styles['WeekHeader']))
week15_days = [
    ("Polymorphism", "Python docs: Data model",
     "Polymorphism exercises", "Payment processor (multiple types)"),
    ("Magic Methods (__str__, __repr__)", "Effective Python Item 75-77",
     "LC: Range Sum Query", "Custom fraction class"),
    ("__eq__, __lt__, __add__", "Python data model docs",
     "LC: Compare Version Numbers", "Money class with operators")
]
content.append(create_week_table(15, "Polymorphism", week15_days))
content.append(Spacer(1, 10))

# Week 16
content.append(Paragraph("Week 16: OOP - Design Principles", styles['WeekHeader']))
week16_days = [
    ("Encapsulation & Properties", "Effective Python Item 44-46",
     "Property exercises", "Temperature class (auto-convert)"),
    ("Composition over Inheritance", "Python patterns",
     "LC: LRU Cache", "Library system (Book, Member)"),
    ("Abstract Base Classes", "Python docs: abc module",
     "LC: Design Browser History", "Plugin system with ABC")
]
content.append(create_week_table(16, "Design", week16_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 17
content.append(Paragraph("Week 17: Iterators & Generators", styles['WeekHeader']))
week17_days = [
    ("Iterator Protocol", "Python docs: Iterator types",
     "Iterator exercises", "Custom range() implementation"),
    ("Generators & yield", "Effective Python Item 30-32",
     "LC: Generate Parentheses", "Fibonacci generator (infinite)"),
    ("Generator Expressions", "Think Python Ch.19",
     "LC: Letter Combinations", "File line generator (lazy)")
]
content.append(create_week_table(17, "Iterators", week17_days))
content.append(Spacer(1, 10))

# Week 18
content.append(Paragraph("Week 18: Functional Programming", styles['WeekHeader']))
week18_days = [
    ("map, filter, reduce", "Python docs: functools",
     "Functional exercises", "Data pipeline with functions"),
    ("Lambda Functions", "Effective Python Item 19",
     "LC: Sort Characters", "Custom sort implementations"),
    ("Decorators Intro", "Python docs: Decorators",
     "LC: Valid Sudoku", "Timing decorator")
]
content.append(create_week_table(18, "Functional", week18_days))
content.append(Spacer(1, 10))

# Week 19
content.append(Paragraph("Week 19: Advanced Decorators", styles['WeekHeader']))
week19_days = [
    ("Decorator Patterns", "Effective Python Item 26",
     "Decorator exercises", "Caching decorator"),
    ("functools & wraps", "Python functools docs",
     "LC: LRU Cache implementation", "Retry decorator with backoff"),
    ("Class Decorators", "Advanced Python",
     "LC: Design Hit Counter", "Rate limiter decorator")
]
content.append(create_week_table(19, "Decorators", week19_days))
content.append(Spacer(1, 10))

# Week 20
content.append(Paragraph("Week 20: Data Processing with Python", styles['WeekHeader']))
week20_days = [
    ("Working with CSV", "Python docs: csv module",
     "CSV exercises", "Sales data analyzer"),
    ("JSON Processing", "Python docs: json module",
     "LC: Serialize/Deserialize BST", "API response processor"),
    ("Data Cleaning Techniques", "Real Python: Data cleaning",
     "LC: String to Integer (atoi)", "Clean messy dataset")
]
content.append(create_week_table(20, "Data Processing", week20_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 21-24: Projects
content.append(Paragraph("Week 21: Real-World Project 1 - Web Scraper", styles['WeekHeader']))
week21_days = [
    ("HTTP Basics & requests", "requests documentation",
     "HTTP exercises", "Fetch and parse web pages"),
    ("HTML Parsing (BeautifulSoup)", "BeautifulSoup docs",
     "Parsing exercises", "Extract structured data"),
    ("Build Complete Scraper", "Scraping best practices",
     "LC: Design Web Crawler", "News headline aggregator")
]
content.append(create_week_table(21, "Project", week21_days))
content.append(Spacer(1, 10))

content.append(Paragraph("Week 22: Real-World Project 2 - REST API Client", styles['WeekHeader']))
week22_days = [
    ("REST API Concepts", "REST API tutorial",
     "API exercises", "Weather API client"),
    ("Authentication & Headers", "requests auth docs",
     "LC: Design Rate Limiter", "GitHub API explorer"),
    ("Error Handling & Retry", "requests retry patterns",
     "LC: Design Logger", "Robust API wrapper library")
]
content.append(create_week_table(22, "Project", week22_days))
content.append(Spacer(1, 10))

content.append(Paragraph("Week 23: Real-World Project 3 - Data Dashboard", styles['WeekHeader']))
week23_days = [
    ("matplotlib Basics", "matplotlib tutorial",
     "Plotting exercises", "Visualize CSV data"),
    ("Data Analysis Intro", "pandas basics",
     "LC: Valid Parenthesis String", "Stock price analyzer"),
    ("Complete Dashboard", "Dashboard tutorial",
     "LC: Basic Calculator", "Personal finance dashboard")
]
content.append(create_week_table(23, "Project", week23_days))
content.append(Spacer(1, 10))

content.append(Paragraph("Week 24: Portfolio Review & Phase 1 Wrap-up", styles['WeekHeader']))
week24_days = [
    ("Code Review & Refactoring", "Clean Code principles",
     "Refactor old projects", "Polish portfolio projects"),
    ("Documentation & README", "README best practices",
     "LC: String Compression", "Write comprehensive docs"),
    ("Git & GitHub Mastery", "Git tutorial advanced",
     "LC: Design File System", "Setup portfolio repository")
]
content.append(create_week_table(24, "Review", week24_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 2: ALGORITHMS ==========
content.append(Paragraph("■ PHASE 2: ALGORITHMS & DATA STRUCTURES (Weeks 25-40)", styles['PhaseHeader']))
content.append(Spacer(1, 8))

# Week 25
content.append(Paragraph("Week 25: Algorithm Analysis - Big O Notation", styles['WeekHeader']))
week25_days = [
    ("Time Complexity Intro", "Grokking Algorithms Ch.1",
     "Calculate Big-O exercises", "Benchmark sorting algorithms"),
    ("Space Complexity", "CLRS Ch.2 (intro only)",
     "LC: Two Sum analysis", "Memory profiler for algorithms"),
    ("Best/Worst/Average Case", "Algorithm Design Manual Ch.2",
     "LC: Binary Search", "Compare algorithm performance")
]
content.append(create_week_table(25, "Analysis", week25_days))
content.append(Spacer(1, 10))

# Week 26
content.append(Paragraph("Week 26: Recursion - The Foundation", styles['WeekHeader']))
week26_days = [
    ("Recursion Basics", "Grokking Algorithms Ch.3",
     "Recursion exercises", "Factorial & Fibonacci variants"),
    ("Recursion Patterns", "Think Python Ch.5-6 review",
     "LC: Climbing Stairs", "Tower of Hanoi solver"),
    ("Recursion vs Iteration", "Algorithm Design Manual",
     "LC: Pow(x, n)", "Visualize recursion tree")
]
content.append(create_week_table(26, "Recursion", week26_days))
content.append(Spacer(1, 10))

# Week 27
content.append(Paragraph("Week 27: Sorting Algorithms - Comparison Based", styles['WeekHeader']))
week27_days = [
    ("Bubble, Insertion, Selection", "Grokking Algorithms Ch.2",
     "Implement 3 sorts", "Sorting visualizer"),
    ("Merge Sort", "CLRS Ch.2.3",
     "LC: Merge Sorted Array", "Merge sort with analysis"),
    ("Quick Sort", "Grokking Algorithms Ch.4",
     "LC: Sort Colors", "Quicksort with pivoting")
]
content.append(create_week_table(27, "Sorting", week27_days))
content.append(Spacer(1, 10))

# Week 28
content.append(Paragraph("Week 28: Sorting - Advanced & Analysis", styles['WeekHeader']))
week28_days = [
    ("Heap Sort", "CLRS Ch.6",
     "LC: Kth Largest Element", "Heapsort implementation"),
    ("Counting & Radix Sort", "CLRS Ch.8",
     "LC: Sort Array", "Sort large integer dataset"),
    ("Stability & When to Use Each", "Algorithm Design Manual",
     "LC: Custom Sort String", "Sorting algorithm chooser")
]
content.append(create_week_table(28, "Advanced Sorting", week28_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 29
content.append(Paragraph("Week 29: Binary Search - Mastery", styles['WeekHeader']))
week29_days = [
    ("Binary Search Foundation", "Grokking Algorithms Ch.1",
     "LC: Binary Search", "Generic binary search template"),
    ("Search Variants", "Elements of Programming",
     "LC: Search Insert Position", "Find first/last occurrence"),
    ("Binary Search on Answer", "Competitive Programming",
     "LC: Find Peak Element", "Square root via binary search")
]
content.append(create_week_table(29, "Binary Search", week29_days))
content.append(Spacer(1, 10))

# Week 30
content.append(Paragraph("Week 30: Two Pointers Technique", styles['WeekHeader']))
week30_days = [
    ("Two Pointer Basics", "Elements of Programming",
     "LC: Two Sum II", "Remove duplicates patterns"),
    ("Fast & Slow Pointers", "Competitive Programming",
     "LC: Linked List Cycle", "Find middle element"),
    ("Sliding Window Intro", "Elements of Programming",
     "LC: Container With Most Water", "Maximum sum subarray")
]
content.append(create_week_table(30, "Two Pointers", week30_days))
content.append(Spacer(1, 10))

# Week 31
content.append(Paragraph("Week 31: Linked Lists", styles['WeekHeader']))
week31_days = [
    ("Linked List Basics", "CLRS Ch.10.2",
     "LC: Reverse Linked List", "Singly linked list from scratch"),
    ("Linked List Problems", "Elements of Programming",
     "LC: Remove Nth Node", "Doubly linked list"),
    ("Advanced LL Patterns", "Competitive Programming",
     "LC: Merge Two Sorted Lists", "Detect cycle & find start")
]
content.append(create_week_table(31, "Linked Lists", week31_days))
content.append(Spacer(1, 10))

# Week 32
content.append(Paragraph("Week 32: Stacks & Queues", styles['WeekHeader']))
week32_days = [
    ("Stack Implementation", "CLRS Ch.10.1",
     "LC: Valid Parentheses", "Stack from scratch (array/LL)"),
    ("Queue Implementation", "CLRS Ch.10.1",
     "LC: Implement Queue using Stacks", "Circular queue"),
    ("Stack/Queue Applications", "Elements of Programming",
     "LC: Min Stack", "Expression evaluator")
]
content.append(create_week_table(32, "Stacks & Queues", week32_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 33
content.append(Paragraph("Week 33: Trees - Binary Trees", styles['WeekHeader']))
week33_days = [
    ("Tree Terminology & Traversals", "CLRS Ch.12.1",
     "LC: Max Depth of Binary Tree", "Binary tree from scratch"),
    ("Recursive Tree Problems", "Elements of Programming",
     "LC: Invert Binary Tree", "Preorder/Inorder/Postorder"),
    ("Level Order Traversal", "CLRS Ch.12.1",
     "LC: Binary Tree Level Order", "BFS on tree")
]
content.append(create_week_table(33, "Binary Trees", week33_days))
content.append(Spacer(1, 10))

# Week 34
content.append(Paragraph("Week 34: Binary Search Trees", styles['WeekHeader']))
week34_days = [
    ("BST Properties", "CLRS Ch.12.1-12.2",
     "LC: Validate BST", "BST insert/search/delete"),
    ("BST Operations", "CLRS Ch.12.3",
     "LC: Kth Smallest in BST", "BST successor/predecessor"),
    ("Balanced BSTs Intro", "CLRS Ch.13 intro",
     "LC: Delete Node in BST", "AVL tree (brief intro)")
]
content.append(create_week_table(34, "BST", week34_days))
content.append(Spacer(1, 10))

# Week 35
content.append(Paragraph("Week 35: Hash Tables Deep Dive", styles['WeekHeader']))
week35_days = [
    ("Hash Function Design", "CLRS Ch.11",
     "LC: Design HashSet", "Hash table from scratch"),
    ("Collision Resolution", "CLRS Ch.11.2-11.3",
     "LC: Design HashMap", "Chaining vs open addressing"),
    ("Hash Table Applications", "Elements of Programming",
     "LC: Group Anagrams", "Frequency counter, cache")
]
content.append(create_week_table(35, "Hash Tables", week35_days))
content.append(Spacer(1, 10))

# Week 36
content.append(Paragraph("Week 36: Heaps & Priority Queues", styles['WeekHeader']))
week36_days = [
    ("Heap Properties", "CLRS Ch.6",
     "LC: Kth Largest Element", "Min heap from scratch"),
    ("Heap Operations", "CLRS Ch.6",
     "LC: Top K Frequent Elements", "Max heap & heapify"),
    ("Priority Queue Applications", "Elements of Programming",
     "LC: Merge K Sorted Lists", "Task scheduler with PQ")
]
content.append(create_week_table(36, "Heaps", week36_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 37
content.append(Paragraph("Week 37: Graph Fundamentals", styles['WeekHeader']))
week37_days = [
    ("Graph Representations", "CLRS Ch.22.1",
     "LC: Find Center of Star Graph", "Adjacency list & matrix"),
    ("Graph Traversal - BFS", "CLRS Ch.22.2",
     "LC: Number of Islands", "BFS implementation"),
    ("Graph Traversal - DFS", "CLRS Ch.22.3",
     "LC: Clone Graph", "DFS iterative & recursive")
]
content.append(create_week_table(37, "Graphs Intro", week37_days))
content.append(Spacer(1, 10))

# Week 38
content.append(Paragraph("Week 38: Graph Algorithms - Paths", styles['WeekHeader']))
week38_days = [
    ("Shortest Path - Dijkstra", "CLRS Ch.24.3",
     "LC: Network Delay Time", "Dijkstra with priority queue"),
    ("Bellman-Ford Algorithm", "CLRS Ch.24.1",
     "LC: Cheapest Flights K Stops", "Negative cycle detection"),
    ("All-Pairs Shortest Path", "CLRS Ch.25",
     "LC: Find the City", "Floyd-Warshall algorithm")
]
content.append(create_week_table(38, "Graph Paths", week38_days))
content.append(Spacer(1, 10))

# Week 39
content.append(Paragraph("Week 39: Graph Algorithms - Trees", styles['WeekHeader']))
week39_days = [
    ("Minimum Spanning Tree - Kruskal", "CLRS Ch.23",
     "LC: Min Cost to Connect Points", "Union-Find + Kruskal"),
    ("MST - Prim's Algorithm", "CLRS Ch.23.2",
     "LC: Min Cost to Connect Cities", "Prim with heap"),
    ("Topological Sort", "CLRS Ch.22.4",
     "LC: Course Schedule II", "Topo sort (DFS & BFS)")
]
content.append(create_week_table(39, "Graph Trees", week39_days))
content.append(Spacer(1, 10))

# Week 40
content.append(Paragraph("Week 40: Algorithm Techniques Review", styles['WeekHeader']))
week40_days = [
    ("Greedy Algorithms", "CLRS Ch.16",
     "LC: Jump Game", "Activity selection problem"),
    ("Divide & Conquer", "CLRS Ch.4",
     "LC: Majority Element", "Master theorem practice"),
    ("Phase 2 Review & Portfolio", "Review all topics",
     "LC: Mixed medium problems", "Algorithm visualization tool")
]
content.append(create_week_table(40, "Review", week40_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 3: SYSTEMS PROGRAMMING ==========
content.append(Paragraph("■ PHASE 3: SYSTEMS PROGRAMMING WITH C (Weeks 41-56)", styles['PhaseHeader']))
content.append(Spacer(1, 8))

content.append(Paragraph(
    "<b>Note:</b> This phase introduces C programming and systems concepts. "
    "The pace is deliberately slower to allow mastery of low-level concepts. "
    "You'll understand how computers actually work at a deeper level.",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Week 41
content.append(Paragraph("Week 41: C Fundamentals", styles['WeekHeader']))
week41_days = [
    ("C Setup & Hello World", "K&R Ch.1",
     "Compile & run C programs", "Hello World with arguments"),
    ("Variables & Types in C", "K&R Ch.2",
     "Type exercises", "sizeof() demonstration"),
    ("Operators & Control Flow", "K&R Ch.3",
     "LC: Factorial (in C)", "Temperature converter in C")
]
content.append(create_week_table(41, "C Intro", week41_days))
content.append(Spacer(1, 10))

# Week 42
content.append(Paragraph("Week 42: Arrays & Strings in C", styles['WeekHeader']))
week42_days = [
    ("Arrays in C", "K&R Ch.5.1-5.5",
     "Array exercises", "Array sum/average/max"),
    ("C Strings", "K&R Ch.5.5",
     "LC: Reverse String (in C)", "String library: strlen, strcpy"),
    ("Command Line Arguments", "K&R Ch.5.10",
     "LC: Valid Anagram (in C)", "CLI calculator in C")
]
content.append(create_week_table(42, "Arrays", week42_days))
content.append(Spacer(1, 10))

# Week 43
content.append(Paragraph("Week 43: Pointers - The Power of C", styles['WeekHeader']))
week43_days = [
    ("Pointer Basics", "K&R Ch.5.1",
     "Pointer exercises", "Swap function via pointers"),
    ("Pointer Arithmetic", "K&R Ch.5.3",
     "Pointer arithmetic drills", "Array traversal with pointers"),
    ("Pointers & Arrays", "K&R Ch.5.4",
     "LC: Reverse Array (in C)", "Generic swap function")
]
content.append(create_week_table(43, "Pointers", week43_days))
content.append(Spacer(1, 10))

# Week 44
content.append(Paragraph("Week 44: Dynamic Memory", styles['WeekHeader']))
week44_days = [
    ("malloc & free", "K&R Ch.7.8.5",
     "Memory allocation exercises", "Dynamic array implementation"),
    ("Memory Leaks & Valgrind", "Valgrind quickstart",
     "LC: Merge Sorted Array (C)", "Fix leaky programs"),
    ("calloc, realloc", "K&R Ch.7.8.5",
     "Memory exercises", "Resizable array (like vector)")
]
content.append(create_week_table(44, "Memory", week44_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 45
content.append(Paragraph("Week 45: Structs & Function Pointers", styles['WeekHeader']))
week45_days = [
    ("Structures in C", "K&R Ch.6",
     "Struct exercises", "Student database with structs"),
    ("typedef & Nested Structs", "K&R Ch.6",
     "LC: Intersection of Arrays", "Linked list node struct"),
    ("Function Pointers", "K&R Ch.5.11",
     "Function pointer exercises", "Generic sort with comparator")
]
content.append(create_week_table(45, "Structs", week45_days))
content.append(Spacer(1, 10))

# Week 46
content.append(Paragraph("Week 46: Data Structures in C", styles['WeekHeader']))
week46_days = [
    ("Linked List in C", "CLRS Ch.10.2",
     "LC: Reverse Linked List (C)", "Singly linked list library"),
    ("Stack & Queue in C", "CLRS Ch.10.1",
     "LC: Valid Parentheses (C)", "Stack & queue implementations"),
    ("Binary Tree in C", "CLRS Ch.12",
     "LC: Max Depth (C)", "Binary tree with malloc")
]
content.append(create_week_table(46, "DS in C", week46_days))
content.append(Spacer(1, 10))

# Week 47
content.append(Paragraph("Week 47: Computer Systems - Memory Hierarchy", styles['WeekHeader']))
week47_days = [
    ("Memory Hierarchy", "CSAPP Ch.6.1-6.2",
     "Memory quiz", "Cache behavior demo"),
    ("Cache Principles", "CSAPP Ch.6.3-6.4",
     "Cache exercises", "Matrix multiply (cache-friendly)"),
    ("Cache Optimization", "CSAPP Ch.6.6",
     "Performance exercises", "Compare blocked vs naive")
]
content.append(create_week_table(47, "Memory Hierarchy", week47_days))
content.append(Spacer(1, 10))

# Week 48
content.append(Paragraph("Week 48: Processes & Virtual Memory", styles['WeekHeader']))
week48_days = [
    ("Process Concepts", "OSTEP Ch.4-6",
     "Process exercises", "Visualize process state machine"),
    ("Virtual Memory Intro", "CSAPP Ch.9.1-9.3",
     "VM exercises", "Address translation simulator"),
    ("Page Tables", "OSTEP Ch.18-20",
     "Page table exercises", "Simple page table simulation")
]
content.append(create_week_table(48, "Processes", week48_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 49
content.append(Paragraph("Week 49: System Calls", styles['WeekHeader']))
week49_days = [
    ("System Call Interface", "OSTEP Ch.5",
     "System call exercises", "Strace exploration"),
    ("Process Creation - fork", "OSTEP Ch.5",
     "Fork exercises", "Parent-child communication"),
    ("Process Control - exec", "Beej §5",
     "Fork+exec exercises", "Simple shell (commands only)")
]
content.append(create_week_table(49, "System Calls", week49_days))
content.append(Spacer(1, 10))

# Week 50
content.append(Paragraph("Week 50: Inter-Process Communication", styles['WeekHeader']))
week50_days = [
    ("Pipes", "Beej §7",
     "Pipe exercises", "Parent-child via pipe"),
    ("Signals", "OSTEP Ch.26",
     "Signal handling exercises", "Signal handler demo"),
    ("Shared Memory Intro", "OSTEP Ch.29",
     "IPC exercises", "Producer-consumer with pipes")
]
content.append(create_week_table(50, "IPC", week50_days))
content.append(Spacer(1, 10))

# Week 51
content.append(Paragraph("Week 51: Concurrency - Threads", styles['WeekHeader']))
week51_days = [
    ("Thread Basics", "OSTEP Ch.26",
     "Thread exercises", "Create & join threads"),
    ("Thread Arguments & Returns", "OSTEP Ch.27",
     "Threading exercises", "Parallel sum"),
    ("Race Conditions", "OSTEP Ch.28",
     "Race condition demos", "Demonstrate data races")
]
content.append(create_week_table(51, "Threads", week51_days))
content.append(Spacer(1, 10))

# Week 52
content.append(Paragraph("Week 52: Synchronization", styles['WeekHeader']))
week52_days = [
    ("Mutexes", "OSTEP Ch.28",
     "Mutex exercises", "Thread-safe counter"),
    ("Condition Variables", "OSTEP Ch.30",
     "Condition var exercises", "Producer-consumer problem"),
    ("Deadlock", "OSTEP Ch.32",
     "Deadlock exercises", "Dining philosophers")
]
content.append(create_week_table(52, "Sync", week52_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 53
content.append(Paragraph("Week 53: Network Programming - Sockets", styles['WeekHeader']))
week53_days = [
    ("Socket Basics", "Beej §8-10",
     "Socket exercises", "TCP echo client"),
    ("Client-Server Model", "Beej §11",
     "LC: Design Hit Counter", "Echo server"),
    ("Multi-Client Server", "Beej §12",
     "Server exercises", "Chat server (multi-threaded)")
]
content.append(create_week_table(53, "Sockets", week53_days))
content.append(Spacer(1, 10))

# Week 54
content.append(Paragraph("Week 54: File Systems", styles['WeekHeader']))
week54_days = [
    ("File System Interface", "OSTEP Ch.39",
     "FS exercises", "File operations (open/read/write)"),
    ("File System Implementation", "OSTEP Ch.40",
     "Inode exercises", "Understand inodes"),
    ("Directories & Links", "OSTEP Ch.41",
     "Directory exercises", "Recursive directory walker")
]
content.append(create_week_table(54, "File Systems", week54_days))
content.append(Spacer(1, 10))

# Week 55
content.append(Paragraph("Week 55: Build Systems & Debugging", styles['WeekHeader']))
week55_days = [
    ("Makefiles", "GNU Make Manual Ch.1-2",
     "Makefile exercises", "Multi-file C project"),
    ("GDB Debugging", "GDB tutorial",
     "Debug buggy C programs", "Use breakpoints & watches"),
    ("Valgrind Mastery", "Valgrind manual",
     "Fix memory leaks", "Clean all memory errors")
]
content.append(create_week_table(55, "Tools", week55_days))
content.append(Spacer(1, 10))

# Week 56
content.append(Paragraph("Week 56: C Project & Phase 3 Review", styles['WeekHeader']))
week56_days = [
    ("Project Planning", "Review C concepts",
     "Design project", "Plan HTTP server in C"),
    ("Project Implementation", "N/A",
     "Code project", "Build simple HTTP server"),
    ("Project Polish & Review", "N/A",
     "Finalize project", "Complete documentation")
]
content.append(create_week_table(56, "Project", week56_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 4: ADVANCED & SPECIALIZATION ==========
content.append(Paragraph("■ PHASE 4: ADVANCED TOPICS & SPECIALIZATION (Weeks 57-72)", styles['PhaseHeader']))
content.append(Spacer(1, 8))

content.append(Paragraph(
    "<b>Customization Note:</b> This phase allows you to choose a specialization path. "
    "The weekly breakdown below shows one possible path (Backend/Systems focus). "
    "You can substitute weeks based on your interests: ML/AI, Web Development, "
    "Performance Engineering, or continue deepening algorithms.",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Week 57
content.append(Paragraph("Week 57: Dynamic Programming - Foundation", styles['WeekHeader']))
week57_days = [
    ("DP Introduction & Memoization", "CLRS Ch.15.1",
     "LC: Fibonacci DP", "Memoization vs tabulation"),
    ("1D DP Problems", "CLRS Ch.15.3",
     "LC: Climbing Stairs", "Solve 5 classic 1D DP"),
    ("DP Problem Recognition", "Elements of Programming",
     "LC: House Robber", "Identify DP characteristics")
]
content.append(create_week_table(57, "DP Intro", week57_days))
content.append(Spacer(1, 10))

# Week 58
content.append(Paragraph("Week 58: Dynamic Programming - 2D", styles['WeekHeader']))
week58_days = [
    ("Grid DP", "CLRS Ch.15.4",
     "LC: Unique Paths", "All paths in grid"),
    ("String DP", "CLRS Ch.15",
     "LC: Longest Common Subsequence", "Edit distance"),
    ("Knapsack Problem", "CLRS Ch.15.3",
     "LC: Partition Equal Subset", "0/1 knapsack variations")
]
content.append(create_week_table(58, "DP 2D", week58_days))
content.append(Spacer(1, 10))

# Week 59
content.append(Paragraph("Week 59: Dynamic Programming - Advanced", styles['WeekHeader']))
week59_days = [
    ("State Machine DP", "Competitive Programming",
     "LC: Buy/Sell Stock variations", "State diagram approach"),
    ("DP Optimization", "CLRS Ch.15",
     "LC: Coin Change", "Space optimization tricks"),
    ("DP Practice Marathon", "Elements of Programming",
     "LC: 10 DP problems", "Master DP thinking")
]
content.append(create_week_table(59, "DP Advanced", week59_days))
content.append(Spacer(1, 10))

# Week 60
content.append(Paragraph("Week 60: Backtracking & Branch-and-Bound", styles['WeekHeader']))
week60_days = [
    ("Backtracking Pattern", "CLRS supplement",
     "LC: Permutations", "Generate all combinations"),
    ("Constraint Satisfaction", "Algorithm Design",
     "LC: N-Queens", "Sudoku solver"),
    ("Branch and Bound", "CLRS Ch.35",
     "LC: Subsets II", "Traveling salesman (small)")
]
content.append(create_week_table(60, "Backtracking", week60_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 61-64: Specialization (Example: Backend/Systems)
content.append(Paragraph("Weeks 61-64: SPECIALIZATION PATH (Choose Yours)", styles['WeekHeader']))
content.append(Spacer(1, 8))
content.append(Paragraph("<b>Path A: Backend Development</b>", styles['SectionHeader']))

week61_days = [
    ("Web Framework (Flask/FastAPI)", "Flask/FastAPI docs",
     "API exercises", "REST API with CRUD"),
    ("Database Basics (SQL)", "SQL tutorial",
     "SQL exercises", "SQLite database operations"),
    ("ORM & Migrations", "SQLAlchemy docs",
     "Database design", "Blog API with database")
]
content.append(create_week_table(61, "Backend 1", week61_days))
content.append(Spacer(1, 10))

week62_days = [
    ("Authentication & Security", "OWASP basics",
     "Auth exercises", "JWT authentication"),
    ("API Design Best Practices", "REST API design",
     "Design exercises", "Versioned API"),
    ("Testing APIs", "pytest docs",
     "API test suite", "Integration tests")
]
content.append(create_week_table(62, "Backend 2", week62_days))
content.append(Spacer(1, 10))

week63_days = [
    ("Caching Strategies", "Redis basics",
     "Caching exercises", "API with Redis cache"),
    ("Message Queues", "RabbitMQ/Celery tutorial",
     "Queue exercises", "Async task processing"),
    ("Microservices Intro", "Microservices primer",
     "Service design", "Split monolith into services")
]
content.append(create_week_table(63, "Backend 3", week63_days))
content.append(Spacer(1, 10))

week64_days = [
    ("Docker Basics", "Docker tutorial",
     "Containerization", "Dockerize Python app"),
    ("CI/CD Pipeline", "GitHub Actions",
     "Pipeline setup", "Automated testing"),
    ("Deployment", "Deployment guide",
     "Deploy exercises", "Deploy to cloud platform")
]
content.append(create_week_table(64, "Backend 4", week64_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Alternative specialization mentions
content.append(Paragraph("<b>Alternative Specialization Paths:</b>", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Path B: Machine Learning</b><br/>"
    "• Week 61: NumPy & Pandas mastery<br/>"
    "• Week 62: scikit-learn fundamentals<br/>"
    "• Week 63: Neural networks with PyTorch/TensorFlow<br/>"
    "• Week 64: ML project (classification/regression)<br/><br/>"
    
    "<b>Path C: Web Development</b><br/>"
    "• Week 61: HTML/CSS/JavaScript basics<br/>"
    "• Week 62: React fundamentals<br/>"
    "• Week 63: Full-stack app (React + Python)<br/>"
    "• Week 64: Deployment & production<br/><br/>"
    
    "<b>Path D: Systems & Performance</b><br/>"
    "• Week 61: Profiling & optimization<br/>"
    "• Week 62: Parallel programming (multiprocessing)<br/>"
    "• Week 63: SIMD & vectorization<br/>"
    "• Week 64: GPU programming intro (CUDA)<br/>",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

# Week 65-68: Advanced topics (universal)
content.append(Paragraph("Weeks 65-68: Advanced Software Engineering", styles['WeekHeader']))

week65_days = [
    ("Design Patterns - Creational", "Gang of Four Ch.3",
     "Pattern exercises", "Singleton, Factory, Builder"),
    ("Design Patterns - Structural", "Gang of Four Ch.4",
     "Pattern exercises", "Adapter, Decorator, Proxy"),
    ("Design Patterns - Behavioral", "Gang of Four Ch.5",
     "Pattern exercises", "Observer, Strategy, Command")
]
content.append(create_week_table(65, "Patterns", week65_days))
content.append(Spacer(1, 10))

week66_days = [
    ("System Design - Scalability", "System Design Primer",
     "Design exercises", "Design URL shortener"),
    ("System Design - Availability", "Designing Data-Intensive Apps",
     "Design exercises", "Design cache system"),
    ("System Design - Databases", "Database internals",
     "Design exercises", "Design rate limiter")
]
content.append(create_week_table(66, "System Design", week66_days))
content.append(Spacer(1, 10))

week67_days = [
    ("Code Quality & Refactoring", "Clean Code",
     "Refactoring exercises", "Refactor legacy code"),
    ("Code Review Skills", "Code review best practices",
     "Review exercises", "Review & improve code"),
    ("Documentation", "Documentation guide",
     "Doc exercises", "Write API documentation")
]
content.append(create_week_table(67, "Quality", week67_days))
content.append(Spacer(1, 10))

week68_days = [
    ("Git Advanced", "Git Pro book",
     "Git exercises", "Rebase, cherry-pick, bisect"),
    ("Open Source Contribution", "Contributing guide",
     "Find issue to fix", "Make first contribution"),
    ("Technical Writing", "Writing guide",
     "Blog post", "Write about what you learned")
]
content.append(create_week_table(68, "Skills", week68_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# Week 69-72: Capstone
content.append(Paragraph("Weeks 69-72: CAPSTONE PROJECT", styles['PhaseHeader']))
content.append(Spacer(1, 8))

content.append(Paragraph(
    "Your capstone project should be a substantial application that demonstrates mastery across multiple domains. "
    "It should combine algorithms, data structures, systems programming concepts (if applicable), "
    "and software engineering best practices. This is your portfolio centerpiece.",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Capstone Project Ideas:</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <b>Database System:</b> Build a simple relational database from scratch in C/Python<br/>"
    "• <b>Web Crawler & Search:</b> Distributed crawler with search engine (inverted index, ranking)<br/>"
    "• <b>Compiler/Interpreter:</b> Build interpreter for simple language (tokenizer, parser, evaluator)<br/>"
    "• <b>Distributed System:</b> Key-value store with replication and consistency guarantees<br/>"
    "• <b>ML Pipeline:</b> End-to-end ML system (data collection, training, serving, monitoring)<br/>"
    "• <b>Game Engine:</b> 2D game engine with physics, rendering, and scripting<br/>"
    "• <b>Operating System Kernel:</b> Minimal OS kernel (bootloader, memory management, processes)<br/>"
    "• <b>Network Protocol:</b> Implement TCP/IP stack or custom protocol<br/>",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

week69_days = [
    ("Project Planning & Design", "System design review",
     "Architecture design", "Write design document"),
    ("Setup & Foundation", "Best practices review",
     "Project scaffolding", "Setup repo, CI/CD, tests"),
    ("Core Feature 1", "N/A",
     "Implementation", "Build first major feature")
]
content.append(create_week_table(69, "Capstone Week 1", week69_days))
content.append(Spacer(1, 10))

week70_days = [
    ("Core Feature 2", "N/A",
     "Implementation", "Build second feature"),
    ("Core Feature 3", "N/A",
     "Implementation", "Integration work"),
    ("Testing & Debugging", "Testing best practices",
     "Write tests", "Achieve 80%+ coverage")
]
content.append(create_week_table(70, "Capstone Week 2", week70_days))
content.append(Spacer(1, 10))

week71_days = [
    ("Performance Optimization", "Profiling guide",
     "Profile & optimize", "Improve critical paths"),
    ("Documentation", "Doc standards",
     "Write docs", "README, API docs, architecture"),
    ("Polish & Edge Cases", "QA checklist",
     "Bug fixes", "Handle edge cases")
]
content.append(create_week_table(71, "Capstone Week 3", week71_days))
content.append(Spacer(1, 10))

week72_days = [
    ("Demo Preparation", "Presentation guide",
     "Prepare demo", "Create demo video"),
    ("Portfolio Update", "Portfolio best practices",
     "Update portfolio", "Showcase all projects"),
    ("Reflection & Next Steps", "Career planning",
     "Plan next steps", "Set goals for continued learning")
]
content.append(create_week_table(72, "Capstone Week 4", week72_days))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== FINAL PAGE: CONGRATULATIONS ==========
content.append(Paragraph("🎉 Congratulations on Completing Your Journey!", styles['TitleCustom']))
content.append(Spacer(1, 12))

content.append(Paragraph("🏆 What You've Accomplished", styles['SectionHeader']))

achievement_data = [
    ["✓", "216 learning sessions over 72 weeks"],
    ["✓", "Mastered Python from basics to advanced concepts"],
    ["✓", "Implemented all major data structures from scratch"],
    ["✓", "Solved 150+ algorithmic problems"],
    ["✓", "Learned C and systems programming fundamentals"],
    ["✓", "Built 30+ projects for your portfolio"],
    ["✓", "Completed a capstone project demonstrating mastery"],
    ["✓", "Developed problem-solving skills that will last a career"],
]

achievement_table = Table(achievement_data, colWidths=[0.5*inch, 7*inch])
achievement_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('ALIGN', (1,0), (1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('TEXTCOLOR', (0,0), (0,-1), colors.HexColor('#2E7D32')),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (0,-1), 14),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 8),
]))

content.append(achievement_table)
content.append(Spacer(1, 12))

content.append(Paragraph("🚀 Your Path Forward", styles['SectionHeader']))
content.append(Paragraph(
    "<b>1. Contribute to Open Source:</b> Find projects that interest you. Start with small contributions. "
    "Open source is how you join the global programmer community.<br/><br/>"
    
    "<b>2. Build in Public:</b> Share your learning journey. Write blog posts about what you've learned. "
    "Teaching others solidifies your own understanding.<br/><br/>"
    
    "<b>3. Specialize Deeper:</b> Choose one domain and go deep. Whether it's distributed systems, machine learning, "
    "graphics, databases, or security - become an expert.<br/><br/>"
    
    "<b>4. Network & Collaborate:</b> Attend meetups, conferences, hackathons. Join online communities. "
    "Some of the best learning happens in collaboration.<br/><br/>"
    
    "<b>5. Never Stop Building:</b> The best way to stay sharp is to keep building. Real projects teach what "
    "textbooks cannot. Build things that solve problems you care about.<br/><br/>"
    
    "<b>6. Interview Preparation:</b> If seeking employment, allocate 2-3 months for focused interview prep. "
    "Use your foundation to quickly master interview-specific patterns.<br/><br/>"
    
    "<b>7. Continuous Learning:</b> Technology evolves rapidly. Dedicate time weekly to learning new things. "
    "Read papers, try new languages, explore new paradigms.",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

content.append(Paragraph("💭 Final Thoughts", styles['SectionHeader']))
content.append(Paragraph(
    "You started this journey 72 weeks ago, perhaps uncertain about programming. "
    "Now you have the tools, knowledge, and confidence to build complex software systems. "
    "You understand not just <i>how</i> to code, but <i>why</i> things work the way they do.<br/><br/>"
    
    "Remember: you haven't learned everything about programming (no one ever does), but you've learned "
    "<b>how to learn</b>. You know how to read documentation, debug systematically, and break down complex "
    "problems. These meta-skills are more valuable than any specific technology.<br/><br/>"
    
    "The world needs what you can build. Your engineering background combined with programming skills "
    "puts you in a unique position to solve important problems. Go build something amazing.",
    styles['BodyJustify']
))
content.append(Spacer(1, 12))

content.append(Paragraph(
    '"The best time to plant a tree was 20 years ago. The second best time is now." '
    '— You\'ve already planted your tree. Now watch it grow.',
    styles['QuoteStyle']
))
content.append(Spacer(1, 10))

content.append(Paragraph(
    '"Programs must be written for people to read, and only incidentally for machines to execute." '
    '— Abelson & Sussman, <i>Structure and Interpretation of Computer Programs</i>',
    styles['QuoteStyle']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Now go build something amazing. 🚀</b>", styles['SubtitleCustom']))

content.append(PageBreak())

# ========== APPENDICES ==========
content.append(Paragraph("📚 Appendix: Recommended Resources", styles['TitleCustom']))
content.append(Spacer(1, 12))

content.append(Paragraph("<b>Free Online Resources</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <b>Python:</b> python.org/docs, realpython.com, pythontutor.com (visualizer)<br/>"
    "• <b>Algorithms:</b> visualgo.net, algorithm-visualizer.org<br/>"
    "• <b>LeetCode:</b> leetcode.com (use Explore section for guided learning)<br/>"
    "• <b>CS Fundamentals:</b> teachyourselfcs.com, cs.stackexchange.com<br/>"
    "• <b>Systems:</b> ops-class.org, OS Three Easy Pieces (free book)<br/>"
    "• <b>Git:</b> learngitbranching.js.org, git-scm.com/book<br/>"
    "• <b>YouTube:</b> MIT OpenCourseWare, freeCodeCamp, CS Dojo, Tech With Tim",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Communities</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• Reddit: r/learnprogramming, r/python, r/cscareerquestions<br/>"
    "• Discord: Python Discord, The Programmer's Hangout<br/>"
    "• Stack Overflow: stackoverflow.com (search first, then ask)<br/>"
    "• GitHub: Follow interesting developers, read their code",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Development Tools</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <b>IDE:</b> VS Code (free, excellent), PyCharm Community<br/>"
    "• <b>Terminal:</b> iTerm2 (Mac), Windows Terminal, tmux<br/>"
    "• <b>Version Control:</b> Git + GitHub/GitLab<br/>"
    "• <b>Python Tools:</b> pip, venv, black (formatter), pylint<br/>"
    "• <b>C Tools:</b> gcc, gdb, valgrind, make<br/>"
    "• <b>Notebook:</b> Jupyter (for exploration), Obsidian (notes)",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Learning Tips</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <b>Spaced Repetition:</b> Review previous weeks' material regularly<br/>"
    "• <b>Active Recall:</b> Code without looking at solutions first<br/>"
    "• <b>Teach Others:</b> Best way to verify your understanding<br/>"
    "• <b>Deliberate Practice:</b> Work slightly beyond your comfort zone<br/>"
    "• <b>Rest:</b> Your brain consolidates learning during sleep<br/>"
    "• <b>Consistency > Intensity:</b> 3 hours/day, 3 days/week beats 12-hour weekend binges<br/>"
    "• <b>Project-Based:</b> Apply concepts immediately in projects<br/>"
    "• <b>Debug Mindset:</b> Errors are learning opportunities, not failures",
    styles['BodyJustify']
))

content.append(Spacer(1, 12))
content.append(Paragraph("— End of Syllabus —", styles['SubtitleCustom']))

# Build PDF
doc.build(content, onFirstPage=add_page_footer, onLaterPages=add_page_footer)

print(f"✅ Improved syllabus generated: {OUTPUT_PATH}")
print(f"📊 Total days: {day_counter - 1}")
print(f"📅 Duration: {TOTAL_WEEKS} weeks ({TOTAL_WEEKS/4:.1f} months)")
print(f"🎯 More realistic pacing for engineering graduates")
print(f"📚 Focused mastery over breadth")
