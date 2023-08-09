# demoFile.py
#파일 쓰기
f=open("c:\\work2\\demo.txt","wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()


#파일 읽기 (raw string notation)
f=open("c:\\work2\demo.txt","rt",encoding="utf-8")
print(f.read())
print("--------rea dline()--------")
f.seek(0) #EOF를 초기화 파일포인터를 다시 처음으로 오게끔
print(f.readline(),end="")  #한줄씩 읽어오기 end =>출력하고 줄바꿀 필요 없음
print(f.readline(),end="")   
print("--------readline()--------")
f.seek(0)
result=f.readlines() #리스트로 가져옴

print(result)
for item in result:
    for x in item:
        print(x)
    print(item,end="")
f.close()

