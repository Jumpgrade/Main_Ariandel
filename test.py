from character import Player_stats
from character import Enemy_Stats
import random


weapon_max = {
    "weapon_1": 20,
    "weapon_2": 10,
    "weapon_3": 5,
}

weapon_min = {
    "weapon_1": 10,
    "weapon_2": 5,
    "weapon_3": 1,
}

healing_values = {
    "banana": 5,
    "apple": 10
}


weapons = list(weapon_max)
heal_item = list(healing_values)
inventory = ["banana", "apple", "weapon_2", "weapon_1"]
weapon = [item for item in inventory if item in weapons]
heal = [item for item in inventory if item in healing_values]
current_hp = 70
weapon_equipped = None
dmg_roll = 1
speed = 10
player_status = "combat_mode"
player = Player_stats(100, current_hp, dmg_roll, speed)
enemy = Enemy_Stats(100, 95, dmg_roll, 5)

stat_buffs = {
    "coke": "player.speed * 2",
    "milk": "player.speed / 2",
}
print(stat_buffs.items())
buff_item = list(stat_buffs)

speed_buff = [item for item, value in stat_buffs.items()
              if "player.speed" in value]
print(speed_buff)
answer = eval(stat_buffs["coke"])
print(answer)


def equipment(player_status):
    while True:
        if player_status == "combat_mode":
            print(inventory)
            choice = input("Choose an item: ")
            if choice.lower() in weapon:
                print(f"Player equipped {choice}")
                return choice
            else:
                print("That's not a weapon")


default_weapon = equipment(player_status)


def inventory_choice(player_status):
    while True:
        dmg_roll = random.randint(
            weapon_min[default_weapon], weapon_max[default_weapon])
        if player_status == "combat_mode":
            print(inventory)
            choice = input("Choose an item: ")
            if choice.lower() == default_weapon:
                print(f"Player already equipped {choice}")
                return choice, dmg_roll
            elif choice.lower() in weapon and choice.lower() != default_weapon:
                dmg_roll = random.randint(
                    weapon_min[choice], weapon_max[choice])
                print(f"Player equipped {choice}")
                return choice, dmg_roll
            elif choice.lower() in heal:

                print(f"Player equipped {choice}")
                return choice, dmg_roll
        else:
            print("You don't own this weapon")


def battle_system(dmg_roll, item_equipped):
    while True:
        battle_input = input("Attack, Item, Run, Defend: ")
        if battle_input.lower() == "attack":
            attack = dmg_roll
            current_hp = player.damage_taken(attack)
            return current_hp, "combat_mode"
        elif battle_input.lower() == "item":
            item = item_equipped
            if item in heal_item:
                current_hp = player.health_boost(healing_values[item])
                return current_hp, "combat_mode"
        elif battle_input.lower() == "run":
            if player.speed >= enemy.speed:
                print("You Successfully Ran Away.")
                return player.current_hp, "idle_mode"
            elif player.speed < enemy.speed:
                print("You failed to run away.")
        else:
            print("That's not an action")


item_equipped, dmg_roll = inventory_choice(player_status)

battle_system(dmg_roll, item_equipped)
