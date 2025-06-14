

import torch
import torch.nn as nn
import torch.optim as optim

class ModelTrainer:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    def train_step(self, input_ids, target_ids):
        self.model.train()
        self.optimizer.zero_grad()

        output = self.model(input_ids)
        loss = self.criterion(output.view(-1, output.size(-1)), target_ids.view(-1))
        loss.backward()
        self.optimizer.step()

        return loss.item()

    def apply_reward(self, reward):
        # Future idea: use reward as feedback signal (RL-like fine-tuning)
        # For now, placeholder
        pass
