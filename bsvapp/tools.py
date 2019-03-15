from flask import Flask, flash, redirect, render_template, request, session, abort
import xlrd 
import os
 
app = Flask(__name__)

class Tool(object):
    sno = ""
    name = ""
    summary = ""
    docs = ""
    tags = ""
    apphub = ""
    toolstage = ""
    supporttype = ""
    technologies = ""
    process = ""
    clientlist = ""
    maincontacts = ""
    cost = ""
    benefits = ""
    def __init__(self, sno, name, summary):
        self.sno = sno
        self.name = name
        self.summary = summary
         
@app.route("/")
def index():
    return "Flask App!"
 
@app.route("/tools/<string:name>/")
def hello(name):
    return render_template('printtools.html', tools=getTools())

def getTools():
    loc = "C:/MyData/myjob/SRM/Box Sync/Box Sync/BSV/todo/Bsv Tools Master.xlsx"
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    tools = []
    row = 0
    moreItems = True
    
    while moreItems:
        row = row+1
        
        seq = sheet.cell_value(row, 0)
        
        name = sheet.cell_value(row, 1)
        summary = sheet.cell_value(row, 2)
        
        tool = Tool(seq, name, summary)
        tool.tags = sheet.cell_value(row, 3)
        tool.apphub = sheet.cell_value(row, 4)
        tool.toolstage = sheet.cell_value(row, 5)
        tool.supporttype = sheet.cell_value(row, 6)
        tool.technologies = sheet.cell_value(row, 7)
        tool.process = sheet.cell_value(row, 8)
        tool.clientlist = sheet.cell_value(row, 9)
        tool.maincontacts = sheet.cell_value(row, 10)
        tool.cost = sheet.cell_value(row, 11)
        tool.benefits = sheet.cell_value(row, 12)
        tool.docs = getFiles(name)
        
        tools.append(tool)
        try:
            nextseq = sheet.cell_value(row+1, 0)
        except:    
            moreItems=False
    
    return tools    
    

def getFiles(foldername):
    startpath = "C:/MyData/myjob/SRM/Box Sync/Box Sync/BSV/tools/" + foldername
    var_files = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        dirname = os.path.basename(root)
        for f in files:            
            var_files.append(dirname + '/' + f)            
    return var_files
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)