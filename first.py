print("Python Quiz Game !!!\n")

questions = [
["Q.1. Who developed the Python language?", "C", 
["A) Bjarne Stroustrup", "B) James Gosling", "C) Guido van Rossum", "D) Dennis Ritchie"]],
["Q.2. In which year was the Python language developed?", "B", 
["A) 1981", "B) 1989", "C) 1990", "D) 1979"]],
["Q.3. In which language is Python written??", "D", 
["A) Java", "B) C++", "C) English", "D) C"]],
["Q.4. Which one of the following is the correct extension of the Python file?", "A", 
["A) .py", "B) .p", "C) .python", "D) .c"]],
]

score=0
for q in questions:
    print(q[0]) 
    for option in q[2]: 
        print(option)
    answer=input("Enter your answer (A/B/C/D): ").strip().upper()
    if answer==q[1]: 
        print("Correct answer...\n")
        score+=1
    else:
        correct_answer=q[2][ord(q[1]) - ord('A')]
        print(f"Incorrect answer...\nThe correct answer was {correct_answer}.\n")

        
print(f"Your score is {score}/{len(questions)}.")
