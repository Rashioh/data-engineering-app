import streamlit as st

# Set page config
st.set_page_config(page_title="📚 Learn Data Engineering", page_icon=":books:")

# App title
st.title("📚 Learn Data Engineering (Beginner App)")

# Sidebar for navigation
st.sidebar.title("📂 Lessons")

# Define lessons
lessons = {
    "Intro to Data Engineering": "Data Engineering helps move data from one place to another, clean it, and store it so others can use it.",
    "Databases & SQL": "Databases store data in tables; SQL is a language to query data (e.g., SELECT * FROM users).",
    "Data Pipelines": "Pipelines move data automatically on a schedule. Tools: Airflow, dbt, etc.",
    "ETL & ELT": "ETL: Extract, Transform, Load. ELT: Extract, Load, Transform. Both prepare data for analytics.",
    "Data Warehousing": "Places like Snowflake, BigQuery, or Redshift store large volumes of clean data for analysis.",
    "Big Data Tools": "Tools like Hadoop and Spark help process huge datasets that don't fit on one machine.",
    "Next Steps": "Build small projects, learn Python & SQL deeply, explore cloud services (AWS, GCP, Azure)."
}

# Choose lesson
choice = st.sidebar.radio("Select a lesson", list(lessons.keys()))

# Show lesson content
st.subheader(f"📖 {choice}")
st.write(lessons[choice])

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit. Edit code on GitHub to add more lessons!")
