# Importing the necessary modules
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to generate code based on user input
def generate_code():

    # Input for the programming language
    inp_language = input('Enter the programming language...')
    inp_task = input('Explain the function...')

    # Initialize an instance of the OpenAI class
    LLM = OpenAI()

    # Define the prompt template for code generation
    code_prompt = PromptTemplate(
        input_variables=['language', 'task'],
        template="Consider you are an Senior software devloper. And write a {language} function to {task}."
    )


    # Chain the prompt template with the language model
    chain = code_prompt | LLM 

     # Invoke code generation by passing language and task as input
    code = chain.invoke({'language': inp_language, 'task': inp_task})

    # Return the generated code
    return code


# Call the function to generate code and print the result
print(generate_code())
