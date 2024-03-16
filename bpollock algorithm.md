# bpollock_combat
compsci120 turn based combat game
TBC Module for import, because actual game is completed.
  Contains at minimum object Character (class), and function Fight
    Defining the “Character” class. 
    Attributes: name, hitPoints, hitChance, maxDamage, armor
  Defining the “Fight” function.
    name, hitPoints, hitChance, maxDamage and armor. 
    Each turn taken, roll hitChance.
      If hitChance succeeds then randint between 1 and maxDamage. 
      Else 
      Tell the user what happens! (name) misses. 
      Print Hero hitPoints and Monster hitPoints 
      Subtract that value from armor
      Subtract that subsequent value from hitPoints of Monster. 
      Tell the user what happens! (name) hits (name2) for [damage] 
      (name2)’s armor can absorb (armor) points. 
      Print Hero hitPoints and Monster hitPoints. 
Create function that prints stats of monster and hero health
When either character has hitPoints =< 0, declare victor.
Damage can’t be negative. 
If the user presses enter, run the fight function.
Plug it all into 
import tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2

    monster = tbc.Character("Monster", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    tbc.fight(hero, monster)

if __name__ == "__main__":
    main()
