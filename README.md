🔐 Vault - Financial AI Assistant
📋 Project Overview
Vault is an intelligent financial chatbot designed exclusively for finance-related queries. Built for the SAP Marathon, this project demonstrates a specialized AI assistant that provides personalized financial advice while strictly adhering to finance-only responses. The system intelligently analyzes user financial situations and offers tailored recommendations.

✨ Key Features
🎯 Core Capabilities
Strict Finance-Only Responses: Automatically filters out non-financial queries

Personalized Financial Advice: Tailored recommendations based on user context

Multi-Language Support: Understanding of Indian languages and local financial terminology

Debt Prioritization Logic: Automatically detects high debt situations and provides clearance roadmaps

File Processing: CSV and Excel financial data analysis

🛡️ Safety & Compliance
No investment advice for users with high debt

Focus on debt clearance before investment recommendations

Strict adherence to financial advisory boundaries

Privacy-focused local data processing

📊 Data Processing
CSV file upload and analysis

Excel spreadsheet parsing

Automated financial insights generation

Column-based financial data identification

🚀 Quick Start
Prerequisites
Python 3.8 or higher

Google Gemini API key

Installation
Clone the repository

bash
git clone <your-repo-url>
cd vault-finance-bot
Create virtual environment (Recommended)

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies

bash
pip install google-genai python-dotenv pandas openpyxl
Configure environment variables

bash
# Create .env file
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
Getting Your API Key
Visit Google AI Studio

Create a new API key

Copy and paste into your .env file

📁 Project Structure
FINANCIAL/
├── .venv/                          # Virtual environment
├── src/
│   ├── conversational_model/       # Core chatbot implementation
│   │   └── llm.py                 # Main LLM integration file
│   ├── experimentations/           # Experimental features
│   ├── __init__.py                # Package initializer
│   └── __init__.py
├── .env                            # Environment variables
├── Dockerfile                      # Container configuration
├── requirements-dev.txt            # Development dependencies
├── requirements.txt               # Production dependencies
└── README.md                      # This file
🎮 Usage Examples
Basic Chat Interface
bash
python src/vault_bot.py
Sample Conversations
Finance Query:

text
You: How should I invest ₹5000 monthly?
Vault: For ₹5000 monthly, consider a diversified SIP portfolio...
Non-Finance Query:

text
You: What's the weather today?
Vault: I can only assist with finance-related queries.
File Upload:

text
You: expenses.csv
Vault: ✅ File loaded successfully! 
       Found: Income: ₹75,000, Expenses: ₹45,000
       Monthly Savings Potential: ₹30,000
