# ----------------------------------------------------------------------------------------------
# Type Guessing : 
# ----------------------------------------------------------------------------------------------

print("=" * 60) 
print("TYPE GUESSING GAME - MCQ Edition!") 
print("=" * 60) 
print("Guess the type of each variable!") 
print("Options: A) str B) int  C) float  D) bool") 
print() 
questions = ["var1 = 100", "var2 = '100'", "var3 = 100.0", 
"var4 = True","var5 = '3.14'", "var6 = 7 + 3", "var7 = 7 / 2", 
"var8 = 7 // 2", "var9 = 'True'", "var10 = 5 < 10"] 
answers = ["B", "A", "C", "D", "A", "B", "C", "B", "A", "D"] 
score = 0 
for i in range(len(questions)): 
    print(f"Question {i + 1}: {questions[i]}") 
    user_answer = input("Your answer (A/B/C/D): ").upper() 
    if user_answer == answers[i]: 
        print("✓ Correct!") 
        score += 1 
    else: 
        print(f"✗ Wrong! The correct answer is {answers[i]}") 
        print() 
print("=" * 60) 
print(f"GAME OVER! Your final score: {score}/{len(questions)}") 
print("=" * 60) 
if score == len(questions): 
    print("Perfect score! You're a Type Master! 🏆") 
elif score >= 7: 
    print("Great job! You know your types well! 🌟") 
elif score >= 5: 
    print("Good effort! Keep practicing! 💪") 
else: 
    print("Keep learning! You'll get better! 📚") 
 