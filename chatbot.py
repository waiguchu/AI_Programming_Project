def chatbot():
    print("Hello! I'm your AI Course Assistant Bot.")
    print("You can ask me about: AI, machine learning, Python, assignments, or grades.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if 'quit' in user_input:
            print("Bot: Goodbye! Good luck with your studies!")
            break

        # Intent 1 - What is AI
        elif 'what is ai' in user_input or 'artificial intelligence' in user_input:
            print("Bot: AI stands for Artificial Intelligence. It is the simulation of human intelligence by machines to perform tasks like learning, reasoning, and problem solving.\n")

        # Intent 2 - Machine Learning
        elif 'machine learning' in user_input or 'ml' in user_input:
            print("Bot: Machine Learning is a subset of AI where computers learn from data to make predictions or decisions without being explicitly programmed.\n")

        # Intent 3 - Python
        elif 'python' in user_input:
            print("Bot: Python is the most popular programming language for AI and ML. Key libraries include NumPy, Pandas, and Scikit-learn.\n")

        # Intent 4 - Assignment help
        elif 'assignment' in user_input or 'cat' in user_input or 'help' in user_input:
            print("Bot: For your CAT, make sure you have at least 3 GitHub commits, a detailed README, and working Python code.\n")

        # Intent 5 - Grades
        elif 'grade' in user_input or 'marks' in user_input or 'score' in user_input:
            print("Bot: Your CAT 2 is worth 20% of your continuous assessment. Focus on clean code and good documentation!\n")

        # Default
        else:
            print("Bot: I'm sorry, I didn't understand that. Try asking about AI, machine learning, Python, assignments, or grades.\n")

# Run the chatbot
chatbot()                  
