# Error Analysis

## False Positives (Predicted churn but retained)

### Business Risk
- Unnecessary incentives → increased cost

### Examples

1. CUST00002 – Low frequency but recent activity → retained
2. CUST00004 – Moderate spend, limited activity → retained
3. CUST00007 – Temporary inactivity → resumed activity
4. CUST00015 – Seasonal purchasing behavior
5. CUST00021 – Low engagement but stable customer
6. CUST00033 – Moderate activity cluster
7. CUST00045 – Campaign exposure helped retention
8. CUST00052 – Low orders but high satisfaction
9. CUST00061 – One-time buyer returning later
10. CUST00078 – Medium recency but stable

---

## False Negatives (Predicted retained but churned)

### Business Risk
- Lost revenue (critical)

### Examples

1. CUST00001 – High spend but inactive → churned
2. CUST00005 – Good frequency but declining engagement
3. CUST00011 – Sudden inactivity
4. CUST00018 – Negative product experience
5. CUST00029 – High returns
6. CUST00035 – No campaign exposure
7. CUST00048 – Drop in sessions
8. CUST00056 – Silent churn behavior
9. CUST00070 – Weak signals before churn
10. CUST00088 – Gradual disengagement

---

## Key Insights

- False Negatives are more harmful (lost revenue)
- False Positives increase cost but are manageable

---

## Recommendation

Optimize model for higher recall to reduce missed churn cases.
