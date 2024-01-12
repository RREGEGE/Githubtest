# %%
class Car:
    def __init__(self, make, model, year, color):
        self.make = make      # 제조사
        self.model = model    # 모델
        self.year = year      # 제조년도
        self.color = color    # 색상
        
        
tesla = Car('tesla','r99','2000','red')
print(vars(tesla)) # attribute를 알아내기

# %%
class FB_Player: # initialize
  def __init__(self,myname,age,backnumber,position,club):
    self.name = myname
    self.age = age
    self.backnumber = backnumber
    self.position = position
    self.club = club
    
  def Info_Pos(self): 
    print(f"저는 {self.position} 포지션입니다.")
    
    

messi = FB_Player("messi","35","10","MF","마이애미")

ronaldo = FB_Player("ronaldo","40","11","DF","한국")


print(hex(id(messi.Info_Pos)))
print("===========================")

print(hex(id(ronaldo.Info_Pos)))
print("===========================")


print(hex(id(messi.Info_Pos())))
print("===========================")

print(hex(id(ronaldo.Info_Pos())))
print("===========================")

print(hex(id(messi.age)))
print(hex(id(ronaldo.age)))

# %%
class Item:
    def __init__(self, Iprice=None, Itype=None):
        self.__Iprice = Iprice
        self.Itype = Itype

    def getIprice(self):
        return self.__Iprice  # 값을 반환하는 것이 더 적절할 것입니다.

class Weapon(Item):
    def __init__(self, Iprice=None, Itype=None, attackDmg=0):
        super().__init__(Iprice, Itype)  # Item 클래스의 생성자 호출
        self.__attackDmg = attackDmg

    def setattackDmg(self, attackDmg):
        self.__attackDmg= attackDmg
    def getattackDmg(self):
        print(self.__attackDmg)

myBow = Weapon(100, 'Bow',100)  # Item 클래스의 생성자와 Weapon 클래스의 생성자에 필요한 인자를 제공
myBow.__dropRate = 100

print(myBow.__attackDmg)

# %%
# 게임만들기 클라이언트 player 직업 몬스터 아이템

def start_():
  id = ""
  password = ""
  start = int(input("1.로그인 2.회원가입 "))
  def login():
    id_input = input("id를 입력하세요")
    password_input = input("password를 입력하세요")
    if id_input == id and password_input == password:
      print("로그인 완료")
    else:
      print("다시 입력하세요")
      return login()
  
  if start == 1:
    return login()
 
  elif start == 2:
    id = input("id를 생성하세요")
    password = input("password를 생성하세요")
    return start_()
  
  else:
    print("잘못 입력하셨습니다")
    return start_()
  
start_()

class Creature:
  def __init__(self,HP,attack_damage, defense, name):
    self.HP = HP
    self.attack_damage = attack_damage
    self.defense = defense
    self.name = name
    
  def attacked(self,enemy : 'Creature'):
    print(f"{enemy.name}에게 공격 받았습니다")
    self.HP = self.HP - enemy.attack_damage + self.defense
    if self.HP > 0:
      print(f"현재 HP:{self.HP}")
      return self
    else:
      print(f"{self.name}님이 전사하셨습니다")
# 플레이어 
class player(Creature):
  def __init__(self, name = None, job = None, HP =None, attack_damage = None, defense = None):
    super().__init__(HP,attack_damage, defense, name)
    self.exp = 90
    self.exp_max = 100
    self.level = 1
    self.job = job
    
  
  def attack(self, enemy):
    print(f"{enemy.name}을 공격하고 있습니다")
    enemy.HP -= self.attack_damage
    print(f"몬스터의 체력이 {enemy.HP}남았습니다.")
    if enemy.HP <= 0:
      self.exp += enemy.give_exp
      print(f"경험치 {enemy.give_exp}를 얻었습니다")
      print(f"현재 경험치:{self.exp}")
      if self.exp >= 100:
        self.levelup(enemy)
    
      
      
      
  def levelup(self, enemy):
     self.level += 1
     self.exp = self.exp - self.exp_max
     self.exp_max += self.level*10
     print(f"{self.level}레벨이 되었습니다")
  
 # 직업 
class worrier(player):
  def __init__(self, name):
    super().__init__()
    self.type_attack = "ad"
    self.HP = 1000
    self.attack_damage = 100
    self.defense = 20
    self.job = "worrier"
    self.name = name
  
  def getitem(self, item):
    if item.Itype == 'Sword' :
      self.attack_damage += item.item_attack_damage
    else:
      print("착용할 수 없습니다")
    
class magician(player):
  def __init__(self,name):
    super().__init__()
    self.type_attack = "ap"
    self.HP = 600
    self.attack_damage = 130
    self.defense = 5
    self.job = "magician"
    self.name = name
  
  def getitem(self, item):
    if item.Itype == 'Wand' :
      self.attack_damage += item.item_attack_damage
    else:
      print("착용할 수 없습니다")  

class archer(player):
  def __init__(self, name):
    super().__init__()
    self.type_attack = "ad"
    self.HP = 700
    self.attack_damage = 120
    self.defense = 10
    self.job = "archer"
    self.name = name
    
  def getitem(self, item):
    print(f"{item.Itype}을 획득하였습니다.")
    if item.Itype == 'Bow' :
      self.attack_damage += item.item_attack_damage
    else:
      print("착용할 수 없습니다")
# 몬스터
class Monster(Creature):
  pass

class zombie(Monster):
   def __init__(self,name):
     self.name = name
     self.HP = 600
     self.attack_damage = 50
     self.class_ = "zombie"
     self.give_exp = 15
     
class animal(Monster):
   def __init__(self,name):
     self.name = name
     self.HP = 150
     self.attack_damage = 40
     self.class_ = "animal"
     self.give_exp = 10

# 아이템
class Item():
  def __init__(self, Iprice = None, Itype = None):
    
    self.Iprice = Iprice
    self.Itype = Itype
  
  def getIprice(self):
    return self.Iprice  
  
class Bow(Item):
  def __init__(self, Iprice = None):
    super().__init__(Iprice)
    self.item_attack_damage = 10
    self.Itype = 'Bow'

class Sword(Item):
  def __init__(self, Iprice = None):
    super().__init__(Iprice)
    self.item_attack_damage = 10
    self.Itype = 'Sword'
class Wand(Item):
  def __init__(self, Iprice = None):
    super().__init__(Iprice)
    self.item_attack_damage = 10
    self.Itype = 'Wand'

myPlayer = archer("캐릭터1")
print(f"직업:{myPlayer.job}")
print(f"HP:{myPlayer.HP}")
mymonster = zombie("괴물1")
print(myPlayer.exp)
'''wh`ile myPlayer.HP > 0:
  myPlayer.attacked(mymonster)'''
while mymonster.HP > 0:
  myPlayer.attack(mymonster)
print(f"현재 경험치:{myPlayer.exp}") 
print(f"HP:{myPlayer.HP}")
print(f"공격력:{myPlayer.attack_damage}")      
myBow = Bow(100)
myPlayer.getitem(myBow)
print(f"공격력:{myPlayer.attack_damage}")
       



