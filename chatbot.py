def chatbot():
    print("Hello! I'm your AI Course Assistant Bot.")
    name = input("Before we begin what is your name? ")
    print(f"\nNice to meet you, {Zoro Roronoa}! You can ask me about: Anything involving AI.")
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

       # Intent 6 - What is Deep Learning
elif 'deep learning' in user_input:
    print("Bot: Deep Learning is a subset of Machine Learning that uses neural networks with many layers to learn from large amounts of data.\n")

# Intent 7 - What is a dataset
elif 'dataset' in user_input or 'data' in user_input:
    print("Bot: A dataset is a collection of data used to train machine learning models. Popular sources include Kaggle, UCI ML Repository, and Google Datasets.\n")

# Intent 8 - What is NumPy
elif 'numpy' in user_input:
    print("Bot: NumPy is a Python library used for numerical computations. It provides support for arrays and mathematical functions used in AI and ML.\n")

# Intent 9 - What is Pandas
elif 'pandas' in user_input:
    print("Bot: Pandas is a Python library used for data manipulation and analysis. It helps load, clean, and explore datasets easily.\n")

# Intent 10 - What is scikit-learn
elif 'scikit' in user_input or 'sklearn' in user_input:
    print("Bot: Scikit-learn is a Python library for machine learning. It provides tools for classification, regression, clustering, and model evaluation.\n")

# Intent 11 - Greeting
elif 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
    print("Bot: Hello! How can I help you today? You can ask me about AI, ML, Python, or your assignments!\n")

# Intent 12 - Thank you
elif 'thank' in user_input or 'thanks' in user_input:
    print("Bot: You are welcome! Feel free to ask me anything else.\n")          
# Intent 13 - What is Neural Network
elif 'neural network' in user_input or 'neurons' in user_input:
    print("Bot: A Neural Network is a series of algorithms that mimic the human brain to recognize patterns. It is the foundation of Deep Learning.\n")

# Intent 14 - What is NLP
elif 'nlp' in user_input or 'natural language' in user_input:
    print("Bot: Natural Language Processing (NLP) is a branch of AI that helps computers understand and interpret human language. Examples include chatbots and translators.\n")

# Intent 15 - What is supervised learning
elif 'supervised' in user_input:
    print("Bot: Supervised Learning is a type of ML where the model is trained on labelled data. Examples include classification and regression tasks.\n")

# Intent 16 - What is unsupervised learning
elif 'unsupervised' in user_input:
    print("Bot: Unsupervised Learning is a type of ML where the model finds patterns in data without labels. Examples include clustering and dimensionality reduction.\n")

# Intent 17 - What is overfitting
elif 'overfitting' in user_input:
    print("Bot: Overfitting happens when a model learns the training data too well and performs poorly on new data. It can be fixed using techniques like cross-validation.\n")

# Intent 18 - What is accuracy
elif 'accuracy' in user_input:
    print("Bot: Accuracy is a metric used to evaluate ML models. It measures the percentage of correct predictions out of total predictions made.\n")

# Intent 19 - What is regression
elif 'regression' in user_input:
    print("Bot: Regression is a type of ML algorithm used to predict continuous values. For example, predicting house prices or student grades.\n")

# Intent 20 - What is classification
elif 'classification' in user_input:
    print("Bot: Classification is a type of ML algorithm used to predict categories. For example, predicting whether a student will pass or fail.\n")

# Intent 21 - What is GitHub
elif 'github' in user_input or 'git' in user_input:
    print("Bot: GitHub is a platform for hosting and sharing code. It uses Git for version control, allowing you to track changes and collaborate with others.\n")

# Intent 22 - What is a model
elif 'model' in user_input:
    print("Bot: In Machine Learning, a model is an algorithm trained on data to make predictions. Examples include Decision Trees, Logistic Regression, and Neural Networks.\n")
#Run the chatbot
chatbot()
