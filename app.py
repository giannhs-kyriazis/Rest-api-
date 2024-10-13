from flask import Flask, request, jsonify

app = Flask(__name__)

stocklist = [
    {"Stock_1": "AAPL", "date": "2024-06-03", "closing_price": 194.03, "prediction": 192.84},
    {"Stock_2": "MSFT", "date": "2024-06-03", "closing_price": 413.52, "prediction": 427.18},
   ]


@app.get("/stocklist")
def get_stocklist():
    return jsonify(stocklist)

@app.post("/stocklist")
def add_stocklist():
  if request.is_json:  
    new_stock = request.get_json()  
    stocklist.append(new_stock)
    return new_stock, 201
  return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
