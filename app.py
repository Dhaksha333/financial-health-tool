from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Read financial data
    data = pd.read_csv("sample_data.csv")

    total_revenue = data["revenue"].sum()
    total_expenses = data["expenses"].sum()
    total_loan = data["loan"].sum()

    profit = total_revenue - total_expenses

    # Health score
    health_score = 100
    if profit < 0:
        health_score -= 40
    if total_expenses > total_revenue * 0.8:
        health_score -= 30
    if total_loan > total_revenue * 0.5:
        health_score -= 30

    # Credit score
    credit_score = health_score

    # Forecasting (simple)
    forecast_revenue = total_revenue * 1.05
    forecast_profit = forecast_revenue - total_expenses

    # AI-style advice (simple)
    if health_score >= 70:
        advice = "Your business is financially healthy. Focus on growth."
    elif health_score >= 40:
        advice = "Your business is stable but expenses should be reduced."
    else:
        advice = "Your business is at financial risk. Immediate action required."

    return jsonify({
        "total_revenue": int(total_revenue),
        "total_expenses": int(total_expenses),
        "profit": int(profit),
        "health_score": int(health_score),
        "credit_score": int(credit_score),
        "forecast_revenue": int(forecast_revenue),
        "forecast_profit": int(forecast_profit),
        "ai_recommendation": advice
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



