from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

# Output path
output_pdf_path = "syllabus/Programming_Syllabus_48Weeks_Complete.pdf"

# Create the document in LANDSCAPE mode
doc = SimpleDocTemplate(output_pdf_path, pagesize=landscape(LETTER),
                        leftMargin=36, rightMargin=36, topMargin=48, bottomMargin=48)

# Styles - improved readability
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontSize=20, leading=18, spaceAfter=12, alignment=TA_CENTER, textColor=colors.HexColor('#1A237E'), bold=True))
styles.add(ParagraphStyle(name='SubtitleCustom', fontSize=12, leading=12, spaceAfter=18, alignment=TA_CENTER, textColor=colors.HexColor('#424242'), italic=True))
styles.add(ParagraphStyle(name='HeadingCustom', fontSize=10, leading=12, spaceAfter=4, textColor=colors.HexColor('#34495E'), bold=True))
styles.add(ParagraphStyle(name='BodyCustom', fontSize=7.5, leading=9, spaceAfter=2))
styles.add(ParagraphStyle(name='BodyJustify', fontSize=10, leading=13, spaceAfter=8, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='HeaderCell', fontSize=7.5, leading=9, bold=True, alignment=TA_CENTER))
styles.add(ParagraphStyle(name='QuoteStyle', fontSize=10, leading=13, spaceAfter=8, alignment=TA_CENTER, italic=True, textColor=colors.HexColor('#37474F')))
styles.add(ParagraphStyle(name='BulletStyle', fontSize=10, leading=13, spaceAfter=6, leftIndent=20, bulletIndent=10))
styles.add(ParagraphStyle(name='SectionHeader', fontSize=13, leading=16, spaceAfter=8, textColor=colors.HexColor('#1976D2'), bold=True))
styles.add(ParagraphStyle(name='TOCStyle', fontSize=9, leading=11, spaceAfter=3, leftIndent=10))
styles.add(ParagraphStyle(name='LegendStyle', fontSize=7, leading=8.5, spaceAfter=1, textColor=colors.HexColor('#555555')))

content = []

# ========== PAGE 1: INTRODUCTION ==========

content.append(Paragraph("# Comprehensive Programming Study Syllabus #", styles['TitleCustom']))
content.append(Paragraph("A 48-Week Syllabus to Dive into Computer Science Fundamentals", styles['SubtitleCustom']))


# Goal Section
content.append(Paragraph("📚 Goal", styles['SectionHeader']))
content.append(Paragraph(
    "To master Python programming in the context of data structures and algorithms, "
    "with emphasis on computer science fundamentals, systems programming (C), and "
    "mathematical foundations for computational problem-solving.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))


# Books Required for This Syllabus
content.append(Paragraph("📚 Required Books for This Syllabus", styles['SectionHeader']))
content.append(Paragraph(
    "<i>The following books are referenced throughout the 48-week curriculum. </i>"
    "<i>The abbreviations shown are used in the daily reading assignments.</i>",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

# Create a cleaner book list without table formatting issues
content.append(Paragraph("<b>Automate</b> — <i>Automate the Boring Stuff with Python</i> by Al Sweigart", styles['BodyJustify']))
content.append(Paragraph("<b>Beej</b> — <i>Beej's Guide to Network Programming</i> by Brian Hall (free online)", styles['BodyJustify']))
content.append(Paragraph("<b>CLRS</b> — <i>Introduction to Algorithms</i> by Cormen, Leiserson, Rivest, and Stein", styles['BodyJustify']))
content.append(Paragraph("<b>CSAPP</b> — <i>Computer Systems: A Programmer's Perspective</i> by Bryant and O'Hallaron", styles['BodyJustify']))
content.append(Paragraph("<b>Dragon Book</b> — <i>Compilers: Principles, Techniques, and Tools</i> by Aho et al.", styles['BodyJustify']))
content.append(Paragraph("<b>Gang of Four</b> — <i>Design Patterns</i> by Gamma, Helm, Johnson, and Vlissides", styles['BodyJustify']))
content.append(Paragraph("<b>Handbook</b> — <i>Competitive Programmer's Handbook</i> by Antti Laaksonen (free PDF)", styles['BodyJustify']))
content.append(Paragraph("<b>K&R</b> — <i>The C Programming Language</i> by Kernighan and Ritchie", styles['BodyJustify']))
content.append(Paragraph("<b>OSTEP</b> — <i>Operating Systems: Three Easy Pieces</i> by Arpaci-Dusseau (free online)", styles['BodyJustify']))
content.append(Paragraph("<b>Sipser</b> — <i>Introduction to the Theory of Computation</i> by Michael Sipser", styles['BodyJustify']))
content.append(Spacer(1, 4))
content.append(Paragraph(
    "<i>Plus specific chapters from:</i> Elements of Programming Interviews, Python Official Tutorial, "
    "Valgrind Manual, GNU Make Manual, Python for Data Analysis, High Performance Python, Hands-On ML, "
    "CUDA by Example, Building Microservices, Designing Data-Intensive Applications, Linux Kernel Development, "
    "Linux Device Drivers, Art of Multiprocessor Programming, Making Embedded Systems, Real-Time Systems, "
    "Distributed Systems (Tanenbaum), Algorithmic Game Theory, and Elements of Information Theory.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(PageBreak())

# How to Use Section
content.append(Paragraph("💡 How to Make the Most of This Syllabus", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Equipment:</b> A reliable laptop (Unix-like OS preferred), internet connectivity, IDE / text editor, terminal environment"
        "<b>Time Commitment:</b> Sample breakout: 3 days/week, 3-4 hours per session. Consistency beats intensity. "
    "<b>Three-Track Syllabus:</b> Each week / 3-day cluster alternates between Python (algorithms), C/Systems (low-level), and Design/Math (theory). "
    "<b>Projects:</b> Every day includes a hands-on project—build your GitHub portfolio.",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

# Methodology Section
content.append(Paragraph("🎯 Methodology", styles['SectionHeader']))
content.append(Paragraph(
    "<b>Build a Portfolio:</b> Construct a comprehensive GitHub repository filled with projects demonstrating mastery across three tracks. "
    "<b>Train on LeetCode:</b> Practice problems assigned by topic (take with a grain of salt, problems assigned by Claude with no human checking. I will review as I take the course and return to the syllabus-generator.py to correct."
    "<b>Read the Classics:</b> References several canonical texts of computer science.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

# Motivation
content.append(Paragraph("🔥 Words of Wisdom", styles['SectionHeader']))
content.append(Paragraph('"Programs must be written for people to read, and only incidentally for machines to execute." — <i>Abelson & Sussman</i>', styles['QuoteStyle']))
content.append(Paragraph('"The only way to learn a new programming language is by writing programs in it." — <i>Dennis Ritchie</i>', styles['QuoteStyle']))
content.append(Paragraph('"Premature optimization is the root of all evil." — <i>Donald Knuth</i>', styles["QuoteStyle"]))
content.append(Paragraph('"Talk is cheap. Show me the code." — <i>Linus Torvalds</i>', styles["QuoteStyle"]))

content.append(Spacer(1, 10))

content.append(PageBreak())

# ========== PAGE 2: TABLE OF CONTENTS ==========

content.append(Paragraph("📋 Table of Contents: 48-Week Curriculum Overview", styles['TitleCustom']))
content.append(Spacer(1, 10))

# Create table of contents organized by phases
toc_content = []

# Phase headers and week summaries
phases = [
    ("PHASE 1: FOUNDATIONS (Weeks 1-12)", [
        "Weeks 1-4: Python Basics, C Introduction, Algorithm Analysis, Recursion, Sorting",
        "Weeks 5-8: Data Structures Basics (Lists, Dicts, Heaps, Hash Tables, Graphs), Memory Management",
        "Weeks 9-12: OOP Fundamentals, File I/O, Binary Search, Greedy Algorithms, Dynamic Programming Intro"
    ]),
    ("PHASE 2: INTERMEDIATE (Weeks 13-24)", [
        "Weeks 13-16: Linked Lists, Binary Trees, BSTs, System Calls (fork/exec), Red-Black Trees",
        "Weeks 17-20: Graph Algorithms (BFS/DFS), Shortest Paths (Dijkstra, Bellman-Ford), Sockets, Dynamic Programming",
        "Weeks 21-24: 2D DP, Backtracking, Tries, Union-Find, MST, Operating Systems Concepts"
    ]),
    ("PHASE 3: ADVANCED (Weeks 25-36)", [
        "Weeks 25-28: Advanced DP (Knapsack), Segment Trees, Concurrency, Network Flow, Virtual Memory",
        "Weeks 29-32: String Algorithms (KMP), File Systems, Topological Sort, Branch & Bound, Profiling",
        "Weeks 33-36: Sliding Window, Assembly, Computational Geometry, Bit Manipulation, Automata Theory"
    ]),
    ("PHASE 4: MASTERY (Weeks 37-48)", [
        "Weeks 37-40: Design Patterns, Kernel Modules, Turing Machines, asyncio, Decidability",
        "Weeks 41-44: Microservices, HPC, Complexity Classes, ML Fundamentals, GPU Programming",
        "Weeks 45-48: Data Engineering, Distributed Systems, System Design, Capstone Project"
    ])
]

for phase_title, week_summaries in phases:
    toc_content.append([Paragraph(f"<b>{phase_title}</b>", styles['TOCStyle'])])
    for summary in week_summaries:
        toc_content.append([Paragraph(f"  • {summary}", styles['TOCStyle'])])
    toc_content.append([Spacer(1, 4)])

toc_table = Table(toc_content, colWidths=[700])
toc_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))

content.append(toc_table)
content.append(Spacer(1, 12))

content.append(Paragraph(
    "<b>Daily Structure:</b> Each day includes a specific Topic, Reading Assignment, LeetCode Problem (where applicable), "
    "and a hands-on Project. Print this syllabus and track your progress week by week.",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== PAGES 3+: CURRICULUM ==========

# Curriculum structure with specific, actionable projects
curriculum = {
    # PHASE 1: FOUNDATIONS (Weeks 1-12)
    1: [
        ("Python", "Python Basics: Variables, Types, Operators", "Automate Ch.1-2", "Two Sum, Add Two Numbers", "Build a temperature converter (C/F/K) with input validation"),
        ("C/System", "C Introduction: Compilation, Basic I/O", "K&R Ch.1, Beej §1-2", "Plus One (in C)", "Create 'Hello World' with command-line arguments parser"),
        ("Design/Math", "Algorithm Analysis: Big-O Notation", "CLRS §3.1-3.2", "Valid Palindrome, Is Subsequence", "Benchmark sorting algorithms and plot runtimes vs input size")
    ],
    2: [
        ("Python", "Control Flow: if/elif/else, while loops", "Automate Ch.2", "Reverse Integer, Palindrome Number", "Number guessing game with difficulty levels and hints"),
        ("C/System", "Data Types & Operators in C", "K&R Ch.2", "Factorial (in C), Power of Two", "Build sizeof() demonstration showing all C data type sizes"),
        ("Design/Math", "Proof Techniques: Induction", "Sipser §0.1-0.2", "Roman to Integer, Integer to Roman", "Prove loop invariants for 3 simple algorithms (max, sum, reverse)")
    ],
    3: [
        ("Python", "Lists & List Operations", "Automate Ch.4, CLRS §10.1", "Remove Duplicates, Remove Element", "Implement todo list manager with add/remove/search/filter"),
        ("C/System", "Arrays & Strings in C", "K&R Ch.5.1-5.5", "Reverse String (in C), Valid Anagram", "Create string library: strlen, strcpy, strcat, strcmp from scratch"),
        ("Design/Math", "Recursion Basics", "CLRS §4.1-4.3", "Fibonacci, Climbing Stairs, Pow(x,n)", "Visualize recursion tree for Fibonacci and Tower of Hanoi")
    ],
    4: [
        ("Python", "Functions & Scope", "Automate Ch.3", "Power of Three, Happy Number", "Build math library with functions for primes, factorials, GCD/LCM"),
        ("C/System", "Functions & Call Stack", "K&R Ch.4, Beej §3", "Factorial Trailing Zeroes, Count Primes", "Recursive factorial with manual stack trace output at each level"),
        ("Design/Math", "Divide & Conquer", "CLRS §4.4-4.5", "Merge Two Sorted Lists, Sort List", "Implement merge sort and quicksort with comparison counter")
    ],
    5: [
        ("Python", "Dictionaries & Sets", "Automate Ch.5", "Contains Duplicate, Single Number", "Word frequency analyzer for text files with top-N display"),
        ("C/System", "Pointers Fundamentals", "K&R Ch.5.6-5.10", "Reverse Linked List (in C)", "Swap function using pointers, pointer arithmetic exercises"),
        ("Design/Math", "Sorting Algorithms: Comparison", "CLRS §6.1-6.4", "Sort Colors, Sort Array", "Implement bubble, insertion, selection sorts and benchmark")
    ],
    6: [
        ("Python", "String Manipulation", "Automate Ch.6", "Valid Anagram, Group Anagrams", "Build Caesar cipher encoder/decoder with frequency analysis"),
        ("C/System", "Dynamic Memory Allocation", "K&R Ch.7.8.5, Beej §4", "Merge Sorted Array", "Dynamic array implementation with resize/grow functionality"),
        ("Design/Math", "Heaps & Priority Queues", "CLRS §6.5", "Kth Largest Element, Last Stone Weight", "Min-heap and max-heap from scratch with heapify operations")
    ],
    7: [
        ("Python", "File I/O & Exception Handling", "Automate Ch.8-9", "Valid Parentheses, Min Stack", "Log parser that extracts errors/warnings from Apache logs"),
        ("C/System", "File Operations in C", "K&R Ch.7.1-7.6", "Read N Characters (simulated)", "File copy utility with progress bar (like 'cp' command)"),
        ("Design/Math", "Hash Tables Theory", "CLRS §11.1-11.3", "Two Sum II, 3Sum, 4Sum", "Implement hash table with chaining and open addressing")
    ],
    8: [
        ("Python", "Regular Expressions", "Automate Ch.7", "Implement strStr(), Repeated Substring", "Email validator and phone number formatter using regex"),
        ("C/System", "Structs & Typedef", "K&R Ch.6.1-6.5", "Intersection of Two Arrays", "Student database with search/sort by name/GPA/ID"),
        ("Design/Math", "Graph Representations", "CLRS §22.1", "Find Center, Find Judge", "Implement adjacency matrix and adjacency list representations")
    ],
    9: [
        ("Python", "OOP Basics: Classes & Objects", "Python Official Tutorial §9.1-9.5", "Design HashSet, Design HashMap", "Create library management system with Book/Member/Transaction classes"),
        ("C/System", "Preprocessor & Macros", "K&R Ch.4.11", "Majority Element", "DEBUG macro system with file/line/function tracking"),
        ("Design/Math", "Stack & Queue ADTs", "CLRS §10.1", "Queue using Stacks, Stack using Queues", "Balanced parentheses checker and expression evaluator")
    ],
    10: [
        ("Python", "Inheritance & Polymorphism", "Python Official Tutorial §9.5-9.8", "Min Stack, Max Stack", "Shape hierarchy (Circle/Rectangle/Triangle) with area/perimeter"),
        ("C/System", "Memory Debugging: Valgrind", "Valgrind Manual Ch.2-3", "Linked List Cycle", "Fix provided buggy C code with memory leaks using Valgrind"),
        ("Design/Math", "Binary Search Variants", "CLRS §2.3.3", "Search Insert Position, First Bad Version", "Implement binary search, lower_bound, upper_bound variants")
    ],
    11: [
        ("Python", "Iterators & Generators", "Python Official Tutorial §9.9-9.10", "Range Sum Query, Running Sum", "Fibonacci generator and prime number generator (infinite)"),
        ("C/System", "Bitwise Operations", "K&R Ch.2.9", "Single Number, Number of 1 Bits", "Bit manipulation toolkit: set/clear/toggle/check individual bits"),
        ("Design/Math", "Greedy Algorithms Intro", "CLRS §16.1-16.2", "Buy Sell Stock, Jump Game", "Activity selection problem and coin change (greedy)")
    ],
    12: [
        ("Python", "Decorators & Context Managers", "Python Official Tutorial §9.11, PEP 343", "LRU Cache, Design Browser History", "Timing decorator and retry decorator with exponential backoff"),
        ("C/System", "Make & Build Systems", "GNU Make Manual Ch.1-2", "Pascal's Triangle", "Multi-file C project with Makefile (separate compilation)"),
        ("Design/Math", "Dynamic Programming Intro", "CLRS §15.1-15.2", "Climbing Stairs, Min Cost Climbing", "Solve Fibonacci with memoization and tabulation comparison")
    ],
    
    # PHASE 2: INTERMEDIATE (Weeks 13-24)
    13: [
        ("Python", "Linked Lists Implementation", "CLRS §10.2", "Reverse Linked List, Remove Nth Node", "Singly and doubly linked list with full CRUD operations"),
        ("C/System", "Linked Lists in C", "K&R Ch.6 (Custom Structures)", "Middle of Linked List, Palindrome Linked List", "Generic linked list in C using void pointers"),
        ("Design/Math", "Amortized Analysis", "CLRS §17.1-17.3", "Design Dynamic Array", "Dynamic array with doubling strategy and amortized cost proof")
    ],
    14: [
        ("Python", "Binary Trees Basics", "CLRS §12.1-12.2", "Max Depth, Min Depth, Invert Tree", "Binary tree with preorder/inorder/postorder traversals"),
        ("C/System", "Tree Structures in C", "K&R Ch.6 (Structures)", "Same Tree, Subtree of Another", "Binary tree in C with malloc'd nodes and traversal functions"),
        ("Design/Math", "Tree Properties & Theorems", "CLRS §12.3", "Symmetric Tree, Balanced Binary Tree", "Calculate height, count nodes, find diameter of binary tree")
    ],
    15: [
        ("Python", "Binary Search Trees", "CLRS §12.1-12.3", "Validate BST, Kth Smallest in BST", "BST with insert/delete/search and in-order successor"),
        ("C/System", "Advanced Pointers: Function Pointers", "K&R Ch.5.11", "Find Peak Element", "Generic sorting function using qsort() with custom comparators"),
        ("Design/Math", "Balanced Trees: AVL Intro", "CLRS §13.1-13.2", "Delete Node in BST", "Implement AVL tree rotations (LL, RR, LR, RL)")
    ],
    16: [
        ("Python", "Tree Traversals: Iterative", "CLRS §12.1", "Inorder Traversal, Preorder Traversal", "Morris traversal (O(1) space) for inorder traversal"),
        ("C/System", "System Calls: fork, exec", "Beej §5-6", "Generate Parentheses", "Mini shell that executes commands with fork/exec (like bash)"),
        ("Design/Math", "Red-Black Trees", "CLRS §13.3-13.4", "BST Iterator", "Trace red-black tree insertions and prove black-height property")
    ],
    17: [
        ("Python", "Heaps & heapq Module", "Python Library Ref: heapq module", "Top K Frequent, Kth Largest in Stream", "Task scheduler using priority queue with deadlines"),
        ("C/System", "Inter-Process Communication", "Beej §7", "Task Scheduler", "Producer-consumer using pipes between parent/child processes"),
        ("Design/Math", "Graph Traversal: BFS", "CLRS §22.2", "Level Order, Zigzag Level Order", "Shortest path in unweighted graph using BFS")
    ],
    18: [
        ("Python", "Graph Algorithms: BFS/DFS", "CLRS §22.2-22.3", "Number of Islands, Clone Graph", "Graph class with BFS/DFS and cycle detection"),
        ("C/System", "Sockets Basics", "Beej §8-10", "Word Ladder (BFS)", "Echo server and client using TCP sockets"),
        ("Design/Math", "Graph Traversal: DFS", "CLRS §22.3", "Course Schedule, Course Schedule II", "Topological sort and strongly connected components (Tarjan)")
    ],
    19: [
        ("Python", "Shortest Paths: Dijkstra", "CLRS §24.3", "Network Delay Time, Path with Max Probability", "Dijkstra's algorithm with priority queue implementation"),
        ("C/System", "Network Programming Patterns", "Beej §11-12", "Cheapest Flights K Stops", "Multi-threaded chat server handling multiple clients"),
        ("Design/Math", "Single-Source Shortest Paths", "CLRS §24.1-24.2", "Cheapest Flights, Min Cost to Hire K", "Bellman-Ford with negative cycle detection")
    ],
    20: [
        ("Python", "Dynamic Programming: 1D", "CLRS §15.3", "House Robber, Decode Ways, Word Break", "Solve: coin change, decode ways, word break (1D DP)"),
        ("C/System", "Memory Management Strategies", "CSAPP §9.9-9.11", "Coin Change, Perfect Squares", "Memory pool allocator (like a simple malloc)"),
        ("Design/Math", "DP: Optimal Substructure", "CLRS §15.3", "Longest Increasing Subsequence, Max Subarray", "Proof of optimal substructure for LIS and knapsack")
    ],
    21: [
        ("Python", "Dynamic Programming: 2D", "CLRS §15.4", "Unique Paths, Min Path Sum, LCS", "Grid DP: unique paths, min path sum, longest common subsequence"),
        ("C/System", "Cache Optimization", "CSAPP §6", "Triangle (min path sum)", "Matrix multiplication with cache-friendly access patterns"),
        ("Design/Math", "DP: Overlapping Subproblems", "CLRS §15.3", "Edit Distance, Interleaving String", "Compare recursive, memoized, and tabulated DP solutions")
    ],
    22: [
        ("Python", "Backtracking Algorithms", "CLRS Ch.8 Supplement", "Permutations, Combinations, Subsets", "Generate all permutations, combinations, and subsets"),
        ("C/System", "Compiler Basics: Lexing", "Dragon Book §1-3", "Letter Combinations Phone, Palindrome Partition", "Tokenizer for simple arithmetic expressions"),
        ("Design/Math", "Search Space Pruning", "CLRS Ch.8 Supplement", "N-Queens, N-Queens II", "N-Queens with backtracking and constraint checking")
    ],
    23: [
        ("Python", "Trie Data Structure", "CLRS §12 Extension", "Implement Trie, Word Search II", "Autocomplete system using trie (like search suggestions)"),
        ("C/System", "Compiler: Parsing", "Dragon Book §4", "Add and Search Word, Replace Words", "Recursive descent parser for arithmetic expressions"),
        ("Design/Math", "String Algorithms", "CLRS §32.1-32.3", "Longest Common Prefix, Repeated DNA", "Rabin-Karp and KMP string matching algorithms")
    ],
    24: [
        ("Python", "Union-Find (Disjoint Set)", "CLRS §21.1-21.3", "Number Connected Components, Graph Valid Tree", "Union-Find with path compression and union by rank"),
        ("C/System", "Operating System Concepts", "OSTEP Ch.1-5", "Accounts Merge, Redundant Connection", "Round-robin process scheduler simulation"),
        ("Design/Math", "Minimum Spanning Trees", "CLRS §23.1-23.2", "Min Cost Connect Points, Water/Land", "Kruskal's and Prim's MST implementations")
    ],
    
    # PHASE 3: ADVANCED (Weeks 25-36)
    25: [
        ("Python", "Advanced DP: Knapsack", "CLRS §15.3-15.4", "Partition Equal Subset, Target Sum", "0/1 knapsack, unbounded knapsack, and partition problems"),
        ("C/System", "Concurrency: Threads", "OSTEP Ch.26-27", "Coin Change, Coin Change 2", "Multi-threaded web server with thread pool"),
        ("Design/Math", "NP-Completeness Intro", "CLRS §34.1-34.2", "Partition to K Equal Sum", "Reduce 3-SAT to Clique problem")
    ],
    26: [
        ("Python", "Segment Trees", "Handbook Ch.9.3", "Range Sum Query Mutable, Count Smaller", "Segment tree for range queries (sum, min, max)"),
        ("C/System", "Thread Synchronization", "OSTEP Ch.28-30", "Design Bounded Blocking Queue", "Dining philosophers problem with mutexes"),
        ("Design/Math", "Approximation Algorithms", "CLRS §35.1-35.2", "Set Cover (greedy)", "2-approximation for vertex cover problem")
    ],
    27: [
        ("Python", "Binary Indexed Trees (Fenwick)", "Handbook Ch.9.4", "Count Smaller After Self, Reverse Pairs", "Fenwick tree for prefix sums and range updates"),
        ("C/System", "Lock-Free Programming Basics", "Art of Multiprocessor Ch.10", "Binary Search Tree Iterator", "Lock-free queue using compare-and-swap (CAS)"),
        ("Design/Math", "Randomized Algorithms", "CLRS §5.1-5.2", "Random Pick with Weight, Shuffle Array", "Randomized quicksort and Monte Carlo primality test")
    ],
    28: [
        ("Python", "Suffix Arrays & LCP", "Handbook Ch.26", "Longest Duplicate Substring, Distinct Subseq", "Build suffix array and LCP array for pattern matching"),
        ("C/System", "Virtual Memory Concepts", "OSTEP Ch.13-16", "LRU Cache, LFU Cache", "Page replacement simulator (FIFO, LRU, Optimal)"),
        ("Design/Math", "Advanced Graph: Network Flow", "CLRS §26.1-26.2", "Maximum Flow, Min Cut", "Ford-Fulkerson max flow with BFS (Edmonds-Karp)")
    ],
    29: [
        ("Python", "KMP String Matching", "CLRS §32.3-32.4", "Implement strStr() KMP, Shortest Palindrome", "KMP pattern matching with failure function construction"),
        ("C/System", "File Systems Basics", "OSTEP Ch.39-40", "Design File System, In-Memory FS", "Simple in-memory file system with directories"),
        ("Design/Math", "Max Flow Min Cut Theorem", "CLRS §26.2", "Max Bipartite Matching", "Bipartite matching using max flow")
    ],
    30: [
        ("Python", "Topological Sorting", "CLRS §22.4", "Course Schedule II, Alien Dictionary", "Topological sort using Kahn's algorithm and DFS"),
        ("C/System", "I/O Scheduling", "OSTEP Ch.37", "Task Scheduler, Reorganize String", "Disk scheduling algorithms (FCFS, SSTF, SCAN)"),
        ("Design/Math", "Strongly Connected Components", "CLRS §22.5", "Strongly Connected Components, Critical Connections", "Kosaraju's algorithm implementation")
    ],
    31: [
        ("Python", "Advanced Backtracking", "CLRS Ch.8 Supplement", "Sudoku Solver, Word Search", "Sudoku solver with constraint propagation optimization"),
        ("C/System", "Memory Hierarchies", "CSAPP §6", "Robot Room Cleaner, Expression Add Operators", "Cache behavior simulator for different access patterns"),
        ("Design/Math", "Branch and Bound", "CLRS Ch.35 Supplement", "Traveling Salesman (small), Assignment Problem", "Traveling salesman with branch and bound")
    ],
    32: [
        ("Python", "Monotonic Stack/Queue", "Elements of Programming Interviews Ch.8", "Largest Rectangle, Maximal Rectangle", "Next greater element using monotonic stack"),
        ("C/System", "System Performance Profiling", "CSAPP §5.14, perf tutorial", "Trapping Rain Water, Container with Water", "Profile C program and optimize hot spots"),
        ("Design/Math", "Computational Geometry Basics", "CLRS §33.1-33.2", "Convex Hull, Max Points on Line", "Graham scan and Jarvis march convex hull algorithms")
    ],
    33: [
        ("Python", "Sliding Window Technique", "Elements of Programming Interviews Ch.5", "Min Window Substring, Longest Substring K Distinct", "Max/min in sliding window and longest substring problems"),
        ("C/System", "Assembly Language Basics", "CSAPP §3", "Permutation in String, Find All Anagrams", "Write simple functions in x86-64 assembly"),
        ("Design/Math", "Sweep Line Algorithms", "CLRS §33.3", "Meeting Rooms II, Merge Intervals", "Interval scheduling and line segment intersection")
    ],
    34: [
        ("Python", "Two Pointers Technique", "Elements of Programming Interviews Ch.5", "3Sum, 4Sum, Container With Most Water", "Two-pointer problems: 3Sum, container with most water"),
        ("C/System", "Linking & Loading", "CSAPP §7", "Trapping Rain Water, Remove Duplicates", "Create and use static and shared libraries in C"),
        ("Design/Math", "Linear Programming Basics", "CLRS §29.1-29.2", "Max Profit Assignment", "Solve LP problems using simplex method (by hand)")
    ],
    35: [
        ("Python", "Bit Manipulation Mastery", "Elements of Programming Interviews Ch.4", "Single Number II, Bitwise AND of Range", "Count set bits, power of 2, XOR tricks compilation"),
        ("C/System", "Security: Buffer Overflows", "CSAPP §3.10", "Sum of Two Integers (bitwise)", "Demonstrate buffer overflow and implement protection"),
        ("Design/Math", "Cryptography Basics", "CLRS §31.6-31.7", "Power (modular exponentiation)", "Implement RSA encryption/decryption")
    ],
    36: [
        ("Python", "Python Internals: CPython", "CPython Source", "Custom Sort String, Sort Characters", "Explore CPython source: object.c, dictobject.c"),
        ("C/System", "Advanced C: Undefined Behavior", "C Standards Doc", "Reverse Bits, Reverse Integer", "Identify and fix undefined behavior in sample C code"),
        ("Design/Math", "Automata Theory", "Sipser Ch.1", "Regular Expression Matching, Wildcard Matching", "Build DFA for regex and simulate on input strings")
    ],
    
    # PHASE 4: MASTERY (Weeks 37-48)
    37: [
        ("Python", "Design Patterns: Creational", "Gang of Four Ch.3", "Design Pattern Implementation, Clone Graph", "Implement Singleton, Factory, Builder, Prototype patterns"),
        ("C/System", "Linux Kernel Modules", "Linux Kernel Development Ch.16-17", "Design Underground System", "Simple 'Hello World' loadable kernel module"),
        ("Design/Math", "Context-Free Grammars", "Sipser Ch.2", "Valid Parenthesis String, Remove Invalid", "Design CFG for balanced parentheses and palindromes")
    ],
    38: [
        ("Python", "Design Patterns: Structural", "Gang of Four Ch.4", "Adapter Pattern, Composite Pattern", "Implement Adapter, Proxy, Decorator, Facade patterns"),
        ("C/System", "Device Drivers Basics", "Linux Device Drivers Ch.1-3", "Design Hit Counter, Logger Rate Limiter", "Character device driver with read/write operations"),
        ("Design/Math", "Pushdown Automata", "Sipser Ch.2", "Decode String, Basic Calculator II", "Design PDA for {a^n b^n | n >= 0}")
    ],
    39: [
        ("Python", "Design Patterns: Behavioral", "Gang of Four Ch.5", "Observer Pattern, Iterator Pattern", "Implement Observer, Strategy, Command, State patterns"),
        ("C/System", "Real-Time Systems", "Real-Time Systems Ch.4-5", "Design Parking System, Seat Reservation", "Rate monotonic scheduling simulation"),
        ("Design/Math", "Turing Machines", "Sipser Ch.3", "Add Strings, Multiply Strings", "Design TM for palindrome recognition")
    ],
    40: [
        ("Python", "Concurrency: asyncio", "Python Library Ref: asyncio", "Async Web Scraper, Parallel Courses", "Async web scraper fetching multiple URLs concurrently"),
        ("C/System", "Embedded Programming", "Making Embedded Systems Ch.1-3", "Fizz Buzz Multithreaded, Print in Order", "LED blink program for Arduino/Raspberry Pi"),
        ("Design/Math", "Decidability", "Sipser Ch.4", "Is Graph Bipartite, Possible Bipartition", "Prove halting problem is undecidable")
    ],
    41: [
        ("Python", "Microservices Architecture", "Building Microservices Ch.1-4", "Design API Gateway, Rate Limiter", "Design REST API for e-commerce (products, orders, users)"),
        ("C/System", "High-Performance Computing", "Parallel Programming Ch.1-2", "Parallel Courses II, Build Array Concurrent", "Parallel matrix multiplication using OpenMP"),
        ("Design/Math", "Reducibility", "Sipser Ch.5", "Word Ladder, Word Ladder II", "Show HALT_TM reduces to EMPTY_TM")
    ],
    42: [
        ("Python", "Testing: Unit & Integration", "pytest Documentation: Getting Started", "Test Suite Design, Valid Parentheses", "Write pytest suite with fixtures, mocks, parametrize"),
        ("C/System", "Compiler Optimization", "Dragon Book §8-9", "Basic Calculator, Expression Tree", "Implement constant folding optimization pass"),
        ("Design/Math", "Complexity Classes", "Sipser Ch.7", "Subset Sum, Hamiltonian Path", "Explore P, NP, NP-Complete relationships")
    ],
    43: [
        ("Python", "Performance Optimization", "High Performance Python Ch.2-3", "Profile & Optimize, LRU Cache", "Profile Python code with cProfile and optimize bottlenecks"),
        ("C/System", "SIMD Programming", "Intel Intrinsics Guide: Getting Started", "Range Sum Query 2D, Matrix Block Sum", "Vectorized dot product using SSE/AVX intrinsics"),
        ("Design/Math", "Advanced Complexity", "Sipser Ch.8-9", "Longest Palindromic Subsequence", "Space complexity and PSPACE examples")
    ],
    44: [
        ("Python", "Machine Learning Fundamentals", "Hands-On ML Ch.1-2", "Linear Regression, K-Means Clustering", "Linear regression from scratch and with sklearn"),
        ("C/System", "GPU Programming Intro", "CUDA by Example Ch.1-4", "Matrix Multiplication, Vector Add", "Vector addition kernel in CUDA"),
        ("Design/Math", "Probability in CS", "CLRS Appendix C", "Random Pick Index, Linked List Random", "Expected runtime of randomized algorithms")
    ],
    45: [
        ("Python", "Data Engineering Basics", "Python for Data Analysis Ch.5-7", "ETL Pipeline, Top K Frequent Words", "CSV ETL pipeline: extract, transform, load with pandas"),
        ("C/System", "Distributed Systems Basics", "Distributed Systems (Tanenbaum) Ch.5", "Design Tic-Tac-Toe, Design Snake Game", "Implement 2-phase commit protocol simulation"),
        ("Design/Math", "Game Theory Basics", "Algorithmic Game Theory Ch.1-2", "Nim Game, Predict Winner, Stone Game", "Solve prisoner's dilemma and Nash equilibrium")
    ],
    46: [
        ("Python", "System Design: Scalability", "Designing Data-Intensive Apps Ch.1", "Design Twitter, Design TinyURL", "Design URL shortener with load estimation"),
        ("C/System", "Consensus Algorithms", "Raft Paper (in Search of Understandable)", "Design Leaderboard, Top K Frequent", "Raft leader election simulation"),
        ("Design/Math", "Information Theory Basics", "Elements of Information Theory Ch.2", "Huffman Encoding, Data Compression", "Calculate entropy and information content")
    ],
    47: [
        ("Python", "Capstone Project Planning", "N/A", "Design comprehensive project combining patterns", "Design full-stack app: web scraper + API + dashboard"),
        ("C/System", "Capstone Project: C Component", "N/A", "Optimize critical path with C", "Build performance-critical data processor in C"),
        ("Design/Math", "Capstone: Algorithm Design", "N/A", "Analyze and optimize algorithms", "Design custom algorithm with complexity analysis")
    ],
    48: [
        ("Python", "Capstone: Implementation", "N/A", "Complete implementation milestone", "Complete implementation with documentation and tests"),
        ("C/System", "Capstone: Integration & Testing", "N/A", "Integration testing", "Integrate C module with Python using ctypes/CFFI"),
        ("Design/Math", "Capstone: Analysis & Presentation", "N/A", "Performance benchmarks", "Performance benchmarks and final presentation")
    ]
}

focus_colors = {
    "Python": colors.HexColor('#E3F2FD'),
    "C/System": colors.HexColor('#E8F5E9'),
    "Design/Math": colors.HexColor('#FFF9C4')
}

# Custom page template with page numbers only (NO LEGEND)
def add_page_footer(canvas, doc):
    page_num = canvas.getPageNumber()
    
    canvas.saveState()
    # Page number only
    canvas.setFont('Helvetica', 9)
    canvas.drawString(doc.leftMargin, 25, f"Page {page_num}")
    canvas.drawRightString(landscape(LETTER)[0] - doc.rightMargin, 25, f"Page {page_num}")
    canvas.restoreState()

# Generate curriculum content
day_counter = 1
weeks_on_page = 0

for week in range(1, 49):
    # Week header with more spacing
    content.append(Paragraph(f"━━━ Week {week} ━━━", styles['HeadingCustom']))
    content.append(Spacer(1, 2))
    
    # Column headers (bold and underlined) - NO CHECKBOX COLUMN
    header_row = [[
        Paragraph("<b><u>Day</u></b>", styles['HeaderCell']),
        Paragraph("<b><u>Focus</u></b>", styles['HeaderCell']),
        Paragraph("<b><u>Topic</u></b>", styles['HeaderCell']),
        Paragraph("<b><u>Reading</u></b>", styles['HeaderCell']),
        Paragraph("<b><u>LeetCode</u></b>", styles['HeaderCell']),
        Paragraph("<b><u>Project</u></b>", styles['HeaderCell'])
    ]]
    
    header_table = Table(header_row, colWidths=[30, 65, 145, 105, 105, 165])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#CCCCCC')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.8, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    
    content.append(header_table)
    content.append(Spacer(1, 1))
    
    for day_data in curriculum[week]:
        focus, topic, reading, leetcode, project = day_data
        
        table_data = [[
            Paragraph(f"<b>{day_counter}</b>", styles['BodyCustom']),
            Paragraph(f"<b>{focus}</b>", styles['BodyCustom']),
            Paragraph(topic, styles['BodyCustom']),
            Paragraph(reading, styles['BodyCustom']),
            Paragraph(leetcode, styles['BodyCustom']),
            Paragraph(project, styles['BodyCustom'])
        ]]
        
        t = Table(table_data, colWidths=[30, 65, 145, 105, 105, 165])
        t.setStyle(TableStyle([
            ('BACKGROUND', (1,0), (1,0), focus_colors[focus]),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('LEFTPADDING', (0,0), (-1,-1), 3),
            ('RIGHTPADDING', (0,0), (-1,-1), 3),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ]))
        
        content.append(t)
        content.append(Spacer(1, 1))
        day_counter += 1
    
    content.append(Spacer(1, 4))
    weeks_on_page += 1
    
    # Page break after every 4 weeks (but keep week 48 with weeks 45-47)
    if weeks_on_page >= 4 and week < 45:
        content.append(PageBreak())
        weeks_on_page = 0

# ========== FINAL PAGES: CONCLUSION & CANON ==========
content.append(PageBreak())

content.append(Paragraph("🎓 Congratulations! You've Completed the Journey!", styles['TitleCustom']))
content.append(Spacer(1, 10))

content.append(Paragraph("📊 Your Achievement Checklist", styles['SectionHeader']))
content.append(Paragraph(
    "If you've made it through all 48 weeks, you've accomplished something remarkable:",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

checklist_data = [
    ["□", "Completed 144 days of structured study across Python, C, and algorithms"],
    ["□", "Solved 300+ LeetCode problems spanning all difficulty levels"],
    ["□", "Built 144 hands-on projects demonstrating practical mastery"],
    ["□", "Read seminal texts: CLRS, K&R, Sipser, CSAPP, and more"],
    ["□", "Created a comprehensive GitHub portfolio showcasing your work"],
    ["□", "Mastered data structures: arrays, trees, graphs, heaps, tries"],
    ["□", "Implemented classic algorithms: sorting, searching, DP, graph traversal"],
    ["□", "Learned systems programming: memory management, concurrency, networking"],
    ["□", "Understood theoretical foundations: complexity theory, computability"],
    ["□", "Completed a capstone project integrating all three tracks"]
]

achievement_table = Table(checklist_data, colWidths=[25, 650])
achievement_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.lightgrey),
]))

content.append(achievement_table)
content.append(Spacer(1, 10))

content.append(Paragraph("🚀 What's Next? Your Path Forward", styles['SectionHeader']))
content.append(Paragraph(
    "<b>1. Contribute to Open Source:</b> Give back to the community. Find projects on GitHub, fix bugs, add features. "
    "<b>2. Specialize Deeper:</b> Choose a domain: ML, Distributed Systems, Compilers, Security, Graphics, Databases, or OS. "
    "<b>3. Teach Others:</b> Write blogs, create tutorials, mentor beginners. Teaching solidifies understanding. "
    "<b>4. Build Something Real:</b> Create a product people use. Real-world problems teach what textbooks can't. "
    "<b>5. Never Stop Learning:</b> Technology evolves. Stay curious, stay humble, keep building.",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("💭 Final Reflections", styles['SectionHeader']))
content.append(Paragraph(
    "This syllabus was never just about learning Python or C or algorithms. It was about transforming how you think—developing "
    "the mental models, problem-solving skills, and persistence that separate great programmers from the rest. "
    "You've learned to think recursively, reason about complexity, debug ruthlessly, and build systems that work.",
    styles['BodyJustify']
))
content.append(Spacer(1, 6))

content.append(Paragraph(
    "That's what makes you a programmer now. Not the syntax you've memorized, but the way you approach problems. "
    "The confidence that no matter how complex the challenge, you can break it down, understand it, and solve it.",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph(
    '"The programmer, like the poet, works only slightly removed from pure thought-stuff. He builds castles in the air, from air, '
    'creating by exertion of the imagination." — <i>Frederick P. Brooks Jr., The Mythical Man-Month</i>',
    styles['QuoteStyle']
))
content.append(Spacer(1, 8))

content.append(Paragraph(
    "<b>Now go build something amazing. The world needs what you can create.</b> 🌟",
    styles['BodyJustify']
))

content.append(PageBreak())

# ========== LAST PAGE: THE CANON ==========
content.append(Paragraph("📖 The Essential Canon: Greatest Books in Computer Science", styles['TitleCustom']))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Algorithms & Data Structures</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <i>Introduction to Algorithms</i> by Cormen, Leiserson, Rivest, and Stein (CLRS) — The definitive algorithm reference<br/>"
    "• <i>The Art of Computer Programming</i> by Donald Knuth — The magnum opus of computer science (Volumes 1-4A)<br/>"
    "• <i>Algorithm Design</i> by Kleinberg and Tardos — Excellent for developing algorithmic intuition",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("<b>Systems & Programming Languages</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <i>The C Programming Language</i> by Kernighan and Ritchie (K&R) — The bible of C, written by its creators<br/>"
    "• <i>Computer Systems: A Programmer's Perspective</i> by Bryant and O'Hallaron (CSAPP) — How computers really work<br/>"
    "• <i>Operating Systems: Three Easy Pieces</i> by Arpaci-Dusseau (OSTEP) — Modern OS concepts, freely available online<br/>"
    "• <i>Structure and Interpretation of Computer Programs</i> by Abelson and Sussman (SICP) — Mind-expanding programming paradigms<br/>"
    "• <i>Compilers: Principles, Techniques, and Tools</i> by Aho, Lam, Sethi, and Ullman (Dragon Book) — The compiler bible<br/>"
    "• <i>Computer Networking: A Top-Down Approach</i> by Kurose and Ross — Comprehensive networking guide",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("<b>Theory & Mathematics</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <i>Introduction to the Theory of Computation</i> by Michael Sipser — Beautiful exploration of computability and complexity<br/>"
    "• <i>Concrete Mathematics</i> by Graham, Knuth, and Patashnik — The mathematical foundations underlying computer science<br/>"
    "• <i>Gödel, Escher, Bach: An Eternal Golden Braid</i> by Douglas Hofstadter — A Pulitzer Prize-winning journey through computation, consciousness, and creativity<br/>"
    "• <i>Algorithmic Game Theory</i> edited by Nisan, Roughgarden, Tardos, and Vazirani — Game theory applications in CS",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))

content.append(Paragraph("<b>Software Engineering & Design</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <i>Design Patterns: Elements of Reusable Object-Oriented Software</i> by Gamma, Helm, Johnson, and Vlissides (Gang of Four) — The classic on design patterns<br/>"
    "• <i>The Mythical Man-Month</i> by Frederick P. Brooks Jr. — Timeless wisdom on software project management<br/>"
    "• <i>Code Complete</i> by Steve McConnell — Comprehensive guide to software construction<br/>"
    "• <i>Clean Code</i> by Robert C. Martin — A handbook of agile software craftsmanship",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("<b>Specialized Topics</b>", styles['SectionHeader']))
content.append(Paragraph(
    "• <i>Competitive Programmer's Handbook</i> by Antti Laaksonen — Advanced data structures and algorithms (free PDF)<br/>"
    "• <i>Elements of Programming Interviews in Python</i> by Aziz, Lee, and Prakash — Interview preparation with practical problems<br/>"
    "• <i>Python for Data Analysis</i> by Wes McKinney — Data manipulation with Pandas<br/>"
    "• <i>Hands-On Machine Learning</i> by Aurélien Géron — Practical ML with Scikit-Learn and TensorFlow<br/>"
    "• <i>CUDA by Example</i> by Sanders and Kandrot — Introduction to GPU programming<br/>"
    "• <i>High Performance Python</i> by Gorelick and Ozsvald — Optimization techniques<br/>"
    "• <i>Building Microservices</i> by Sam Newman — Modern distributed architecture<br/>"
    "• <i>Designing Data-Intensive Applications</i> by Martin Kleppmann — The big ideas behind reliable, scalable systems<br/>"
    "• <i>Distributed Systems</i> by Tanenbaum and Van Steen — Principles and paradigms<br/>"
    "• <i>The Art of Multiprocessor Programming</i> by Herlihy and Shavit — Concurrent programming principles<br/>"
    "• <i>Linux Device Drivers</i> by Corbet, Rubini, and Kroah-Hartman — Kernel programming<br/>"
    "• <i>Linux Kernel Development</i> by Robert Love — Understanding the Linux kernel<br/>"
    "• <i>Making Embedded Systems</i> by Elecia White — Design patterns for great embedded software<br/>"
    "• <i>Real-Time Systems</i> by Jane W. S. Liu — Real-time and embedded systems<br/>"
    "• <i>Elements of Information Theory</i> by Cover and Thomas — Information theory fundamentals<br/>"
    "• <i>Parallel Programming</i> by Pacheco — Introduction to parallel programming with MPI and OpenMP",
    styles['BodyJustify']
))
content.append(Spacer(1, 8))
content.append(Paragraph(
    "<b>Extended reading on these and more topics above. Read on to learn more.</b>",
    styles['BodyJustify']
))
content.append(Spacer(1, 10))

content.append(Paragraph("— End of Syllabus —", styles['SubtitleCustom']))

# Build PDF with custom page template
doc.build(content, onFirstPage=add_page_footer, onLaterPages=add_page_footer)

print(f"✅ Syllabus generated successfully: {output_pdf_path}")
print(f"📊 Total days: {day_counter - 1}")
print(f"📚 Coverage: Python, C/Systems Programming, Algorithms & Theory")
print(f"📄 Features: Landscape format, TOC, 4 weeks per page, 300+ LeetCode problems, legend footer")
