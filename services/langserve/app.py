from fastapi import FastAPI
from langserve import add_routes
from chains.my_chain import MyChainRunnable

app = FastAPI()
add_routes(app, MyChainRunnable(), path="/invoke/my_chain")