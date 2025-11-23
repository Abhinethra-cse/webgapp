#timer
import time
seconds = int(input("Enter time in seconds: "))
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)
    seconds -= 1
print("Time's up!")

#alphabet count
letter = input("Enter a letter: ")
count = 0
for ch in "abcdefghijklmnopqrstuvwxyz":
    count += 1
    if ch == letter:
        print("The position is:", count)



#question with choice
question = "How many days are there in a week?"
options = ["A) 5", "B) 6", "C) 7", "D) 8"]
answer = "C) 7"
print(question)
for opt in options:
    print(opt)
print("\nCorrect Answer:", answer)
