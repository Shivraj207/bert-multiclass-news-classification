# 🧠 BERT-Based Multi-Class News Classification

## 📌 Project Overview

This project focuses on classifying news articles into four categories:

- 🌍 World  
- ⚽ Sports  
- 💼 Business  
- 🧪 Sci/Tech  

A pre-trained **BERT (bert-base-uncased)** model is fine-tuned on the **AG News dataset** to perform multi-class classification.

---

## 🚀 Motivation

Traditional models struggle with understanding context in text data.  
This project leverages **Transformer-based architecture (BERT)** to capture semantic meaning and improve classification performance.

---

## 🏗️ Project Structure
bert-multiclass-news-classification/
│
├── notebooks/
│ └── 01_bert_ag_news_experiment.ipynb
│
├── src/
│ ├── config.py
│ ├── model.py
│ ├── predict.py
│
├── saved_model/
│ └── bert_ag_news/
│
├── outputs/
│ └── plots/
│
├── main.py
├── requirements.txt
└── README.md

---

## ⚙️ Tech Stack

- Python  
- PyTorch  
- Hugging Face Transformers  
- Scikit-learn  
- Matplotlib / Seaborn  

---

## 🧠 Model Details

- Model: `bert-base-uncased`
- Task: Multi-class classification
- Number of classes: 4
- Loss Function: CrossEntropyLoss
- Optimizer: AdamW
- Max sequence length: 128

---

## 📊 Results

- **Accuracy:** ~92%
- **F1 Score (Macro Avg):** ~0.92

### 🔍 Key Observations

- The model performs well overall but shows confusion between:
  - **World ↔ Sci/Tech**
  - **Sports ↔ Sci/Tech**

### 📉 Reason for Errors

This is due to **semantic overlap** between categories.  
For example:
- Technology-related policy news → World vs Sci/Tech  
- Sports analytics or tech usage → Sports vs Sci/Tech  


---

## 🧪 Sample Predictions

| Input Text | Predicted Category |
|----------|------------------|
| Apple announces new AI features | Sci/Tech |
| India defeated Australia in cricket match | Sports |
| Stock markets surged after earnings | Business |

---
## 📊 Confusion Matrix

![Confusion Matrix][def]

## ▶️ How to Run

### 1. Clone repository
git clone <your-repo-link>
cd bert-multiclass-news-classification


### 2. Install dependencies
pip install -r requirements.txt


### 3. Run prediction
python main.py


---

## 💡 Future Improvements

- Train on larger dataset / more epochs  
- Compare with baseline models (Logistic Regression, LSTM)  
- Deploy using Streamlit or FastAPI  
- Use DistilBERT for faster inference  

---

## 🎯 Key Learnings

- Hands-on experience with Transformer models  
- Understanding tokenization (input_ids, attention_mask)  
- Fine-tuning pre-trained models  
- Evaluating classification models beyond accuracy  

---

## 📌 Conclusion

This project demonstrates how **pre-trained language models like BERT significantly improve text classification tasks**, while also highlighting challenges in handling semantically overlapping categories.



#Confusion Matrix Image
[def]: outputs/plots/confusion_matrix.png