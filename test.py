import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_aws import ChatBedrockConverse

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

llm_bedrock = ChatBedrockConverse(model="meta.llama3-8b-instruct-v1:0",
    temperature=0,
    max_tokens=None,)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming and india."),
]
ai_msg = llm_bedrock.invoke(messages)
print(ai_msg)