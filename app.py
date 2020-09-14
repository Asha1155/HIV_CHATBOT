from flask import Flask,request,jsonify

app = Flask(__name__)

#@app.route("/", methods = ["POST", "GET"])
#def hello_bot():
    #return "Hello how are you"

import re


qa={
    "ukimwi ni nini":"ukimwi ni upungufu wa kinga mwilini",
    "dalili za ukimwi ni zipi":"homa kali, kupungua uzito, vidonda mdomoni, kukohoa, kukosa hamu ya kula",
    "je ukimwi unaambukizwa":"ndio ukimwi unaambukizwa",
    "ukimwi huambukizwajwe":"kuchangia vitu vyenye ncha kali, kwa njia ya kujaamiana, ",
    "je ukimwi una tiba":"hapana ukimwi hauna tiba",
    "je mama mwenye mimba anaweza kumuambukiza mtoto ukimwi":"mtoto anaweza asipate maambukizi ya ukimwi",
    "mtoto anapataje ukimwi kutoka kwa mama":"kwa njia ya kunyonya",
    "athari za uikiwmi ni zipi":"mwili kudhoofu, magonjwa mbalimbali",
    "je ukimwi una dawa":"ukimwi hauna dawa",
    "vvu ni nini":"vvu ni virusi vya ukimwi",
    "arv ni nini":"arv ni dawa ya kupunguza makali vvu mwilini"
}
@app.route("/",methods=["POST","GET"])
def ask(questions):
    if(re.search(ukimwi) and re.search(nini)):
        return qa["ukimwi ni nini"]
    elif(re.search(ukimwi) and re.search(dalili)):
        return qa["dalili za ukimwi ni zipi"]
    elif(re.search(ukimwi) and re.search(tiba)):
        return qa["je ukimwi una tiba"]
    elif(re.search(ukimwi) and re.search(unaambukizwajwe)):
        return qa["ukimwi unaambukizwajwe"]
    elif(re.search(ukimwi) and re.search(athari)):
        return qa["athari za ukimwi ni zipi"]
    elif(re.search(ukimwi) and re.search(dawa)):
        return qa["je ukimwi una dawa"]
    elif(re.search(vvu) and re.search(nini)):
        return qa["vvu ni nini"]
    elif(re.search(arv) and re.search(nini)):
        return qa["arv ni nini"]
    else:
        return "samahani rudia tena"

while 1:
    question = input("Ask me:    ")
    question = question.lower()
    if(question == "quit"):
        break
    else:
        print(ask(question))        
   
  
