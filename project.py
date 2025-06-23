import random
import json
import sys
import os


def choose_cat():
    with open("questions.json", "r") as file:
        quiz_data = json.load(file)
    print("Choose one category: Geography | Science | Literature | History | Technology")
    category = input()
    print("...")
    questions = []
    for question in quiz_data:
        if question["category"] == category:
            questions.append(question)
    print(f"You chose {category}")
    print("...")
    print("...")
    return questions


def choose_questions(questions):
    chosen_questions = []
    i = 5
    while i > 0:
        question = random.choice(questions)
        if question not in chosen_questions:
            chosen_questions.append(question)
            i -= 1
    return chosen_questions


def ask_questions(questions):
    score = 0
    for question in questions:
        print(question["question"])
        print(f"A: {question["options"][0]} | B: {question["options"][1]} | C: {question["options"][2]} | D: {question["options"][3]}")
        answer = input("Your answer: ").strip().upper()
        print("...")
        letters = ["A", "B", "C", "D"]
        answer_index = question["options"].index(question["answer"])
        corect_answer = letters[answer_index]
        if answer == corect_answer:
            print("Correct answer!")
            score += 1
            print("...")
            print("...")
        else:
            print(f"Wrong! Correct answer was {question["answer"]}")
            print("...")
            print("...")
    print(f"Your final score is: {score}")
    print("Whats your name? ")
    name = input()
    save_leaderboards(score, name)


def save_leaderboards(score, name):
    scores = get_leaderboards()

    scores.append({"name": name, "score": score})

    with open("leaderboards", "w") as file:
        json.dump(scores, file, indent=4)


def get_leaderboards():
    if os.path.exists("leaderboards"):
        with open("leaderboards", "r") as file:
            try:
                scores = json.load(file)  # Load existing scores
            except json.JSONDecodeError:
                scores = []
    else:
        scores = []

    return scores


def print_leaderboards():
    leaderboards = get_leaderboards()
    sorted_leaderboards = sorted(leaderboards, key=lambda x: x["score"], reverse=True)
    for position in sorted_leaderboards:
        print(f"Name: {position["name"]} | Score: {position["score"]}")

def start_game():
    print("Type: Start | Leaderboards | Quit") #main menu
    user_input = input("").strip().lower()
    print("...")
    print("...")

    if user_input == "start":
        ask_questions(choose_questions(choose_cat())) #game
    if user_input == "leaderboards":
        print_leaderboards()
    if user_input == "quit":
        sys.exit()


def main():
    start_game()


if __name__ == "__main__":
    main()
