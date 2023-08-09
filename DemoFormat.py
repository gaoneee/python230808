# DemoFormat.py
for x in range(1,6):
    print(x,"*",x,x*x)

print("-----오른쪽정렬-----")
for x in range(1,6):
    print(x,"*",x,str(x*x).rjust(3))


print("-----0으로 채우기-----")
for x in range(1,6):
    print(x,"*",x,str(x*x).zfill(5))


print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:,}".format(17000))
print("{0:f}".format(4/3))
print("{0:2f}".format(4/3))

#strURL="https://www.ycampus.co.kr/?page="+1 #앞은 string인데 뒤가 int여서 에러 
for i in range(0,10):
    #동적으로 주소를 생성
    strURL="https://www.ycampus.co.kr/?page="+str(i)
    print(strURL)