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

        #Stemming Docs
        data_stemmed = stemming_doc(data)

        #Stemming query
        query_stemmed = stemming_doc(queryform)

        #Count jumlah kata di .txt
        jumlah_kata = count_word(data)

        #Kemunculan query pada .txt
        nquery_data = count_query_word(data_stemmed, query_stemmed)


        return f"""<h1>Query yang diinput: {query_stemmed}</h1>
        <p>Jumlah kata pada tes.txt adalah {jumlah_kata}</p>
        <p>Jumlah query pada text: {nquery_data}</p>
        <p>Setelah di stemming: {data_stemmed} </p>
        """
        
    else:
        return render_template("index.html")

def stemming_doc(docs):
    import Sastrawi
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

    #Create Stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    #Stemming
    output = stemmer.stem(docs)
    return output

def count_word(docs):
    words = docs.split()
    return len(words)

def count_query_word(docs, queryform):
    #Prekondisi: Docs dan queryform keduanya sudah distemming
    count = 0
    docs = docs.split()
    for word in docs:
        if word==queryform:
            count = count+1
    return count

if __name__ == "__main__":
    app.run(debug=True)