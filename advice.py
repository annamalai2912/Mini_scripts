import requests
import customtkinter as ctk
from tkinter import messagebox
import time

# Function to fetch advice from the API
def fetch_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        new_advice = res["slip"]["advice"]
        display_typing_effect(new_advice)
    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Error", "Failed to fetch advice. Please check your internet connection.")

# Function to simulate typing animation
def display_typing_effect(new_advice):
    advice_text.set("")
    for i in range(len(new_advice) + 1):
        root.after(i * 100, update_advice_text, new_advice[:i])

# Function to update the displayed text
def update_advice_text(text):
    advice_text.set(f'"{text}"')

# Function to toggle advice visibility with hotkey (Ctrl+T)
def toggle_advice(event=None):
    if advice_label.winfo_ismapped():  # Check if the label is currently displayed
        advice_label.pack_forget()  # Hide it
    else:
        advice_label.pack(pady=40)  # Show it

# Create the main window with customtkinter
root = ctk.CTk()
root.title("Random Advisor Application")
root.geometry("500x150")  # Adjusted window size

# Set a custom color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create and configure widgets
advice_text = ctk.StringVar()

# Advice label styled like a quote box from a book
advice_label = ctk.CTkLabel(
    root, textvariable=advice_text, wraplength=450, font=("Georgia", 18, "italic"), text_color="black", padx=20, pady=40,
    fg_color="#f7f3e9", bg_color="#f7f3e9"
)

# Initial advice fetching
fetch_advice()

# Update the advice every 5 seconds
def periodic_advice():
    fetch_advice()
    root.after(10000, periodic_advice)

# Bind hotkey (Ctrl+T) to toggle the advice visibility
root.bind("<Control-t>", toggle_advice)

# Start periodic advice updates
periodic_advice()

# Run the main event loop
root.mainloop()
