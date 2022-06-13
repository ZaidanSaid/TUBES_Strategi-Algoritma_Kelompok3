import random
import time

n = 1000000000
p = (n * 10) - 1

def generate_password(): #function to generate a random number between 1000 and 9999, stored in global variable "pw"
    global pw
    pw = random.randrange(n, p)
    print("Generated password is:", pw)


#Brute force algorithm
def brute_force():
    start_time = time.perf_counter_ns()
    guess = n
    attempts = 0
    while (guess != pw):
        attempts = attempts + 1
        guess = guess + 1
    end_time = time.perf_counter_ns()

    print("Brute force answer =", guess)
    print("Number of attempts =", attempts)
    global bf_time
    bf_time = end_time - start_time

#Divide and conquer algorithm

dnc_answer = []
split_amount = 0

def dnc(dg):
    global dnc_answer
    global split_amount

    if (len(dg) == 1):
        dg = int(dg[0])
        guess = 0
        while (guess != dg):
            guess = guess + 1
        dnc_answer.append(guess)
    else:
        length = len(dg)
        middle_index = length // 2
        split_amount = split_amount + 1
        dg1 = dg[:middle_index]
        dg2 = dg[middle_index:]
        dnc(dg1)
        dnc(dg2)

#Start of main


generate_password()

#Brute force
brute_force()
print("Brute force time taken =", bf_time, "nanoseconds")
print("")

#Divide and conquer
start_time = time.perf_counter_ns()
pw_list = [int(x) for x in str(pw)]

dnc(pw_list)

end_time = time.perf_counter_ns()

dnc_time = end_time - start_time

print("Amount divided:", split_amount)
print("Divide and Conquer answer:", dnc_answer)
print("Divide and Conquer time taken:", dnc_time, "nanoseconds")
