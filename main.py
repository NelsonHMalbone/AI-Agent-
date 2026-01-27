from dotenv import load_dotenv
import os

load_dotenv() #reads .env file

# gathering api keys
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

print(todoist_api_key)
print(gemini_api_key)