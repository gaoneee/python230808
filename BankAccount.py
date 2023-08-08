# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 메서드
    def __init__(self, id, name, balance):
        #내부에 멤버변수를 숨기기 (이름변경) __이거 붙이기 이거 안붙이면 밑에 27,28 주석 풀면 달라짐
        self.__id = id
        self.__name = name 
        self.__balance = balance
    #입금 
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #객체문자열 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#account1.balance=15000000
#print(account1)
#print(account1.__balance) ##숨김처리 확인
