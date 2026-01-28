# 💰 Vault Finance Bot - SAP Marathon Project

A finance-only chatbot that answers financial questions. It strictly filters non-finance queries and provides personalized financial advice.

## 🏗️ Project Structure
FINANCIAL/
├── .venv/ # Virtual environment
├── src/
│ └── conversational_model/
│ └── llm.py # Main chatbot with Gemini API
├── .env # Environment variables
├── requirements.txt # Dependencies
└── README.md # This file

text

## ✨ Features

- **Finance-Only Responses**: Strictly answers only finance-related questions
- **Google Gemini Integration**: Uses state-of-the-art AI for responses
- **Simple Terminal Interface**: Easy to use command-line interface
- **Error Handling**: Graceful handling of API errors
- **Multi-Model Fallback**: Tries different Gemini models if one fails

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

1. **Clone and navigate**
```bash
cd FINANCIAL
Create virtual environment

bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
Install dependencies

bash
pip install google-genai python-dotenv
Setup API key
Create .env file:

env
GOOGLE_API_KEY=your_api_key_here
Run the bot

bash
python src/conversational_model/llm.py
📖 Usage
Basic Commands
text
Type your finance question
Type 'quit' or 'exit' to end
Example Conversations
text
You: How to save money as a student?
Bot: Start by tracking expenses, create a budget...

You: Should I invest in stocks?
Bot: Consider your risk tolerance...

You: What's the weather?
Bot: I only answer finance questions.
⚙️ Environment Variables
Variable	Description	Required
GOOGLE_API_KEY	Google Gemini API key	Yes
🐛 Troubleshooting
Common Issues
1. ModuleNotFoundError

bash
pip install google-genai python-dotenv
2. API Key Error

Check .env file exists

Verify API key is valid

Get new key from: https://makersuite.google.com/app/apikey

3. Quota Exceeded

Wait 1 minute before retrying

Check your Google Cloud quota

🧪 Running Tests
Currently manual testing:

bash
# Test finance detection
python -c "from src.conversational_model.llm import SimpleFinanceBot; bot=SimpleFinanceBot(); print('Test passed')"
🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is created for SAP Marathon.

👥 Authors
@Mahantesh - Developer

🙏 Acknowledgements
Google Gemini API for AI capabilities

SAP for organizing the marathon

Python community for amazing libraries

🔗 Links
Repository: https://github.com/yourusername/FINANCIAL

SAP Marathon: SAP TechEd

🛠️ Tech Stack
Language: Python 3.8+

AI API: Google Gemini

Environment: Virtual Environment

Dependency Management: pip

📈 Roadmap
Add CSV file support

Multi-language responses

Web interface

Database integration

Advanced financial analysis

❓ FAQ
Q: How do I get an API key?
A: Visit https://makersuite.google.com/app/apikey and create a free API key.

Q: Why won't it answer non-finance questions?
A: By design - it's a specialized finance-only bot for the SAP Marathon.

Q: Can I add more features?
A: Yes! Check the roadmap section for ideas.

💬 Feedback
If you have any feedback, please reach out via GitHub issues.

🆘 Support
For support, check the troubleshooting section or create a GitHub issue.

Built with ❤️ for SAP Marathon 2024

text

This is specifically for YOUR project with YOUR structure. Just copy-paste and fill in your GitHub username!
