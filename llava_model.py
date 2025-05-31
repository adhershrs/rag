## llava_model.py
import ollama

def chat_with_llava(prompt, context):
    """Function to interact with LLaVA using extracted PDF text as context."""
    response = ollama.chat(model='llama3.2:3b', messages=[
        {"role": "system", "content": "Use the following context to answer the user query: " + context},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']