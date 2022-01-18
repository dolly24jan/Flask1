from flask import Flask,render_template,request,jsonify
import os
import codecs
app= Flask(__name__)
@app.route('/', defaults={'file_name': "file1.txt",'start_line_no': "0",'end_line_no':"150"})
@app.route('/<file_name>',defaults={'start_line_no': "0", 'end_line_no':"150"})
@app.route('/<file_name>/<start_line_no>',defaults={'end_line_no':"150"})
@app.route('/<file_name>/<start_line_no>/<end_line_no>')

def user(file_name,start_line_no,end_line_no):
    try:
        if file_name =="file2.txt":
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'r', encoding='utf-16be',errors='ignore') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("index2.html", content=txt)
            else:    
                with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("index2.html", content=contents)
            
        elif file_name =="file3.txt":
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'rb') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("index2.html", content=txt)
            else:    
                with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("index2.html", content=contents)

        elif file_name =="file4.txt":
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'r', encoding='utf-16be',errors='ignore') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("index2.html", content=txt)
            else:    
                with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("index2.html", content=contents)
        else:
            # with codecs.open("file1.txt",'r') as file:
            with open('file1.txt','r') as file:
                contents = file.read()
                # return jsonify(contents)
            return render_template("index2.html", content=contents)

    except Exception as e:
        return {"status":False,"message":"Not displayed due to :"+str(e)}

if __name__=="__main__":
    app.run(debug=True)