import random
import time
import os
from colorama import *
def clean():
    clean = os.system("cls")
clean()
print(f"{Fore.YELLOW}Добро пожаловать в мир Колизея, здесь ты сталкнёшся с сильнейшими войнами! \nИ если одолеешь их, сможешь взабраться на вершину!")
time.sleep(10)
clean()
name_person = input("Поведай же своё имя храбрый воин! \n-")
print(f"\nУдачи тебе, {name_person}!")
time.sleep(3)
clean()
          

class Person:
    role = { "1": "Воин",
            "2": "Лучник",
            "3": "Маг",
            "4": "Ассасин",
            "god": "Бог",
    }

    classes = {

            'Воин': {
                'здоровье': 100,
                'атака': 50,
                'защита': 15,
                'навыки': {
                    'щит': 15
                }

            },

            'Лучник': {
                'здоровье': 100,
                'атака': 45,
                'защита': 10,
                'навыки': {
                    'отступление': 15
                }

            },

            'Маг': {
                'здоровье': 100,
                'атака': 40,
                'защита': 10,
                'навыки': {
                    'магический щит': 20
                }

            },

            'Ассасин': {
                'здоровье': 100,
                'атака': 40,
                'защита': 5,
                'навыки': {
                    'теневой шаг': 25
                }

            },

            'Бог': {
                'здоровье': 1000000,
                'атака': 10000000,
                'защита': 1000,
                'навыки': {
                    'благословление': 100
                }

            }

        }


    def __init__(self, name, is_enemy) -> None:
        self.is_enemy = is_enemy
        self.name = name
        self.person_class = self.get_person_class()
        self.person_class_dict = self.classes[self.person_class]
        self.health = self.person_class_dict["здоровье"]
        self.attack = self.person_class_dict["атака"]
        self.defens = self.person_class_dict["защита"]
        self.skills = self.person_class_dict["навыки"]
        self.money = 1000.0
        self.is_alive = True
        print(f"Его зовут {self.name}, он {self.person_class}")
        print(f"У него такие характеристики: ")
        print(f"{Fore.GREEN}здоровье: {self.health}, \n{Fore.RED}атака: {self.attack}, \n{Fore.BLUE}защита: {self.defens}, \n{Fore.MAGENTA}навыки: {self.skills}")
        time.sleep(15)
        clean()
         

    def get_person_class(self):
        if self.is_enemy:
            random_choise = random.choice(list(self.role.keys()))
            return self.role[random_choise]
        else:
                try:     
                        choise = input(f"{Fore.YELLOW}Выберите класс персонажа 1: Воин, 2: Лучник, 3: Маг, 4: Ассасин,  \n")
                        return self.role[choise]
                except:
                        print(f"{Fore.RED}Вы ввели недопустимый символ! Вы можете ввести только предложеные числа. \n")
        
    def attack_enemy(self, enemy1, enemy2):
        time.sleep(2)
        print(f"{Fore.RED}{enemy1.name} атакует {enemy2.name}")
        time.sleep(2)
        defend = enemy2.defens
        if random.randint(1, 100) > 30:
            defend = enemy2.defens + list(enemy2.skills.items())[0][1]
            time.sleep(2)
            print(f"Сработал навык {enemy2.skills}")
        if defend >= enemy1.attack:
            enemy2.health -= 1
            time.sleep(2)
            print(f"{Fore.YELLOW}{enemy2.name} получил {Fore.RED}-1 урона \n{Fore.YELLOW}У {enemy2.name} осталось {enemy2.health} очков здоровья")
        else:
            enemy2.health -= enemy1.attack - defend
            time.sleep(2)
            print(f"{enemy2.name} получил {Fore.RED}{enemy1.attack - defend} урона \n{Fore.YELLOW}У {enemy2.name} осталось {enemy2.health} очков здоровья")

    def fight_for_the_win(self, attacker, defender):
        while attacker.is_alive and defender.is_alive:
            if attacker.health > 0:
                self.attack_enemy(attacker, defender)
            else:
                attacker.is_alive = False
                print(f"{Style.BRIGHT}{attacker.name} потерпел поражение")
                print(Style.RESET_ALL)
                return False
            if defender.health > 0:
                self.attack_enemy(defender, attacker)
            else:
                defender.is_alive = False
                print(f"{Style.BRIGHT}{defender.name} потерпел поражение")
                print(Style.RESET_ALL)
                return True

def name_generate():
         first_name = ["Великий", "Храбрый", "Могучий", "Храмой", "Одноглазый"]
         second_name = ["Орк", "Русский", "Гном", "Друид", "Утюг"]
         random_name = random.choice(first_name) + random.choice(second_name)
         return random_name


enemy = Person(name_generate(), is_enemy=True)
player = Person(name_person, is_enemy=False)
player.fight_for_the_win(player, enemy)