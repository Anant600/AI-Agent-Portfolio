import ollama

# 1. Personality & Memory Setup
chat_history = [{
    'role': 'system', 
    'content': 'You are a Fitness Coach for Anant, a BCA student. You prioritize vegetarian muscle gain and quick student workouts.'
}]

print("--- AI COACH ONLINE (type 'quit' to stop) ---")

# 2. The Interactive Loop
while True:
    user_input = input("\nAnant: ")
    if user_input.lower() == 'quit':
        break

    # 3. Add your question to Memory
    chat_history.append({'role': 'user', 'content': user_input})

    # 4. Get AI Answer
    response = ollama.chat(model='llama3.2', messages=chat_history)
    coach_reply = response['message']['content']

    # 5. Save Answer to Memory
    chat_history.append({'role': 'assistant', 'content': coach_reply})

    print(f"\nCoach: {coach_reply}")