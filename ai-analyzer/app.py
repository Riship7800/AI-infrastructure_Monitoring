from flask import Flask,request
import requests

app = Flask(__name__)

OLLAMA_URL="http://ollama:11434/api/generate"

@app.route("/analyze",methods=["POST"])
def analyze():

    alert=request.json["alert"]

    prompt=f"""
    Analyze this infrastructure alert:

    {alert}

    Give:

    1. Root Cause
    2. Impact
    3. Recommendation
    """

    response=requests.post(
        OLLAMA_URL,
        json={
            "model":"llama3",
            "prompt":prompt,
            "stream":False
        }
    )

    return response.json()

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
