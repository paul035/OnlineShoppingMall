from Tkinter import *

def fun():
    root.destroy()
def splashscreen():
    global root
    root=Tk()
    #root.geometry("1000x800")
    t=PhotoImage(file='100.gif')
    Label(root,image=t).grid(row=0,column=0)
   
    root.configure(bg='Blue')
    Label(root,text="Online Shopping Mall", font="tims 8 bold", bg="blue", fg="white").grid(row=1,column=3)
    Label(root,text="Enrollment No.:", bg="blue", fg="white", font="tims 8 bold").grid(row=3,column=1,sticky='w',pady=10)
    Label(root,text="Name :", bg="blue", fg="white", font="tims 8 bold").grid(row=2,column=1,sticky='w',pady=10)
    #Label(root,text=":",font="Aerial 10 bold",bg='coral').grid(row=2,column=2)
    Label(root,text="Ankur Pal", bg="blue", fg="white", font="tims 8 bold").grid(row=2,column=3,sticky=E,pady=10)

    #Label(root,text=":",font="Aerial 10 bold",bg='coral').grid(row=3,column=2)
    Label(root,text="161B035", bg="blue", fg="white", font="tims 8 bold").grid(row=3,column=3,sticky=E,pady=10)
    Label(root,text="Batch:", bg="blue", fg="white", font="tims 8 bold").grid(row=4,column=1,sticky='w',pady=10)
  #  Label(root,text=":",font="Aerial 10 bold",bg='coral').grid(row=4,column=2)
    Label(root,text="B_2(BX)", bg="blue", fg="white", font="tims 8 bold").grid(row=4,column=3,sticky=E,pady=10)
    Label(root,text="Branch:", bg="blue", fg="white", font="tims 8 bold").grid(row=5,column=1,sticky='w',pady=10)
  #  Label(root,text=":",font="Aerial 10 bold",bg='coral').grid(row=5,column=2)
    Label(root,text="Computer Science & Engineering", bg="blue", fg="white", font="tims 8 bold").grid(row=5,column=3,sticky=E,pady=10)
   # Label(root,text="& Engineering",font="Aerial 10 bold",bg='coral').grid(row=6,column=3,sticky=W)
    Label(root,text="Course:", bg="blue", fg="white", font="tims 8 bold").grid(row=7,column=1,sticky='w',pady=10)
   # Label(root,text=":",font="Aerial 10 bold",bg='coral').grid(row=7,column=2)
    Label(root,text="B. Tech (IInd Year)", bg="blue", fg="white", font="tims 8 bold").grid(row=7,column=3,sticky=E,pady=10)
    Label(root,text="E. Mail id:", bg="blue", fg="white", font="tims 8 bold").grid(row=8,column=1,sticky='w',pady=10)
    #Label(root,text="",font="Aerial 10 bold",bg='coral').grid(row=8,column=2)
    Label(root,text="ankurpal1997@gmail.com", bg="blue", fg="white", font="tims 8 bold").grid(row=8,column=3,sticky=E,pady=10)
   
    root.after(5000,fun)
    root.mainloop()
