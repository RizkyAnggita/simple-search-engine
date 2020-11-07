# Tubes Algeo 2
from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename
import os, shutil

app = Flask(__name__)
app.secret_key = 'secret key'
path = os.getcwd()
upload_folder = os.path.join(path, 'uploads')

if os.path.exists(upload_folder):   #Kalau folder sudah ada, kosongkan
    shutil.rmtree(upload_folder)
os.makedirs(upload_folder)      #Create new folder


app.config['upload_folder'] = upload_folder

allowed_ext = set(['txt'])      #hanya txt yang boleh diupload

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext

@app.route("/")
def home():
    a = "Rizky Anggita"
    return f"<h1>Hello{a}</h1>"

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method=="POST":
        queryform = request.form["query"]

        #Contoh
        file1 = open("Deretan Kasus Korupsi Rugikan Negara di Atas Rp100 Miliar.txt", "rt")
        data1 = file1.read()
        # panjang = len(words)

        filenames = []
        filenames, files = request_txt()
        
        #Nama file yang diupload di simpan di list filenames
        #mengakses file nya -> "uploads/namafiles.txt"
        count_kata = 0 #sebelum di stemming
        for file in filenames:
            file2 = open("uploads/"+file,"rt")
            data2 = file2.read()
            print(data2)
            count_kata = count_kata + count_word(data2)


        #Stemming Docs dan filtering stopword
        data_stemmed = stemming_doc(data1)
        data_clean = filtering_stopword(data_stemmed)

        #Stemming query dan filtering stopword
        query_stemmed = stemming_doc(queryform)
        query_clean = filtering_stopword(query_stemmed)

        #Count jumlah kata di .txt
        jumlah_kata = count_word(data1)

        #Kemunculan query pada .txt
        nquery_data = count_query_word(data_clean, query_clean)


        return f"""<h1>Query yang diinput: {query_clean}</h1>
        <p>Daftar file yang dimasukkan: {filenames} </p>
        <p>Jumlah kata pada seluruh dokumen yang dimasukkan : {count_kata}</p>
        <p>Jumlah kata pada tes.txt adalah {jumlah_kata}</p>
        <p>Jumlah query pada text: {nquery_data}</p>
        <p>Setelah di stemming: {data_clean} </p>
        """
        
    else:
        return render_template("index.html")


# Nanti yang fungsi" ini dipisah aja di file .py lain, baru di import

def request_txt():
    filenames = []
    files = request.files.getlist('files[]')

    print(files)
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload_folder'],filename))
            filenames.append(filename)

    for file in filenames:
        print(file)
    return filenames,  files

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