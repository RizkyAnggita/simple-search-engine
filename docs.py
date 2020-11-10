def open_doc(doc):
    #Melakukan open file dan return data yang dibaca
    file = open("uploads/" + doc, "rt")
    data = file.read()
    return data

def count_kata_doc(filenames):
    # Menghitung kata tiap dokumen awal sebelum di stemming
    # F.S. return sebuah list, elemennya banyaknya kata pada dokumen,
    # berurut sesuai inputan
    list_count_kata = []
    for dokumen in filenames:
        data = open_doc(dokumen)
        list_count_kata.append(count_word(data))
    return list_count_kata

def count_word(docs):
    #Menghitung banyaknya kata pada dokumen awal
    words = docs.split()
    return len(words)

def removeDuplicate(term):
    term = term.split()
    unique = []
    for word in term:
        if word not in unique:
            unique.append(word)
    return unique
    
def makeTerm (data_stemmed_clean, query_stemmed_clean):
    term = ""
    for i in range(len(data_stemmed_clean)):
        term = term + " " +  data_stemmed_clean[i]
        
    for i in range(len(query_stemmed_clean)):
        term = term + " " +  query_stemmed_clean[i]
    return term