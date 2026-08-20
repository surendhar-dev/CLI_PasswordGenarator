# def print_header():
#     print("\n==============================")
#     print("      PASSWORD GENERATOR      ")
#     print("==============================")

# def display_history(history: list):
#     if not history:
#         print("\nNo password history found.")
#         return

#     print("\n" + "="*50)
#     print(f"{'ID':<4} | {'Password':<20} | {'Strength':<12} | {'Created At'}")
#     print("-" * 50)
#     for item in history:
#         print(f"{item['id']:<4} | {item['password']:<20} | {item['strength']:<12} | {item['created_at']}")
#     print("="*50)
# generator/cli.py
def print_header():
    print("\n==============================")
    print("      PASSWORD GENERATOR      ")
    print("==============================")

def display_history(history: list):
    if not history:
        print("\nNo password history found.")
        return

    print("\n" + "="*50)
    print(f"{'ID':<4} | {'Password':<20} | {'Strength':<12} | {'Created At'}")
    print("-" * 50)
    for item in history:
        print(f"{item['id']:<4} | {item['password']:<20} | {item['strength']:<12} | {item['created_at']}")
    print("="*50)