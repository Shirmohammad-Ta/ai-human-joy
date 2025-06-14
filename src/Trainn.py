

import torch
from torch.utils.data import DataLoader, Dataset
from src.agent.model import SimpleResponseModel
from src.agent.optimizer import ModelTrainer


class SimpleTextDataset(Dataset):
    def __init__(self, data, vocab):
        self.data = data
        self.vocab = vocab
        self.word2idx = {w: i for i, w in enumerate(vocab)}

    def __len__(self):
        return len(self.data)

    def encode(self, sentence):
        return [self.word2idx.get(w, 0) for w in sentence.split()]

    def __getitem__(self, idx):
        text = self.data[idx]
        input_ids = torch.tensor(self.encode(text[:-1]), dtype=torch.long)
        target_ids = torch.tensor(self.encode(text[1:]), dtype=torch.long)
        return input_ids, target_ids

def train():

    sentences = [
        "hi how are you",
        "i am learning",
        "this is fun",
        "let us optimize happiness"
    ]


    vocab = list(set(" ".join(sentences).split()))

    dataset = SimpleTextDataset(sentences, vocab)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

    model = SimpleResponseModel(vocab_size=len(vocab))
    trainer = ModelTrainer(model)

    epochs = 5
    for epoch in range(epochs):
        total_loss = 0
        for input_ids, target_ids in dataloader:
            loss = trainer.train_step(input_ids, target_ids)
            total_loss += loss
        print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss/len(dataloader):.4f}")

if __name__ == "__main__":
    train()
