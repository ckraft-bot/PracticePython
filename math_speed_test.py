import random
import time
# Note: global constants naver change throughout and is typically all caps for the naming convention
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator =random.choice(OPERATORS)
    
    expr = f"{str(left)} {operator} {str(right)}"
    #print(expr)
    answer = eval(expr)
    return expr, answer

# tally of correct/wrong problems
wrong = 0
input("Press enter to start!")
print("----------------------")

# trigger timer
start_time = time.time()

# generate as many problems as specified above in TOTAL_PROBLEMS variable
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem # {str(i + 1)}: {expr} = ")
        if guess == str(answer):
            break
        wrong += 1

# stop timer
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print(f"Nice work! You finished in 10 problems {total_time} seconds!")
