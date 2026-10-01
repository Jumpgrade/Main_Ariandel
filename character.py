class Player_stats:
    def __init__(self, max_health, current_health, damage, speed):
        self.max_health = max_health
        self.current_health = current_health
        self.damage = damage
        self.speed = speed

    def health_boost(self, item):
        if self.current_health < self.max_health:
            heal = item
            self.current_health += heal
            if self.current_health <= self.max_health:
                print(self.current_health)
            else:
                self.current_health = self.max_health
                print(self.current_health)
        else:
            print("Full Health")

    def damage_taken(self, attack):
        self.current_health -= attack
        current_health = self.current_health
        if 0 < self.current_health < self.max_health:
            print(
                f"You have taken {attack} dmg, Your hp is {self.current_health}")
            return current_health
        if self.current_health == 0:
            print(f"You are dead")
            return current_health

    def speed_boost(self, item):
        self.speed += item
        print(f"You feel faster")
        return self.speed


class Enemy_Stats:
    def __init__(self, max_health, current_health, damage, speed):
        self.max_health = max_health
        self.current_health = current_health
        self.damage = damage
        self.speed = speed

    def health_boost(self, item):
        if self.current_health < self.max_health:
            heal = item
            self.current_health += heal
            if self.current_health <= self.max_health:
                print(self.current_health)
                current_health = self.current_health
                return current_health
            else:
                self.current_health = self.max_health
                print(self.current_health)
                return current_health
        else:
            print("Full Health")
            return current_health

    def damage_taken(self, attack):
        self.current_health -= attack
        current_health = self.current_health
        if 0 < self.current_health < self.max_health:
            print(
                f"You have taken {attack} dmg, Your hp is {self.current_health}")
            return current_health
        if self.current_health == 0:
            print(f"You are dead")
            return current_health
