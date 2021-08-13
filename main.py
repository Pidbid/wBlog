# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/08/13 16:53:57
@Author  :   Wicos 
@Version :   1.0
@Contact :   wicos@wicos.cn
@Blog    :   https://www.wicos.me
'''

# here put the import lib
from threading import Thread
from fastapi import FastAPI, Form, Cookie, Response, File, UploadFile
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import time, os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"],
)  # 允许跨域的headers，可以用来鉴别来源等作用。

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.variable_start_string = "[["
templates.env.variable_end_string = "]]"



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info",reload=True)