import streamlit as st
import requests

st.title("AI Resume Builder")

name = st.text_input("Enter Your Name")
email = st.text_input("Enter Your Email")
skills = st.text_area("Enter Your Skills")
exp = st.text_area("Enter Your Expirence")
projects = st.text_area("Enter Your Projects")

key =st.secrets["OPENROUTER_API_KEY"]

if st.button("Generate"):
    if not name  or not email or not skills or not exp or not projects:
        st.warning("Plz Fill All Fields")
    else:
        with st.spinner("Resume Building..."):
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                        "Authorization" : f"Bearer {key}",
                        "Content-Type": "application/json"
                    }
            body = {
                        "model":"openai/gpt-4o-mini",
                        "messages":[
                            {
                                "role":"user",
                                "content":f"Create A Professional Freasher Resume Name:{name} , Email: {email} , Skills:{skills} , Experence:{exp} , Projects:{projects} Generate Resume Used Clear Headings and Bullets Points"
                            }
                        ]
                    }
            try:
                        responce = requests.post(
                            url,
                            headers=headers,
                            json=body,
                            timeout=60
                        )
                        data = responce.json()
                        resume = data['choices'][0]['message']['content']
                        st.success("Resume Generate Sucessfuly")
                        st.markdown(resume)
            except requests.RequestException as e :
                        st.error(e)
            
            
            
