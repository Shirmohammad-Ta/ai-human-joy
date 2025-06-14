

from src.environment.interactive_env import InteractiveEnvironment

def main():
    env = InteractiveEnvironment()
    print("✨ Welcome to the AI-Human-Joy CLI Interface! ✨")
    rounds = 0
    while True:
        rounds += 1
        env.run_once()
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break
    print(f"📝 You had {rounds} rounds of interaction. Thank you for your participation! ❤️")

if __name__ == "__main__":
    main()
