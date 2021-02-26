import subprocess
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import traceback
from selenium.webdriver.support.wait import WebDriverWait
import AutomationWorking
listProject = {}
def insertItemToTree(item):
    tree.insert('', 'end', values=item)

def EnterProjectRangeAndPath(item , listProject):
    insertItemToTree(item)
    listProject.append(item)


def run(inputPathCom , procedure):
    i = 0
    for line in tree.get_children():
        try:
            [KDPrange , comName , exceptCom ,isDone ] = tree.item(line)['values']
            AutomationWorking.run(KDPrange , inputPathCom+comName , exceptCom , procedure )
            tree.item(line)['values'] = [KDPrange , comName , 'True']
            AutomationWorking.waitThreadAndJoin(5)
        except:
            print(traceback.format_exc())
            print('exception happend and cant handle it')
            continue
def AllHandle(value):
    if value == 1:
        for cb in CBoxs:
            cb.select()
    else:
        for cb in CBoxs:
            cb.deselect()
header = ['Range', 'Path','Except' ,'Done']
root = Tk()
root.title('Stop-AutomationBot')
root.geometry('400x800')
hello = Label(root , text='Created by ThanhCong', fg='#2631ab')
hello.place(relx=0.6 , rely=0.9)
startButton = Button(root , text='Start' , command=lambda: run(inputPathCom.get() ,[CheckVarStart.get() , CheckVarClose.get(),  CheckVarPaste.get() ,
                                                                                    CheckVarOpen.get() , CheckVarEnterCode.get() , CheckVarHandleFirefox.get()] ))
startButton.place(relx=0.5,rely=0.85)
container = ttk.Frame(root, width=400, height=100)
container.pack(fill='both', expand=True)
# create a treeview with dual scrollbars
tree = ttk.Treeview(columns=header, show="headings")
vsb = ttk.Scrollbar(orient="vertical",
command= tree.yview)
hsb = ttk.Scrollbar(orient="horizontal",
command= tree.xview)
tree.configure(yscrollcommand=vsb.set,
xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew', in_=container)
vsb.grid(column=1, row=0, sticky='ns', in_=container)
hsb.grid(column=0, row=1, sticky='ew', in_=container)
container.pack(fill=None, expand=False)
container.grid_columnconfigure(0, weight=1)
container.grid_rowconfigure(0, weight=1)
for col in header:
        tree.heading(col, text=col.title())
        # adjust the column's width to the header string
        tree.column(col,width=tkFont.Font().measure(col.title()))


rangeInputFrame = Frame(root)
rangeInputFrame.pack(fill='both', expand=FALSE)
labelRange = Label(rangeInputFrame, text='Range')
inputRange = Entry(rangeInputFrame)
labelRange.pack(side=LEFT , anchor=NW , padx=20)
inputRange.pack(side=RIGHT , anchor=NE , padx=40)

rangeInputFrame2 = Frame(root)
rangeInputFrame2.pack(fill='both', expand=FALSE)
labelPath = Label(rangeInputFrame2, text='Name')
inputPath = Entry(rangeInputFrame2)
labelPath.pack(side=LEFT , anchor=NW , padx=20)
inputPath.pack(side=RIGHT , anchor=NE , padx=40)


rangeInputFrame7 = Frame(root)
rangeInputFrame7.pack(fill='both', expand=FALSE)
labelExcept7 = Label(rangeInputFrame7, text='Except')
inputExcept7 = Entry(rangeInputFrame7)
labelExcept7.pack(side=LEFT , anchor=NW , padx=20)
inputExcept7.pack(side=RIGHT , anchor=NE , padx=40)

AddButton = Button(root , text='add project' , command=lambda: insertItemToTree([inputRange.get() , inputPath.get() , inputExcept7.get() ,'false']))
AddButton.pack()

rangeInputFrame3 = Frame(root)
rangeInputFrame3.pack(fill='both', expand=FALSE)
labelPathCom = Label(rangeInputFrame3, text='PathToComputer')
inputPathCom = Entry(rangeInputFrame3)
labelPathCom.pack(side=LEFT , anchor=NW , padx=20)
inputPathCom.pack(side=RIGHT , anchor=NE , padx=40)

rangeInputFrame4 = Frame(root)
rangeInputFrame4.pack(fill='both', expand=FALSE)
labelPathCode = Label(rangeInputFrame4, text='PathOfCode')
inputPathCode = Entry(rangeInputFrame4)
labelPathCode.pack(side=LEFT , anchor=NW , padx=20)
inputPathCode.pack(side=RIGHT , anchor=NE , padx=40)

rangeInputFrame5 = Frame(root)
rangeInputFrame5.pack(fill='both', expand=FALSE)
labelPathChrome = Label(rangeInputFrame5, text='PathOfChrome')
inputPathChrome = Entry(rangeInputFrame5)
labelPathChrome.pack(side=LEFT , anchor=NW , padx=20)
inputPathChrome.pack(side=RIGHT , anchor=NE , padx=40)

rangeInputFrame6 = Frame(root)
rangeInputFrame6.pack(fill='both', expand=FALSE)
labelBill = Label(rangeInputFrame6, text='BillNumber')
inputBill = Entry(rangeInputFrame6)
labelBill.pack(side=LEFT , anchor=NW , padx=20)
inputBill.pack(side=RIGHT , anchor=NE , padx=40)

CheckVarStart = IntVar()
CheckVarClose = IntVar()
CheckVarPaste = IntVar()
CheckVarOpen = IntVar()
CheckVarEnterCode = IntVar()
CheckVarHandleFirefox = IntVar()
CheckVarAll = IntVar()
CStart = Checkbutton(root, text = "Start Computer", variable = CheckVarStart, \
                 onvalue = 1, offvalue = 0)
CClose = Checkbutton(root, text = "Close Opening Window", variable = CheckVarClose, \
                 onvalue = 1, offvalue = 0)
CPaste = Checkbutton(root, text = "Paste File", variable = CheckVarPaste, \
                 onvalue = 1, offvalue = 0)
COpen = Checkbutton(root, text = "Open File", variable = CheckVarOpen, \
                 onvalue = 1, offvalue = 0)
CEnterCode = Checkbutton(root, text = "Enter Code", variable = CheckVarEnterCode, \
                 onvalue = 1, offvalue = 0)
CHandleFirefox = Checkbutton(root, text = "Handle FireFox", variable = CheckVarHandleFirefox, \
                 onvalue = 1, offvalue = 0)

CheckVars = [CheckVarStart , CheckVarClose , CheckVarPaste , CheckVarOpen , CheckVarEnterCode , CheckVarHandleFirefox]
CBoxs = [CStart , CClose ,CPaste ,COpen ,CEnterCode ,CHandleFirefox ]

CAll = Checkbutton(root, text = "All", variable = CheckVarAll, \
                 onvalue = 1, offvalue = 0 , command=lambda:AllHandle(CheckVarAll.get()))
CStart.pack()
CClose.pack()
CPaste.pack()
COpen.pack()
CEnterCode.pack()
CHandleFirefox.pack()
CAll.pack()

root.mainloop()