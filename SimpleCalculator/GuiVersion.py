import customtkinter as ctk


app = ctk.CTk()

app.title("CALCULATOR")
app.geometry("400x500")
app.resizable(False,False)
app.configure(fg_color="#1E1E1E")
Entry = ctk.CTkEntry(
    app,
    width=350,
    height=50,
    font=("Segoe UI", 30),
    justify = "right",
    fg_color="#070707",
    text_color="white",
    border_color="#FFAA00"
)

Entry.grid(row = 0, column = 0 , columnspan = 4, padx = 20, pady = 10,
           )
           
def press(value):
    if value=="c":
        Entry.delete(0,"end")
        
    else:
        current = Entry.get()
        Entry.delete(0,"end")
        Entry.insert(0, current + str(value))

def calculate():
    current = Entry.get()
    try:
        result = eval(current)
    except Exception:
        result = "Error"
    Entry.delete(0,"end")
    Entry.insert(0, str(result))


#["AC","%","/"],

Button = [["c"],
          [7,8,9,"+"],
          [6,5,4,"-"],
          [1,2,3,"*"],
          [".",0,"=","/"]
         ]


row = 1

for row_value in Button:
    column = 0


    for value in row_value:
        
        if value == "=" :
            Btn = ctk.CTkButton(
                app,
                text = "=",
                font=("Segoe UI", 22, "bold"),
                height = 75,
                width = 35,
                border_color = "black",
                fg_color="#45B807",
                hover_color="#64E600",
                text_color="white",
                corner_radius = 12,

                command =lambda : calculate()
            )
        elif value in ["+", "-", "*", "/"]:
            Btn = ctk.CTkButton(
            app,
            text=str(value),
            font=("Segoe UI", 22, "bold"),
            height=75,
            width=35,
            fg_color="#FF9500",
            hover_color="#E68600",
            text_color="white",
            corner_radius=12,

            command =lambda  v=value: press(v)
            )
        elif value == "c":
            Btn = ctk.CTkButton(
            app,
            text=value,
            font=("Segoe UI", 20, "bold"),
            height=75,
            width=35,
            fg_color = "#D32F2F",
            hover_color = "#B7121C",
            text_color="white",
            corner_radius=22,

            command=lambda  v=value: press(v)
            )
            
        else:
            Btn = ctk.CTkButton(
            app,
            text = str(value),
            font=("Segoe UI", 18, "bold"),
            height = 75,
            width = 35,
            border_color = "black",
            fg_color="#333333",
            hover_color="#444444",
            text_color="white",
            corner_radius = 12,

            command =lambda v=value: press(v)
            )
        
        Btn.grid(row = row, column = column , sticky = "nsew" , padx =2,pady = 2 )

            


        column +=1
    row +=1

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

for i in range(1, 6):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()