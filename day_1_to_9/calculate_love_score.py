def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).upper()

    t = combined_names.count("T")
    r = combined_names.count("R")
    u = combined_names.count("U")
    e = combined_names.count("E")
    true_total = t + r + u + e

    l = combined_names.count("L")
    o = combined_names.count("O")
    v = combined_names.count("V")
    e = combined_names.count("E")
    love_total = l + o + v + e

    love_score = int(f"{true_total}{love_total}")

    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")
