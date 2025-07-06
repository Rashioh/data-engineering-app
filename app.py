import streamlit as st

# Set the page configuration
st.set_page_config(page_title="📚 Learn Data Engineering", page_icon=":books:")

# App title
st.title("📚 Learn Data Engineering (Beginner App)")

st.markdown("""
Welcome! Use the menu on the left to pick a lesson and start learning 🚀
""")

# Define lessons dictionary
lessons = {
    "1️⃣ What is Data Engineering?": """
**Data Engineering** is about designing, building, and maintaining systems to collect, move, store, and process data.

Think of it as building roads that data travels on so analysts and data scientists can use it.

As a data engineer you might:
- Collect raw data from APIs, logs, databases
- Clean and transform it
- Load it into warehouses
- Automate pipelines
- Monitor and keep data flowing
"""},

    "2️⃣ Databases & SQL": """
Most data is stored in **databases**.

- *Relational Databases*: PostgreSQL, MySQL
- Use **SQL** to ask questions about data

Example:
```sql
SELECT name, email FROM users WHERE country = 'USA'; """

