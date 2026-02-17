import random

responses = {
    "sad": [
        "I'm really sorry you're feeling sad. Want to talk about what's going on?",
        "It's okay to feel sad sometimes. I'm here for you. 💙",
        "That sounds tough. You don't have to go through this alone.",
    ],
    "lonely": [
        "I'm right here with you. You're not alone! 🌻",
        "Loneliness is hard. I'm glad you reached out.",
        "Tell me about your day — I'm all ears.",
    ],
    "stressed": [
        "Take a deep breath. You've got this. 💪",
        "Stress is tough. What's been weighing on you?",
        "One step at a time. What's the biggest thing on your mind right now?",
    ],
    "tired": [
        "Rest is important. Have you been sleeping okay?",
        "Being tired makes everything harder. Be gentle with yourself today.",
        "Sometimes the bravest thing is just to rest. 🌙",
    ],
    "happy": [
        "That's amazing! I love hearing that! 😊",
        "Yay! Tell me more — what made you happy?",
        "That makes me happy too! 🎉",
    ],
    "anxious": [
        "Anxiety is really hard. Try to focus on just this moment.",
        "You're safe right now. Take it one breath at a time. 🌬️",
        "What's worrying you? Talking about it might help.",
    ],
    "angry": [
        "It's okay to feel angry. What happened?",
        "That sounds really frustrating. I'm listening.",
        "Your feelings are valid. Let it out — I'm here.",
    ],
    "default": [
        "I'm here and I'm listening. Tell me more. 💙",
        "That sounds really important. Can you share more?",
        "I hear you. How long have you been feeling this way?",
        "You matter, and so does what you're going through.",
        "Thanks for trusting me with this. I'm not going anywhere.",
    ]
}

keywords = {
    "sad":     ["sad", "cry", "crying", "unhappy", "down", "depressed", "miserable", "upset"],
    "lonely":  ["lonely", "alone", "no one", "nobody", "isolated", "left out"],
    "stressed":["stress", "stressed", "overwhelmed", "pressure", "too much", "can't cope"],
    "tired":   ["tired", "exhausted", "drained", "sleepy", "no energy", "worn out"],
    "happy":   ["happy", "good", "great", "amazing", "wonderful", "excited", "awesome"],
    "anxious": ["anxious", "anxiety", "worried", "nervous", "scared", "fear", "panic"],
    "angry":   ["angry", "mad", "furious", "annoyed", "frustrated", "irritated"],
}

def get_response(user_input):
    text = user_input.lower()
    for mood, words in keywords.items():
        if any(word in text for word in words):
            return random.choice(responses[mood])
    return random.choice(responses["default"])

def main():
    print("\n🌻 Hey! I'm Sunny, your friend bot.")
    print("   Talk to me whenever you feel low. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Sunny: Take care! I'm always here. 🌻\n")
            break
        print(f"Sunny: {get_response(user_input)}\n")

if __name__ == "__main__":
    main()
