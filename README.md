# D2C Customer Churn Prediction – Model & Analysis

## Project Overview
This project builds a churn prediction model to identify customers likely to churn within the next 60 days using historical transaction, behavioral, and support data.

---

## Objective
- Build churn prediction models
- Prevent data leakage using snapshot-based filtering
- Evaluate models with proper metrics
- Perform error analysis
- Provide explainable insights

---

## Dataset
- customers.csv → demographics
- orders.csv → transactions
- support_tickets.csv → customer issues
- web_events_snapshot.csv → engagement
- intervention_history.csv → campaign exposure
- churn_labels.csv → target variable

---

## Key Feature Signals

- Recency (days since last order)
- Frequency (number of orders)
- Monetary (total spend)
- Support tickets & sentiment
- Web engagement (sessions)
- Campaign exposure

---

## Models Used

### Baseline Model
- Logistic Regression

### Final Model
- Random Forest Classifier

---

## Key Findings

- Recency is the strongest churn predictor
- High inactivity customers are most likely to churn
- Negative support sentiment increases churn risk
- Campaign exposure helps reduce churn probability

---

## Files

- churn_model.ipynb
- model.pkl
- metrics.json
- error_analysis.md
- model_card.md
- requirements.txt

---

## Conclusion

The model successfully identifies at-risk customers and enables targeted retention actions.

---

## Author

Capstone Submission – Part 3
``
