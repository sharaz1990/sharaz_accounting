from flask import Flask, render_template

app = Flask(__name__)

# Home route for the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route for customers
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Route for nominals
@app.route('/nominals')
def nominals():
    return render_template('nominals.html')

# Route for transactions
@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

# Route for inventory
@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
