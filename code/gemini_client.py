import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a story about a ninja.")
response = model.generate_content("You are an expert on mathematics.")
print(response.text)
