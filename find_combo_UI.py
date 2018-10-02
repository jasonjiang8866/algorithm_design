from find_combo import find_combo
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
fields = 'Starting Number', 'Ending Number', 'Number of choice'

def makeform(root, fields):
   entries = []
   for field in fields:
      row = tk.Frame(root)
      lab = tk.Label(row, width=15, text=field, anchor='w')
      ent = tk.Entry(row)
      row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
      lab.pack(side=tk.LEFT)
      ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
      entries.append((field, ent))
   return entries

def fetch(entries):
    starting=entries[0][1].get()
    ending=entries[1][1].get()
    number=entries[2][1].get()
    #resultTxt.set(find_combo(range(int(starting),int(ending)+1),2).show_me_result(int(number)))
    outcome=find_combo(range(int(starting),int(ending)+1),2).show_me_result(int(number))
    sum_str=diff_str=''
    try:
        for item in outcome['sum']:
            sum_str+=str(item)[1:-1]
            sum_str+='\n'
    except Exception as e:
        sum_str="Unlucky man!!"
    try:
        for item in outcome['diff']:
            diff_str+=str(item)[1:-1]
            diff_str+='\n'
    except Exception as e:
        diff_str="Unlucky man!!"
    result.delete('1.0', tk.END)
    result.insert(tk.END, "sum pair is\n{0}\n diff pair is\n{1} ".format(sum_str,diff_str) )
    

root = tk.Tk()
#resultTxt = tk.StringVar()
#a=find_combo([1,2,3,4,5,6,7,8,9],2)

w = tk.Label(root, text='Python App')
w.pack()
inst = "Input the range and a number"
msg = tk.Message(root, text = inst)
msg.config(font=('Arial', 10, 'bold'),width=1000)
msg.pack()
ents = makeform(root, fields)
#root.bind('<Return>', (lambda event, e=ents: fetch(e)))
row1 = tk.Frame(root)
b1 = tk.Button(row1, text='Show',
          command=(lambda e=ents: fetch(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b2 = tk.Button(row1, text='Quit', command=root.quit)
b2.pack(side=tk.LEFT, padx=5, pady=5)
row1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
row2 = tk.Frame(root)
m = tk.Message(root)
result = ScrolledText(row2,background=m.cget("background"), relief="flat",
    borderwidth=0, font=m.cget("font"))
result.insert(tk.END,'Pending Input')
row2.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)
result.pack()



root.mainloop()
        
            
