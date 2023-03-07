import openai

def query_gpt_35_turbo(query):  
  response = openai.ChatCompletion.create(  
    model="gpt-3.5-turbo",
    messages=[{"role": "system",
               "content":"You are a helpful assistant that helps users generate ..."}, 
              {"role":"user",
               "content": query}]  
  )  
  return response.choices[0].message.content

def translate(query):  
  response = openai.ChatCompletion.create(  
    model="gpt-3.5-turbo",
    messages=[{"role": "system",
               "content":"You are a helpful assistant that translates Chinese to Korean."}, 
              {"role":"user",
               "content": query}]  
  )  
  return response.choices[0].message.content

print(translate("您保存好，好吧? 保存? 那么您的书，您的书，第一课，要好，下节课我们看，好吗? 好的，好的。"))
