# Tubes Algeo 2

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    a = "Rizky Anggita"
    return f"<h1>Hello{a}</h1>"

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method=="POST":
        queryform = request.form["query"]

        #Contoh
        file = open("Deretan Kasus Korupsi Rugikan Negara di Atas Rp100 Miliar.txt", "rt")
        data = file.read()
        # panjang = len(words)

        #Stemming Docs dan filtering stopword
        data_stemmed = stemming_doc(data)
        data_clean = filtering_stopword(data_stemmed)

        #Stemming query dan filtering stopword
        query_stemmed = stemming_doc(queryform)
        query_clean = filtering_stopword(query_stemmed)

        #Count jumlah kata di .txt
        jumlah_kata = count_word(data)

        #Kemunculan query pada .txt
        nquery_data = count_query_word(data_clean, query_clean)


        return f"""<h1>Query yang diinput: {query_clean}</h1>
        <p>Jumlah kata pada tes.txt adalah {jumlah_kata}</p>
        <p>Jumlah query pada text: {nquery_data}</p>
        <p>Setelah di stemming: {data_clean} </p>
        """
        
    else:
        return render_template("index.html")


# Nanti yang fungsi" ini dipisah aja di file .py lain, baru di import

def stemming_doc(docs):
    #Proses Stemming dokumen
    import Sastrawi
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

    #Create Stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    #Stemming
    output = stemmer.stem(docs)
    return output

def filtering_stopword(docs):
    #Membersihkan stopword
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    output = stopword.remove(docs)
    return output

def count_word(docs):
    #Menghitung banyaknya kata pada dokumen awal
    words = docs.split()
    return len(words)

def count_query_word(docs, queryform):
    #Prekondisi: Docs dan queryform keduanya sudah distemming & filter stopword
    count = 0
    docs = docs.split()
    queryform = queryform.split()

    #Menghitung banyaknya kemunculan sebuah query pada docs
    #Nantinya, ngehitungnya satu" per term
    for word in docs:
        if word in queryform:
            count = count+1
    return count

if __name__ == "__main__":
    app.run(debug=True)