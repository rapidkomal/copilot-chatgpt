import os
import openai
openai.api_key = ""
# print(openai.Model.list())
model_lst = openai.Model.list()


for i in model_lst['data']:
    print(i['id'])