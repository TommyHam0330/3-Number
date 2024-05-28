import random

def guess_number():
    # 랜덤으로 1부터 100 사이의 숫자 선택
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while True:
        try:
            guess = int(input("추측한 숫자를 입력하세요: "))
            attempts += 1

            if guess < secret_number:
                print("너무 작아요! 다시 시도해보세요.")
            elif guess > secret_number:
                print("너무 커요! 다시 시도해보세요.")
            else:
                print(f"축하합니다! {secret_number}를 {attempts}번 만에 맞추셨어요!")
                break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

guess_number()