# Tubes Algeo 2
from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename
from collections import Counter
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

@app.route("/test")
def test():
    filenames = ['dokumen 1','dokumen 2','dokumen 3']
    return render_template("search.html", filename = filenames, lendata = len(filenames))

@app.route("/view/<filename>")
def show(filename):
    
    data = open_doc(filename)
    return f"""
    <h2>{filename} </h2>
    <p> {data} </p> 
    """

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method=="POST":
        queryform = request.form["query"]
        if os.path.exists(upload_folder):   #Kalau folder sudah ada, kosongkan
            shutil.rmtree(upload_folder)
        os.makedirs(upload_folder)      #Create new folder

        #Upload multiple files txt
        filenames = []
        filenames= request_txt()
        
        #Nama file yang diupload di simpan di list filenames
        #mengakses file nya -> "uploads/namafiles.txt"
        array_count_kata = count_kata_doc(filenames)

        #Stemming Docs dan filtering stopword
        data_stemmed_clean = stemming_filtering_doc(filenames)

        #Stemming query dan filtering stopword
        query_stemmed_clean = stemming_filtering_query(queryform)

        # Kondisi di sini, sudah terbentuk sebuah array data_stemmed_clean
        # data_stemmed_clean berisi SELURUH kata pada tiap dokumen,
        # Elemen ke-i berisi dokumen ke-i dari file yang di upload
        # Langkah selanjutnya

        #Membuat sebuah array term (gabungan seluruh kata dari dokumen + query)
        #  caranya adalah dengan menggabung seluruh elemen pada data_stemmed_clean,
        #  kemudian split(), kemudian hapus elemen yang berulang/ganda
        # Terbentuk sebuah array Term dengan tiap elemen ADALAH SEBUAH KATA

        # Hitung kemunculan tiap term(KATA) pada tiap dokumen (yaitu pada setiap data_stemmed_clean[i]),
        # kemudian masukkan jumlah kemunculan term pada sebuah array baru, yaitu array Di (D1,D2,...Dn)


        # Hitung kemunculan tiap term(KATA) pada query
        # kemudian masukkan jumlah kemumculan term pada sebuah array baru, yaitu array query

        #Terbentuk 16 buah array baru, array Term dan array D1,D2,...Dn

        #Membentuk Term
        term = ""
        for i in range(len(data_stemmed_clean)):
            term = term + " " +  data_stemmed_clean[i]
        
        for i in range(len(query_stemmed_clean)):
            term = term + " " +  str(query_stemmed_clean[i])

        print(term)

        nonDuplicate = removeDuplicate(term)
        
        return f"""<h1>Query yang diinput: {query_stemmed_clean}</h1>
        <p>Sebelum diremove double: {term}</p>
        <p>Sesudah diremove double: {nonDuplicate}</p>        
        <p>Daftar file yang dimasukkan: {filenames} </p>
        <p>Banyaknya kata tiap dokumen: {array_count_kata}</p>
        <p>Dokumen yang telah distemming dan filtering stopword: {data_stemmed_clean} </p>
        <p></p>
        <p>Jumlah query: {len(query_stemmed_clean)}</p>
        """

        #kalau mau pake search.html, uncomment
        # return render_template("search.html", txt= filenames, lendata=len(filenames), NKata= array_count_kata)
        
    else:
        return render_template("index.html")


# Nanti yang fungsi" ini dipisah aja di file .py lain, baru di import

def sort(arrayHasil, arrayDokumen, array_count_kata):     #arrayDokumen = filenames
    n = len(arrayHasil)
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arrayHasil[j] > arrayHasil[j+1] : 
                arrayHasil[j], arrayHasil[j+1] = arrayHasil[j+1], arrayHasil[j]
                arrayDokumen[j], arrayDokumen[j+1] = arrayDokumen[j+1], arrayDokumen[j]
                array_count_kata[j], array_count_kata[j+1] = array_count_kata[j+1], array_count_kata[j]
    return arrayHasil, arrayDokumen, array_count_kata

def removeDuplicate(term):
    term = term.split()
    unique = []
    for word in term:
        if word not in unique:
            unique.append(word)
    return unique

def request_txt():
    #Melakukan request upload multiple files txt
    filenames = []
    files = request.files.getlist('files[]')

    print(files)
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload_folder'],filename))
            filenames.append(filename)
    return filenames

def count_kata_doc(filenames):
    # Menghitung kata tiap dokumen awal sebelum di stemming
    # F.S. return sebuah list, elemennya banyaknya kata pada dokumen,
    # berurut sesuai inputan
    list_count_kata = []
    for dokumen in filenames:
        data = open_doc(dokumen)
        list_count_kata.append(count_word(data))
    return list_count_kata

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

def open_doc(doc):
    #Melakukan open file dan return data yang dibaca
    file = open("uploads/" + doc, "rt")
    data = file.read()
    return data

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