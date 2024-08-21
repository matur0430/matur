import random

class Roulette:
    def __init__(self):
        # 룰렛의 숫자와 색상 설정
        self.numbers = list(range(0, 37))
        self.colors = ["Red", "Black"] * 18 + ["Green"] # 0은 Green
        
    def spin(self):
        # 룰렛의 숫자와 색상을 무작위로 선택
        number = random.choice(self.numbers)
        color = self.colors[number]
        return number, color

    def bet(self, bet_type, bet_value):
        number, color = self.spin()
        print(f"Spin result: {number} {color}")
        
        if bet_type == "number" and bet_value == number:
            return "Win"
        elif bet_type == "color" and bet_value.lower() == color.lower():
            return "Win"
        elif bet_type == "range":
            if bet_value == "1-18" and 1 <= number <= 18:
                return "Win"
            elif bet_value == "19-36" and 19 <= number <= 36:
                return "Win"
        return "Lose"

# 게임 시작
roulette = Roulette()
while True:
    print("\nPlace your bet:")
    bet_type = input("Bet type (number, color, range): ").strip().lower()
    if bet_type == "number":
        bet_value = int(input("Bet value (0-36): ").strip())
    elif bet_type == "color":
        bet_value = input("Bet value (Red, Black): ").strip().capitalize()
    elif bet_type == "range":
        bet_value = input("Bet value (1-18, 19-36): ").strip()
    else:
        print("Invalid bet type. Please try again.")
        continue

    result = roulette.bet(bet_type, bet_value)
    print(f"Result: {result}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
