import torch
from src.model import model, tokenizer, device
from src.config import LABEL_NAMES, MAX_LENGTH


def predict_news_category(text: str) -> str:
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=MAX_LENGTH,
        return_tensors="pt"
    )

    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()

    return LABEL_NAMES[predicted_class]


if __name__ == "__main__":
    text = "Apple announced new AI features for the upcoming iPhone."
    print("Prediction:", predict_news_category(text))