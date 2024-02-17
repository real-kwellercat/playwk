import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import getpass
import subprocess
import time

gamefile = "C:\\WK\\windowkill-vulkan.exe"

def open_program():
    # Specify the path to the program you want to open
    
    # Open the program
    program_process = subprocess.Popen(gamefile + " --rendering-driver opengl3")
    
    # Wait for 5 minutes
    time.sleep(6 * 60)  # 5 minutes in seconds would be 5 * 60.
    
    # Check if the program is still running
    if program_process.poll() is None:
        # If the program is still running, terminate the process
        program_process.terminate()
        # Display a popup message when the timer is over
        messagebox.showinfo("Timer Over", "The timer has ended. Please close the program.")
    
        # Terminate the Tkinter window when the button in the popup is clicked
        root.destroy()
    else:
        messagebox.showinfo("nope.", "Try that again.")
        program_process = subprocess.Popen(program_path)

def on_button_click():
    # Call the function to open the program
    open_program()

# Create a borderless window
root = tk.Tk()
root.overrideredirect(True)
# Set window attributes
root.attributes("-topmost", False)  # Set topmost attribute to False


# Set transparency level (0.0 to 1.0)
root.attributes('-alpha', 1)

# Set window size and position
root.geometry('600x600+100+100')

# Get the username of the currently logged-in user
username = getpass.getuser()

profile_image = Image.open("vmpfp-malware-testing.jpg")
profile_image = profile_image.resize((100, 100))
profile_photo = ImageTk.PhotoImage(profile_image)
# Create a circular mask
mask = Image.new("L", profile_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, profile_image.size[0], profile_image.size[1]), fill=255)

# Apply the circular mask to the profile picture
profile_image.putalpha(mask)

# Convert the image to PhotoImage format
profile_photo = ImageTk.PhotoImage(profile_image)

# Create a label widget to display the profile picture
profile_label = tk.Label(root, image=profile_photo, bg=root.cget("bg"))
profile_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)  # Position the profile picture

# Create a label widget to display the username
text_label = tk.Label(root, text=f"Hello, {username}!\nI have a challenge for you.", font=("Arial", 12), bg=root.cget("bg"))
text_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)  # Position the text label

# Create a label widget to display the message.
text_label = tk.Label(root, text=f"Play windowkill for 5 minutes, and I will let you go.", font=("Arial", 12), bg=root.cget("bg"))
text_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)  # Position the text label

# Create a button to trigger the program opening
button = tk.Button(root, text="Okay...?", command=on_button_click)
button.grid(row=2, column=0, columnspan=2, pady=(20, 0), padx=10, sticky="ew")  # Use grid instead of pack




# Run the Tkinter event loop
root.mainloop()
