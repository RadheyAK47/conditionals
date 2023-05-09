from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("condition")
root.geometry("400x400")


#Question1
que1_radiobutton=StringVar(value="0")

que1=Label(root,text="Q.1 : Do you have headache and sore throat?")
que1.place(relx=0.5,rely=0.05,anchor=CENTER)

que1_r1=Radiobutton(root,text="Yes",variable=que1_radiobutton,value="yes")
que1_r1.place(relx=0.3,rely=0.1,anchor=CENTER)

que1_r2=Radiobutton(root,text="No",variable=que1_radiobutton,value="no")
que1_r2.place(relx=0.3,rely=0.15,anchor=CENTER)
#Q1 end


#Q2
que2_radiobutton=StringVar(value="0")

que2=Label(root,text="Q.2 : Is your body temprature high?")
que2.place(relx=0.445,rely=0.25,anchor=CENTER)

que2_r1=Radiobutton(root,text="yes",variabl=que2_radiobutton,value="yes")
que2_r1.place(relx=0.3,rely=0.3,anchor=CENTER)

que2_r2=Radiobutton(root,text="No",variable=que2_radiobutton,value="no")
que2_r2.place(relx=0.3,rely=0.35,anchor=CENTER)
#Q2 end


#Q3
que3_radiobutton=StringVar(value="0")

que3=Label(root,text="Q.3 : Are there any symptoms of eye redness?")
que3.place(relx=0.45,rely=0.45,anchor=CENTER)

que3_r1=Radiobutton(root,text="yes",variabl=que3_radiobutton,value="yes")
que3_r1.place(relx=0.3,rely=0.5,anchor=CENTER)

que3_r2=Radiobutton(root,text="No",variable=que3_radiobutton,value="no")
que3_r2.place(relx=0.3,rely=0.55,anchor=CENTER)

def score():
    s=0
    if(que1_radiobutton.get()=="yes"):
        s=s+20
    if(que2_radiobutton.get()=="yes"):
        s=s+20    
    if(que3_radiobutton.get()=="yes"):
        s=s+20
        
    if(s<=20):
        messagebox.showinfo("Report","you dont need to visit a doctor")
    elif(s>20 and s<=40):
        messagebox.showinfo("Report","you might perhaps have to visit a doctor")
    else:
        messagebox.showinfo("Report","I strongly need to visit a doctor")

btn=Button(root,text="Report",command=score)
btn.place(relx=0.5,rely=0.75,anchor=CENTER)

root.mainloop()
