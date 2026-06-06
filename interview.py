print("================================")
print("     AI Interview Simulator     ")
print("================================")

name = input("Enter your name: ")

print("\nHello", name)
print("Answer the following questions.\n")

score = 0

q1 = input("1. Tell me about yourself: ")

if len(q1) > 20:
    print("Good answer!")
    score += 10
else:
    print("Try giving more details.")

q2 = input("\n2. Why should we hire you? ")

if len(q2) > 20:
    print("Good answer!")
    score += 10
else:
    print("Try giving more details.")

q3 = input("\n3. What are your strengths? ")

if len(q3) > 20:
    print("Good answer!")
    score += 10
else:
    print("Try giving more details.")

q4 = input("\n4. What is your biggest weakness? ")

if len(q4) > 20:
    print("Good answer!")
    score += 10
else:
    print("Try giving more details.")

q5 = input("\n5. Where do you see yourself in 5 years? ")

if len(q5) > 20:
    print("Good answer!")
    score += 10
else:
    print("Try giving more details.")

print("\n================================")
print("           RESULT")
print("================================")

print("Name:", name)
print("Score:", score, "/50")

if score >= 40:
    print("Performance: Excellent")
elif score >= 30:
    print("Performance: Good")
elif score >= 20:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")

print("\nThank you for using AI Interview Simulator!")