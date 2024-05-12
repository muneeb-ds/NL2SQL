examples = [
    {
        "input": "List all customers in France with a credit limit over 20,000.",
        "query": "SELECT * FROM customers WHERE country = 'France' AND creditLimit > 20000;"
    },
    {
        "input": "Get the highest payment amount made by any customer.",
        "query": "SELECT MAX(amount) FROM payments;"
    },
    {
        "input": "Show product details for products in the 'Motorcycles' product line.",
        "query": "SELECT * FROM products WHERE productLine = 'Motorcycles';"
    },
    {
        "input": "Retrieve the names of employees who report to employee number 1002.",
        "query": "SELECT firstName, lastName FROM employees WHERE reportsTo = 1002;"
    },
    {
        "input": "List all products with a stock quantity less than 7000.",
        "query": "SELECT productName, quantityInStock FROM products WHERE quantityInStock < 7000;"
    },
    {
        'input':"what is price of `1968 Ford Mustang`",
        "query": "SELECT `buyPrice`, `MSRP` FROM products  WHERE `productName` = '1968 Ford Mustang' LIMIT 1;"   
    },
    {
        "input": "List all orders placed by customers from Canada.", 
        "query": "SELECT * FROM orders WHERE customerNumber IN (SELECT customerNumber FROM customers WHERE country = 'Canada');"
    },
    {
        "input": "Find the total number of employees in each department.", 
        "query": "SELECT department, COUNT(employeeNumber) as total_employees FROM employees GROUP BY department;"
    },
    {
        "input": "Show details of the product with the highest MSRP.", 
        "query": "SELECT * FROM products WHERE MSRP = (SELECT MAX(MSRP) FROM products);"
    },
    {
        "input": "Find the average payment amount made by customers in the UK.", 
        "query": "SELECT AVG(amount) FROM payments WHERE customerNumber IN (SELECT customerNumber FROM customers WHERE country = 'UK');"
    },
    {
        "input": "List all employees who have no direct reports.", 
        "query": "SELECT employeeNumber, firstName, lastName FROM employees WHERE employeeNumber NOT IN (SELECT reportsTo FROM employees);"
    },
    {
        "input": "kun si products hain jo 'Sports Cars' product line mein hain?", 
        "query": "SELECT * FROM products WHERE productLine = 'Sports Cars';"
    },
    {
        "input": "sab se zyada stock mein maujud product kya hai?", 
        "query": "SELECT productName, quantityInStock FROM products WHERE quantityInStock = (SELECT MAX(quantityInStock) FROM products);"
    },
    {
        "input": "kun si orders hain jo 'Classic Cars' product line ke products ke liye place kiye gaye hain?", 
        "query": "SELECT DISTINCT orderNumber FROM orderdetails WHERE productCode IN (SELECT productCode FROM products WHERE productLine = 'Classic Cars');"
    },
    {
        "input": "'Italy' mein kon si customers hain jo credit limit 10,000 se zyada rakhte hain?", 
        "query": "SELECT * FROM customers WHERE country = 'Italy' AND creditLimit > 10000;"
    },
    {
        "input": "kis employee ke reportsTo '1003' hain?", 
        "query": "SELECT firstName, lastName FROM employees WHERE reportsTo = 1003;"
    }

]

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import streamlit as st

model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs),
        Chroma,
        k=2,
        input_keys=["input"],
    )
    return example_selector