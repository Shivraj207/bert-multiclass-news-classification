from src.predict import predict_news_category

if __name__ == "__main__":
    text = input("Enter news text: ")
    result = predict_news_category(text)
    print("Predicted Category:", result)