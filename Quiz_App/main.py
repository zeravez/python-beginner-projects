score = 0

print("quiz time!")

questions = [
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Egypt?", "Cairo"),
    ("What is the capital of Canada?", "Ottawa"),
    ("what is the capital of Germany?", "Berlin"),
    ("what is the capital of Spain?", "Madrid"),
    ("what is the capital of Russia?", "Moscow"),
    ("what is the capital of China?", "Beijing"),
    ("what is the capital of India?", "New Delhi"),
]
for question, correct in questions:
    answer = input(question + " ")
    if answer.lower() == correct.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", correct)
print("Your score is", score, "out of", len(questions))

