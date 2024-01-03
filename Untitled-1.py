# %%
print("Hello world")

# %%
a=6
b=4

# %%
print(a+b)

# %% [markdown]
# # 쥬피터 단축키
# 셀 생성: b, a

# %%
import keyword
import math
print(keyword.kwlist)

# %%
abs(-3.14)

# %%
# 안녕하세요

# %%
print("Hello, World")
print("Hello", "Python")

# %%
print("Hello","World!",sep = "+")
print("Hello","+","World") # sep = " "로 기본설정 돼있기 때문에 띄어쓰기로 써짐

# %%
print("Hello"+"World") #문자열끼리만 연산을 했기 때문에 가능
print("Hello",42)

# %%
print("hello")
print("world")

# %%
print("hello",end=" ")
print("world")

# %%
name = 'groot'
age = 26
hobby = "축구"
add = 'Seoul'
height = 173
print(f"저의 이름은 {name}, 나이는 {age}, 취미는 {hobby}이고 사는곳은 {add}")
name = "강낭콩"
print(name)

# %% [markdown]
# # 자료형

# %%
a = int(input("숫자를 넣어주세요"))
a_modified=int (a)


# %%
print("|\\_/|")
print('|q p|   /}')
print('( o )"""\\')
print("|\"^\"'    |")
print("||_/=\\\\__|")


# %%
print("    []")
print("    []")
print("[      ]")
print("[      ]")

# %%
print(3//2)
print(3.25//2)

# %%
print(11%3)
print(11.5%2)

# %%
print(2**3)

# %%
print("ㅎㅇ"+"ㅠㅠ")
print("hi"*4)

# %%
print("banana".count("a"))

# %%
"apple"[-5:-1]

# %%
list = "a b c"
print(list.split())
email = "abc@naver.com"
print(email.split("@"))

# %%
a = "apple"
print("apple"[0:5:2]) #인덱스 0~5를 2간격으로 출력
print("apple"[-1:-6:-1])
print(a[6::-1])
# 2024-01-02
'''
2024-01-02
'''

# %%
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요")
print(f"안녕하세요! {name}님 ({age}세)")

name = input("이름을 입력하세요.")
born_year = int(input("태어난 년도를 입력하세요."))
current_year = int(input("올해 년도를 입력하세요."))
age = current_year - born_year + 1
print(f"올해는 {current_year}년, {name}님의 나이는 {age}세 입니다.") 


# %%
a = 472
b = 385

one = a*int(str(b)[2])
two = a*int(str(b)[1])
three = a*int(str(b)[0])
c = a*b
print(one)
print(two)
print(three)
print(c)

# %% [markdown]
# # 리스트

# %%
shop = ["반팔", "청바지", "이어폰", "키보드"]
print(shop[0:2])

# %%
a = [1,2,3]
b = [2,3]
print(a+b)
print(a*2)
print(len(a))

# %%
shop[0] = "긴팔" # 인덱스 바꾸기

# %%
a = [1, 2, 3,8 ,4]
a.reverse()
print(a)

# %%
num = [4,1,2,3]
print(sorted(num))
print(num)

# %%
shop.append("치마")
print(shop)
shop.remove("치마")
print(shop)

# %%
shop.insert(1, "b")
print(shop)

# %%
shop = [1, 2, 3, 4, 5, 6]
print(shop.index(2))

# %%
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2])
print(sorted(rainbow))
rainbow.append('black')
print(rainbow)
del rainbow[2:6]
print(rainbow)

# %%
a = 3
b = 2
if a>b:
  print("a>b")
if a<b:
  print("a<b")

# %%
num =  int(input())

if num%2 == 0:
  print("짝수")
if num%2 == 1:
  print("홀수")

# %%
a = int(input())

if a>=90:
  print("A")
elif a>=80:
  print("B")
elif a>=70:
  print("C")
elif a>=60:
  print("D")
else:
  print("E")

# %%
age = int(input("나이를 숫자로 입력해 주세요"))
bus = input("결제 방법을 선택해 주세요('카드' 또는 '현금'만 입력)")

if age<8:
  print(f"{age}세의 요금은 무료입니다")
elif age<14:
  print(f"{age}세의 요금은 450원입니다.")
elif age<20:
  if bus == "카드":
    print(f"{age}세의 {bus}요금은 720원입니다")
  else:
    print(f"{age}세의 {bus}요금은 1000원입니다")
elif age<75:
  if bus == "카드":
    print(f"{age}세의 {bus}요금은 1200원입니다")
  else:
    print(f"{age}세의 {bus}요금은 1300원입니다")
else:
  print(f"{age}세의 요금은 무료입니다")

# %%
print(list("abc"))

# %%
mylist = list("abc")
print(mylist)

# %%
mylist = list("abc")
mylist.reverse()
print(*mylist,sep="")

# %% [markdown]
# # 반복문

# %%
tuple_ = (1,2,3)
list_ = {"a","b","c"}
str = ""
for t in list_:
  str = t + str
print(str)

# %%
for i in range(10):
  print(i)

# %%
mystr = "apple is red"
mystr = mystr[::2]


print(mystr)


# %%
for i in range(3,10,2):
  print(i)

# %%
for i in range(10,-1,-1):
  print(i)

# %%
num = int(input("어디까지 계산할까요?"))

sum = 0
sum1 = 0
for i in range(1,num+1):
  if i%2 == 1:
    sum = sum + i
print(sum)

for i in range(1,num+1,2):
  sum1 = sum1 + i
print(sum1)

# %%
# 홀수 빨리 찾는 법
n = 5
mylist = list(range(1,n+1))
oddsum = 0
for i in mylist:
  if(i&1):
    oddsum += i
    
print(oddsum)

# %%
num = int(input(print("몇 초?", end = " ")))
print(num)

for i in range(num,0,-1):
  print(i, end =" ")
print("발사!!")

# %%
num = int(input("몇 초?"))

for i in range(num,0,-1):
  print(i, end = " ")
print("발사!")

# %%
num = int(input("몇 단을 출력할까요?"))

for i in range(1,10):
  print(f"{num} * {i} = {num*i}")

# %%
# 팁) 객체 필요없이 10번만 반복할래
for _ in range(10):
  print("안녕")

# %%
#2중 for문 구구단
for y in range(1,10):
  for x in range(1,10):
    print(f"{y} * {x} = {y*x}")
  print()

# %%
while True:
  lunch = input("뭐 먹을까")
  if lunch == "그만":
    break
  print(lunch+"!!")
print("done")

# %%
line = int(input("몇 줄?"))
i=1
while (i <= line):
  print("*"*i)
  i = i+1

# %%
line = int(input("몇 줄?"))
i=1

while (i<=line):
  a=line-i
  print(" "*a,"*"*i)
  i = i+1

# %%
line = int(input("몇 줄?"))
i=1

while (i<=line):
  a=line-i
  b=2*i-1
  print(" "*a,"*"*b)
  i = i+1

# %%

a = input()
b = list(a.split())
c=[]
i = 0
while (i <= len(b)-1):
  c.append(int(b[i]))
  i = i+1
max_ = max(c)
min_ = min(c)
print("가장 큰 값:",max_)
print("가장 작은 값:", min_)
c.remove(max_)
c.remove(min_)
sum=0
for i in c:
  a=int(i)
  sum=sum+a
mean = sum/len(c)
print(mean)







# %%
a = input()
b = list(a.split())
c=[]
i = 0
while (i <= len(b)-1):
  c.append(int(b[i]))
  i = i+1
max_ = max(c)
min_ = min(c)
print("가장 큰 값:",max_)
print("가장 작은 값:", min_)
c.remove(max_)
c.remove(min_)
_len = len(c)-1
sum=0

i=0
while (i <= _len):
  h=c[i]
  sum=sum+h
  i=i+1
mean = sum/len(c)
print(mean)

# %%
num = input("숫자 여러 개 입력: ")
num_list = list(map(float, num.split()))
max_ = max(num_list)
min_ = min(num_list)
print(max_)
print(min_)

# %% [markdown]
# # 튜플

# %%
# set
number1 = {1,2,3,4,5}
number2 = set([1,2,3,4,5,5])
apple = set('apple')

print(number2)
print(apple)

print(1 in number1)
print('c' in apple)

number1.add(6)
print(number1)

number1.remove(1)
print(number1)

print(number1.pop())
print(number1)

number1.clear()
print(number1)

# %%
dict = {'apple': '사과', "banana": "바나나", "peach": "복숭아"}
print(dict.values())
print(list(dict.keys()))

# %%
for s in dict.keys():
  print(s,dict[s])
"apple in dict"
dict.clear()
print(dict)

# %%
num = int(input())
list_ = []
for i in range(1,num+1):
  list_.append(i)
print(list_)

list_1 = list_[0::2]
list_2 = list_[1::2]
print(list_1)
print(list_2)

# %%
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']

berverage = input("마시고 싶은 음료?")

if berverage in vending_machine:
  print(f"{berverage} 드릴게요")
else:
  print(f"{berverage}는 지금 없네요")

# %%
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

ask = input("주인 or 소비자")
print(f"남은 음료수:{vending_machine}")
if ask == "소비자":
  berverage = input("마시고 싶은 음료")
  if berverage in vending_machine:
    vending_machine.remove(berverage)
    print(f"{berverage}드릴게요")
  else:
    print("없음")
elif ask == "주인":
  y_n = input("추가 or 삭제")
  if y_n == "추가":
    add_b = input("추가할 음료수")
    vending_machine.append(add_b)
  elif y_n == "삭제":
    sub_b = input("삭제할 음료")
    vending_machine.remove(sub_b)
  else:
    print("잘못된 접근입니다")
else:
  print("잘못된 접근입니다.")
print(f"남은 음료수{vending_machine}")    


