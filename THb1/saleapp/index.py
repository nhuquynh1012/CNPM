from itertools import product

from flask import Flask, render_template,request
import dao
app = Flask(__name__)


@app.route("/")
def index():
    # name = "Phan Nguyen Nhu Quynh"
    categories = dao.load_categories()
    q = request.args.get("q")
    cate_id = request.args.get("product_id")
    products = dao.load_product(q,cate_id)
    return render_template("index.html" , c= categories,products=products)
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)