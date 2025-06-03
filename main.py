import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import gradio as gr

# Load environment variables
load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Initialize Azure OpenAI client
openai = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint
)

# System prompt
system_message = "You are a helpful assistant."

# Streaming Chat Generator
def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": message})

    try:
        # Start streaming from Azure OpenAI
        stream = openai.chat.completions.create(
            model=deployment,
            messages=messages,
            stream=True
        )

        response = ""
        for chunk in stream:
            # Check if chunk has choices and content
            if (hasattr(chunk, 'choices') and 
                len(chunk.choices) > 0 and 
                hasattr(chunk.choices[0], 'delta') and
                hasattr(chunk.choices[0].delta, 'content') and
                chunk.choices[0].delta.content is not None):
                
                response += chunk.choices[0].delta.content
                yield response
                
    except Exception as e:
        yield f"Error: {str(e)}"

# Gradio streaming UI 
gr.ChatInterface(fn=chat).launch()