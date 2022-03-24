# Installation Set-up:
from cltk import NLP
#from cltk.tokenize.sentence import TokenizeSentence 
import os
from unicodedata import normalize
import nltk
#nltk.download('punkt')
from nltk.corpus import reuters
from nltk import sent_tokenize
from nltk.tokenize import *
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import bigrams

def analitzar (txt):
    #txt = "Aspiciebam in visu noctis et ecce: viri tres diverso tramite venientes coram me astiterunt, quos ego statim iuxta visionis modum, cuius sint professionis vel cur ad me venerint, interrogo."
    txt = "Aspiciebam in visu noctis et ecce: viri tres diverso tramite"
    #manual_tok = word_tokenize(txt)
    #print(manual_tok[0:5])

    #tokenizer = TokenizeSentence('latin')
    #sentence_tokens = tokenizer.tokenize_sentences(txt)
    cltk_nlp = NLP(language="lat")
    #print("estic entrant a l'analisi")
    cltk_doc = cltk_nlp.analyze(txt)
    #print("estic be :D")
    print (cltk_doc)
    #cltk_tokens = (txt)
    #....
    #print(txt)
    #print (cltk_tokens)

def buscar_textos(path, all_files):
    for it in all_files:
        path_aux = path + "/" + it 
        if ".txt" in it:
            text = llegir(path_aux)
            print(path_aux)
            analitzar(text)
        else:
            all_files_aux = os.listdir(path_aux)
            buscar_textos(path_aux,all_files_aux)
    

def llegir (path):
    
    with open(path, 'r', encoding='utf-8') as f: 
        test_1 = f.read()
        return test_1 


#main 
path = "../cltk_data"
#path = "../cltk_data/lat/text/lat_text_latin_library"
all_files = os.listdir(path)
#recorre sequencialment tots els documents
buscar_textos(path, all_files)
#print(all_files)

