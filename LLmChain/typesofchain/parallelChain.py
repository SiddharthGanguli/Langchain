from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from langchain_core.runnables import RunnableSequence

# Define models
model1 = Ollama(model='gemma:2b')
model2 = Ollama(model='llama3')

# Prompt to generate notes
prompt1 = PromptTemplate(
    template='Generate detailed notes on the topic: {topic}',
    input_variables=['topic']
)

# Prompt to generate quiz questions
prompt2 = PromptTemplate(
    template='Generate 5 question-and-answer pairs for: {topic}',
    input_variables=['topic']
)

# Prompt to create a quiz using both notes and questions
prompt3 = PromptTemplate(
    template='Based on the following notes:\n{notes}\nand quiz questions:\n{quiz}\nGenerate a test to assess learning.',
    input_variables=['notes', 'quiz']
)

# Run prompt1 and prompt2 in parallel
parallelchain = RunnableParallel({
    'notes': prompt1 | model1,
    'quiz': prompt2 | model2
})

# Merge outputs into a quiz using prompt3
mergeChain = prompt3 | model2

# Complete chain: parallel generation -> final quiz
chain = parallelchain | mergeChain

# Run the full chain
result = chain.invoke({'topic': 'Artificial Intelligence'})

# Print the result
print(result)
