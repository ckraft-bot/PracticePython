# greet the user to D-SAT  
print("Welcome to the Data Science Acronym Trivia (D-SAT)")  

# invite user to play D-SAT  
invite = input("Do you want to play? ")  

# if user rejects to play then quit the game  
if invite.lower() != "yes":  
    quit()  

# otherwise we'll begin the game  
print("Okay, Let's play.")  

# scoreboard set up  
score = 0  

# round 1  
answer = input("What does EDA stand for? ")  
if answer.lower() == "Exploratory Data Analysis":  
    print('Correct')  
    score += 1  
else:  
    print('Incorrect')  

# round 2  
answer = input("What does ML stand for? ")  
if answer.lower() == "Machine Learning":  
    print('Correct')  
    score += 1  
else:  
    print('Incorrect')  

# round 3  
answer = input("What does ETL stand for? ")  
if answer.lower() == "Extract Transform Load":  
    print('Correct')  
    score += 1  
else:  
    print('Incorrect')  

# round 4  
answer = input("What does DDL stand for? ")  
if answer.lower() == "Data Definition Language":  
    print('Correct')  
    score += 1  
else:  
    print('Incorrect')  

# round 5  
answer = input("What does SLA stand for in DevOps? ")  
if answer.lower() == "Service Level Agreement":  
    print('Correct')  
    score += 1  
else:  
    print('Incorrect')  


print("You got " + str(score) + " questions Correct.")  
print("You got " + str((score / 6) * 100) + "%.")  



"""
QUESTION AND ANSWER KEY
-----------------------------------------
What does EDA stand for?
Answer: Exploratory Data Analysis

What does ML stand for?
Answer: Machine Learning

What does NLP stand for?
Answer: Natural Language Processing

What does AI stand for?
Answer: Artificial Intelligence

What does SVM stand for?
Answer: Support Vector Machine

What does PCA stand for?
Answer: Principal Component Analysis

What does RDBMS stand for?
Answer: Relational Database Management System

What does DDL stand for?
Answer: Data Definition Language

What does DML stand for?
Answer: Data Manipulation Language

What does ACID stand for?
Answer: Atomicity, Consistency, Isolation, Durability

What does CRUD stand for?
Answer: Create Read Update Delete

What does ETL stand for?
Answer: Extract Transform Load

What does SLA stand for in DevOps?
Answer: Service Level Agreement

What does AWS stand for in DevOps?
Answer: Amazon Web Services
"""