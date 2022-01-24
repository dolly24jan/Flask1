from flask import Flask,render_template,request,jsonify
import os
import codecs
app= Flask(__name__)
"""
    1. this API used for reading files by default
    2. this Api used for reading files from by default start line number to ending line number 
    3. this API used for reading files from start line number(entered by user) and takes by default ending line number
    4. this API uised for reading files from start line number to ending line number(both entered by user) 
"""
@app.route('/', defaults={'file_name': "file1.txt",'start_line_no': "0",'end_line_no':"150"}, methods=['GET'])
@app.route('/<file_name>',defaults={'start_line_no': "0", 'end_line_no':"150"}, methods=['GET'])
@app.route('/<file_name>/<start_line_no>',defaults={'end_line_no':"150"}, methods=['GET'])
@app.route('/<file_name>/<start_line_no>/<end_line_no>', methods=['GET'])

def user(file_name,start_line_no,end_line_no):
    try:
        if (file_name =="file1.txt") or (file_name =="file2.txt") or (file_name =="file3.txt") or (file_name =="file4.txt") :
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'r',encoding='utf8',errors='ignore') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("index2.html", content=txt)
            elif int(start_line_no) > int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                return {"status":False,"message":"Not displayed due to invalid input of line no. :"}
            else:    
                with codecs.open(file_name, 'rb', encoding='utf8',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("index2.html", content=contents)
        else:
            return {"status":False,"message":"Invalid File Name...Please enter existing file name"}

    except Exception as e:
        return {"status":False,"message":"Not displayed due to :"+str(e)}

if __name__=="__main__":
    app.run(debug=True)
