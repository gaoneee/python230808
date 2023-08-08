#DemoSlice.py
strA="python is very powerful"
strB="파이썬은 강력해"
print(len(strA))
print(len(strB))

print(strA[0:6])
print(strB[0:4])

print(strA[:6])
print(strB[4])

print(strA[-3:])
print(strB[-3:])

strC="""다중라인을
저장해서
작업한은 경우"""

print(strC)
print(strA)

#대소문자 구분 대소문자가 다르면 메모리에 다르게 올라감 (C언어의 성격)
friend=5
Friend=6
print(friend)
print(Friend)
#리스트는 값의 나열,,순서가 존재하고 여러개 담기 가능
#함수()/// 클래스 OR 인스턴스.메서드()

colors=["red","green","blue"]
colors
colors.append("white")
colors
colors +="red"
colors
print (type(colors))
colors.insert(1,"pink")
print(colors)
print(colors.index("pink"))
colors +=["red"]  #가능한 append를 쓰는게 안전함
print(colors)
print(colors.pop())  #보여주고 삭제하기 기능
print(colors.pop())
print(colors.pop())
print(colors)

#정순으로 정렬
colors.sort() #정순
print(colors)  
colors.reverse() #역순
print(colors)

print("----set형식---")
a={1,2,3,4}
b={3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print(colors)



def calc(a,b):
    return a+b,a*b

result=calc(5,6)
print(result)

print("id:%s, name:%s"%("kim","김유신"))
args=(4,5)

print(calc(*args)) #튜플에 있는 값을 함수 인자로 사용하는 경우