from flask import Flask, render_template, request, url_for, redirect, jsonify, flash
from fetch_earthquakes import to_json



app = Flask(__name__)

""" pip install -r requirements.txt  """
""" python3 app.py """

app.config["SECRET_KEY"] = "thisisasecretkey"

çeviri_tablosu = str.maketrans("şçöğüıŞÇÖĞÜİ", "scoguiSCOGUI")

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city").upper()
        city = city.translate(çeviri_tablosu)
        if not city:
            flash("Lütfen bir şehir adı giriniz..")
            return redirect(url_for("index"))
        earthquake_list = []
        for earthquake in to_json.values():
            location = " ".join(earthquake["location"])          
            if city in location:
                earthquake_list.append(earthquake)
            
        return jsonify(earthquake_list)

    return render_template("index.html")

@app.route('/api')
def api():
    return to_json

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 