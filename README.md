# NL2SQL
Execute SQL queries from Natural language

# Instructions (Python 3.10)
1. Setup your MySQL database [(Sample Database used for this repo)](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/)
2. Create a .env file with the following content. Get [GROQ](https://console.groq.com/keys) & [LangSmith](https://docs.smith.langchain.com/#:~:text=To%20create%20an%20API%20key,Then%20click%20Create%20API%20Key.) API Keys.
```
db_user="root"
db_password=""
db_host="localhost"
db_name="classicmodels"

GROQ_API_KEY="<your-groq-api-key>"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<your-langsmith-api-key>"
LANGCHAIN_PROJECT="<langchain-project-name>"
```
3. Install requirements and run app
```
pip install -r requirements.txt
cd nl2sql
streamlit run app.py
```

