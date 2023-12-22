from flask import Flask ,render_template,request
from dotenv import load_dotenv
import os
import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
app = Flask(__name__)

#   FUNCTION FOR CLEANING TEXT AND GERNATE THE EASY TO UNDERSTANF TEXT
def convertText(text):
    newText = text.strip()
    SECRET_KEY = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=SECRET_KEY)
    try:
        textSummary = llm.predict(f"Explain the text give blow in natural language {newText}?")
        print(textSummary)
        return textSummary
    except ValueError:
        return "Oops! Some problem"
    


#    ROUTES
@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/service")
def Service():
    return render_template("Service.html")

@app.route("/about")
def About():
    return render_template("About.html")

@app.route("/docexp",methods=["GET","POST"])
def docExp():
    if request.method == 'POST':
        docContent = request.form.get('docText')
        text_in_easy_lang =  convertText(docContent)
        return render_template("Summary.html",params=text_in_easy_lang)

    return render_template("docExp.html")

@app.route("/chatbot")
def ChatBot():
    return render_template("ChatBot.html")


# print(docContent)

app.run(debug=True)    