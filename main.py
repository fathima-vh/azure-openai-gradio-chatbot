import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import gradio as gr

# ————— Load environment variables —————
load_dotenv()
endpoint    = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key     = os.getenv("AZURE_OPENAI_API_KEY")
deployment  = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# ————— Initialize Azure OpenAI client —————
openai = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint
)

# ————— System prompt —————
system_message = "You are a helpful assistant."

# ————— Streaming Chat Function —————
def chat(message, history):
    # 1) Always include the system prompt
    messages = [{"role": "system", "content": system_message}]

    # 2) Rebuild past turns, skipping any None
    for user_msg, assistant_msg in history:
        if user_msg is not None:
            messages.append({"role": "user", "content": user_msg})
        if assistant_msg is not None:
            messages.append({"role": "assistant", "content": assistant_msg})

    # 3) Finally, append the new user message
    messages.append({"role": "user", "content": message})

    try:
        # 4) Start streaming
        stream = openai.chat.completions.create(
            model=deployment,
            messages=messages,
            stream=True
        )

        # 5) Accumulate and yield tokens as they arrive
        response = ""
        for chunk in stream:
        # Safe access to chunk data
            if (hasattr(chunk, 'choices') and 
                chunk.choices and 
                len(chunk.choices) > 0 and 
                chunk.choices[0].delta and 
                chunk.choices[0].delta.content):
                response += chunk.choices[0].delta.content
                yield response  
    except Exception as e:
            yield f"Error: {e}"

# ————— Launch Gradio’s ChatInterface —————
# Gradio will automatically keep 'history' as pairs of [user, assistant].
gr.ChatInterface(fn=chat).launch()
