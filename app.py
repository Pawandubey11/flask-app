from flask import Flask, request

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    try:
        itemName = request.form.get('itemName')
        itemDescription = request.form.get('itemDescription')
        return f"Todo submitted: {itemName} - {itemDescription}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
