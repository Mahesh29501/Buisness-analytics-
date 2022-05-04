from tkinter import *
from tkinter import messagebox, filedialog
import os
import _thread
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


fln = ""
filesize = ""

def startDownload():
    global fln
    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save File", filetypes=(("JPG Image File","*.jpg"), ("JPEG Image File","*.jpeg"), ("PNG Image File","*.png"),\
                                                                                             ("ZIP File","*.zip"), ("ALl Files","*.*")))
    filename.set(os.path.basename(fln))
    _thread.start_new_thread(initDownload,())

def initDownload():
    global filesize
    furl = url.get()
    target = urlopen(furl)
    meta = target.info()
    filesize = float(meta["Content-Length"])
    downloaded = 0
    chunks = 1025*5
    filesize_mb = round((filesize/1024/1024),2)
    with open(fln,"wb") as f:
        while True:
            parts = target.read(chunks)
            if not parts:
                messagebox.showinfo("Download Completed", "Your file has been downloaded")
                break
            downloaded += chunks
            percentage = round((downloaded/filesize)*100,2)
            if percentage >100:
                percentage =100
            dowloadProgress.set(str(round((downloaded/1024/1024), 2)) + "MB/ " + str(filesize_mb) + "MB")
            dowloadPercentage.set(str(percentage) + "%")
            f.write(parts)
        f.close()

def exitProg():
    if messagebox.askyesno("Exit Program?", "Are you sure you want to exit the program?") == False:
        return False
    exit()

root = Tk()

url = StringVar()
filename = StringVar()
dowloadProgress = StringVar()
dowloadPercentage = StringVar()

dowloadProgress.set("N/A")
dowloadPercentage.set("N/A")

wrapper = LabelFrame(root, text="File URL")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

wrapper2 = LabelFrame(root, text="Download Information")
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(wrapper, text="Download URL: ")
lbl.grid(row=0, column=0, padx=10, pady=10)

ent = Entry(wrapper, textvariable=url)
ent.grid(row=0, column=1, padx=5, pady=10)

btn = Button(wrapper, text="Download", command=startDownload)
btn.grid(row=0, column=2, padx=5, pady=10)

lbl2 = Label(wrapper2, text="File")
lbl2.grid(row=0, column=0, padx=10, pady=10)
lbl3 = Label(wrapper2, textvariable=filename)
lbl3.grid(row=0, column=1, padx=10, pady=10)

lbl4 = Label(wrapper2, text="Download Progress")
lbl4.grid(row=1, column=0, padx=10, pady=10)
lbl5 = Label(wrapper2, textvariable=dowloadProgress)
lbl5.grid(row=1, column=1, padx=10, pady=10)

lbl6 = Label(wrapper2, text="Download Percentage")
lbl6.grid(row=2, column=0, padx=10, pady=10)
lbl7 = Label(wrapper2, textvariable=dowloadPercentage)
lbl7.grid(row=2, column=1, padx=10, pady=10)

Button(wrapper2, text="Exit Download", command=exitProg).grid(row=3, column=0, padx=10, pady=10)

root.geometry("450x400")
root.title("Downloader by Mahesh")
root.resizable(False, False)
root.mainloop()