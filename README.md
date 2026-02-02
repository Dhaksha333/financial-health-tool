# Financial Health Assessment Tool for SMEs

## Overview
The Financial Health Assessment Tool is an AI-powered backend application designed for Small and Medium Enterprises (SMEs). It helps business owners quickly assess their financial condition using structured financial data.

The system analyzes revenue, expenses, and loan information to generate key financial metrics and actionable insights.

---

## Features
- Calculates total revenue, total expenses, and profit
- Computes financial health score
- Evaluates basic credit score
- Performs simple financial forecasting
- Provides AI-style business recommendations
- Publicly accessible deployed web service

---

## Technology Stack
- **Backend:** Python, Flask  
- **Data Processing:** Pandas  
- **Deployment:** Render  
- **Input Format:** CSV  

---

## Input Data
The application accepts a CSV file containing financial information such as:
- Revenue
- Expenses
- Loan / credit values

---

## Output
The API returns a JSON response that includes:
- Total Revenue
- Total Expenses
- Profit
- Financial Health Score
- Credit Score
- Forecasted Revenue
- Forecasted Profit
- AI Recommendation Summary

---

## How It Works
1. The user uploads a CSV file with financial data.
2. The backend processes the data using Pandas.
3. Key financial metrics are calculated.
4. Health score and credit score are derived.
5. Forecasting and AI-style recommendations are generated.
6. Results are returned as a JSON response via the API.

---

## Use Case
This tool helps SME owners:
- Understand financial performance
- Identify potential financial risks
- Make informed business decisions
- Analyze profitability without advanced financial expertise

---

## Live Demo
Deployed URL:  
https://financial-health-tool-bcm0.onrender.com

---

## GitHub Repository
https://github.com/Dhaksha333/financial-health-tool

---

## Future Enhancements
- Advanced AI-based financial forecasting
- Creditworthiness modeling
- GST and banking API integration
- Frontend dashboard for data visualization
- Multilingual support
- Enhanced security and compliance

