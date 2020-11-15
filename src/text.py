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
        data_clean = filtering_stopword(data)
        data_stemmed = stemming_doc(data_clean)
        data_stemmed_clean.append(data_stemmed)
    return data_stemmed_clean

def stemming_filtering_query(query):
    #Stemming query dan filtering stopword
    query_clean = filtering_stopword(query)
    query_stemmed = stemming_doc(query_clean)
    return query_stemmed.split()

def first_sentence(filenames):
     # Mengambil first sentence, ada 2 cara
    # Pertama, asumsi bahwa tiap line hanya satu kalimat
    # Kedua, asumsi bahwa tiap kalimat hanya terdapat satu buah titik, 
    # yaitu titik yg menandakan akhir kalimat (tidak ada titik di tengah kalimat)

    kalimat_pertama = []
    for dokumen in filenames:
        data = open_doc(dokumen)
        #Cara 1
        # data.splitlines())
        # Cara 2
        kalimat_pertama.append(data.split(".", 1)[0])
    return kalimat_pertama