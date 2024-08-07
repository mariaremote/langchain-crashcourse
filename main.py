# from langchain.llms import OpenAI 
from langchain_openai import OpenAI #or any other (Hugging Face) model
from dotenv import load_dotenv

load_dotenv()

def generate_username():
    llm = OpenAI(temperature = 0.8) # the higher the more creative
    name = llm("Suggest five cool usernames for a new Github profile")

    return name

if __name__ == "__main__":
    print(generate_username())