from pyswip import Prolog
import tkinter as tk

################################################################################################
# STEP1: Define the knowledge base of illnesses and their symptoms

prolog = Prolog()

# TODO: read illnesses descriptions from illnesses.txt and add them to the prolog knowledge base
with open('illnesses.txt', 'r') as file:
    for line in file:
        illness = line.split(' ')[0].lower()
        start_index = line.index("are") + len("are") + 1
        symptoms = line[start_index:].split(", ")
        symptoms[-1] = symptoms[-1][:-2].split(' ')[1]
        for symptom in symptoms:
            prolog.assertz(f'symptom({illness}, {symptom})')
        prolog.assertz(f'illness({illness})')

################################################################################################
# STEP2: Define a function to diagnose illnesses based on symptoms

def diagnose(symptoms):
    #TODO: Define this function to diagnose illnesses based on symptoms

    diagnoses = []
    query = list(prolog.query(f"illness(X), findall(S, symptom(X, S), L), intersection(L, {symptoms}, R), length(R, N)"))
    max_value = max([result['N'] for result in query])
    for result in query:
        if result['N'] == max_value:
            diagnoses.append(result['X'])

    return diagnoses

################################################################################################
# STEP3: Define a function to ask yes/no questions about the remaining symptoms to decide on the illness

def ask_question(illnesses, common_symptoms):
    # Enabling YES and NO Button
    yes_button.config(state=tk.NORMAL)
    no_button.config(state=tk.NORMAL)
    
    # TODO: Define a function to diagnose illnesses based on user answers to yes/no questions
    remaining_symptoms = []
    for illness in illnesses:
        query = list(prolog.query(f"symptom({illness}, X), not(member(X, {common_symptoms})), not(member(X, {remaining_symptoms}))"))
        remaining_symptoms += [symptom['X'] for symptom in query]

    #example of working with buttons
    while remaining_symptoms and len(illnesses) > 1:
        question_symptom = remaining_symptoms.pop(0)
        question_label.config(text=f"Do you have {question_symptom}?")
        yes_button.config(command=lambda: on_question_answer(question_symptom, True, illnesses))
        no_button.config(command=lambda: on_question_answer(question_symptom, False, illnesses))

    with open("diagnosed_illness.txt", "w") as f:
        f.write(", ".join(illnesses))
    root.destroy()

def on_question_answer(symptom, answer, illnesses: list):
    # TODO: Define a function to handle the answer to yes/no question and
    #       to diagnose illnesses based on user answers to yes/no questions
    if answer:
        for illness in illnesses:
            symptoms = [symptom['Y'] for symptom in prolog.query(f"symptom({illness}, Y)")]
            if symptom not in symptoms:
                illnesses.remove(illness)
    else:
        for illness in illnesses:
            symptoms = [symptom['Y'] for symptom in prolog.query(f"symptom({illness}, Y)")]
            if symptom in symptoms:
                illnesses.remove(illness)
        

################################################################################################
# The code is for GUI creation and functionality
# You don't need to directly change it

#"Next" button click event
def on_next_click():
    symptom = symptom_entry.get()
    if symptom:
        symptoms.append(symptom)
        symptom_entry.delete(0, tk.END)
    
#"Finish" button click event
def on_finish_click():
    illnesses = diagnose(symptoms)
    if len(illnesses) == 1:
        with open("diagnosed_illness.txt", "w") as f:
            f.write(illnesses[0])
        root.destroy()
    else:
        ask_question(illnesses, symptoms)

# Create the GUI
root = tk.Tk()
root.title("Illness Diagnosis System")

# Create the symptom entry field
symptom_label = tk.Label(root, text="Enter a symptom:")
symptom_label.grid(row=0, column=0, padx=5, pady=5)
symptom_entry = tk.Entry(root)
symptom_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the "Next" button
next_button = tk.Button(root, text="Next", command=on_next_click)
next_button.grid(row=1, column=0, padx=5, pady=5)

# Create the "Finish" button
finish_button = tk.Button(root, text="Finish", command=on_finish_click)
finish_button.grid(row=1, column=1, padx=5, pady=5)

# Create the question label
question_label = tk.Label(root, text="")
question_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create the "Yes" button
yes_button = tk.Button(root, text="Yes")
yes_button.grid(row=3, column=0, padx=5, pady=5)

# Create the "No" button
no_button = tk.Button(root, text="No")
no_button.grid(row=3, column=1, padx=5, pady=5)

# Buttons are disabled at first
yes_button.config(state=tk.DISABLED)
no_button.config(state=tk.DISABLED)

# Initialize the symptoms list
symptoms = []

# Start the GUI
root.mainloop()