from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() #reads .env file

# gathering api keys
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# initialize google genai model
llm = ChatGoogleGenerativeAI( # takes 3 agruments
    model = 'gemini-2.5-flash', # freer rate make several request in a min or so
    google_api_key = gemini_api_key, # just your api key goes here
    temperature = 0.3 # closer to 0 more determine then creative
)
system_prompt = "What Can I Help you with?"
user_input = "Tell me the best way to manage my time with learning to code"
prompt = ChatPromptTemplate([
    ("system", system_prompt),
    ("user", user_input)
])

chain = prompt | llm | StrOutputParser()

# chain invoke
chain_invoke = chain.invoke({"input": user_input})
print(chain_invoke)