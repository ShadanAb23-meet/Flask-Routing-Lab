from flask import Flask,  render_template


app = Flask(  
    __name__)

# Your code should be below
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product')
def home():
    return render_template("product.html")

@app.route('/cart')
def home():
    return render_template("cart.html")


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
