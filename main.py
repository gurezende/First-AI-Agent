# Importing modules
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import os


# Defining the LLM
llm = LLM(
    model="groq/qwen-qwq-32b",
    api_key= os.environ.get("GROQ_API_KEY"),
    temperature=0.7)

# Defining the LLM
# llm = LLM( model = "gpt-4", temperature = 0.7,
#           api_key= os.environ.get("OPENAI_API_KEY"))

# Agent Definition
researcher = Agent(
    role = "{topic} Products Researcher",
    goal= '''Compare the performance of different brands of {topic} based on review articles and news. Search for Best {topic} Brands''',
    backstory='''You are a product researcher the compares the performance of different brands of {topic}. 
    Present the best 3 on a table and recommend the best brand.''',
    tools=[SerperDevTool()],
    llm=llm
)

# Define the research task for the Product Researcher
product_research_task = Task(
    description = '''Research the best {topic} brands and compare their price average, ratings and performance.''',
    expected_output='''Based on maximum 2 searches on Amazon and Google US, present a table comparing the price average,
    performance and overall rating of different brands of {topic} and 
    a recommendation for the best brand.''',
    agent = researcher
)

# Launch the Product Researcher
def main(topic):
    crew = Crew(
        agents = [researcher],
        tasks = [product_research_task],
        process= Process.sequential,
        verbose = True
    )

    result = crew.kickoff(inputs={'topic': topic})

    print(result)


if __name__ == "__main__":

    main(topic="Laptop PC")