from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Read CSV file
    data = pd.read_csv("sample_data.csv")

    # Calculate totals
    total_revenue = data["revenue"].sum()
    total_expenses = data["expenses"].sum()
    total_loan = data["loan"].sum()

    profit = total_revenue - total_expenses

    # Health score logic
    health_score = 100

    if profit < 0:
        health_score -= 40
    if total_expenses > total_revenue * 0.8:
        health_score -= 30
    if total_loan > total_revenue * 0.5:
        health_score -= 30

    # Advice
    if health_score >= 70:
        advice = "Your business is financially healthy. Keep it up!"
    elif health_score >= 40:
        advice = "Your business is okay but expenses should be controlled."
    else:
        advice = "Your business is at financial risk. Reduce expenses and manage loans."

    return jsonify({
        "total_revenue": int(total_revenue),
        "total_expenses": int(total_expenses),
        "profit": int(profit),
        "health_score": int(health_score),
        "advice": advice
    })

if __name__ == "__main__":
    app.run(debug=True)
