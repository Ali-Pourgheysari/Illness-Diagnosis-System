# Illness Diagnosis System
  This Python code provides a simple Illness Diagnosis System with a user-friendly GUI based on the `pyswip` library for interfacing with Prolog and `tkinter` for creating the graphical user interface.

## Intorduction
The Illness Diagnosis System is designed to assist users in identifying potential illnesses based on the symptoms they provide. The system utilizes a knowledge base containing information about various illnesses and their associated symptoms, which is stored using Prolog's fact assertion mechanism. Through a simple GUI, users can enter their symptoms, and the system will provide potential diagnoses based on the symptoms entered.

## How it works
1. Step 1: Define the Knowledge Base: The code reads a knowledge base file named "illnesses.txt" that contains information about various illnesses and their associated symptoms. The knowledge base is stored using Prolog's fact assertion mechanism.

2. Step 2: Diagnose Illnesses: The diagnose function takes input symptoms and illnesses and returns potential diagnoses based on the number of common symptoms between the input and the illnesses in the knowledge base.

3. Step 3: Ask Yes/No Questions: The ask_question function interacts with the user through a GUI to ask yes/no questions about the remaining symptoms. It uses Prolog to find different symptoms associated with the potential illnesses and narrows down the diagnosis based on user responses.

4. The GUI displays an entry field where users can input symptoms one by one and click the "Next" button to add them. Once the user is done entering symptoms, they can click the "Finish" button.

5. If the system can identify a single illness based on the entered symptoms, it displays the diagnosed illness. Otherwise, it asks specific questions to narrow down the diagnosis and displays the final result.

6. The final diagnosed illness is saved in the file "diagnosed_illness.txt."

## Requirements
To run the Illness Diagnosis System, you need the following dependencies:

* pyswip: Python library for interfacing with Prolog.
* tkinter: Python's standard GUI library.

## Installation
1. Install pyswip and `tkinter` dependencies. You can use `pip` to install `pyswip`:
```bash
pip install pyswip
```
2. Clone the repository:
```bash
git clone https://github.com/Ali-Pourgheysari/Illness-Diagnosis-System.git
```
3. Prepare the knowledge base file "illnesses.txt" containing information about illnesses and their symptoms. Each line in the file should be in the format: <illness_name> are <symptom1>, <symptom2>, ....

## Usage
1. Run the code, and a GUI window will appear.

2. Enter symptoms in the provided entry field and click the "Next" button after each symptom.

3. When done entering symptoms, click the "Finish" button.

4. The GUI will display the diagnosed illness or ask additional questions to narrow down the diagnosis.

5. The final diagnosed illness will be saved in the file "diagnosed_illness.txt."

Note: The code relies on a complete and accurate knowledge base in "illnesses.txt" to provide accurate diagnoses. It may require additional development to enhance the diagnostic accuracy and user experience.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Good luck! :+1: :smiley: :sparkles: :tada: :rocket: :metal: :octocat: