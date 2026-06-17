# Model Card – Customer Churn Prediction

## Model Overview
Random Forest model predicting whether a customer will churn in the next 60 days.

---

## Intended Use
- Identify churn-risk customers
- Support marketing and retention campaigns

---

## Data Used
Customer behavior data filtered up to snapshot_date (2025-09-30) to avoid leakage.

---

## Model Type
Random Forest Classifier

---

## Features
- Recency, Frequency, Monetary
- Support tickets & sentiment
- Engagement metrics
- Campaign exposure

---

## Performance

- Accuracy: 0.84
- F1 Score: 0.78
- ROC-AUC: 0.86

---

## Threshold
0.5 used for classification

---

## Limitations

- Does not include external factors (pricing, competition)
- May miss sudden churn behavior
- Works best for customers with historical data

---

## Ethical Considerations

- Avoid over-targeting vulnerable customers
- Ensure fairness across segments

---

## Monitoring

- Track model performance drift
- Re-train periodically
- Monitor campaign outcomes

---

## When Not to Use

- New customers with no history
- Real-time decisions (batch model only)
