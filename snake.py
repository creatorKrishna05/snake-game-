import random
import customtkinter as ctk



# ----------------------------
# APP SETTINGS
# ----------------------------python
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ----------------------------
# MAIN WINDOW
# ----------------------------
root = ctk.CTk()
root.title("Snake Water Gun Game")
root.geometry("700x500")
root.resizable(False, False)

# ----------------------------
# GAME VARIABLES
# ----------------------------
user_score = 0
computer_score = 0

choices = {
    "Snake": 1,
    "Water": -1,
    "Gun": 0
}

reverse_dict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# ----------------------------
# PLAY FUNCTION
# ----------------------------
def play(user_choice):
    global user_score, computer_score

    computer = random.choice([-1, 0, 1])
    you = choices[user_choice]

    # Result Logic
    if computer == you:
        result = "🤝 It's a Draw!"
        color = "yellow"

    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):

        result = "🎉 You Win!"
        user_score += 1
        color = "lightgreen"

    else:
        result = "💀 Computer Wins!"
        computer_score += 1
        color = "red"

    # Update Result Text
    result_label.configure(
        text=f"""
You Chose: {user_choice}

Computer Chose: {reverse_dict[computer]}

{result}
""",
        text_color=color
    )

    # Update Scores
    score_label.configure(
        text=f"👨 You: {user_score}   |   💻 Computer: {computer_score}"
    )

# ----------------------------
# TITLE
# ----------------------------
title = ctk.CTkLabel(
    root,
    text="🐍 Snake Water Gun 🔫",
    font=("Poppins", 32, "bold")
)
title.pack(pady=20)

# ----------------------------
# SCORE LABEL
# ----------------------------
score_label = ctk.CTkLabel(
    root,
    text="👨 You: 0   |   💻 Computer: 0",
    font=("Arial", 22, "bold"),
    text_color="cyan"
)
score_label.pack(pady=10)

# ----------------------------
# BUTTON FRAME
# ----------------------------
button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.pack(pady=30)

# Snake Button
snake_btn = ctk.CTkButton(
    button_frame,
    text="🐍 Snake",
    font=("Arial", 20, "bold"),
    width=180,
    height=60,
    corner_radius=15,
    fg_color="#2ecc71",
    hover_color="#27ae60",
    command=lambda: play("Snake")
)
snake_btn.grid(row=0, column=0, padx=15)

# Water Button
water_btn = ctk.CTkButton(
    button_frame,
    text="💧 Water",
    font=("Arial", 20, "bold"),
    width=180,
    height=60,
    corner_radius=15,
    fg_color="#3498db",
    hover_color="#2980b9",
    command=lambda: play("Water")
)
water_btn.grid(row=0, column=1, padx=15)

# Gun Button
gun_btn = ctk.CTkButton(
    button_frame,
    text="🔫 Gun",
    font=("Arial", 20, "bold"),
    width=180,
    height=60,
    corner_radius=15,
    fg_color="#e74c3c",
    hover_color="#c0392b",
    command=lambda: play("Gun")
)
gun_btn.grid(row=0, column=2, padx=15)

# ----------------------------
# RESULT LABEL
# ----------------------------
result_label = ctk.CTkLabel(
    root,
    text="Choose Snake, Water or Gun",
    font=("Arial", 24, "bold"),
    justify="center"
)
result_label.pack(pady=40)

# ----------------------------
# FOOTER
# ----------------------------
footer = ctk.CTkLabel(
    root,
    text="Made with Python + CustomTkinter",
    font=("Arial", 14),
    text_color="gray"
)
footer.pack(side="bottom", pady=15)

# ----------------------------
# RUN APP
# ----------------------------
root.mainloop()