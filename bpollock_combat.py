import tbc
from tbc import printStats
def main():
    Hero = tbc.Character()
    Hero.name = "Hero"
    Hero.hitPoints = 10
    Hero.hitChance = 50
    Hero.maxDamage = 5
    Hero.armor = 2

    Monster = tbc.Character()
    Monster.name = "Monster"
    Monster.hitPoints = 20
    Monster.hitChance = 30
    Monster.maxDamage = 5
    Monster.armor = 0

    tbc.printStats()
    tbc.fight(Hero, Monster)

if __name__ == "__main__":
    main()