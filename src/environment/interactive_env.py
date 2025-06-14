

from src.feedback.sentiment import analyze_sentiment
from src.feedback.reward_converter import sentiment_to_reward

class InteractiveEnvironment:
    def __init__(self):
        self.history = []  # To store interaction history

    def get_user_input(self):
        user_text = input("👤 You: ")
        return user_text

    def generate_response(self, user_text):
        """
        Currently returns a simple response. Will be integrated with a model later.
        """
        return "🤖 AI: I'm learning to make you happier! 🌟"

    def compute_reward(self, user_feedback_text):
        sentiment_score = analyze_sentiment(user_feedback_text)
        reward = sentiment_to_reward(sentiment_score)
        return reward, sentiment_score

    def run_once(self):
        user_input = self.get_user_input()
        ai_response = self.generate_response(user_input)
        print(ai_response)

        feedback = input("💬 Feedback on AI response (e.g., 'It was great', 'It was weak'): ")
        reward, sentiment_score = self.compute_reward(feedback)

        print(f"🎯 Sentiment: {sentiment_score:.2f} → Reward: {reward:.2f}")

        self.history.append({
            "input": user_input,
            "response": ai_response,
            "feedback": feedback,
            "sentiment": sentiment_score,
            "reward": reward
        })

    def run_loop(self, rounds=5):
        print("🎉 Welcome to AI-Human-Joy Interactive Mode!")
        for _ in range(rounds):
            self.run_once()
        print("📝 Session complete. Thank you for your feedback!")
