def record_score(limit):
    while True:
        score = int(input(f"Enter a score (must be <= {limit}): "))
        if score <= limit:
            return score  # Return the actual score


a = record_score(30)
b = record_score(30)
c = record_score(40)

result = a + b + c

print(f"Total score: {result}")
