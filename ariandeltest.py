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


current_location = "World"
current_status = "idle_mode"
npc_state = 1

story_progress("""Your goal as an adventurer wandering 
the world of Ariandel is to defeat 
monsters and fight the demon king 
to free the world of Ariandel"""
               )
story_progress("You enter the Tavern of Ariandel")

story_progress(
    "You meet Felix the innkeeper of the tavern (type talk to interact with people)")

current_location = "Tavern"


player_movement = {
    "Tavern": {
        "north": "Tavern Room",
        "west": "Tavern Bar",
        "east": "Blacksmith",
        "south": "Woods",
    },

    "Tavern Room": {
        "south": "Tavern"
    },

    "Blacksmith": {
        "west": "Tavern"
    },

    "Tavern Bar": {
        "east": "Tavern"
    },

    "Woods": {
        "north": "Tavern",
        "south": "Deeper Woods"
    },
}

player_action = {
    "Tavern": {
        "talk": {1: "You talk to Felix the innkeeper of the Tavern",
                 2: "Felix: Feel Free to look around the cabin.",
                 5: "amogus"
                 },
    },

    "Blacksmith": {
        "talk": {1: "You talk to Dray the Blacksmith"}
    },

    "Tavern Bar": {
        "talk": {1: "You talk to Bob the Bartender"}
    },

    "Woods": {
        "talk": {2: "Eca: What do you want? Don't waste my time.",
                 1: "You talk to Eca the Swordsmaster",
                 5: "Banana",
                 6: "Bananas"}
    },
}

dialogue_interaction = {
    "Tavern": 1,
    "Blacksmith": 1,
    "Tavern Bar": 1,
    "Woods": 1,

}


def player_choice(current_location, current_status):
    movement = player_movement.get(current_location, {})
    action = player_action.get(current_location, {})
    npc_state = dialogue_interaction.get(current_location, {})
    while True:
        choice = input(">")

        if choice.lower() in movement and current_status == "idle_mode":
            destination = movement[choice.lower()]
            print(f"You went to the {destination}")
            npc_state = dialogue_interaction.get(destination, {})
            return destination, "idle_mode", npc_state, "move"

        elif choice.lower() in action and current_status == "idle_mode":
            try:
                npc_dialogue = action[choice.lower()]
                print(npc_dialogue[npc_state])
                npc_check = max(npc_dialogue.keys())
                if npc_state in npc_dialogue and npc_state < npc_check:
                    npc_state += 1
                    return current_location, "idle_mode", npc_state, "talk"
                else:
                    return current_location, "idle_mode", npc_state, "talk"
            except KeyError:
                safety_net = [
                    option for option in npc_dialogue if option < npc_state]
                if safety_net:
                    safe_number = max(safety_net)
                    safe = npc_dialogue[safe_number]
                    print(safe)

                    return current_location, "idle_mode", npc_state, "talk"
        else:
            print("You can't do that")


def npc_chat(npc_name, npc_text1, wrong_response, npc_text2, location1, current_location, current_status, npc_states, expected_answer):
    print(f"{npc_name}: {npc_text1}")
    npc_state = dialogue_interaction.get(current_location, {})
    while True:
        chat1 = input(">")
        if chat1.lower() in expected_answer and current_location == location1 and current_status == "idle_mode" and npc_states == npc_state:
            print(f"{npc_name}: {npc_text2}")
            npc_state += 0
            return npc_state

        else:
            print(f"{npc_name}: {wrong_response}")


while True:

    current_location, current_status, npc_state, action = player_choice(
        current_location, current_status,)
    bartender_choices = "beer", "wine"
    check = dialogue_interaction[current_location]
    print(check)
    print(npc_state)
    dialogue_interaction[current_location] = npc_state
    print(dialogue_interaction)
    if current_location == "Tavern" and current_status == "idle_mode" and action == "talk" and check == 1:
        npc_state = npc_chat("Felix",
                             "Hey, you're new here. What's your name?",
                             "I don't believe you",
                             f"Oh hey {username} nice to meet you",
                             "Tavern",
                             current_location,
                             current_status,
                             npc_state,
                             (username.lower(),))

    elif current_location == "Tavern Bar" and current_status == "idle_mode" and action == "talk":

        npc_state = npc_chat("Bob",
                             "Hey what do you want? Beer or Wine",
                             "We don't serve that here",
                             "Don't drink too much",
                             "Tavern Bar",
                             current_location,
                             current_status,
                             npc_state,
                             bartender_choices)

    elif current_location == "Woods" and current_status == "idle_mode" and action == "talk" and check == 1:
        npc_state = npc_chat("Eca",
                             "Seems like the army has found new fresh meat",
                             "What do you want?",
                             "Be careful out here, legion of the demon king lurks around these parts.",
                             "Woods",
                             current_location,
                             current_status,
                             npc_state,
                             "talk")


    else:
        print("\nType a direction to move")
