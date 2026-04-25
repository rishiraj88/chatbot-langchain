from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

prompt = open('website_text.txt', 'r').read()

hotel_assistant__template = prompt + """
You are the hotel manager of Landon Hotel, named "Mr. Landon". 
Your expertise is exclusively in providing information and advice about anything related to Landon Hotel. 
This includes any general Landon Hotel related queries. 
You do not provide information outside of this scope. 
If a query is not about Landon Hotel, respond with, "I can't assist you with that, sorry!" 
Query: {query} 
Answer: 
"""

hotel_assistant__prompt_template = PromptTemplate( 
    input_variables=["query"], 
    template=hotel_assistant__template 
    ) 

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0) 

language_chain = hotel_assistant__prompt_template | llm 

def query_language_model(query): 
    print(language_chain.invoke({'query': query})) 

while True:
    query_language_model(input())