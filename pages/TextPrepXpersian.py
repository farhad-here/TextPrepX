import streamlit as st
import parsivar as pars
import re

class PersianText():
    def __init__(self, text):
        self.text = text

    # Normalization
    def Norm(self):
        normal = pars.Normalizer()
        normalized_text = normal.normalize(self.text)
        return normalized_text

    # Remove stop words
    def stopw(self):
        try:
            # Make sure to upload 'persianstopwords.txt' file
            psw = st.file_uploader('Drag and drop the Persian stopwords file (persianstopwords.txt)')
            if psw is not None:
                STOPWORDS = set(psw.read().decode('utf-8').splitlines())
                words = self.Norm().split()
                filtered = [word for word in words if word not in STOPWORDS]
                self.text = ' '.join(filtered)
            return self.text
        except:
            return "Please upload the stopwords file."

    # Tokenize sentence
    def tokenSen(self):
        self.text = self.stopw()
        tokenizer = pars.Tokenizer()
        tokenized_sent = tokenizer.tokenize_sentences(self.text)
        return tokenized_sent

    # Tokenize word
    def tokenWor(self):
        self.text = self.Norm()
        tokenizer = pars.Tokenizer()
        tokenized_word = tokenizer.tokenize_words(self.text)
        return tokenized_word

    # Stemmer
    def stem(self):
        self.text = self.tokenWor()
        stemmer = pars.FindStems()
        stem_token = [stemmer.convert_to_stem(i) for i in self.text]
        self.text = ' '.join(stem_token)
        return self.text

    # Final cleaning (spell check, punctuation removal, etc.)
    def finalCleaning(self):
        try:
            spell = pars.SpellCheck()
            misspelled = self.stem()
            self.text = spell.spell_corrector(misspelled)
            self.text = re.sub(r'[^\w\s]', '', self.text)  # Remove punctuation
            self.text = re.sub(r'\d+', '', self.text)  # Remove numbers
            self.text = re.sub(r'\s+', ' ', self.text).strip()  # Remove extra spaces
            return self.text
        except Exception as e:
            return f"Error: {str(e)}"

'''---'''
'''# Persian Text Preprocessing'''
st.warning("#### Just for Persian")

'''---'''
# Upload file or write
upload_file = st.file_uploader('Drag file here')
write_file = st.text_input('Write something')
if upload_file:
    text = upload_file.read().decode('utf-8')
elif write_file:
    text = write_file

'''---'''
if upload_file or write_file:
    '''## Text Display'''
    html_code = f"""
                <div dir="rtl" style="
                background-color: #3b2f2f;
                padding: 16px;
                border-radius: 10px;
                border: 1px solid #a67c52;
                color: #ffd580;
                font-family: 'monospace', sans-serif;
                font-size: 24px;
                line-height: 1.8;
                ">
                {text}
                </div>
                """
    st.markdown(html_code, unsafe_allow_html=True)

    '''---'''
    oop = PersianText(text)

    '''## Normalize'''
    html_code = f"""
                <div dir="rtl" style="
                background-color: #3b2f2f;
                padding: 16px;
                border-radius: 10px;
                border: 1px solid #a67c52;
                color: #ffd580;
                font-family: 'monospace', sans-serif;
                font-size: 24px;
                line-height: 1.8;
                color: #ffd580; /* Text color */
                font-size: 18px; /* Font size larger */
                ">
                {oop.Norm()}
                </div>
                """
    st.markdown(html_code, unsafe_allow_html=True)

    '''---'''
    '''## StopWord Removal in Persian'''
    try:
        # Upload stopwords file
        psw = st.file_uploader('Drag persianstopwords.txt here')
        html_code = f"""
                <div dir="rtl" style="
                background-color: #3b2f2f;
                padding: 16px;
                border-radius: 10px;
                border: 1px solid #a67c52;
                color: #ffd580;
                font-family: 'monospace', sans-serif;
                font-size: 24px;
                line-height: 1.8;
                ">
                {oop.stopw()}
                </div>
                """
        st.markdown(html_code, unsafe_allow_html=True)

        '''---'''
        '''# Tokenization - Sentence and Word'''

        '''#### Sentence Tokenization'''
        st.dataframe(oop.tokenSen())

        '''#### Word Tokenization'''
        st.dataframe(oop.tokenWor())

        '''---'''
        '''## Stem'''
        html_code = f"""
                <div dir="rtl" style="
                background-color: #3b2f2f;
                padding: 16px;
                border-radius: 10px;
                border: 1px solid #a67c52;
                color: #ffd580;
                font-family: 'monospace', sans-serif;
                font-size: 24px;
                line-height: 1.8;
                ">
                {oop.stem()}
                </div>
                """
        st.markdown(html_code, unsafe_allow_html=True)

        '''---'''
        '''## Final Cleaning Result'''
        html_code = f"""
                <div dir="rtl" style="
                background-color: #3b2f2f;
                padding: 16px;
                border-radius: 10px;
                border: 1px solid #a67c52;
                color: #ffd580;
                font-family: 'monospace', sans-serif;
                font-size: 24px;
                line-height: 1.8;
                ">
                {oop.finalCleaning()}
                </div>
                """
        st.markdown(html_code, unsafe_allow_html=True)

    except Exception as e:
        st.warning(f'Error: {str(e)}')
