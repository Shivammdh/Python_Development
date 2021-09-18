from tkinter import*
from pytube import YouTube

root=Tk()
root.geometry('1200x1500')
root.resizable(0,0)
root.title("Youtube video downloader @_shivam_sharma")
Label(root,text="Youtube vidio downloader",font='arial 15 bold').pack()
Label(root,text="@_shivam_sharma",font='arial 10 bold').pack()

link=StringVar()
Label(root,text="paste link here:",font='arial 10 bold').place(x=60,y=200)
link_enter=Entry(root,width=70,textvariable=link).place(x=20,y=280)

def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root,text='DOWNLOADED',font='arial 15').place(x=180,y=210)
    
Button(root,text='DOWNLOAD',font='arial 15 bold',bg='pale violet red',padx=2,command=Downloader).place(x=200,y=400)
root.mainloop()