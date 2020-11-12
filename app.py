# Tubes Algeo 2
from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename
import os, shutil
import text, docs, similarity

app = Flask(__name__)
app.secret_key = 'secret key'
path = os.getcwd()
upload_folder = os.path.join(path, 'uploads')

if os.path.exists(upload_folder):   #Kalau folder sudah ada, kosongkan
    shutil.rmtree(upload_folder)
os.makedirs(upload_folder)      #Create new folder

app.config['upload_folder'] = upload_folder

allowed_ext = set(['txt'])      #hanya txt yang boleh diupload

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")
def test():
    filenames = ['dokumen 1','dokumen 2','dokumen 3']
    return render_template("search.html", filename = filenames, lendata = len(filenames))

@app.route("/view/<filename>")
def show(filename):
    
    data = docs.open_doc(filename)
    return render_template("view.html", filename = filename, data = data)

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method=="POST":
        queryform = request.form["query"]
        if os.path.exists(upload_folder):   #Kalau folder sudah ada, kosongkan
            shutil.rmtree(upload_folder)
        os.makedirs(upload_folder)      #Create new folder

        #Upload multiple files txt
        filenames = []
        filenames = request_txt()

        #Menghitung jumlah kata pada tiap dokumen awal
        array_count_kata = docs.count_kata_doc(filenames)

        #Stemming Docs, query dan filtering stopword
        data_stemmed_clean = text.stemming_filtering_doc(filenames)
        query_stemmed_clean = text.stemming_filtering_query(queryform)
        query_stemmed_clean.sort()

        #Membentuk Term
        term = docs.makeTerm(data_stemmed_clean, query_stemmed_clean)

        #Melakukan penghitungan kemunculan term pada tiap dokumen dan query
        arrayHasil = similarity.countFoundTerm(term, data_stemmed_clean, query_stemmed_clean, False)
        
        #Menghitung similarity 
        similar = similarity.sim(arrayHasil)

        #Persen kemiripan, pembulatan 3 angka di belakang koma
        simPercentage = [round(similar[i]*100, 3) for i in range (len(similar))]

        #Hanya diambil dari indeks ke-1 s.d. habis, karena indeks ke-0 adalah persentase kemiripan query
        simPercentage = simPercentage[1: ]

        # Term untuk ditampilkan di page
        termTabel = similarity.countFoundTerm(term, data_stemmed_clean, query_stemmed_clean, True)
        queryTabel = termTabel[0]
        termTabel = termTabel[1: ]
        query = docs.removeDuplicate2(query_stemmed_clean)

        # Melalukan sorting dari dokumen dengan tingkat kemiripan paling tinggi
        simPercentage, filenames, array_count_kata, termTabel = similarity.sortHasil(simPercentage, filenames, array_count_kata, termTabel)

        # return f"""<h1>Query yang diinput: {query_stemmed_clean}</h1>
        # <p>Sebelum diremove double: {term}</p>
        # <p>Sesudah diremove double: {nonDuplicate}</p>
        # <p> Array Hasil:   {arrayHasil}</p>
        # <p> Similarity : {similar} </p>
        # <p> Persen Similarity : {simPercentage} </p>      
        # <p>Daftar file yang dimasukkan: {filenames} </p>
        # <p>Banyaknya kata tiap dokumen: {array_count_kata}</p>
        # <p>Dokumen yang telah distemming dan filtering stopword: {data_stemmed_clean} </p>
        # <p></p>
        # <p>Jumlah query: {len(query_stemmed_clean)}</p>
        # """

        #kalau mau pake search.html, uncomment
        return render_template("search.html", txt= filenames, lendata=len(filenames), lenquery=len(query),lentabel = len(termTabel), NKata= array_count_kata, persen = simPercentage, query = queryform, term_tabel = termTabel, temp = queryTabel, querysplit=query)
        
    else:
        return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext

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

if __name__ == "__main__":
    app.run(debug=True)