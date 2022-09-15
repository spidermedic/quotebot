import random
import quotes


def get_quote():
    r = random.randint(0, len(quotes.quotes) - 1)
    print(f"\n{quotes.quotes[r]['quote']}\n-{quotes.quotes[r]['by']}\n")


if __name__ == "__main__":
    get_quote()
