from langchain.llms import OpenAI
from langchain.schema.runnable import RunnableLambda
import os

def MyChainRunnable():
    llm = OpenAI(temperature=0.7)
    chain = RunnableLambda(lambda x: llm.predict(x["input"]))
    return chain