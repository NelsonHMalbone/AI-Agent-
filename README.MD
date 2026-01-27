# Build an AI Agent with python and LangChain

udemy project section 24 new portion of the udemy project

creating a AI Agent using python and LangChain

## 01-26 
installed all libs with the requirement.txt file created a todoist to get the api along with a google al studio api key
place both api keys into a .env file
update the git in pushed everything

## 01-27
loading the apis

using the libary's dotenv and os together you get retrieve api keys from .env files
from dotenv import load_dotenv
import os 

load_dotenv()

ex:
v1_api_key = os.getenv("APIKEYNAME")

to make sure api is being seen or read you can 
print(v1_api_key)

