
# Google Calendar Assistant

This project is a Google Calendar LLM Assistant build with React and Flask. AI Agent logic build on LangChain and the OpenAI Api


## Setup Instructions

### 1. Prerequisites
- **Google API Credentials**:
  1. Enable the Google Calendar API on the [Google Cloud Console](https://console.cloud.google.com/).
  2. Download the `credentials.json` file and place it in the project root directory.

- **OpenAI API Key**
Create a `.env` file in the project root directory to securely store your OpenAI API key 
```
OPENAI-API_KEY=<YOUR_API_KEY>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## How to Use

### Run the program
Run the flask backend server
```bash
cd backend
python3 routes.py
```
Run the frontend 
```bash
cd frontend
npm run dev
```

Navigate to your https://localhost:5000/chat URL


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.
