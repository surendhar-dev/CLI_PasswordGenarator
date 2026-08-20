import generator.cli as cli
import generator.core as core
import generator.storage as storage

def get_bool_input(prompt: str) -> bool:
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice == 'y'

def run():
    while True:
        cli.print_header()
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Password History")
        print("4. Clear History")
        print("5. Exit")

        choice = input("\nChoose: ").strip()

        if choice == "1":
            try:
                length = int(input("\nPassword length: "))
                if length < 8:
                    print("\n❌ Password must be at least 8 characters.")
                    continue
            except ValueError:
                print("\n❌ Invalid number format.")
                continue

            print("\nInclude:")
            use_upper = get_bool_input(" Include Uppercase letters?")
            use_lower = get_bool_input(" Include Lowercase letters?")
            use_nums = get_bool_input(" Include Numbers?")
            use_syms = get_bool_input(" Include Symbols?")

            if not (use_upper or use_lower or use_nums or use_syms):
                print("\n❌ You must enable at least one character type.")
                continue

            try:
                password = core.generate_password(length, use_upper, use_lower, use_nums, use_syms)
                score, rating, bar = core.evaluate_strength(password)

                storage.save_password_record(password, rating)

                print("\nGenerating...")
                print(f"\nYour password : {password}")
                print(f"Strength      : {bar} {rating} ({score}/6 pts)")

            except ValueError as e:
                print(f"\n❌ Error: {e}")

        elif choice == "2":
            pwd = input("\nEnter password to check: ").strip()
            if not pwd:
                print("Password cannot be empty.")
                continue
            score, rating, bar = core.evaluate_strength(pwd)
            print(f"\nPassword : {pwd}")
            print(f"Strength : {bar} {rating} ({score}/6 pts)")

        elif choice == "3":
            history_data = storage.load_history()
            cli.display_history(history_data["history"])

        elif choice == "4":
            confirm = get_bool_input("\nAre you sure you want to clear history?")
            if confirm:
                storage.clear_history()
                print("History cleared successfully!")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    run()