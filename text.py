import Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from docs import open_doc 

def stemming_doc(docs):
    #Proses Stemming dokumen

    #Create Stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    #Stemming
    output = stemmer.stem(docs)
    return output

def filtering_stopword(docs):
    #Membersihkan stopword
    

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    output = stopword.remove(docs)
    return output

def stemming_filtering_doc(filenames):
    #Stemming dokumen dan filtering stopword
    data_stemmed_clean = []
    for dokumen in filenames:
        data = open_doc(dokumen)
        data_stemmed = stemming_doc(data)
        data_clean = filtering_stopword(data_stemmed)
        data_stemmed_clean.append(data_clean)
    return data_stemmed_clean

def stemming_filtering_query(query):
    #Stemming query dan filtering stopword
    query_stemmed = stemming_doc(query)
    query_clean = filtering_stopword(query_stemmed)
    return query_clean.split()