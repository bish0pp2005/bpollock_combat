import random
class Character():
        def ___init__(self, name: str, hitPoints: int, hitChance: int, maxDamage: int, armor: int):
            self.name = name
            self.hitPoints = hitPoints
            self.hitChance = hitChance
            self.maxDamage = maxDamage
            self.armor = armor
            self.hitPoints_max = hitPoints        
            def fight(self, target) -> None:
                self.hitChance = random.randint(1-100)
                if hitChance >= 50:
                    maxDamage = random.randint(1-self.maxDamage)
                    target.hitPoints -= (maxDamage-target.armor)
                    target.hitPoints = max(target.hitPoints, 0)
                    print(f"""The attack hit! 
                               Hero health: {Hero.hitPoints}
                               Monster health: {Monster.hitPoints}""")
                else: 
                         print(F"""The attack missed!
                               Hero health: {Hero.hitPoints}
                               Monster health: {Monster.hitPoints}""")
def printStats():
    print(f"""{Hero.name}, Health: {Hero.hitPoints}, Hit Chance: {Hero.hitChance}, Max Damage: {Hero.maxDamage}, Armor: {Hero.armor}
          {Monster.name}, Health: {Monster.hitPoints}, Hit Chance: {Monster.hitChance}, Max Damage: {Monster.maxDamage}, Armor: {Monster.armor}""")
                      
              
class Hero():
        def ___init___(self, name: str, hitPoints: int, hitChance: int, maxDamage: int, armor: int) -> None:
            super().__init__(name=name, hitPoints=hitPoints, hitChance=hitChance, maxDamage=maxDamage, armor=armor)
class Monster():
        def ___init___(self, name: str, hitPoints: int, hitChance: int, maxDamage: int, armor: int) -> None:
            super().__init__(name=name, hitPoints=hitPoints, hitChance=hitChance, maxDamage=maxDamage, armor=armor)
def main():
    if __name__ == "__main__":
        main()