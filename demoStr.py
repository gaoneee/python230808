# demoStr.py

strA="파이썬은 강력해"
strB="python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.upper())
print(strB.count("p"))
print(strB.count("p",7))
print(strB.startswith("python"))
print(strB.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isalnum())
#data =" spam and ham "
#문자열 전처리
data ="<<<spam and ham>>>"
result=data.strip("<> ")
print(data)
print(result)
result2=result.replace("spam","spam egg")
lst=result2.split() #쪼개기
print(lst)
result3=":)".join(lst) #합치기
#print(data.strip()) #strip 공백문자 없애기
print(result3)