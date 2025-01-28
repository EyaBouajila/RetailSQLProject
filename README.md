# RetailSQLProject
![Screenshot 2025-01-28 223734](https://github.com/user-attachments/assets/9e5db134-7791-472b-b7b3-9d56fc5fe0b4)
![2](https://github.com/user-attachments/assets/3047a45e-f48a-4803-8d03-c93ebd0fadef)


## A Streamlit-based application for querying a MySQL database of t-shirt inventory using LangChain and Google Generative AI.

### Features :
- Accepts natural language questions about the t-shirt inventory.
- Generates SQL queries dynamically to retrieve data from the database.
- Uses Few-Shot Examples to improve query accuracy.
- Displays results in an easy-to-read format on the Streamlit interface.

### Technologies Used :
- Streamlit: For the web interface.
- LangChain: For dynamic SQL generation and query handling.
- Google Generative AI: For processing natural language inputs using "gemini-1.5-flash" LLM.
- Chroma: For semantic similarity in few-shot examples.
- MySQL: For database storage.
