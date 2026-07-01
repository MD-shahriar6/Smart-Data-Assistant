# 🤖 Smart Data Assistant

Smart Data Assistant is a multi-tool AI agent that accepts questions in natural language. It generates SQL queries from the user's question, executes them on the appropriate database, or searches the web if the information is not available in the databases. Finally, it returns the answer in natural language.

---

# ✨ Features

This is a **multi-tool AI agent** that can generate SQL queries from natural language questions.

### 🗄️ Database Tools
The agent can communicate with the following databases:

- Hospitals Database
- Institutional Database
- Restaurants Database

### 🌐 Web Search Tool
If the required information is not available in the databases, the agent searches the web using:

- DuckDuckGo Search

---

# 📁 Project Structure

```text
Project/
│
├── SQLite_DBs/
│   ├── hospitals.db
│   ├── institutional.db
│   └── restaurants.db
│
├── CSV_files/
│   ├── hospitals.csv
│   ├── institutional.csv
│   └── restaurants.csv
│
├── create_db.py
├── main.ipynb
├── requirements.txt
├── README.md
└── .env
```

### Folder Description

- **CSV_files/** → Original datasets used to create the databases.
- **create_db.py** → Creates SQLite databases and tables from the CSV files.
- **SQLite_DBs/** → SQLite databases used by the SQL tools.
- **main.ipynb** → Jupyter notebook containing the complete implementation.
- **requirements.txt** → Python dependencies.
- **.env** → API keys and environment variables.

---

# 🏗️ Architecture

> **(Architecture diagram will be added here.)**

---

# 🛠️ Technologies Used

- Python
- LangChain
- SQLite
- SQLAlchemy
- OpenAI
- DuckDuckGo

---

# ⚙️ Installation

```bash
conda create -n sql-agent python=3.11
conda activate sql-agent

pip install -r requirements.txt
```

---

# ▶️ How to Run

1. Activate the conda environment.
2. Open `main.ipynb`.
3. Select the correct Python environment.
4. Run all notebook cells.

---

# 💡 Example Questions

### 1. Institution Database

**Question**

> Give me 3 madrasa names from Barguna.

**Answer**

1. ALHAJ MD. SHAMIM AHSAN DAKHIL MADRASAH, MOHISDANGA
2. AMRAGACHIA SHALEHIA DAKHIL MADRASAH
3. AMTALI BONDER HOSAINIA FAZIL MADRASAH

---

### 2. Restaurants Database

**Question**

> Give me 3 restaurant names inside Dhaka with a rating greater than 4.

**Answer**

1. শুভ এন্টারপ্রাইজ অলটাইম ডিলার — Rating: 5.0
2. ভাত ঘর — Rating: 5.0
3. আপন নিবাস — Rating: 5.0

---

### 3. Web Search

**Question**

> What is the healthcare policy of Bangladesh?

**Answer**

The healthcare policy of Bangladesh aims to ensure an effective healthcare system that meets the needs of the nation. The policy provides a vision and mission for healthcare development while encouraging quality healthcare services. It also focuses on financing, legal frameworks, antimicrobial resistance, zoonotic diseases, food safety, and progress toward Universal Health Coverage.

---

# 🎯 Design Decisions

### 🧰 Separate Database Tools

Three separate tools are used for three different databases:

- Institution Database Tool
- Hospitals Database Tool
- Restaurants Database Tool

Each tool is responsible for generating SQL queries and retrieving information from its own database.

### 🤖 Main Agent

The user communicates only with the **Main Agent** in natural language.

The Main Agent decides which tool should be used based on the user's question.

### 🌐 Web Search Tool

If the required information is not available in the databases, the Main Agent uses the **DuckDuckGo Search Tool** to retrieve information from the web.