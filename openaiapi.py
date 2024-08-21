from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["API_KEY"])


def text_return(promft):
  chat_completion = client.chat.completions.create(
      messages=[{
          "role": "user",
          "content": promft,
      }],
      model="gpt-4o",
  )
  return chat_completion.choices[0].message.content


def image_url_return(promft):
  response = client.images.generate(
      model="dall-e-3",
      prompt=promft,
      size="1024x1024",
      quality="standard",
      n=1,
  )
  return response.data[0].url
