import tkinter as tk
from tkinter import simpledialog

def get_frame(root, pets):
    frame = tk.Frame(root, bg="#F5F5DC")  # match Cesar's background color

    # Food options for dropdown
    food_options = ["Hard Food", "Soft Food", "Fresh Food"]

    # Initialize feeding schedules for each pet
    feeding_schedules = {pet[0]: {  # pet[0] is the pet's name
        "Breakfast": {"time": "8:00 AM", "food": "Hard Food"},
        "Lunch": {"time": "12:00 PM", "food": "Soft Food"},
        "Dinner": {"time": "6:00 PM", "food": "Fresh Food"}
    } for pet in pets}

    # Current pet selection
    selected_pet_var = tk.StringVar(value=pets[0][0] if pets else "")

    tk.Label(frame, text="Select Pet:", font=("Arial", 12, "bold"), bg="#F5F5DC").pack(pady=5)
    pet_menu = tk.OptionMenu(frame, selected_pet_var, *[pet[0] for pet in pets])
    pet_menu.config(bg="#F5F5DC", relief="raised", width=15)
    pet_menu.pack(pady=5)

    # Container for meal widgets
    meals_frame = tk.Frame(frame, bg="#F5F5DC")
    meals_frame.pack(pady=5)
    meal_widgets = {}

    def refresh_meals():
        # Clear current widgets
        for widget in meals_frame.winfo_children():
            widget.destroy()
        meal_widgets.clear()

        current_pet = selected_pet_var.get()
        schedule = feeding_schedules.get(current_pet, {})

        for meal_name, info in schedule.items():
            row = tk.Frame(meals_frame, bg="#F5F5DC")
            row.pack(pady=2, fill="x")

            tk.Label(row, text=meal_name, width=10, bg="#F5F5DC").pack(side="left")

            time_var = tk.StringVar(value=info["time"])
            time_entry = tk.Entry(row, textvariable=time_var, width=10, bg="white")
            time_entry.pack(side="left", padx=5)

            food_var = tk.StringVar(value=info["food"])
            food_menu = tk.OptionMenu(row, food_var, *food_options)
            food_menu.config(bg="white", relief="raised")
            food_menu.pack(side="left", padx=5)

            def update_meal(m=meal_name, t_var=time_var, f_var=food_var):
                feeding_schedules[selected_pet_var.get()][m] = {
                    "time": t_var.get(),
                    "food": f_var.get()
                }

            update_btn = tk.Button(row, text="Update", command=update_meal, bg="#F44336")
            update_btn.pack(side="left", padx=5)

            meal_widgets[meal_name] = {"time_var": time_var, "food_var": food_var}

    # Refresh meals when pet selection changes
    def on_pet_change(*args):
        refresh_meals()

    selected_pet_var.trace_add("write", on_pet_change)

    refresh_meals()

    # Add new meal button for the selected pet
    def add_meal():
        current_pet = selected_pet_var.get()
        new_meal = simpledialog.askstring("Add Meal", "Enter new meal name:")
        if not new_meal:
            return
        feeding_schedules[current_pet][new_meal] = {"time": "00:00 AM", "food": food_options[0]}
        refresh_meals()

    add_button = tk.Button(frame, text="Add Meal", command=add_meal, bg="#4CAF50")
    add_button.pack(pady=5)

    # Function to update pet menu if pets list changes
    def update_pet_menu():
        menu = pet_menu["menu"]
        menu.delete(0, "end")
        for pet in pets:
            menu.add_command(label=pet[0], command=lambda value=pet[0]: selected_pet_var.set(value))

    frame.update_pet_menu = update_pet_menu
    frame.feeding_schedules = feeding_schedules
    frame.selected_pet_var = selected_pet_var

    return frame