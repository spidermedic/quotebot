import random
import quotes


def get_quote():
    r = random.randint(0, 1871)
    print(f"\n{quotes.quote[r]['quote']}\n-{quotes.quote[r]['by']}\n")


if __name__ == "__main__":
    get_quote()
