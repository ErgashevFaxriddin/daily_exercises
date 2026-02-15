# Kompyuter 1 dan 10 gacha bir raqamni “yashirin” tanlaydi.
# Siz u raqamni topishga harakat qilasiz.
# Agar sizning taxminingiz kichik bo‘lsa, kompyuter “Kattaroq raqamni o‘yladim” deydi.
# Agar katta bo‘lsa, “Kichikroq raqamni o‘yladim” deydi.
# To‘g‘ri topganingizda, “Tabriklayman, topdingiz!” degan xabar chiqadi.

import random

import random

def guess_num():
    secret = random.randint(1, 10)
    while True:
        guess = int(input("GUESS THE NUMBER (1-10): "))
        if guess < secret:
            print("BIGGER")  # Higher
        elif guess > secret:
            print("SMALLER")  # Lower
        else:
            print("CONGRATULATIONS, YOU WON!")  # Correct
            break
