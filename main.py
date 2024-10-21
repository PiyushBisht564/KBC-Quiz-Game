import time

# Function to ask a question
def ask_question(question, options, correct_ans, prize):
    print("\n", question)
    for option in options:
        print(option)
    answer = input("Enter your answer: ").lower()

    if answer == correct_ans:
        print(f"Congratulations! \n YOU WON {prize} rupees")
        return True
    else:
        print("YOU LOST!")
        raise SystemExit

def main():
    print("Welcome to Kaun Banega Crorepati\n")
    
    questions = [
        ("What is the smallest prime number?", ["a. 2", "b. 3", "c. 4", "d. 6"], "a", "1000"),
        ("What is the capital of India?", ["a. Mumbai", "b. Delhi", "c. Kolkata", "d. Chennai"], "b", "2000"),
        ("Who is the current Home Minister of India?", ["a. Narendra Modi", "b. Rahul Gandhi", "c. Amit Shah", "d. Arvind Kejriwal"], "c", "3000"),
        ("What is the national animal of India?", ["a. Lion", "b. Tiger", "c. Cheetah", "d. Leopard"], "b", "4000"),
        ("What was Albert Einstein's famous formula?", ["a. E=mc^2", "b. E=mc^3", "c. E=mc^9", "d. E=mc^10"], "a", "5000")
    ]
    
    for i, (question, options, correct_ans, prize) in enumerate(questions):
        print(f"\nQuestion {i+1}:")
        time.sleep(1)  # Adds suspense
        if not ask_question(question, options, correct_ans, prize):
            break

if __name__ == "__main__":
    main()
