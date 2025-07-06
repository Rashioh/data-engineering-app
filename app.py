import streamlit as st

# Set page config
st.set_page_config(page_title="📚 Learn Data Engineering", page_icon=":books:")

# App title
st.title("📚 Learn Data Engineering (Beginner App)")

st.markdown("""
Welcome to your beginner-friendly Data Engineering course!  
Use the menu on the left to pick a lesson and start learning.
""")

# Sidebar for navigation
st.sidebar.title("📂 Lessons")

# Define real lessons
lessons = {
    "1️⃣ What is Data Engineering?": """
**Data Engineering** is about designing, building, and maintaining systems that move, store, and process data.  
Think of it as building the roads and bridges that data travels on.

As a data engineer you:
- Collect data from different sources (web, databases, APIs)
- Clean and transform it (fix errors, format it properly)
- Store it in databases or data warehouses so analysts and data scientists can use it
- Automate the flow using pipelines and schedulers

It's one of the fastest-growing fields in tech!
""",

    "2️⃣ Databases & SQL": """
Data is usually stored in **databases**.

🧩 *Relational Databases* (e.g., PostgreSQL, MySQL, SQL Server):
- Store data in tables with rows & columns
- Use SQL (Structured Query Language) to query data

🧰 Example SQL:
```sql
SELECT name, email FROM customers WHERE country = 'USA';
