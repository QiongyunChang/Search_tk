'''
2019/10/02
Frame: Tkinter                                
Function module using: wolframalpha wikipedia 
Qiongyun Zhang                               
'''
import tkinter as tk
import wolframalpha 
import wikipedia

def function_1():
        #the second window   
        win2 = tk.Tk()
        win2.geometry("650x300") #the size of window
        win2.title("Result")
        txt = tk.Text(win2,height=25,font=18) 
        txt.pack()
        try : 
            #connect to wolframalpha             
            id = "3QJ59U-539QW66HE8"
            client = wolframalpha.Client(id)
            res = client.query(estr.get())
            answer = next(res.results).text
            txt.insert("end",answer)
            # print (answer)
            
            
        except:
            #connect to wiki
            wiki=wikipedia.summary(estr.get(), sentences = 3)
            txt.insert('2.0',wiki)
            
        win2.mainloop()
          
#build the windows       
win = tk.Tk() 
#win.configure(background='SlateGray')
win.geometry("500x150")
win.title("Search")
#msg for button
#info for entry 
#word color = white ,fg='white',bg='SlateGray'
label = tk.Label(win,text = "Searching ",font=14).pack()
estr = tk.StringVar()
entry = tk.Entry(win,text= estr).pack()

b = tk.Button(win,text="Submit",padx=1,pady=1,command= function_1).pack()
#interact with users
win.mainloop() 
