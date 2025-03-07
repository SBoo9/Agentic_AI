from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

## Web Search Agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Scraping web for usefull informaiton",
    model=Groq(id="llama-3.2-1b-preview"),
    tool=[DuckDuckGo()],
    instructions=["Always show timestamp"],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent

financial_agent=Agent(
    name="Financial Agent",
    model=Groq(id="llama-3.2-1b-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True,
)


## Combining multiple agents
multi_ai_agent=Agent(
    teams=[web_search_agent,financial_agent],
    instructions=["Always show timestamp","Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=True,
)


multi_ai_agent.print_response("Share the analysis. And showcase the latest news for NVDA", stream=True)
