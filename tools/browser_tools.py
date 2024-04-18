import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from bs4 import BeautifulSoup

from langchain_google_genai import ChatGoogleGenerativeAI
api_gemini = os.environ.get("GEMINI_API_KEY")
mmodal_llm = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.2, google_api_key=api_gemini
)

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""

    # "crafty prompt"
    content = mmodal_llm.predict(f"""you are a Principal Researcher. You do amazing research and summaries based on the content you are working with. 
                                 Analyze and summarize the content for {website}, 
                                 make sure to only include the most relevant information from the content in the summary, return only the summary nothing else.""")

    return content
