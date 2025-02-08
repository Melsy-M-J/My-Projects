import random
questions = {
 "What is the capital of France?": "Paris","What is the largest planet in our solar system?":"Jupiter","Who painted the Mona Lisa?": "Leonardo da Vinci", "In what year did World War II begin?": "1939"
,"What is the chemical symbol for gold?": "Au","How many continents are there?":"7","What is the highest mountain in the world?": "Mount Everest","Who wrote 'Hamlet'?": "William Shakespeare","What is the currency of Japan?": "Japanese Yen","What is the smallest country in the world?": "Vatican City"
}
def gk():
	questions_list= list(questions.keys())
	total_questions=5
	score=0
	selected=random.sample(questions_list,total_questions)
	for i, question in enumerate(selected):
		print(f"{i+1}.{question}")
		user_answer=input("Your answer: ").lower().strip()
		correct_answer = questions[question]
		if user_answer==correct_answer.lower().strip():
			print("Correct!\n")
			score+=1
		else:
			print(f"Wrong. The correct answer is:{correct_answer}.\n")
	print(f"You scored {score} on {total_questions}")


gk()
