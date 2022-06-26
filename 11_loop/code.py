# while statement
number = 7
while True:
    isPlaying = input("Would you like to play guessing game? (Y/n): ")
    if (isPlaying == 'n'):
        break

    guess = int(input("Guess the magic number => "))
    if guess == number:
        print(":-) Kabooz! You got it right")
    elif guess < number:
        print(":-( Your guess is smallert than target number")
    elif guess > number:
        print(":-( Your guess is bigger than target number")
    

# for statement
subjects = ["maths", "english", "chemistry"]
for subject in subjects:
    print(subject)  

for index in range(len(subjects)):
    print(subjects[index])

numbers = [1,2,3,4,5]
even = []

for x in numbers:
    even.append(x * 2)
print(even)