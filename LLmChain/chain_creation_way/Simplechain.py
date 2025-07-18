from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

templete=ChatPromptTemplate.from_messages([
    ('system','You are a helpfull question answers given bot. Your name is Landu'),
    ('human','content{content}'),
    ('human','Question{question}')
])

prompt=({
    'content':'''arge Language Models (LLMs) are deep learning-based models trained on massive amounts of text data. They use transformer architectures to understand, generate, and manipulate human language. Examples include OpenAI’s GPT series, Google’s PaLM, Meta’s LLaMA, and Anthropic’s Claude.
     Key Features
Natural Language Understanding (NLU): Comprehends human language, including grammar, semantics, and context.

Natural Language Generation (NLG): Generates coherent, context-aware text.

Scalability: Performance improves with increased parameters and data.

Multimodal Capability (Advanced Models): Some LLMs handle text, images, audio, and video inputs.
    ''',
    'question':'What is a large language model, and how is it trained?'
})

model=Ollama(model='gemma:2b')

chain=templete | model

response = chain.invoke(prompt)

print(response)

# pip install grandalf
chain.get_graph().print_ascii()