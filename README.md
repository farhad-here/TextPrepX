# TextPrepX (Multilingual Text Preprocessing)

TextPrepX is a Streamlit-based web application for preprocessing text data in both **English** and **Persian**. It supports common preprocessing steps like lowercasing, removing punctuation and emojis, handling contractions, stemming, spell correction, and more.

# 📄 Description:
This project is an interactive text preprocessing tool built with Streamlit, designed to clean and prepare both English and Persian texts for natural language processing (NLP) tasks.

It supports a wide range of preprocessing options, including:

Lowercasing

Removing punctuation, numbers, and emojis

Expanding contractions

Spell correction using TextBlob (for English) and Parsivar (for Persian)

Stopword removal (customizable for Persian)

Lemmatization and stemming

Tokenization (word and sentence level)

Repetition reduction and slang replacement

Unicode normalization and formatting cleanup

The Persian module leverages the Parsivar library, while the English module utilizes NLTK, TextBlob, and contractions for more nuanced cleaning. Users can either upload .txt files or enter raw text directly. Results are displayed in a styled, readable format.

This toolkit is ideal for data preprocessing in NLP pipelines, educational purposes, and rapid text cleaning for bilingual corpora.
---

## ✨ Features

### ✅ English Text
- Lowercasing
- Removing numbers and punctuation
- Handling contractions (e.g., can't → cannot)
- Removing emojis
- Spell correction using TextBlob
- Stopword removal
- Lemmatization + Stemming
- Reducing repeated characters and slang normalization (e.g., gonna → going to)

### ✅ Persian Text
- Normalization using Parsivar
- Custom stopword removal
- Tokenization (words & sentences)
- Stemming
- Spell correction using Parsivar
- Removing punctuation, numbers, and extra whitespaces

---

## 🚀 How to Run

1. Clone this repository or download the code.
2. Install dependencies:

```bash
pip install -r requirements.txt
```
```bash
streamlit run TEP.py
```
TextPrepX/
├── TEP.py                      # Main Streamlit app
├── persianstopwords.txt        # Custom Persian stopword list
├── models/
│   └── cnn-lstm-probwordnoise/ # (Optional) NeuSpell model folder for advanced spellcheck
├── requirements.txt

# 📌 Notes
Persian spell correction is handled by Parsivar.

For advanced English spell correction (NeuSpell), set up the model separately.

You can enhance further by adding Named Entity Recognition (NER) or keyword extraction.

# 📷 Screenshots
![tt1](https://github.com/user-attachments/assets/507e2c86-f4ce-4df3-bf8b-6812f4012268)
![tt2](https://github.com/user-attachments/assets/25f1eac9-6af0-4897-8634-3c0bc34a6f3e)
![tt3](https://github.com/user-attachments/assets/a4e963bf-bd56-45f6-a0df-a56a099a681b)
![tt4](https://github.com/user-attachments/assets/dafaaa0c-d63b-45ce-986f-aaa89645bceb)
![tt5](https://github.com/user-attachments/assets/11951d21-6ae3-4990-a016-da4af5215de5)

# 🧑‍💻 Author
Created by [Farhad Ghaherdoost] – Feel free to fork and customize.😄










