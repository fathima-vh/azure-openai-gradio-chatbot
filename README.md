# Azure OpenAI Gradio Chatbot

A simple streaming chatbot built with Gradio and Azure OpenAI. This project demonstrates how to connect to Azure’s OpenAI service, stream responses token-by-token, and display them in a minimal Gradio chat interface.

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Environment Variables](#environment-variables)  
5. [Usage](#usage)  
6. [Code Overview](#code-overview)  
7. [Troubleshooting](#troubleshooting)  
8. [License](#license)  

---

## Features

- **Streaming Responses**: Uses `stream=True` to display tokens as they arrive.
- **Minimal UI**: Leverages `gr.ChatInterface` for automatic history management.
- **Azure OpenAI Client**: Uses `AzureOpenAI` from the official `openai` Python SDK.
- **.env Integration**: Reads endpoint, key, deployment, and API version from a `.env` file.

---

## Prerequisites

- Python 3.8 or higher  
- An Azure OpenAI resource with:
  - Endpoint URL  
  - API key  
  - A deployed chat model (for example: `gpt-35-turbo` or `gpt-4`)  
- [pipenv](https://pipenv.pypa.io/) or `venv` (optional but recommended for virtual environments)

---

## Installation

1. **Clone the repository** (or copy the code into your project directory):

   
   git clone https://github.com/fathima-vh/conversational-chatbot.git
   cd conversational-chatbot
   python main.py
