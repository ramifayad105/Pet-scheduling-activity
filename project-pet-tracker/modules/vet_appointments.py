import tkinter as tk

def get_frame(root):
    """
    Returns a Tkinter Frame for the Vet Appointments module.
    """
    # --- Color Palette ---
    BEIGE_BG = '#F5F5DC'   #frames
    LISTBOX_BG = "#FAFAFA" #listbox
    GREEN_BTN = '#4CAF50'  #add button
    RED_BTN = '#F44336'    #remove button
    TEXT_COLOR = '#333333' #text
    
    # Configure the main frame for the vet module
    frame = tk.LabelFrame(
        root, 
        text="Upcoming Vet Appointments", 
        padx=10, 
        pady=10, 
        bg=BEIGE_BG, 
        font=("Arial", 12, "bold"),
        fg=TEXT_COLOR
    )
    
    # List to store the appointment tuples
    upcoming_appointments = [
        ('2025-11-15', 'Annual Checkup'),
        ('2025-12-10', 'Vaccine Booster'),
    ]
    
    # Listbox to display the appointments
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

    def refresh_listbox():
        """Clears and repopulates the listbox from the upcoming_appointments list."""
        listbox.delete(0, tk.END)
        for appt in upcoming_appointments:
            date, reason = appt
            listbox.insert(tk.END, f"Date: {date}  |  Reason: {reason}")

    # Frame to hold the "add" widgets
    add_frame = tk.Frame(frame, bg=BEIGE_BG)
    add_frame.pack(pady=5, fill=tk.X)

    # Label for the date entry
    tk.Label(add_frame, text="Date:", bg=BEIGE_BG, fg=TEXT_COLOR).grid(row=0, column=0, padx=5)
    # Entry field for the date
    date_entry = tk.Entry(add_frame, width=15, bg='white', fg=TEXT_COLOR, relief=tk.FLAT)
    date_entry.grid(row=0, column=1)

    # Label for the reason entry
    tk.Label(add_frame, text="Reason:", bg=BEIGE_BG, fg=TEXT_COLOR).grid(row=0, column=2, padx=5)
    # Entry field for the reason
    reason_entry = tk.Entry(add_frame, width=20, bg='white', fg=TEXT_COLOR, relief=tk.FLAT)
    reason_entry.grid(row=0, column=3)

    def add_appointment():
        """Adds a new appointment to the list from the entry fields."""
        date = date_entry.get()
        reason = reason_entry.get()
        
        if date and reason: 
            new_appt = (date, reason)
            upcoming_appointments.append(new_appt)
            refresh_listbox()
            date_entry.delete(0, tk.END)
            reason_entry.delete(0, tk.END)

    # Button to trigger adding an appointment
    add_button = tk.Button(
        add_frame, 
        text="Add Visit", 
        command=add_appointment,
        bg=GREEN_BTN,
        fg='white',
        relief=tk.FLAT,
        activebackground='#45a049', # Slightly darker green on click
        activeforeground='white'
    )
    add_button.grid(row=0, column=4, padx=10)

    def remove_appointment():
        """Removes the selected appointment from the list."""
        try:
            selected_index = listbox.curselection()[0]
            upcoming_appointments.pop(selected_index)
            refresh_listbox()
        except IndexError:
            pass

    # Button to trigger removing an appointment
    remove_button = tk.Button(
        frame, 
        text="Remove Selected Visit", 
        command=remove_appointment,
        bg=RED_BTN,
        fg='white',
        relief=tk.FLAT,
        activebackground='#e53935', # Slightly darker red on click
        activeforeground='white'
    )
    remove_button.pack(pady=5)

    # Load the initial data
    refresh_listbox()
    
    return frame