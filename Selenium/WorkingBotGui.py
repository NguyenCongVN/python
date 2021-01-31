from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import AutomationWorking
import WindowAutomationPart
import traceback
from selenium.webdriver.support.wait import WebDriverWait
listProject = {}
def insertItemToTree(item):
    tree.insert('', 'end', values=item)

def EnterProjectRangeAndPath(item , listProject):
    insertItemToTree(item)
    listProject.append(item)


def run(inputPathCom , inputPathCode , inputPathChrome , inputBill):
    try:
        i = 0
        for line in tree.get_children():
            if i == 0:
                driver = AutomationWorking.InitRun(inputPathChrome, inputPathCode , True)
                i = i + 1
            else:
                driver = AutomationWorking.InitRun(inputPathChrome, inputPathCode , False)
            wait = WebDriverWait(driver, 40)
            [KDPrange , comName , isDone ] = tree.item(line)['values']
            AutomationWorking.run(driver , wait ,KDPrange , inputPathCom+comName , inputBill)
            tree.item(line)['values'] = [KDPrange , comName , 'True']
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
                driver.close()
    except:
        print(traceback.format_exc())
        while True:
            try:
                driver = AutomationWorking.InitRun(inputPathChrome, inputPathCode)
                wait = WebDriverWait(driver, 40)
                AutomationWorking.disableBill(driver, wait, KDPrange)
                break
            except:
                continue
header = ['Range', 'Path', 'Done']
root = Tk()
root.title('Stop-AutomationBot')
root.geometry('400x600')
hello = Label(root , text='Created by ThanhCong', fg='#2631ab')
hello.place(relx=0.6 , rely=0.9)
startButton = Button(root , text='Start' , command=lambda: run(inputPathCom.get() ,inputPathCode.get() , inputPathChrome.get() , inputBill.get()))
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
AddButton = Button(root , text='add project' , command=lambda: insertItemToTree([inputRange.get() , inputPath.get(),'false']))
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

root.mainloop()