from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("BMI calculator")
root.minsize(600,400)
root.maxsize(600,400)


photo=PhotoImage(file="icon.png")
root.iconphoto(True,photo)
root.configure(background="#999999")


label_titleb =Label(root,text="BODY MASS INDEX",font=("Arial", 30), foreground="black",background="#999999",padx=15,pady=15)
label_titleb.pack(pady=5)


lable_weight=Label(root,text="Enter your weight in kg     ",font=("Arial",20),foreground="Black",background="#999999",padx=5,pady=5)
lable_weight.place(x=20,y=100)
lable_height=Label(root,text="Enter your Height in meter",font=("Arial",20),foreground="Black",background="#999999",padx=5,pady=5)
lable_height.place(x=20,y=160)
lable_bmi=Label(root,text="Your body mass index",font=("Arial",20),foreground="Black",background="#999999",padx=5,pady=5)
lable_bmi.place(x=20,y=220)

weight = Entry(root,width=20,font=("Arial",14))
weight.place(x=370,y=120)
height=Entry(root,width=20,font=("Arial",14))
height.place(x=370,y=170)


def submit():
    global lableout11
    input_data=(weight.get(),height.get())
    count=0
    for i in input_data:
        k=str(i)
        if len(k)==0:
            count+=1
    if count>0:
        messagebox.showwarning("Warning","Please fill all the fields")
    else:
        ans=float(input_data[0])/(float(input_data[1])*float(input_data[1]))
        ans1=round(ans,2)
        lableout11=Label(root,text=str(ans1),font=("Arial",16),foreground="black",background="#999999",padx=15,pady=15)
        lableout11.place(x=370,y=220)


def reset():
    for i in root.winfo_children():
        if isinstance(i,Entry):
            i.delete(0,"end")
    lableout11.destroy()


submit_button=Button(root,text="SUBMIT",font=("Arial",14),foreground="Black",background="#999999",padx=5,pady=5,width=10,command=submit)
submit_button.place(x=50,y=290)

reset_button=Button(root,text="RESET",font=("Arial",14),foreground="Black",background="#999999",padx=5,pady=5,width=10,command=reset)
reset_button.place(x=230,y=290)

exit_button=Button(root,text="EXIT",font=("Arial",14),foreground="Black",background="#999999",padx=5,pady=5,width=10,command=root.destroy)
exit_button.place(x=410,y=290)

root.mainloop()