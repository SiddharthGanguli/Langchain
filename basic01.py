# Step 1: Import the Ollama module from LangChain community integration
from langchain_community.llms import Ollama

# Step 2: Initialize the LLM model via Ollama
# You can change 'gemma:2b' to any other model like 'llama2', 'mistral', etc. that you have locally
# download it using ollama pull "model name "
model = Ollama(model='gemma:2b')

# Step 3: Write your prompt here
prompt = "What is the capital of India?"

# Step 4: Send the prompt to the model and get the response
response = model.invoke(prompt)

# Step 5: Print the model’s response
print("Model response::- ")
print(response)