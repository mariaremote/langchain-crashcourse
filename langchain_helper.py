# TODO: replace deprecated classes

from dotenv import load_dotenv
# from langchain.llms import OpenAI 
from langchain_openai import OpenAI #or any other (Hugging Face) model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain # deprecated
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()

def generate_username(platform, color, keyword):
    llm = OpenAI(temperature = 0.8) # the higher the more creative
    prompt_template_name = PromptTemplate(
        input_variables = ["platform","color",'keyword'],
        template = "Suggest five cool usernames for a new {platform} profile. Use the color {color} or some other variations of it in the usernames. If provided, make use of the keyword {keyword} in the usernames as well.",
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='usernames')

    response = name_chain({'platform': platform, 'color': color, 'keyword': keyword})
    return response

def langchain_agent():
    llm = OpenAI(temperature = 0.5)

    tools = load_tools(["wikipedia"], llm=llm)

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent.run(
        "What is the average weight for a woman in her thirties across the globe?" # specify the task
    )

    return result

if __name__ == "__main__":
    # print(generate_username('Github', 'green', 'yoga'))
    print(langchain_agent())