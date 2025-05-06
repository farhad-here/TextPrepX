#libraries
import re
import contractions
import emoji
import textblob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import streamlit as st
from cleantext import clean
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
import nltk

#oop text preprocessing
class CleanText:
       def __init__(self,text):
              self.text = text
       # Lower case the text
       def lowerText(self):
              self.text = self.text.lower()
              return self.text
       # remove the numbers
       def rmNum(self):
              self.text = re.sub(r'\d+','',self.text)
              return self.text
       # remove punctuatuion(?! and etc)
       def rmPunc(self):
              self.text = re.sub(r'[^\w\s]', '',self.text)
              return self.text
       # remove contractions(can't,cannot)
       def rmContract(self):
              self.text = contractions.fix(self.text)
              return self.text
       # remove emoji
       def rmEmoji(self):
              self.text = emoji.demojize(self.text)
              return self.text
       # checking Spell
       def spllcktextblob(self):
              self.text = textblob.TextBlob(self.text)
              self.text = self.text.correct()
              return self.text
       
      
       # remove stopwords(and is the)
       def stopWord(self):
              stp_wrd = stopwords.words('english')
              sp_txt = self.text.split(' ')
              text = [w for w in sp_txt if w not in stp_wrd]
              return " ".join(text)
       #Stem and lem(running->run)
       def get_wordnet_pos(self, treebank_tag):
              if treebank_tag.startswith('J'):
                     return wordnet.ADJ
              elif treebank_tag.startswith('V'):
                     return wordnet.VERB
              elif treebank_tag.startswith('N'):
                     return wordnet.NOUN
              elif treebank_tag.startswith('R'):
                     return wordnet.ADV
              else:
                     return wordnet.NOUN
       
       

       def lemStem(self):
                     
                     lemmatizer = WordNetLemmatizer()
                     tokens = word_tokenize(self.text)
                     tagged = pos_tag(tokens)
                     lemmatized = [lemmatizer.lemmatize(w, self.get_wordnet_pos(pos)) for w, pos in tagged]
                     self.text = " ".join(lemmatized)
                     return self.text
       # reduce character and spell

       def reduceRepeatChar(self):
              slng = {
              "neva": "never",
              "wanna": "want to",
              "r": "are",
              "gonna": "going to",
              "ya": "you",
              "imma": "I'm going to",
              "cuz": "because",
              "doin'": "doing",
              "gotta": "got to",
              "shoulda": "should have",
              "coulda": "could have",
              "woulda": "would have",
              "whatcha": "what are you",
              "y'all": "you all",
              "lol": "laugh out loud",
              "brb": "be right back",
              "btw": "by the way",
              "omg": "oh my god",
              "ttyl": "talk to you later",
              "tbh": "to be honest",
              "idk": "I don't know",
              "smh": "shaking my head"
              }
              xx = self.text.split(" ")
              print(xx)
              for i in self.text.split():
                     if i in slng.keys():
                            xx[xx.index(i)] = slng[i]    
              self.text = ' '.join(xx)
              return re.sub(r'(.)\1{2,}', r'\1', self.text)


       def result(self):
              if lower_case:
                     self.text = self.lowerText()
              if remove_number:
                     self.text = self.rmNum()
              if remove_punctuatuion:
                     self.text = self.rmPunc()
              if remove_contractions:
                     self.text = self.rmContract()
              if remove_emoji:
                     self.text = self.rmEmoji()
              if chk_spl:
                     self.text = self.spllcktextblob()
              if remove_stopwords:
                     self.text = self.stopWord()
              if Stemming:
                     self.text = self.lemStem()
              if reduce_repeat:
                     self.text = self.reduceRepeatChar()

            
              return self.text

#nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
"""# text pre-processing"""
st.warning("#### Just for English")
c_1,c_2 = st.columns(2)

upload = c_1.checkbox('upload txt',key="upload")
enter_text = c_2.checkbox('Type')
if enter_text:
       #type
       inp = st.chat_input('text here')
       st.write(inp)

   

       cleaned = clean(inp,
              fix_unicode= True,
              to_ascii=True,
              lower= True,
              normalize_whitespace= True,
              no_line_breaks= True,
              strip_lines= True,
              keep_two_line_breaks= True,
              no_urls= True,
              no_emails= True,
              no_phone_numbers= True,
              no_numbers= True,
              no_digits= True,
              no_currency_symbols= True,
              no_punct= True,
              no_emoji= True,
              lang='en'
       )
       cleaned = CleanText(cleaned).reduceRepeatChar()
       html_code = f"""
                            <div  style="
                            background-color: #3b2f2f;
                            padding: 16px;
                            border-radius: 10px;
                            border: 1px solid #a67c52;
                            color: #ffd580;
                            font-family: 'monospace', sans-serif;
                            font-size: 24px;
                            line-height: 1.8;
                            ">
                            {cleaned}  
                            """
       st.markdown(html_code, unsafe_allow_html=True)

              
if upload:
       #upload
       inp_2 = st.file_uploader('Drop txt file here',type=["txt"])
       if inp_2:
              show_text = st.checkbox("show the text",key="shw upload txt")
              text = inp_2.read().decode("utf-8")
              if show_text:

                     html_code = f"""
                            <div  style="
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
                            """
                     st.markdown(html_code, unsafe_allow_html=True)
    
              '''# options for text preprocessing'''
              lo,rn = st.columns(2)
              rp,rc = st.columns(2)
              remj,chspll = st.columns(2)
              rs,rl,splck = st.columns(3)
              lower_case = lo.checkbox('lowercase the text',key='lower option')
              remove_number = rn.checkbox('remove number',key='remove number option')
              remove_punctuatuion = rp.checkbox('remove punctuatuion',key='remove punctuatuion option')
              remove_contractions = rc.checkbox('remove contractions',key='remove contractions option')
              remove_emoji = remj.checkbox('remove emoji',key='remove emoji option')
              chk_spl=chspll.checkbox('checkspell (weaker)',key='checkspell option')
              remove_stopwords =rs.checkbox('remove stopwords',key='remove stopwords option')
              Stemming = rl.checkbox('Stemming',key='Stemming option')
              reduce_repeat = splck.checkbox('reduce repetition', key='reduce_repeat_option')

              # spellpy = splck.checkbox('spllpy',key='spllcksymspellpy option')
              text_cln = CleanText(text)

              button_show_cleaned_text = st.button('show text')
              if button_show_cleaned_text:
                     html_code = f"""
                            <div  style="
                            background-color: #3b2f2f;
                            padding: 16px;
                            border-radius: 10px;
                            border: 1px solid #a67c52;
                            color: #ffd580;
                            font-family: 'monospace', sans-serif;
                            font-size: 24px;
                            line-height: 1.8;
                            ">
                            {text_cln.result()}  
                            """
                     st.markdown(html_code, unsafe_allow_html=True)
