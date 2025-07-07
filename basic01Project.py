## User friendly chat bot


from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage

# initilize the model 

model=Ollama(model="gemma:2b")

# users questions
def users(message):
    prompt=[HumanMessage(content=message)]
    respose=model.invoke(prompt)
    return respose

# chat loop
if __name__ == "__main__":
    print("welcome Rik's Local Chat bot -> ")
    while True: 
        user_input=input("You: ")
        if user_input.lower() in ['exit','bye','quit']:
            break
        else:
            ans=users(user_input)
            print(f"AI : {ans}")
