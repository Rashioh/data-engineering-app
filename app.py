import streamlit as st

# Page config
st.set_page_config(page_title="📚 Learn Data Engineering", page_icon=":books:")

# App title
st.title("📚 Learn Data Engineering (Beginner App)")

st.markdown("""
Welcome to your beginner-friendly Data Engineering course!  
Use the menu on the left to pick a lesson and start learning. 🚀
""")

# Define lessons
lessons = {
    "1️⃣ What is Data Engineering?": """
**Data Engineering** is about designing, building, and maintaining systems to collect, move, store, and process data.  
Think of it as building the highways that data travels on so it can be used by analysts, data scientists, and applications.

As a data engineer you often:
- Collect raw data from APIs, files, or databases
- Clean and transform it to fix errors or standardize formats
- Load it into data warehouses or databases
- Build automated **pipelines** to refresh data regularly
- Monitor data quality and performance

It's a creative and high-impact field that powers data-driven decisions!
""",

    "2️⃣ Databases & SQL": """
Most data lives in **databases**.

🧩 *Relational Databases* (PostgreSQL, MySQL, SQL Server):
- Store data in tables with rows and columns
- Use **SQL** (Structured Query Language) to query and update data

🧰 Example SQL:
```sql
SELECT name, email 
FROM customers 
WHERE country = 'USA'; """}
