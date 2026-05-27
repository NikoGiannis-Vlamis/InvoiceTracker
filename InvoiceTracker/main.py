from drinks import drinks
import tkinter as tk

window = tk.Tk()
window.title("Invoice Tracker")
window.geometry("400x600")
window.configure(bg="#1a1a2e")

total = 0
selected_drink = None

title_label = tk.Label(window, text="Invoice Tracker",
    bg="#1a1a2e", fg="#e94560", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

subtitle_label = tk.Label(window, text="Παρακολούθηση παραλαβής τιμολογίου",
    bg="#1a1a2e", fg="#8888aa", font=("Arial", 11))
subtitle_label.pack()

drinks = {"Coke": 2.50, "Beer 330ml": 3.50, "Beer 500ml": 5.00, "Water": 2.00}

def select_drink(name):
    global selected_drink
    selected_drink = name
    selected_label.config(text=f"Επιλέχθηκε: {name} - {drinks[name]}€")

for drink, price in drinks.items():
    btn = tk.Button(window, text=f"{drink} - {price}€",
        bg="#16213e", fg="#e0e0ff", font=("Arial", 11), width=25,
        command=lambda d=drink: select_drink(d))
    btn.pack(pady=5)

selected_label = tk.Label(window, text="Επιλέξτε προϊόν",
    bg="#1a1a2e", fg="#8888aa", font=("Arial", 11))
selected_label.pack(pady=10)

tk.Label(window, text="Ποσότητα:", bg="#1a1a2e",
    fg="#e0e0ff", font=("Arial", 11)).pack()
amount_entry = tk.Entry(window, font=("Arial", 12), width=10)
amount_entry.pack(pady=5)
total_label = tk.Label(window, text="Σύνολο: 0.00€",
    bg="#1a1a2e", fg="#e94560", font=("Arial", 14, "bold"))
total_label.pack(pady=10)

def add_item():
    global total
    if selected_drink is None:
        selected_label.config(text="Επιλέξτε προϊόν πρώτα!")
        return
    try:
        amount = int(amount_entry.get())
        apot = amount * drinks[selected_drink]
        total += apot
        total_label.config(text=f"Σύνολο: {total:.2f}€")
        selected_label.config(text=f"✓ {amount}x {selected_drink} = {apot:.2f}€")
        current = items_label.cget("text")
        items_label.config(text=f"{current}\n{amount}x {selected_drink} = {apot:.2f}€")
        amount_entry.delete(0, tk.END)
    except ValueError:
        selected_label.config(text="Βάλε έγκυρη ποσότητα!")

add_btn = tk.Button(window, text="Προσθήκη",
    bg="#e94560", fg="white", font=("Arial", 12, "bold"),
    width=20, command=add_item)
add_btn.pack(pady=10)

items_label = tk.Label(window, text="",
    bg="#1a1a2e", fg="#e0e0ff", font=("Arial", 10))
items_label.pack()

def clear_all():
    global total
    total = 0
    total_label.config(text="Σύνολο: 0.00€")
    selected_label.config(text="Επιλέξτε προϊόν")
    items_label.config(text="")
    amount_entry.delete(0, tk.END)

clear_btn = tk.Button(window, text="Καθαρισμός",
    bg="#16213e", fg="#8888aa", font=("Arial", 11),
    width=20, command=clear_all)
clear_btn.pack(pady=5)

window.mainloop()