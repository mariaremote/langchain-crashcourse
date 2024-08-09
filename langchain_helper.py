# TODO: replace deprecated classes

from dotenv import load_dotenv
# from langchain.llms import OpenAI 
from langchain_openai import OpenAI #or any other (Hugging Face) model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain # deprecated

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

if __name__ == "__main__":
    print(generate_username('Github', 'green', 'yoga'))