from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import time
from tkinter.simpledialog import *
from tkinter.font import *
from tkinter.colorchooser import askcolor

#file menu methods
def newFile(event=""):
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END) #firstline 0th character 1.0
def openFile(event=""):
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def saveFile(event=""):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp(event=""):
    root.destroy()

#edit menu methods
def find(event=""):
    TextArea.tag_remove('found', 1.0, END)
    target = askstring('Find', 'Search String :')
    if target:
        idx = '1.0'
        while 1:
            idx = TextArea.search(target, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(target))
            TextArea.tag_add('found', idx, lastidx)
            idx = lastidx
            TextArea.tag_configure('found', foreground='white', background='blue')
def undo(event=""):
    TextArea.event_generate("<<Undo>>")
def redo(event=""):
    TextArea.event_generate("<<Redo>>")
def paste(event=""):
    TextArea.event_generate("<<Paste>>")
def cut(event=""):
    TextArea.event_generate("<<Cut>>")
def copy(event=""):
    TextArea.event_generate("<<Copy>>")
def select_all(event=""):
    #select sel tag to select all text
    TextArea.tag_add(SEL, 1.0, END)
    #TextArea.mark_set(0.0, END)
    #TextArea.see(INSERT)
def delete(event=""):
    TextArea.delete(1.0,END)

#help menu start
def about():
    showinfo("About", "Notepad by-- keya panja")
def feedback():
    value=tmsg.askquestion("Feedback? ","Was your experience good ,you used this GUI....")
    if value=="yes":
        msg="Great....Rate us in playstore"
    else:
        msg="tell us what went wrong,we will back to you soon..."
    tmsg.showinfo("Experience",msg)
def get_time():
        global hours,minute,second,am_pm,day,month,year
        hours = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm =time.strftime("%p")
        day =time.strftime("%A")
        month = time.strftime("%B")
        year =time.strftime("%Y")
def showTime():
        get_time()
        tmsg.showinfo("Time",
                      "      " + hours + " : " +minute + " : " + second + " " + am_pm + "\n" + day + "," + month + "," + year)
#format menu
def changebg():
    (triple, color) = askcolor()
    if color:
        TextArea.config(bg=color)

    # If the user clicks the OK button on the pop-up, the returned value will be a tuple (triple, color), where triple is a tuple (R, G, B) containing red, green, and blue values in the range [0,255] respectively, and color is the selected color as a regular Tkinter color object.
    # If the users clicks Cancel, this function will return (None, None).
def changefg():
    (triple, color) = askcolor()
    if color:
        TextArea.config(fg=color)
def italicText(event=""):
        # works only if text is selected
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "italic" in current_tags:
            TextArea.tag_remove("italic", "sel.first", "sel.last")
        else:
            TextArea.tag_add("italic", "sel.first", "sel.last")
            italic_font = Font(TextArea, TextArea.cget("font"))
            italic_font.configure(slant="italic")
            TextArea.tag_configure("italic", font=italic_font)
    except:
        pass
def overstrickText(event=""):
        # works only if text is selected
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "overstrike" in current_tags:
            TextArea.tag_remove("overstrike", "sel.first", "sel.last")
        else:
            TextArea.tag_add("overstrike", "sel.first", "sel.last")
            overstrike_font = Font(TextArea,TextArea.cget("font"))
            overstrike_font.configure(overstrike=1)
            TextArea.tag_configure("overstrike", font=overstrike_font)
    except:
        pass
def underlineText(event=""):
        # works only if text is selected
    try:
        current_tags = TextArea.tag_names("sel.first")
        if "underline" in current_tags:
            TextArea.tag_remove("underline", "sel.first", "sel.last")
        else:
            TextArea.tag_add("underline", "sel.first", "sel.last")
            underline_font = Font(TextArea, TextArea.cget("font"))
            underline_font.configure(underline=1)
            TextArea.tag_configure("underline", font=underline_font)
    except:
        pass
def boldText(event="", *args):
        # works only if text is selected
    try:
        current_tag = TextArea.tag_names("sel.first")
        if "bold" in current_tag:
            TextArea.tag_remove("bold", "sel.first", "sel.last")
        else:
            TextArea.tag_add("bold", "sel.first", "sel.last")
            bold_font = Font(TextArea, TextArea.cget("font"))
                # cget(self, key)
                # Return the resource value for a KEY given as string.
            bold_font.configure(weight="bold")
            TextArea.tag_configure("bold", font=bold_font)
    except:
        pass

#view menu
def status_update():
    sb=status_var.get()
    if sb==1:
        sbar.pack(side=BOTTOM, fill=X)
        statusvar.set("    Notepad.......")
        sbar.update()
    else:
        sbar.pack_forget()
def zoom():
    pass

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad_icon.ico")
    root.geometry("300x250+300+300")
    root.minsize(350, 370)
#Add TextArea
    TextArea = Text(root.master,undo=True, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
# Lets create a menubar
    MenuBar = Menu(root)
#File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile,accelerator="Ctrl+N")
    FileMenu.add_command(label="Open", command = openFile,accelerator="ctrl+O")
    FileMenu.add_command(label = "Save", command=saveFile,accelerator="ctrl+S")
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp,accelerator="Ctrl+Q")
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    root.bind_all("<Control-s>",saveFile)
    root.bind_all("<Control-n>", newFile)
    root.bind_all("<Control-o>" ,openFile)
    root.bind_all("<Control-q>",quitApp)
# File Menu ends
#edit menu starts
    EMenu = Menu(MenuBar, tearoff=0)
    EMenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
    EMenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
    EMenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
    EMenu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
    EMenu.add_command(label="Redo", command=redo, accelerator="Ctrl+Y")
    EMenu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
    EMenu.add_separator()
    EMenu.add_command(label="Find", command=find, accelerator="Ctrl+F")
    EMenu.add_command(label="clear All", command=delete)
    MenuBar.add_cascade(label="Edit", menu=EMenu)
    root.bind_all("<Control-f>",find)
    root.bind_all("<Control-z>",undo)
    root.bind_all("<Control-y>",redo)
    root.bind_all("<Control-c>",copy)
    root.bind_all("<Control-v>",paste)
    root.bind_all("<Control-x>",cut)
    root.bind_all("<Control-a>",select_all)
    root.bind_all("<Control-d>", delete)
#format menu
    fontOptions = families(root)
    font1 = Font(family="Arial", size=11)
    TextArea.configure(font=font1)
    FMenu = Menu(MenuBar,tearoff=0)
    fsubmenu = Menu(FMenu, tearoff=0)
    ssubmenu = Menu(FMenu, tearoff=0)
    for option in fontOptions:
        fsubmenu.add_command(label=option, command=lambda option=option: font1.config(family=option))
    for I in range(1, 31):
        ssubmenu.add_command(label=str(I), command=lambda I=I: font1.configure(size=I))
    FMenu.add_command(label="Change Background color", command=changebg)
    FMenu.add_command(label="Change Font Color", command=changefg)
    FMenu.add_cascade(label="Font style", underline=0, menu=fsubmenu)
    FMenu.add_cascade(label="Font Size", underline=0, menu=ssubmenu)
    FMenu.add_command(label="Bold", command=boldText, accelerator="Ctrl+B")
    FMenu.add_command(label="Italic", command=italicText, accelerator="Ctrl+I")
    FMenu.add_command(label="Underline", command=underlineText, accelerator="Ctrl+U")
    FMenu.add_command(label="Overstrick", command=overstrickText, accelerator="Ctrl+O")
    MenuBar.add_cascade(label="Format", menu=FMenu)
    root.configure(menu=MenuBar)
    root.bind_all("<Control-b>",boldText)
    root.bind_all("<Control-i>",italicText)
    root.bind_all("<Control-u>",underlineText)
    root.bind_all("<Control-o>",overstrickText)
# view menu
    VMenu = Menu(MenuBar, tearoff=0)
    status_var = BooleanVar()
    statusvar = StringVar()
    sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
    v = VMenu.add_checkbutton(label='Status Bar', onvalue=1, offvalue=0, variable=status_var,
                              command=status_update)
    zoom = Menu(VMenu, tearoff=0)
    zoom.add_command(label="zoom in", accelerator="Ctrl+PLUS")
    zoom.add_command(label="zoom out", accelerator="Ctrl+MINUS")
    zoom.add_command(label="Default zoom restore", accelerator="Ctrl+O")
    VMenu.add_cascade(label="zoom", menu=zoom)
    MenuBar.add_cascade(label="View", menu=VMenu)
#help menu
    HMenu = Menu(MenuBar, tearoff=0)
    HMenu.add_command(label="Time", command=showTime)
    HMenu.add_command(label="Feedback", command=feedback)
    HMenu.add_separator()
    HMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HMenu)
    root.config(menu=MenuBar)
#Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    TextArea.focus_set()
    root.mainloop()