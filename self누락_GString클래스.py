# 전역변수
str = "Not Class Member"
#클래스정의 파이썬은 모호한것 보다 명확한것이 좋다..밖에 뭐가 있는지 모름..
class GString:
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #print(str)
        print(self.str)  #명확하게 self의 str로 정의
#인스턴스 생성
g = GString()
g.set("First Message") #8행으로 감
g.print()
