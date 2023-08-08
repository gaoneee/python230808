# -*- 생성자와 소멸자 -*-
class MyClass:
    #초기화(생성자)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    # 소멸자(생성하고 메모리에서 삭제)
    def __del__(self):
        print("Instance is deleted!")
#인스턴스 생성
m=MyClass(5)
#삭제 위에 클래스에서 알아서 해주니까 13행과 같은 코드는 쓸데없는 코드임
#del m
#마무리
print("전체 코드 실행 종료")
