from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from flask import Flask, render_template, request, jsonify

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
    response = llm_chain.invoke({'question': question}) 
    return response 

app = Flask(__name__) 

@app.route("/") 
def index(): 
    return render_template("index.html") 

@app.route("/chat", methods=["POST"]) 
def chatbot(): 
    data = request.get_json() 
    query = data["query"] 
    response = query_language_model(query) 
    return jsonify({"response": response}) 

if __name__ == "__main__": 
    app.run(debug=True)