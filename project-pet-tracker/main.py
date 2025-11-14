import tkinter as tk
from modules import pet_info, feeding_schedule, vet_appointments, favorite_toys

root = tk.Tk()
root.title("Pet Tracker")
# Give the window a good starting size
root.geometry("1280x720") 

# --- Configure the Grid Layout ---
# We are creating a 2x2 grid.
# We must tell the grid's rows and columns to "expand" 
# when the user resizes the window. 'weight=1' does this.
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# --- Load pet info frame first ---
# We still need this to get the 'pets' list
pet_info_frame = pet_info.get_frame(root)
# Place it in the top-left cell
pet_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# --- Pass pets list to feeding schedule ---
# Place it in the top-right cell
feeding_frame = feeding_schedule.get_frame(root, pet_info_frame.pets)
feeding_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# --- Other frames ---

# Place vet frame in the bottom-left cell
vet_frame = vet_appointments.get_frame(root)
vet_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Place toys frame in the bottom-right cell
toys_frame = favorite_toys.get_frame(root)
toys_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

root.mainloop()