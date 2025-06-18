questions = [
    {"q": "What is the capital of France?", "options": ["a) Paris", "b) London", "c) Rome"], "answer": "a"},
    {"q": "Which planet is known as the Red Planet?", "options": ["a) Venus", "b) Mars", "c) Jupiter"], "answer": "b"},
    {"q": "Who wrote 'Romeo and Juliet'?", "options": ["a) Dickens", "b) Shakespeare", "c) Tolkien"], "answer": "b"}
]

score = 0
for i, q in enumerate(questions):
    print(f"\nQ{i+1}: {q['q']}")
    for opt in q['options']:
        print(opt)
    ans = input("Your answer: ").lower()
    if ans == q['answer']:
        score += 1

print(f"\nFinal Score: {score} out of {len(questions)}")

