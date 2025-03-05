def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_letters = "true"
    love_letters = "love"

    true_count = sum(combined_names.count(letters) for letters in true_letters)
    love_count = sum(combined_names.count(letters) for letters in love_letters)

    love_score = int(str(true_count) + str(love_count))

    print(f"Your love score is {love_score}")

calculate_love_score("naveen sita reddy kovvuri", "tadi eswari")