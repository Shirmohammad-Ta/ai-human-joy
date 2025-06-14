

def sentiment_to_reward(sentiment_score, scale=1.0):
    """
    Convert a sentiment score to a reward usable in reinforcement learning.
    For example:
        -1 → -1 * scale
         0 →  0
        +1 → +1 * scale
    """
    reward = sentiment_score * scale
    return reward
