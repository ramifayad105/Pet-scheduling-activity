import tkinter as tk

def get_frame(root):
    """
    Returns a Tkinter Frame for the Favorite Toys module.
    """
    # --- Color Palette (Copied from vet_appointments) ---
    BEIGE_BG = '#F5F5DC'   # frames
    LISTBOX_BG = "#FAFAFA" # listbox
    GREEN_BTN = '#4CAF50'  # add button
    RED_BTN = '#F44336'    # remove button
    TEXT_COLOR = '#333333' # text
    
    # Configure the main frame for the toys module
    frame = tk.LabelFrame(
        root, 
        text="Favorite Toys", 
        padx=10, 
        pady=10, 
        bg=BEIGE_BG, 
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR
    )
    
    # A list to store all the toy tuples
    # Each toy is a tuple: (Toy Name, Toy Type)
    favorite_toys_list = [
        ('Squeaky Hedgehog', 'Plush Toy'),
        ('Red Ball', 'Chew Toy'),
        ('Feather Wand', 'Interactive'),
    ]
    
    # Listbox to display the toys
    listbox = tk.Listbox(
        frame, 
        width=50, 
        height=5, 
        bg=LISTBOX_BG, 
        fg='black', 
        selectbackground=GREEN_BTN,
        selectforeground='white',
        bd=1,
        relief=tk.FLAT
    )
    listbox.pack(pady=5, fill=tk.X)

    def refresh_toys_listbox():
        """Clears and re-adds all toys to the listbox."""
        listbox.delete(0, tk.END)
        for toy in favorite_toys_list:
            name, toy_type = toy
            listbox.insert(tk.END, f"Name: {name}  |  Type: {toy_type}")

    # A frame to hold the "add toy" widgets
    add_frame = tk.Frame(frame, bg=BEIGE_BG)
    add_frame.pack(pady=5, fill=tk.X)

    # Label for the toy name
    tk.Label(add_frame, text="Toy Name:", bg=BEIGE_BG, fg=TEXT_COLOR).grid(row=0, column=0, padx=5)
    # Entry field for the toy name
    name_entry = tk.Entry(add_frame, width=20, bg='white', fg=TEXT_COLOR, relief=tk.FLAT)
    name_entry.grid(row=0, column=1)

    # Label for the toy type
    tk.Label(add_frame, text="Toy Type:", bg=BEIGE_BG, fg=TEXT_COLOR).grid(row=0, column=2, padx=5)
    # Entry field for the toy type
    type_entry = tk.Entry(add_frame, width=15, bg='white', fg=TEXT_COLOR, relief=tk.FLAT)
    type_entry.grid(row=0, column=3)

    def add_toy():
        """Adds a new toy to the list from the entry fields."""
        name = name_entry.get()
        toy_type = type_entry.get()
        
        # Only add if both fields have text
        if name and toy_type: 
            # Create a new tuple for the toy
            new_toy = (name, toy_type)
            # Add the new tuple to our list
            favorite_toys_list.append(new_toy)
            # Update the listbox on screen
            refresh_toys_listbox()
            # Clear the entry boxes
            name_entry.delete(0, tk.END)
            type_entry.delete(0, tk.END)

    # Button to add a new toy
    add_button = tk.Button(
        add_frame, 
        text="Add Toy", 
        command=add_toy,
        bg=GREEN_BTN,
        fg='white',
        relief=tk.FLAT,
        activebackground='#45a049',
        activeforeground='white'
    )
    add_button.grid(row=0, column=4, padx=10)

    def remove_toy():
        """Removes the selected toy from the list."""
        try:
            # Get the index of the item selected in the listbox
            selected_index = listbox.curselection()[0]
            # Remove that item from our data list
            favorite_toys_list.pop(selected_index)
            # Update the listbox on screen
            refresh_toys_listbox()
        except IndexError:
            # This stops a crash if the user clicks "Remove" with no toy selected
            pass

    # Button to remove the selected toy
    remove_button = tk.Button(
        frame, 
        text="Remove Selected Toy", 
        command=remove_toy,
        bg=RED_BTN,
        fg='white',
        relief=tk.FLAT,
        activebackground='#e53935',
        activeforeground='white'
    )
    remove_button.pack(pady=5)

    # Load the starting toys into the listbox
    refresh_toys_listbox()
    
    # Return the fully built frame to main.py
    return frame