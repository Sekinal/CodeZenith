import os
import openai
import memory as mm

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt_answer(prompt, model_name):
    """
    Generates a response to a given prompt using a given OpenAI model.

    Args:
        prompt (str): The prompt to generate a response to.
        model_name (str): The name of the OpenAI model to use.

    Returns:
        str: The generated response to the prompt.
    """
    # Create a chat completion request with the given prompt and system message
    response = openai.ChatCompletion.create(
        model=f"{model_name}",
        messages=[
            {"role": "system", "content": "You're an Artificial Intelligence coding assistant. You'll write the code requested by the user and/or give directions and ideas on how to build the requested software. If code is requested, always, under no exceptions, write the requested code as one block first and any example use cases after that (on separate code blocks). Include comments and docstrings. Make the code use the best of practices and extremely readable but concise."},
            {"role": "user", "content": f"Previous relevant information: {mm.extract_from_memory(prompt)}"},
            {"role": "user", "content": f"{prompt}"},
        ]
    )
    
    # Return the generated response from the chat completion request
    return response['choices'][0]['message']['content']