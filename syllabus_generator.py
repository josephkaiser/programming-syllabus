"""
Programming Mastery: Foundation for the Long Haul - Version 3
30-Week Intensive Learning Path for Career Changers with Technical Backgrounds

Key Updates in v3:
- Fixed phase headers (now appear before weeks 11, 19, 25)
- Added grey transition callout boxes after weeks 10, 18, 24
- Revised Phase 3: Terminal basics, testing, Git, CI/CD, performance
- Added Week 2: Debugging fundamentals (high-level practices)
- Integrated venv/pip/terminal in Week 1
- Adjusted LeetCode to ~40 problems total with 1/day habit
- Added bash scripting to systems career path
- FIXED: Week boxes now stay on single pages (KeepTogether)
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

# Configuration
OUTPUT_PATH = "syllabus/programming-syllabus.pdf"

def add_page_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.grey)
    page_num = canvas.getPageNumber()
    text = f"Page {page_num}"
    canvas.drawCentredString(4.25*inch, 0.5*inch, text)
    canvas.restoreState()

doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=LETTER,
                        leftMargin=48, rightMargin=48, topMargin=60, bottomMargin=60)

# Styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontSize=20, leading=24, spaceAfter=10,
                         alignment=TA_CENTER, textColor=colors.HexColor('#1A237E'), bold=True))
styles.add(ParagraphStyle(name='SubtitleCustom', fontSize=11, leading=14, spaceAfter=14,
                         alignment=TA_CENTER, textColor=colors.HexColor('#424242'), italic=True))
styles.add(ParagraphStyle(name='SectionHeader', fontSize=12, leading=15, spaceAfter=6,
                         textColor=colors.HexColor('#1976D2'), bold=True))
styles.add(ParagraphStyle(name='WeekHeader', fontSize=10, leading=13, spaceAfter=4,
                         textColor=colors.HexColor('#2E7D32'), bold=True))
styles.add(ParagraphStyle(name='BodyJustify', fontSize=9, leading=11, spaceAfter=6, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='PhaseHeader', fontSize=13, leading=16, spaceAfter=8,
                         textColor=colors.HexColor('#D32F2F'), bold=True))
styles.add(ParagraphStyle(name='BulletList', fontSize=8.5, leading=10.5, spaceAfter=3, leftIndent=12))
styles.add(ParagraphStyle(name='Quote', fontSize=8.5, leading=10.5, spaceAfter=5,
                         alignment=TA_CENTER, italic=True, textColor=colors.HexColor('#555555')))
styles.add(ParagraphStyle(name='DayHeader', fontSize=8, leading=10, bold=True))
styles.add(ParagraphStyle(name='TransitionBox', fontSize=9, leading=11, spaceAfter=6,
                         leftIndent=20, rightIndent=20, alignment=TA_JUSTIFY,
                         textColor=colors.HexColor('#424242')))

content = []

# ========== TITLE PAGE ==========
content.append(Paragraph("Programming Foundation: Built to Last", styles['TitleCustom']))
content.append(Paragraph("30 Weeks to Deep Understanding and Practical Mastery", styles['SubtitleCustom']))
content.append(Spacer(1, 12))

content.append(Paragraph("🎯 Philosophy: Learning for the Long Haul", styles['SectionHeader']))
content.append(Paragraph(
    "This curriculum is designed for beginning programmers with technical backgrounds who want to "
    "<b>build deep fundamentals</b> in programming. The focus is on retention, understanding, and building "
    "toward meaningful personal projects that demonstrate real capability.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("⏱️ Time Investment", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Duration:</b> 30 weeks (7-8 months)<br/>"
    "<b>Schedule:</b> 4 days per week, 3-4 hours per session<br/>"
    "<b>Total Hours:</b> ~400-500 hours of focused work<br/>"
    "<b>Pace:</b> Aims to be sustainable alongside full-time commitments",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("🛠️ What You'll Need", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Required:</b><br/>"
    "• Computer (Mac, Linux, or Windows with WSL2)<br/>"
    "• Text editor: VS Code (recommended) or Neovim (if you prefer)<br/>"
    "• Internet connection<br/>"
    "• GitHub account (free)<br/><br/>"
    
    "<b>Cost:</b><br/>"
    "• All resources: $0-50 (one book purchase optional)<br/>"
    "• LeetCode Premium: $35/month (optional, weeks 25-30 only)<br/>"
    "• Hosting: $0-5/month (free tiers available)",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("📚 Primary Textbook", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Python Crash Course (3rd Edition) by Eric Matthes</b><br/>"
    "This will be your primary resource for Weeks 1-10. It's project-focused, clear, and comprehensive. "
    "Purchase the book ($40) or access via library. Supplementary readings will be provided for specific topics.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("📋 How to Use This Syllabus", styles['SectionHeader']))
content.append(Paragraph(
    "Each week contains:<br/>"
    "• <b>Week Goal:</b> What you'll accomplish<br/>"
    "• <b>Reading:</b> Specific chapters/pages or online resources<br/>"
    "• <b>Daily Tasks:</b> 4 days of specific work (Day 1-4)<br/>"
    "• <b>Weekly Project:</b> One concrete project to build<br/><br/>"
    
    "Complete textbook exercises as you encounter them. The syllabus points you to resources but doesn't "
    "prescribe every detail—learn to navigate documentation and tutorials as part of the process.",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== CURRICULUM OVERVIEW ==========
content.append(Paragraph("📋 Curriculum Overview", styles['TitleCustom']))
content.append(Spacer(1, 8))

content.append(Paragraph("PHASE 1: PYTHON MASTERY (Weeks 1-10)", styles['PhaseHeader']))
content.append(Paragraph(
    "Master Python fundamentals through hands-on practice. Build command-line tools and work with data. "
    "By week 10, you'll be comfortable with Python syntax, data structures, debugging, and object-oriented programming.",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

content.append(Paragraph("PHASE 2: WEB & DATABASES (Weeks 11-18)", styles['PhaseHeader']))
content.append(Paragraph(
    "Learn to build full-stack web applications. Work with databases, create APIs, and deploy real projects. "
    "Build a personal website or application that you'll continue to develop.",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

content.append(Paragraph("PHASE 3: PROFESSIONAL PRACTICES (Weeks 19-24)", styles['PhaseHeader']))
content.append(Paragraph(
    "Learn how professional developers work: terminal proficiency, testing, version control workflows, CI/CD automation, "
    "deployment, and performance optimization. Polish projects to professional quality.",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

content.append(Paragraph("PHASE 4: ALGORITHMS & CAPSTONE (Weeks 25-30)", styles['PhaseHeader']))
content.append(Paragraph(
    "Strengthen algorithmic thinking through focused problem-solving practice. Build a substantial capstone project that "
    "demonstrates all your skills. Establish the habit of daily algorithm practice to maintain and grow your abilities.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(PageBreak())

def create_transition_box(phase_num, title, what_mastered, common_struggles, what_to_review, next_phase_mindset):
    """Create a grey callout box for phase transitions"""
    data = [
        [Paragraph(f"<b>■ CHECKPOINT: Phase {phase_num} Complete — {title}</b>", styles['WeekHeader'])],
        [Paragraph(f"<b>What You've Mastered:</b><br/>{what_mastered}", styles['TransitionBox'])],
        [Paragraph(f"<b>Common Struggles at This Point:</b><br/>{common_struggles}", styles['TransitionBox'])],
        [Paragraph(f"<b>Review If Needed:</b><br/>{what_to_review}", styles['TransitionBox'])],
        [Paragraph(f"<b>Mindset for Next Phase:</b><br/>{next_phase_mindset}", styles['TransitionBox'])],
    ]
    
    table = Table(data, colWidths=[6*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F5F5')),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E0E0E0')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#9E9E9E')),
        ('LINEBELOW', (0,0), (-1,0), 1, colors.HexColor('#9E9E9E')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    
    return table

def create_week_box(week_num, title, goal, reading, day1, day2, day3, day4, project):
    """Create a detailed week breakdown that stays together on one page"""
    data = [
        [Paragraph(f"<b>Week {week_num}: {title}</b>", styles['WeekHeader']), ''],
        [Paragraph('<b>Goal:</b>', styles['BodyJustify']), Paragraph(goal, styles['BodyJustify'])],
        [Paragraph('<b>Reading:</b>', styles['BodyJustify']), Paragraph(reading, styles['BodyJustify'])],
        ['', ''],
        [Paragraph('<b>Day 1:</b>', styles['DayHeader']), Paragraph(day1, styles['BodyJustify'])],
        [Paragraph('<b>Day 2:</b>', styles['DayHeader']), Paragraph(day2, styles['BodyJustify'])],
        [Paragraph('<b>Day 3:</b>', styles['DayHeader']), Paragraph(day3, styles['BodyJustify'])],
        [Paragraph('<b>Day 4:</b>', styles['DayHeader']), Paragraph(day4, styles['BodyJustify'])],
        ['', ''],
        [Paragraph('<b>Weekly Project:</b>', styles['BodyJustify']), Paragraph(project, styles['BodyJustify'])],
    ]
    
    table = Table(data, colWidths=[1.2*inch, 4.8*inch])
    table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('BACKGROUND', (0,0), (1,0), colors.HexColor('#E8F5E9')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 1, colors.grey),
        ('LINEBELOW', (0,0), (-1,0), 1, colors.grey),
        ('LINEBELOW', (0,2), (-1,2), 0.5, colors.lightgrey),
        ('LINEBELOW', (0,8), (-1,8), 0.5, colors.lightgrey),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor('#F5F5F5')),
        ('BACKGROUND', (0,2), (0,2), colors.HexColor('#F5F5F5')),
        ('BACKGROUND', (0,9), (0,9), colors.HexColor('#F5F5F5')),
    ]))
    
    # KEY FIX: Wrap in KeepTogether to prevent page breaks within weeks
    return KeepTogether([table, Spacer(1, 6)])

# ========== PHASE 1: PYTHON MASTERY ==========
content.append(Paragraph("■ PHASE 1: PYTHON MASTERY", styles['PhaseHeader']))
content.append(Spacer(1, 6))

# Week 1
content.append(create_week_box(
    1,
    "Setup, Terminal & First Programs",
    "Set up development environment, learn terminal basics, write first Python programs",
    "Python Crash Course: Chapters 1-2 (pages 1-40), basic terminal tutorial",
    "Install Python, VS Code (or Neovim). Learn terminal: cd, ls, mkdir, pwd. Set up PATH. Create virtual environment (venv), install packages with pip.",
    "Work through Chapter 2: variables, strings, numbers. Complete Try It Yourself exercises (2-1 through 2-9). Practice in terminal.",
    "Practice string methods and number operations. Build simple calculator (add, subtract, multiply, divide) that runs from command line.",
    "Create temperature converter (Celsius/Fahrenheit/Kelvin) with input validation and error messages. Package with proper venv.",
    "Command-line calculator and temperature converter. Comfortable with terminal and virtual environments."
))

# Week 2  
content.append(create_week_box(
    2,
    "Debugging Fundamentals",
    "Learn systematic debugging approaches and tools",
    "Python Crash Course: Chapter 3 (Lists), debugging tutorial (choose your editor)",
    "Learn Chapter 3 basics. Set up debugger: VSCode debugger OR Neovim DAP (see documentation). Set breakpoints, step through code.",
    "Practice debugging: intentionally break code, use debugger to find issues. Learn to read stack traces and error messages.",
    "Learn print debugging and logging module. When to use each approach. Debug previous week's projects.",
    "Build number guessing game with intentional bugs, then systematically debug using multiple techniques. Document debugging process.",
    "Number guessing game (debugged) and documented debugging workflow that you can reference."
))

content.append(PageBreak())

# Week 3
content.append(create_week_box(
    3,
    "Lists and Loops",
    "Master lists and iteration for working with collections",
    "Python Crash Course: Chapter 4 (pages 59-82)",
    "Study Chapter 4 on loops. Complete exercises 4-1 through 4-13. Practice for loops and range().",
    "Work with list slicing and list comprehensions. Create lists of squares, cubes, and filtered lists.",
    "Practice nested loops and enumerate(). Build multiplication table generator.",
    "Build todo list manager: add tasks, mark complete, remove tasks, display all. Save to/load from file.",
    "Command-line todo list application with persistent storage using a text file."
))

# Week 4
content.append(create_week_box(
    4,
    "Dictionaries and User Input",
    "Work with key-value pairs and create interactive programs",
    "Python Crash Course: Chapters 5-7 (pages 83-132)",
    "Chapter 5: if statements and conditional logic. Exercises 5-1 through 5-11.",
    "Chapter 6: dictionaries. Work through all examples and complete exercises 6-1 through 6-11.",
    "Chapter 7: user input and while loops. Practice input validation. Exercises 7-1 through 7-10.",
    "Build complete program: phone book with add contact, search by name, list all, save/load from file.",
    "Phone book application using dictionaries, with persistent file storage."
))

# Week 5
content.append(create_week_box(
    5,
    "Functions",
    "Organize code with functions and understand scope",
    "Python Crash Course: Chapter 8 (pages 133-154)",
    "Read entire chapter on functions. Understand parameters, arguments, and return values. Exercises 8-1 through 8-7.",
    "Practice functions with default values and keyword arguments. Exercises 8-8 through 8-11.",
    "Work with arbitrary arguments (*args, **kwargs). Build function library: math utilities (GCD, LCM, prime check).",
    "Create text analysis tool with functions: word count, character count, most frequent words, reading time estimate.",
    "Text analysis library with multiple functions that process and analyze text files."
))

content.append(PageBreak())

# Week 6
content.append(create_week_box(
    6,
    "Classes and OOP Basics",
    "Learn object-oriented programming with classes and objects",
    "Python Crash Course: Chapter 9 (pages 155-182)",
    "Read Chapter 9 on classes. Understand __init__, self, and methods. Exercises 9-1 through 9-5.",
    "Practice inheritance and method overriding. Exercises 9-6 through 9-9.",
    "Work with importing classes and organizing code in modules. Exercises 9-10 through 9-13.",
    "Build bank account simulator: Account class with deposit, withdraw, transfer. SavingsAccount with interest.",
    "Bank account system with multiple account types using inheritance."
))

# Week 7
content.append(create_week_box(
    7,
    "Files and Exceptions",
    "Work with files and handle errors gracefully",
    "Python Crash Course: Chapter 10 (pages 183-208)",
    "Read about file operations: reading and writing. Work through all file examples. Exercises 10-1 through 10-5.",
    "Study exception handling with try-except blocks. Exercises 10-6 through 10-10.",
    "Practice JSON for data storage. Store and retrieve structured data. Exercises 10-11 through 10-13.",
    "Build expense tracker: log expenses with date/category/amount, view by month, calculate totals, export to CSV.",
    "Expense tracking application with JSON storage and CSV export functionality."
))

content.append(PageBreak())

# Week 8
content.append(create_week_box(
    8,
    "Testing Your Code",
    "Write tests to ensure code works correctly",
    "Python Crash Course: Chapter 11 (pages 209-226)",
    "Read about testing with pytest. Install pytest. Understand test functions and assertions. Exercises 11-1 through 11-2.",
    "Learn to test classes. Write tests for previous projects. Exercise 11-3.",
    "Practice test-driven development: write tests first, then implementation.",
    "Build tested library: string manipulation functions with full test coverage (reverse, palindrome, anagram check).",
    "String utility library with comprehensive pytest test suite."
))

# Week 9
content.append(create_week_box(
    9,
    "Working with APIs",
    "Fetch and process data from web APIs",
    "Python Crash Course: Chapter 17 (pages 355-378), requests documentation",
    "Install requests library. Learn HTTP GET requests. Fetch data from simple APIs (JSONPlaceholder).",
    "Work with API authentication and headers. Practice parsing JSON responses.",
    "Handle rate limits and errors. Cache API responses to files.",
    "Build weather application: fetch current weather and 5-day forecast, display nicely formatted, cache data.",
    "Weather application using OpenWeatherMap API with caching."
))

# Week 10
content.append(create_week_box(
    10,
    "Data Visualization & Web Scraping",
    "Create charts from data and extract data from websites",
    "Python Crash Course: Chapters 15-16 (pages 305-354), BeautifulSoup basics",
    "Install matplotlib. Create basic plots: line graphs, scatter plots. Work through Chapter 15 examples.",
    "Study Chapter 16: download and analyze CSV data. Create bar charts and histograms.",
    "Install BeautifulSoup. Learn HTML basics. Parse simple web pages and extract data.",
    "Build price tracker: scrape product prices, store history in CSV, visualize price trends with matplotlib.",
    "Price tracking and visualization tool combining web scraping and data visualization."
))

# TRANSITION BOX 1
content.append(Spacer(1, 10))
content.append(create_transition_box(
    1,
    "You Now Think in Python",
    "Python syntax, data structures (lists, dicts), functions, OOP, file I/O, error handling, testing, APIs, debugging workflow, terminal comfort.",
    "OOP concepts might still feel abstract. Debugging complex issues takes time. Testing feels tedious but necessary.",
    "If OOP is unclear: redo Week 6 bank account project. If debugging is slow: practice with Week 2 techniques. If APIs confuse you: redo Week 9 weather app.",
    "Now you shift from 'learning Python' to 'building applications.' Phase 2 uses everything you learned to create real web apps people can use."
))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 2: WEB & DATABASES ==========
content.append(Paragraph("■ PHASE 2: WEB & DATABASES", styles['PhaseHeader']))
content.append(Spacer(1, 6))

# Week 11
content.append(create_week_box(
    11,
    "HTML/CSS & Flask Basics",
    "Learn web fundamentals and build your first web application",
    "MDN HTML/CSS basics, Flask Quickstart (flask.palletsprojects.com)",
    "Learn HTML essentials: tags, forms, links, semantic markup (3 hours). Build a static page with proper structure.",
    "Learn CSS basics: selectors, box model, flexbox (3 hours). Style your static page. Understand browser inspector.",
    "Install Flask. Create hello world app. Understand routes and views. Learn Jinja2 templates and template inheritance.",
    "Build personal website: home page, about page, contact page. Use Flask with styled templates.",
    "Multi-page personal website with navigation, styling, and Flask backend."
))

# Week 12
content.append(create_week_box(
    12,
    "Flask Forms and Validation",
    "Handle user input securely with forms",
    "Flask-WTF documentation, form handling tutorials",
    "Install Flask-WTF. Create form classes with validation rules. Understand POST vs GET.",
    "Handle form submissions and display validation errors. Use flash messages for user feedback.",
    "Add CSRF protection. Practice form processing with different field types.",
    "Build working contact form: name, email, subject, message fields with validation. Store submissions in JSON file.",
    "Contact form with validation and data persistence to JSON."
))

content.append(PageBreak())

# Week 13
content.append(create_week_box(
    13,
    "SQL Fundamentals (Week 1)",
    "Learn to query and manipulate databases",
    "SQLite Tutorial (sqlitetutorial.net): Core concepts through JOINs",
    "Install DB Browser for SQLite. Learn database concepts. Practice CREATE TABLE, INSERT, data types.",
    "Master SELECT queries: WHERE, ORDER BY, LIMIT, DISTINCT. Practice on sample database.",
    "Study aggregate functions: COUNT, SUM, AVG, GROUP BY, HAVING. Analyze data with queries.",
    "Practice on sample database: write 20+ queries of increasing complexity. Save and document your queries.",
    "Portfolio of SQL queries demonstrating core competency."
))

# Week 14
content.append(create_week_box(
    14,
    "SQL Fundamentals (Week 2)",
    "Master JOINs and database design",
    "SQLite Tutorial: JOINs, subqueries, indexes. Database design principles.",
    "Learn JOINs: INNER, LEFT, RIGHT. Practice combining data from multiple tables.",
    "Study subqueries and nested queries. Learn when to use vs JOINs.",
    "Understand indexes and query performance. Learn database normalization basics.",
    "Design database schema for blog: users, posts, comments, tags tables with relationships. Create, populate, query.",
    "Blog database schema with sample data and complex queries demonstrating JOINs."
))

content.append(PageBreak())

# Week 15
content.append(create_week_box(
    15,
    "SQLAlchemy ORM",
    "Work with databases using Python objects",
    "SQLAlchemy documentation, Flask-SQLAlchemy quickstart",
    "Install Flask-SQLAlchemy. Define models as Python classes. Understand ORM concepts.",
    "Practice CRUD operations: create, read, update, delete records using ORM instead of raw SQL.",
    "Learn relationships: one-to-many with foreign keys. Query across relationships.",
    "Build note-taking app with database: create notes with title/content, list all, view one, update, delete.",
    "Note-taking web app with SQLite database and full CRUD operations."
))

# Week 16
content.append(create_week_box(
    16,
    "Database Migrations",
    "Version control your database schema",
    "Flask-Migrate documentation, Alembic basics",
    "Install Flask-Migrate. Initialize migrations. Create first migration. Understand migration files.",
    "Practice schema changes: add columns, create new tables. Apply and rollback migrations.",
    "Learn migration best practices. Handle data migrations safely.",
    "Add features to note app: created_at timestamp, updated_at, categories. Use migrations for all schema changes.",
    "Enhanced note app with timestamps and proper database migrations."
))

# Week 17
content.append(create_week_box(
    17,
    "User Authentication",
    "Implement login and user sessions",
    "Flask-Login documentation, password hashing guide",
    "Install Flask-Login. Create User model with password hashing (werkzeug.security).",
    "Implement registration: new user signup with password validation and email verification format.",
    "Build login/logout functionality. Protect routes with @login_required decorator. Understand sessions.",
    "Add user accounts to note app: each user sees only their notes, user profile page, password change.",
    "Multi-user note application with authentication and private notes per user."
))

content.append(PageBreak())

# Week 18
content.append(create_week_box(
    18,
    "Building REST APIs & Frontend Integration",
    "Create API endpoints and connect with JavaScript",
    "Flask-RESTful documentation, MDN Fetch API tutorial",
    "Understand REST principles: resources, HTTP methods, status codes. Build API for one resource.",
    "Implement CRUD API endpoints. Return JSON responses. Test with curl or Postman.",
    "Learn JavaScript fetch() API basics. Make requests to your backend. Handle JSON responses.",
    "Build dynamic todo page: JavaScript frontend fetches from Flask API, add/delete without page refresh.",
    "Single-page todo application with JavaScript frontend calling your REST API."
))

# TRANSITION BOX 2
content.append(Spacer(1, 10))
content.append(create_transition_box(
    2,
    "You Can Build Full-Stack Applications",
    "HTML/CSS basics, Flask web framework, form handling, SQL and database design, ORM with SQLAlchemy, database migrations, user authentication, REST APIs, JavaScript/frontend basics.",
    "Database design is hard. Authentication security is tricky. Frontend/backend integration can be confusing at first.",
    "If SQL unclear: redo Weeks 13-14 exercises. If authentication confuses you: review Week 17 step-by-step. If stuck on APIs: review REST principles and practice with Postman.",
    "You can now build any CRUD application. Phase 3 teaches you to work like a professional: testing, version control, CI/CD, deployment, performance."
))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 3: PROFESSIONAL PRACTICES ==========
content.append(Paragraph("■ PHASE 3: PROFESSIONAL PRACTICES", styles['PhaseHeader']))
content.append(Spacer(1, 6))

# Week 19
content.append(create_week_box(
    19,
    "Terminal & Testing Web Applications",
    "Deepen terminal skills and test Flask apps",
    "Bash scripting basics (high-level overview), pytest-flask plugin documentation",
    "Review terminal fundamentals: navigation, file operations, pipes, grep, environment variables. Practice bash command chaining.",
    "Install pytest-flask. Learn to test routes and views. Write test client requests for your Flask apps.",
    "Test form submissions and validation. Mock database operations. Understand fixtures.",
    "Add comprehensive test suite to your note app: test all routes, authentication, CRUD operations, edge cases.",
    "Full test coverage for note app with pytest. Comfort with terminal for daily tasks."
))

# Week 20
content.append(create_week_box(
    20,
    "Advanced Testing & Code Quality",
    "Master testing patterns and write professional code",
    "pytest documentation, PEP 8 style guide, type hints tutorial",
    "Learn test organization: fixtures, parametrize, markers. Practice testing with databases.",
    "Install black, pylint, mypy. Format and lint your code. Add type hints to functions.",
    "Test API endpoints: verify status codes, response data, error handling. Achieve >80% coverage.",
    "Add tests to todo API: test all CRUD operations, authentication, error cases. Format all code with black.",
    "Professionally tested and formatted API with comprehensive test suite."
))

content.append(PageBreak())

# Week 21
content.append(create_week_box(
    21,
    "Git Workflows & Collaboration",
    "Master version control for professional development",
    "Pro Git book (free online), Atlassian Git tutorials, learngitbranching.js.org",
    "Review Git basics. Practice branching and merging. Create feature branches for each feature.",
    "Learn rebase vs merge. Handle merge conflicts. Practice interactive rebase to clean history.",
    "Understand pull request workflow. Write good commit messages. Learn .gitignore patterns.",
    "Organize all projects in GitHub: clean commit history, comprehensive READMEs, proper .gitignore files.",
    "All previous projects properly organized in GitHub with professional repository structure."
))

# Week 22
content.append(create_week_box(
    22,
    "Environment & Configuration Management",
    "Handle configuration and secrets properly",
    "12-factor app methodology, python-dotenv documentation",
    "Learn environment variables. Never commit secrets. Use .env files with python-dotenv.",
    "Create separate configs for development, testing, production environments.",
    "Practice with config objects and environment-based settings. Understand security implications.",
    "Refactor Flask app: move all secrets to environment variables, create config classes for each environment.",
    "Application properly configured with environment variables and multiple environments."
))

# Week 23
content.append(create_week_box(
    23,
    "CI/CD with GitHub Actions",
    "Automate testing and deployment",
    "GitHub Actions official documentation and tutorials (comprehensive)",
    "Learn GitHub Actions basics: workflows, jobs, steps. Follow comprehensive tutorial (day 1-2 of work).",
    "Create workflow: run tests on every push and PR. Set up automated linting and formatting checks.",
    "Add deployment automation: automatically deploy to production when tests pass on main branch.",
    "Implement full CI/CD for one project: automated tests, linting, deployment. Watch it work on a real PR.",
    "Project with complete CI/CD pipeline: auto-test and auto-deploy."
))

content.append(PageBreak())

# Week 24
content.append(create_week_box(
    24,
    "Performance & Deployment",
    "Optimize and deploy production applications",
    "Flask performance tips, cProfile documentation, deployment platform docs (Render/Railway)",
    "Profile your app with cProfile. Identify slow queries. Add database indexes where needed.",
    "Implement caching with Flask-Caching. Cache expensive operations and repeated queries.",
    "Deploy your best project to Render/Railway/PythonAnywhere. Set up proper environment config and monitoring.",
    "Optimize deployed app: add caching, fix N+1 queries, monitor performance. Ensure it handles real traffic.",
    "Production-ready application deployed with performance optimizations and monitoring."
))

# TRANSITION BOX 3
content.append(Spacer(1, 10))
content.append(create_transition_box(
    3,
    "You Code Like a Professional",
    "Terminal proficiency, comprehensive testing, Git workflows, environment configuration, CI/CD automation, deployment experience, performance optimization.",
    "CI/CD can break in unexpected ways. Performance optimization is an art. Deployment has many moving parts.",
    "If CI/CD fails: read error messages carefully, check GitHub Actions docs. If performance unclear: review database indexes. If deployment fails: verify environment variables.",
    "You have professional developer skills. Phase 4 adds algorithmic thinking and a capstone project to demonstrate everything you've learned."
))
content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PHASE 4: ALGORITHMS & CAPSTONE ==========
content.append(Paragraph("■ PHASE 4: ALGORITHMS & CAPSTONE", styles['PhaseHeader']))
content.append(Spacer(1, 6))

# Week 25
content.append(create_week_box(
    25,
    "Algorithm Fundamentals",
    "Learn Big-O and problem-solving patterns",
    "Grokking Algorithms: Chapters 1-4, LeetCode Easy problems",
    "Study Big-O notation. Analyze time and space complexity. Practice examples on paper.",
    "Learn two pointers pattern. Solve: Two Sum II, Remove Duplicates from Sorted Array (LeetCode).",
    "Study sliding window pattern. Solve: Maximum Average Subarray, Longest Substring Without Repeating.",
    "Solve 6 more LeetCode Easy problems mixing patterns. Focus on understanding, not speed. Start habit: 1 problem per day.",
    "10 solved algorithm problems with documented solutions and complexity analysis."
))

# Week 26
content.append(create_week_box(
    26,
    "Arrays, Strings & Hash Tables",
    "Master fundamental data structure patterns",
    "LeetCode Arrays 101 explore card, String problems, Hash Table patterns",
    "Solve 4 array problems: Best Time to Buy Stock, Rotate Array, Plus One, Move Zeroes.",
    "Solve 4 string problems: Valid Palindrome, Reverse String, Valid Anagram, First Unique Character.",
    "Study hash table pattern. Solve: Group Anagrams, Contains Duplicate, Two Sum.",
    "Solve 5 more mixed problems. Maintain 1 problem per day habit. Focus on pattern recognition.",
    "Approximately 16 more solved problems (26 total). Strong foundation in arrays, strings, hash tables."
))

content.append(PageBreak())

# Week 27
content.append(create_week_box(
    27,
    "Linked Lists & Trees + Capstone Planning",
    "Learn node-based structures and plan final project",
    "LeetCode Linked List and Binary Tree explore cards",
    "Implement LinkedList from scratch. Solve: Reverse Linked List, Merge Two Sorted Lists.",
    "Study binary tree traversals: preorder, inorder, postorder, level-order. Solve: Max Depth, Invert Tree.",
    "Solve: Same Tree, Symmetric Tree, Path Sum. Practice recursion on trees.",
    "Plan capstone project: write specification, design database schema, create wireframes. Solve 1 problem/day.",
    "4-5 more solved problems (~31 total). Detailed capstone project plan ready to implement."
))

# Week 28
content.append(create_week_box(
    28,
    "Capstone Project (Week 1)",
    "Begin building comprehensive project",
    "None - focus on building. Continue 1 LeetCode problem per day.",
    "Set up project structure. Initialize Git repo. Create virtual environment. Set up database and models.",
    "Build core backend functionality: all database models, CRUD operations, business logic.",
    "Implement authentication if needed. Build API endpoints. Write tests as you go.",
    "Continue backend implementation. Achieve >80% test coverage. Keep up with 1 problem/day.",
    "Well-structured capstone project with working backend. ~35 total problems solved."
))

# Week 29
content.append(create_week_box(
    29,
    "Capstone Project (Week 2)",
    "Build frontend and polish project",
    "None - focus on building. Continue 1 LeetCode problem per day.",
    "Build frontend interface. Connect to API. Ensure all features work together end-to-end.",
    "Style with CSS. Make it look professional. Test on different browsers if web app.",
    "Fix bugs discovered during testing. Improve error handling and user experience.",
    "Add any missing features. Ensure everything works smoothly. Maintain 1 problem/day habit.",
    "Fully functional capstone project with professional frontend. ~39 total problems solved."
))

# content.append(PageBreak())

# Week 30
content.append(create_week_box(
    30,
    "Capstone Project (Week 3)",
    "Complete, deploy, and document your work",
    "None - focus on completion. Maintain 1 problem/day habit for life!",
    "Write comprehensive tests if not already done. Aim for >80% coverage. Fix all bugs.",
    "Write documentation: README with setup instructions, API docs if applicable, user guide.",
    "Deploy project with CI/CD. Ensure it's accessible online. Verify all features work in production.",
    "Write blog post explaining what you built, technologies used, challenges overcome. Reflect on 30-week journey!",
    "Finished, tested, documented, and deployed capstone project. ~42-43 total problems solved. Daily problem habit established."
))

content.append(PageBreak())

# ========== CAPSTONE IDEAS ==========
content.append(Paragraph("🎯 Capstone Project Ideas", styles['TitleCustom']))
content.append(Spacer(1, 8))

content.append(Paragraph(
    "Your capstone should demonstrate everything you've learned. Choose something that interests you:<br/><br/>"
    
    "<b>Personal Finance Tools:</b><br/>"
    "• Budget tracker with spending analytics and visualizations<br/>"
    "• Investment portfolio tracker with API data and historical charts<br/>"
    "• Bill reminder and payment tracking system<br/><br/>"
    
    "<b>Content Management:</b><br/>"
    "• Personal blog platform with markdown editor and RSS feed<br/>"
    "• Recipe organizer with meal planning and shopping lists<br/>"
    "• Reading list tracker with notes and recommendations<br/><br/>"
    
    "<b>Data Analysis:</b><br/>"
    "• Stock screening tool with technical indicators<br/>"
    "• Weather pattern analyzer with historical data<br/>"
    "• Text analysis tool (sentiment, keywords, summaries)<br/><br/>"
    
    "<b>Automation:</b><br/>"
    "• Job application tracker with deadline reminders<br/>"
    "• Habit tracker with streaks and statistics<br/>"
    "• Automated report generator from data sources<br/><br/>"
    
    "<b>Requirements for any capstone:</b><br/>"
    "• 500+ lines of code<br/>"
    "• Database with multiple related tables<br/>"
    "• User authentication (if multi-user)<br/>"
    "• API or significant data processing component<br/>"
    "• Test coverage >80%<br/>"
    "• Professional documentation<br/>"
    "• Deployed and accessible online<br/>"
    "• Solves a real problem or demonstrates interesting technical skills",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== COMPLETION PAGE ==========
content.append(Paragraph("🎓 You've Completed 30 Weeks!", styles['TitleCustom']))
content.append(Spacer(1, 10))

content.append(Paragraph("What You've Accomplished", styles['SectionHeader']))
content.append(Paragraph(
    "Over 30 weeks and 400-500 hours, you have:<br/><br/>"
    
    "• Mastered Python from basics to advanced concepts<br/>"
    "• Developed debugging skills and terminal proficiency<br/><br/>"
    "• Created full-stack web applications with databases<br/>"
    "• Built and deployed a comprehensive capstone project<br/>",
    
    styles['BodyJustify']
))
content.append(Spacer(1, 4))

content.append(Paragraph("Next Steps: Illustrative Paths Forward", styles['SectionHeader']))
content.append(Paragraph(
    # "<b>Continue Building:</b> Build one project per month minimum to retain your skills. "
    # "Maintain your daily 1 LeetCode problem habit—it compounds over months into deep expertise.<br/><br/>"
    
    "<b>Path 1: Web Developer (Most Jobs)</b><br/>"
    "• Weeks 31-32: JavaScript/TypeScript fundamentals<br/>"
    "• Weeks 33-34: React basics and component patterns<br/>"
    "• Weeks 35-38: Next.js, Vercel deployment, server components<br/>"
    "• Weeks 39-40: Rebuild capstone in Next.js<br/>"
    "• Continue: 1 LeetCode/day, 1 side project/month<br/>"
    "• Result: Full-stack developer with modern stack ($80-120k entry level)<br/><br/>"
    
    "<b>Path 2: Backend/Systems Engineer</b><br/>"
    "• Learn C (K&R book), understand memory management<br/>"
    "• <b>Bash scripting deep dive</b> (1-2 weeks): Automate system tasks, write deployment scripts<br/>"
    "• Study networking (Beej's Guide), build socket programs<br/>"
    "• Deep dive databases: query optimization, indexes, replication<br/>"
    "• Consider Rust for modern systems programming<br/>"
    "• Continue: 1 LeetCode/day focusing on systems problems<br/>"
    "• Result: Backend specialist, infrastructure roles ($90-140k)<br/><br/>"
    
    "<b>Path 3: Data Analysis/Financial Engineering</b><br/>"
    "• Master NumPy, pandas for data manipulation<br/>"
    "• Learn data visualization: matplotlib, plotly, dashboards<br/>"
    "• Statistics and probability foundations<br/>"
    "• C for performance-critical algorithms if needed<br/>"
    "• Build trading backtesting systems, portfolio analytics<br/>"
    "• Continue: 1 LeetCode/day, especially DP and math problems<br/>"
    "• Result: Quant developer, data analyst ($100-180k)<br/><br/>"
    
    "<b>Path 4: Machine Learning Engineer</b><br/>"
    "• Mathematics: linear algebra, calculus, statistics (essential foundation)<br/>"
    "• scikit-learn for classical ML<br/>"
    "• PyTorch or TensorFlow for deep learning<br/>"
    "• Deploy models with FastAPI<br/>"
    "• Continue: 1 LeetCode/day, focus on optimization problems<br/>"
    "• Result: ML engineer, AI roles ($110-160k)<br/><br/>"
    
    "<b>Path 5: Open Source Contributor</b><br/>"
    "• Contribute to Python projects (Flask, pandas, pytest)<br/>"
    "• Learn C/Rust to contribute to core tools (CPython, ripgrep)<br/>"
    "• Build developer tools and libraries<br/>"
    "• Continue: 1 LeetCode/day to strengthen problem-solving<br/>"
    "• Result: Deep expertise, recognition, job opportunities<br/><br/>",
    
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("— End of Syllabus —", styles['Quote']))

# Build PDF
doc.build(content, onFirstPage=add_page_footer, onLaterPages=add_page_footer)

print(f"✅ Syllabus v3 generated: {OUTPUT_PATH}")
print("✅ Week boxes will stay on single pages (no mid-week splits)")
