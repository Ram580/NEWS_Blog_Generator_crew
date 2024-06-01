from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_groq import ChatGroq

## call the gemini models
# llm=ChatGoogleGenerativeAI(#model="gemini-1.5-flash",
#                            model="gemini-pro",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


## load the Groq API key
groq_api_key=os.environ['GROQ_API_KEY']
available_llms = ["llama3-8b-8192", "mixtral-8x7b-32768", "llama3-70b-8192","gemma-7b-it"]
llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama3-8b-8192")
             #model_name="mixtral-8x7b-32768")

# Creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

