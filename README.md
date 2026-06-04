# Healthcare Symptom Checker

A secure, multi-turn clinical symptom-checking application built with a Flask backend and vanilla JavaScript frontend. This tool provides an educational environment for querying potential medical conditions based on symptom input using the Gemini LLM.

## Architecture

- **Backend**: Python / Flask API.
- **Database**: SQLite with a relational schema (`chats` and `messages` tables).
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, and CSS3.
- **LLM Integrations**: Google Generative AI integration via `google-generativeai`.

## Features

- **Multi-Turn Context**: Maintains conversational memory natively via relational chat identification.
- **Session Management**: Chat pinning algorithms, live renaming capabilities, historic data extraction, and cascade deletion.
- **Responsive UI**: Custom EKG DOM loading animations, SVG mapping, auto-scrolling interfaces, and responsive grid/flex layouts.

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure credentials:
   - Create a `.env` file in the root directory.
   - Insert your developer token: `GEMINI_API_KEY=your_key_here`.
3. Initialize Server:
   ```bash
   python app.py
   ```
4. The service will compile and host locally at `http://localhost:5000`.

## Notice
This repository is developed strictly for educational and academic use-cases. It does NOT constitute valid medical advice.
