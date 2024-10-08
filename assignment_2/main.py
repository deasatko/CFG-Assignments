import requests
from pprint import pprint as pp
import random
import tkinter as tk

# A bit of frontend to visualise if it's a win or loss.
def open_dialog(result):
    reg_font = ("Verdana", 18)
    msg = f"YOU {result}!"
    popup = tk.Tk()
    popup.minsize(200, 100)
    popup.wm_title(msg)
    popup.geometry("200x100")
    text = tk.Label(popup, text=msg, font=reg_font)
    text.pack(side="top")
    b1 = tk.Button(popup, text="CLOSE", command=popup.destroy)
    b1.config(height = 20, width = 20)
    b1.pack()
    popup.mainloop()
    
"""
Map method is a function that accepts one or more functions as parameters.
I used a lambda function here
We usually define functions with def. However these ones are anonymous functions and one of the use cases is to pass the function as a parameter but without defining the function with the name.
"""

def get_100_pokemon_name():
    endpoint_100pokemon = "https://pokeapi.co/api/v2/pokemon?limit=100" # set the limit of the pokemons to consider to 100.
    response = requests.get(endpoint_100pokemon)
    data = response.json()
    return list(map(lambda pokemon: pokemon["name"], data["results"]))  # functions with return and inbuilt functions

"""
The lambda function is comparable to the code below:

    def get_single_pokemon(pokemon):
        return pokemon["name"]
"""

# The below function defines the battle vs the pokemon of choice with linked msges which will be printed in the txt file created "Battles.txt"
def save_battle_results(choice,cpu_fighter):
    result = ""
    choice_stat = get_pokemon_stat(choice)
    cpu_stat = get_pokemon_stat(cpu_fighter)
    if choice_stat > cpu_stat:
        result = "WON"
    else:
        result = "LOST"
    open_dialog(result)
    slice_assignment(result)
    msg = f"Battle result: Your {choice} {result} the fight against {cpu_fighter} with a difference in stats of: {choice_stat - cpu_stat}"
    with open("assignment_2/report.txt", "a") as text_file:
        text_file.write(msg + "\n")

# Calling the API again here to get only the fields that we want (base_stat)
def get_pokemon_stat(choice):
    endpoint_single_pokemon = f"https://pokeapi.co/api/v2/pokemon/{choice.lower()}"
    response = requests.get(endpoint_single_pokemon)
    data = response.json()
    return sum(list(map(lambda stat: stat["base_stat"],data["stats"])))

# Added this to incude the string slicing requested by the assignment.
def slice_assignment(result):
    s = ("you", f"{result}")
    x = slice(1, 2)
    print(s[x])
    
# Calling the main function here to run the imputs below. When choice is null it returns an error msg as well.
if __name__ == "__main__":
    choice = ""
    while choice == "":
        choice = input("What is the name of the pokemon you wish to choose as your fighter?")
        if choice == "":
            print("Pokemon name cannot be empty, please enter again")
    cpu_fighter = get_100_pokemon_name()[random.randrange(0,99)] # using random function to pick a pokemon to fight against our chosen pokemon based on the base_stats only.
    save_battle_results(choice, cpu_fighter)
