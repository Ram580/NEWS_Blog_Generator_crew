from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
import streamlit as st

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)


## starting the task execution process wiht enhanced feedback

# result=crew.kickoff(inputs={'topic':'AI in Automotive Industry'})
# print(result)

# Create a Streamlit app
st.title("AI News Blog Generator")

# Input Variables
topic = st.text_input("Enter the topic of the blog post")
input={'topic':topic}

# Run CrewAI
if st.button("Run CrewAI"):
    # Set inputs for the execution of the Crew
    result=crew.kickoff(inputs=input)
    st.markdown(result)