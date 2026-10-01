print("Welcome to the Ariandel Text World, Please type your username")
command = ""
while True:
    command = input(">")
    character = len(command)

    if character >= 5:
        print(f"Welcome {command}")
        username = command
        break
    else:
        print("Please type a username")

print("Type Next to move forward")


def story_progress(story_text):
    forward = "Next"
    while True:
        command = input(">")

        if command.lower() == forward.lower():
            print(story_text)
            break

        else:
            print("Please type Next")


dialogue_interaction1 = False
dialogue_interaction2 = False
dialogue_interaction3 = False


current_location = "World"
current_status = "idle_mode"

story_progress("""Your goal as an adventurer wandering 
the world of Ariandel is to defeat 
monsters and fight the demon king 
to free the world of Ariandel"""
               )
story_progress("You enter the Tavern of Ariandel")

story_progress(
    "You meet Felix the innkeeper of the tavern (type talk to interact with people)")

current_location = "Tavern"


def player_choice(current_location, current_status,):
    while True:
        choice = input(">")

        if choice.lower() == "north" and current_location == "Tavern" and current_status == "idle_mode":
            print("You went inside the room")
            return "Tavern Room", "idle_mode", "move"

        elif choice.lower() == "east" and current_location == "Tavern" and current_status == "idle_mode":
            print("You went inside the bar")
            print("Bob the bartender is here")
            return "Tavern Bar", "idle_mode", "move"

        elif choice.lower() == "west" and current_location == "Tavern" and current_status == "idle_mode":
            print("You went inside the blacksmith")
            print("Dray the Blacksmith is here")
            return "Blacksmith", "idle_mode", "move"

        elif choice.lower() == "south" and current_location == "Tavern" and current_status == "idle_mode":
            print("You went outside")
            print("Eca the swordswoman is here")
            return "Woods", "idle_mode", "move"

        elif choice.lower() == "south" and current_location == "Tavern" and current_status == "idle_mode" and dialogue_interaction3 == False:
            print("Eca the Swordswoman is here")
            return "Woods", "idle_mode", "move"

        elif choice.lower() == "south" and current_location == "Tavern Room" and current_status == "idle_mode":
            print("You went back to the Tavern")
            print("Felix the innkeeper is here")
            return "Tavern", "idle_mode", "move"

        elif choice.lower() == "talk" and current_location == "Tavern" and current_status == "idle_mode" and dialogue_interaction1 == False:
            print("You talk to Felix the innkeeper of the Tavern")
            return "Tavern", "idle_mode", "talk"

        elif choice.lower() == "talk" and current_location == "Tavern" and current_status == "idle_mode" and dialogue_interaction1:
            print("Felix: Feel Free to look around the cabin.")
            return "Tavern", "idle_mode", "move"

        elif choice.lower() == "talk" and current_location == "Tavern Bar" and current_status == "idle_mode":
            print("You talk to Bob the bartender")
            return "Tavern Bar", "idle_mode", "move"

        elif choice.lower() == "talk" and current_location == "Woods" and current_status == "idle_mode" and dialogue_interaction3 == False:
            print("You talk to Eca the Swordswoman")
            return "Woods", "idle_mode", "talk"

        elif choice.lower() == "talk" and current_location == "Woods" and current_status == "idle_mode" and dialogue_interaction3:
            print("Eca: What do you want? Don't waste my time.")
            return "Woods", "idle_mode", "move"

        elif choice.lower() == "talk" and current_location == "Blacksmith" and current_status == "idle_mode" and dialogue_interaction3:
            print("You talked to Dray the Blacksmith")
            return "Blacksmith", "idle_mode", "move"

        elif choice.lower() == "west" and current_location == "Tavern Bar" and current_status == "idle_mode":
            print("You went back to the Tavern")
            print("Felix the innkeeper is here")
            return "Tavern", "idle_mode", "move"

        elif choice.lower() == "east" and current_location == "Blacksmith" and current_status == "idle_mode":
            print("You went back to the Tavern")
            return "Tavern", "idle_mode", "move"

        else:
            print("You can't do that")


def npc_chat(npc_name, npc_text1, wrong_response, npc_text2, location1, current_location, current_status, dialogue_interaction, expected_answer):
    print(f"{npc_name}: {npc_text1}")
    while True:
        chat1 = input(">")
        if chat1.lower() in expected_answer and current_location == location1 and current_status == "idle_mode" and dialogue_interaction == False:
            print(f"{npc_name}: {npc_text2}")
            return True

        else:
            print(f"{npc_name}: {wrong_response}")


while True:
    current_location, current_status, action = player_choice(
        current_location, current_status,)
    bartender_choices = "beer", "wine"

    if current_location == "Tavern" and current_status == "idle_mode" and dialogue_interaction1 == False and action == "talk":
        dialogue_interaction1 = npc_chat("Felix",
                                         "Hey, you're new here. What's your name?",
                                         "I don't believe you",
                                         f"Oh hey {username} nice to meet you",
                                         "Tavern",
                                         current_location,
                                         current_status,
                                         dialogue_interaction1,
                                         (username.lower(),))

    elif current_location == "Tavern Bar" and current_status == "idle_mode":

        dialogue_interaction2 = npc_chat("Bob",
                                         "Hey what do you want? Beer or Wine",
                                         "We don't serve that here",
                                         "Don't drink too much",
                                         "Tavern Bar",
                                         current_location,
                                         current_status,
                                         False,
                                         bartender_choices)

    elif current_location == "Woods" and current_status == "idle_mode" and dialogue_interaction3 == False and action == "talk":
        dialogue_interaction3 = npc_chat("Eca",
                                         "Seems like the army has found new fresh meat",
                                         "What do you want?",
                                         "Be careful out here, legion of the demon king lurks around these parts.",
                                         "Woods",
                                         current_location,
                                         current_status,
                                         dialogue_interaction3,
                                         "talk")

    else:
        print("\nType a direction to move")
