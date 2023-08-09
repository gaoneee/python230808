import re

def test_email_extraction():
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    test_cases = [
        "이메일 주소는 abc@example.com과 xyz123@gmail.com입니다.",
        "문자열 중간에 @가 있는 test@test.com 케이스도 처리해야 합니다.",
        "이메일 주소 없는 문장도 있습니다.",
        "이메일 주소가 특수문자로 끝나는 경우 test@example.com! 같은 경우 처리가 필요합니다.",
        "도메인이 숫자로 끝나는 경우 test@123.com도 포함해야 합니다.",
        "도메인의 길이가 2자 미만인 경우도 처리가 필요합니다.",
        "이메일 주소가 모두 대문자인 경우 TEST@EXAMPLE.COM",
        "여러 이메일 주소가 한 문장에 있을 수 있습니다: one@example.com, two@test.com",
        "도메인에 하이픈이 있는 경우 test@my-domain.com",
        "도메인 형식이 .co.kr 등과 같이 긴 경우도 처리가 필요합니다."
    ]

    for i, text in enumerate(test_cases):
        emails_found = re.findall(email_pattern, text)
        print(f"Test Case {i+1}:")
        print(f"Text: {text}")
        print(f"Emails Found: {emails_found}")
        print("="*40)

if __name__ == "__main__":
    test_email_extraction()
