def home_page():
    print("🎌 Welcome to Anime Quiz 🎌")

    player_name = input("Enter your name: ")

    print("\nChoose Difficulty level")
    print("1. Easy")
    print("2. Moderate")
    print("3. Medium")
    print("4. Hard")

    choice = input("Enter Choice: ")

    if choice == "1":
        difficulty = "Easy"

    elif choice == "2":
        difficulty = "Moderate"

    elif choice == "3":
        difficulty = "Medium"

    elif choice == "4":
        difficulty = "Hard"

    else:
        difficulty = "Easy"   # temporary fallback
        print("Invalid choice. Defaulting to Easy.")

    return player_name, difficulty




