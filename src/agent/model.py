

import torch
import torch.nn as nn

class SimpleResponseModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim=128, hidden_dim=256):
        super(SimpleResponseModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)
        lstm_out, _ = self.lstm(embedded)
        output = self.fc(lstm_out)
        return output
