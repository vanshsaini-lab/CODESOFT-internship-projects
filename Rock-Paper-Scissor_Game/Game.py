import customtkinter as ctk
import random as random

                             
app = ctk.CTk()

app.title("Mini Game")
app.geometry("400x500")
app.resizable(True,True)
app.configure(fg_color="#F5F5F5")

title_Label = ctk.CTkLabel(
    app,
    text = "  Rock-Paper-Scissor Game  ",
    font=("Segoe UI", 25, "bold" ),
    fg_color="#00E5FF",
    text_color="white",
    corner_radius=12
)
title_Label.pack( padx = 10 , pady = 20 )




user_label = ctk.CTkLabel(
    app, 
    text = "  user choice : none  ",
    font=("Segoe UI",18),
    fg_color="#FF9500",
    text_color="white",
    corner_radius=12
    
)
user_label.pack(  pady = 10 )



computer_label = ctk.CTkLabel(
    app, 
    text = "  computer choice : none  ",
    font=("Segoe UI", 18),
    fg_color="#FF9500",
    text_color="white",
    corner_radius=12
    
)
computer_label.pack( pady = 10 )



result_label = ctk.CTkLabel(
    app,
    text = "Choose : 🪨 Rock , 📄 Paper , ✂️ Scissors",
    font=("Segoe UI", 18),
    fg_color="#FF9500",
    text_color="black",
    corner_radius=12
  
)
result_label.pack( pady = 10 )



score_label = ctk.CTkLabel(
    app,
    text = "🏆 Score:\nYou = 0\nComputer = 0",
    font=("Segoe UI", 18),
    fg_color="#FF9500",
    text_color="white",
    corner_radius=12
    
)
score_label.pack( pady = 10 )




Btn_Frame = ctk.CTkFrame(
                        app,
                        fg_color = "#E4DFDF"
                        )
Btn_Frame.pack(pady=20)


Button_rock = ctk.CTkButton(
    Btn_Frame,
    text =  " 🪨 Rock ",
    width=120,
    height=75,
    font=("Segoe UI", 18),
    fg_color = "#7B2CBF",
    hover_color = "#9D4EDD",
    text_color = "#F8BA01",
    border_width = 5,
    border_color = "#FAA803",
    corner_radius = 12,
    command = lambda : press("🪨 Rock")
)

Button_rock.grid( row = 0 , column = 0 ,padx = 5 , pady = 10 , sticky = "ew" )


Button_paper = ctk.CTkButton(
    Btn_Frame,
    text =  " 📄 Paper ",
    width=120,
    height=75,
    font=("Segoe UI", 18),
    fg_color = "#7B2CBF",
    hover_color = "#9D4EDD",
    text_color = "#F8BA01",
    border_width = 5,
    border_color = "#FAA803",
    corner_radius = 12,
    command = lambda : press( "📄 Paper")
)

Button_paper.grid( row = 0 , column = 1 ,padx = 5 , pady = 10 , sticky = "ew")



Button_scissor = ctk.CTkButton(
    Btn_Frame,
    text =    "✂️ Scissors",
    width=120,
    height=75,
    font=("Segoe UI", 18),
    fg_color = "#7B2CBF",
    hover_color = "#9D4EDD",
    text_color = "#F8BA01",
    border_width = 5,
    border_color = "#FAA803",
    corner_radius = 12,
    command = lambda : press("✂️ Scissors")
)

Button_scissor.grid(row = 0 , column = 2 ,padx = 5 , pady = 10 , sticky = "ew")

for i in range(3):
    Btn_Frame.grid_columnconfigure(i, weight=1)




#control buttons

control_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

control_frame.pack(pady=10)

play_again_btn = ctk.CTkButton(
    control_frame,
    text="▶ Play Again",
    command=lambda : play_again(),
    fg_color="#0078D7",
    hover_color="#0063B1"
)

play_again_btn.grid(row=0, column=0, padx=10)


reset_btn = ctk.CTkButton(
    control_frame,
    text="🔄 Reset Score",
    command= lambda : reset(),
    fg_color="#D32F2F",
    hover_color="#B71C1C"
)

reset_btn.grid(row=0, column=1, padx=10)





user_score = 0
computer_score = 0




def press(value):
    user_choice = value
    user_label.configure(text = f"  user choice : {user_choice}  ")
    choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
    computer_choice = random.choice(choices)
    computer_label.configure(text = f"  computer choice : {computer_choice}  ")

    global user_score , computer_score 
    # Rock beats Scissors
    # Paper beats Rock
    # Scissors beats Paper


    if user_choice == computer_choice:
        result = "Tie"


    elif (
        (user_choice == "🪨 Rock" and computer_choice == "✂️ Scissors")
        or (user_choice == "📄 Paper" and computer_choice == "🪨 Rock")
        or (user_choice == "✂️ Scissors" and computer_choice == "📄 Paper")
    ):
        result = "YOU WIN!"
        user_score +=1


    else:
        result = "YOU LOSE!"
        computer_score +=1

# result_label change colors according to the results

    if result == "YOU WIN!":
        result_label.configure(
        text="🏆 YOU WIN!",
        fg_color="#00C853"
    )

    elif result == "YOU LOSE!":
        result_label.configure(
            text="❌ YOU LOSE!",
            fg_color="#FF1744"
            )

    else:
        result_label.configure(
            text="🤝 IT'S A TIE!",
            fg_color="#FFD600"
        )
    score_label.configure(
    text=f"🏆 Score:\nYou = {user_score}\nComputer = {computer_score}"
    )

# the buttons stops working when the score of anyone reaches  5
    if user_score == 5 or computer_score == 5:

        Button_rock.configure(state="disabled")
        Button_paper.configure(state="disabled")
        Button_scissor.configure(state="disabled")

def play_again():
    Button_rock.configure(state="normal")
    Button_paper.configure(state="normal")
    Button_scissor.configure(state="normal")

def reset():
    global user_score , computer_score 
    user_score = 0
    computer_score = 0

    score_label.configure(
        text = "🏆 Score:\nYou = 0\nComputer = 0"
    )

    user_label.configure(text = "  user choice : none  ")

    computer_label.configure(text = "  computer choice : none  ")

    result_label.configure(
        text = " Choose : 🪨 Rock , 📄 Paper , ✂️ Scissors",
        fg_color ="#FF9500"
        )
    play_again()
    

app.mainloop()




