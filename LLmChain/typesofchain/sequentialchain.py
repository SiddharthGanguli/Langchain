from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

from langchain_core.prompts import PromptTemplate

prompt1=PromptTemplate(
    template="generate detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='generate 5 following summary from the following text \n{text}',
    input_variables=['text']
)

model=Ollama(model='gemma:2b')

chain=prompt1 | model | prompt2 | model

response=chain.invoke({'topic':'Upcoming It trending job with highest package'})

print(response)

chain.get_graph().print_ascii()