import tkinter as tk

def get_frame(root):
    frame = tk.Frame(root, bg="#F5F5DC")
    
    #############################
    # Start Coding
    # ###########################    
    frame.pack(padx=10, pady=10)

    pet1 = ("Oso", "Golden Doodle", 1)
    pet2 = ("Lilly", "Golden Retriever", 2)
    pet3 = ("Jack", "Poodle", 4)

    pets = [pet1, pet2, pet3]


    tk.Label(frame, text=f"Pet Information", font=("Arial", 16, "bold"), bg="#F5F5DC").pack(pady=10)

    listbox = tk.Listbox(frame, width=40, height=8, font=("Arial", 11))
    listbox.pack(pady=10)

    def refresh_listbox():
        listbox.delete(0, tk.END)
        for i, (name, breed, age) in enumerate(pets, start=1):
            listbox.insert(tk.END, f"{i}. Name: {name} | Breed: {breed} | Age: {age} years")


    entry_frame = tk.Frame(frame, bg="#F5F5DC")
    entry_frame.pack(pady=10)
    
    tk.Label(entry_frame, text="Name:", bg="#F5F5DC").grid(row=0, column=0)
    name_entry = tk.Entry(entry_frame, width=15)
    name_entry.grid(row=0, column=1)

    tk.Label(entry_frame, text="Breed:", bg="#F5F5DC").grid(row=1, column=0)
    breed_entry = tk.Entry(entry_frame, width=15)
    breed_entry.grid(row=1, column=1)

    tk.Label(entry_frame, text="Age:", bg="#F5F5DC").grid(row=2, column=0)
    age_entry = tk.Entry(entry_frame, width=15)
    age_entry.grid(row=2, column=1)
    
    error_label = tk.Label(frame, text="", bg="#F5F5DC", fg="red")
    error_label.pack()

    def add_pet():
        name = name_entry.get()
        breed = breed_entry.get()
        age_text = age_entry.get()

        if name and breed and age_text.isdigit():
            new_pet = (name, breed, int(age_text))
            pets.append(new_pet)
            refresh_listbox()
            name_entry.delete(0, tk.END)
            breed_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            error_label.config(text=f"Added: {name} to the list! They are a {breed}, and are {age_text} years old! ")
        else:
           error_label.config(text="Please enter valid information! Age must be a number!", fg="red")


    def delete_pet():
        try:
            selected_index = listbox.curselection()[0]
            removed_pet = pets[selected_index]
            pets.pop(selected_index)
            refresh_listbox()

            pet_name = removed_pet[0]
            error_label.config(text=f"Removed: {pet_name} from the list successfully!", fg="green")
        except IndexError:
            error_label.config(text= "Please select which pet you'd like to remove!", fg="red")

    tk.Button(frame, text="Add New Pet", command=add_pet, bg="#4CAF50").pack(pady=5)
    tk.Button(frame, text="Delete Selected Pet", command=delete_pet, bg="#F44336", fg="white").pack(pady=5)
    refresh_listbox()
    frame.pets = pets
    #############################
    # End Coding
    # ########################### 
    return frame