import re
import tkinter as tk

# Function to check password strength
def check_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate password score
    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, etc.).")
    
    # Assess password strength
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, feedback

# Function to assess password and show results in GUI
def assess_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    
    # Display strength
    strength_label.config(text=f"Password Strength: {strength}")
    
    # Display feedback if necessary
    if feedback:
        feedback_text = "\n".join(feedback)
        feedback_label.config(text=feedback_text)
    else:
        feedback_label.config(text="Your password is strong.")

# Function to toggle password visibility
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show='')  # Show the password (plain text)
    else:
        password_entry.config(show='*')  # Hide the password (masked with *)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")

# Label for instructions
instruction_label = tk.Label(root, text="Enter your password:")
instruction_label.pack(pady=10)

# Entry widget for password input (initially hidden by `*`)
password_entry = tk.Entry(root, show='*', width=30)
password_entry.pack(pady=10)

# Checkbox for "Show Password"
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.pack()

# Button to trigger the password assessment
check_button = tk.Button(root, text="Check Password Strength", command=assess_password)
check_button.pack(pady=10)

# Label to display the password strength
strength_label = tk.Label(root, text="")
strength_label.pack(pady=10)

# Label to display feedback
feedback_label = tk.Label(root, text="", wraplength=350, justify="left")
feedback_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()

