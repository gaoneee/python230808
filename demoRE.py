# demoRE.py
import re
#빈칸 포함하고 있으면 검색
result =re.search("[0-9]*th","  35th") #[0-9]숫자가 와야함 *이니까 출현횟수가 0~n임
print(result)
print(result.group())  #리턴받은것에서 찾은것만
#정확하게 일치하는것만 검색
# result=re.match("[0-9]*th","192535th")
# print(result)
# print(result.group())

result=re.search("apple","빅테크에서 Apple의 위상".lower())
print(result.group())
print("-------연도검색------")
result=re.search("\d{4}","올해는 2023년 입니다.") #4자리 숫자 찾기
print(result.group())
print("-------우편번호검색------")
result=re.search("\d{5}","우리 동네는 52300입니다.") #5자리 숫자찾기
print(result.group())
