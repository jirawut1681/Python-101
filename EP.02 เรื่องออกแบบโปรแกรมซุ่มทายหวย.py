#นำเข้า function monitor
from tkinter import *                                     #นำเข้า function tkinter , " * " คือทั้งหมด
from tkinter import ttk                                   #นำเข้า theme ของ tkinter
from tkinter import messagebox                            #นำเข้า messagebox
import random

from datetime import datetime

#เรียกคำสั่งเพื่อสร้างโปรแกรม
GUI = Tk()                                                #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรม:สุ่มหวย')                                 #นี่คือชื่อโปรแกรม
GUI.geometry('400x450')                                   #นี่คือขนาดโปรแกรม



#############################################
c = random.randint(0,99)
 
    
def Button2():                                            #เรียก function 
    text = (c)
    messagebox.showinfo('เลขที่ออก',text)                    #โชว์ Alert มีคำสั่ง 3 = showinfo, showwarning, showerror 



#สร้าง Button 1
FB1 = LabelFrame(GUI,text='กล่องเสี่ยงโชค',font=('Angsana'),fg='green')                     #คล้ายกระดาน มีกรอบLabel
FB1.place(x=125,y=50)                                      #ตำแหน่งของ Button
B1 = ttk.Button(FB1,text='สุ่มหวย',command=Button2)           #ชื่อ Button 3
B1.pack(ipadx=20,ipady=20,padx=20,pady=10)                 #ขนาดของ Button 3

##############################################################################

#GUI = Tk()
#GUI.title('Clock')
#GUI.geometry('60x60')

lb_clock = Label(font='times 16')
lb_clock.pack(anchor=CENTER, expand=YES)

def tick():
    global curtime
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')
    lb_clock.config(text=ftime)
    lb_clock.after(1000, tick)                                  #ให้เรียกฟังก์ชันตัวมันเองทุก 1 วินาที

tick()          #เรียกฟังก์ชันขึ้นมาทำงานครั้งแรก

#############################################################################

GUI.mainloop()                                                  #function mainloop
