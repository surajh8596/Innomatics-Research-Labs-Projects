import re
from unittest import result
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def regex101():
    if request.method=='POST':
        regex = request.form['exp']
        text = request.form['txt']
        cnt=0
        if (len(regex) ==0 or len(text) == 0):
            cnt=-1
            return render_template("index.html",result="Please Provide Input",count=cnt)
        else:
            match_no=[]
            match_str=[]
            indices=[]
            for match in re.finditer(r'{}'.format(regex),text):
                cnt+=1
                match_no.append(cnt)
                match_str.append(match.group())
                indices.append(match.span())
            return render_template("index.html", exp=regex, txt=text, match_no=match_no, indices=indices, match_str=match_str, count=cnt)

    return render_template("index.html", count=-1)

if __name__ == '__main__':
    app.run(debug=True)