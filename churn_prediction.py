import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

# Optional: Colab upload support
def upload_csv_files():
    try:
        from google.colab import files
        print("📂 Please upload your CSV files")
        uploaded = files.upload()
        print("✅ Upload complete:", list(uploaded.keys()))
    except ImportError:
        print("ℹ️ Not running in Colab, skipping upload prompt")

def main():
    # =====================================
    # STEP 1: UPLOAD DATA (Colab option)
    # =====================================
    upload_csv_files()

    # =====================================
    # STEP 2: LOAD DATA
    # =====================================
    customers = pd.read_csv('customers.csv')
    orders = pd.read_csv('orders.csv')
    tickets = pd.read_csv('support_tickets.csv')
    web = pd.read_csv('web_events_snapshot.csv')
    interventions = pd.read_csv('intervention_history.csv')
    churn = pd.read_csv('churn_labels.csv')
    print("✅ Data loaded successfully")

    # =====================================
    # STEP 3: DATE PROCESSING
    # =====================================
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    tickets['ticket_date'] = pd.to_datetime(tickets['ticket_date'])
    churn['snapshot_date'] = pd.to_datetime(churn['snapshot_date'])

    # =====================================
    # STEP 4: FILTER (NO LEAKAGE)
    # =====================================
    orders = orders.merge(churn[['customer_id','snapshot_date']], on='customer_id')
    orders = orders[orders['order_date'] <= orders['snapshot_date']]

    tickets = tickets.merge(churn[['customer_id','snapshot_date']], on='customer_id')
    tickets = tickets[tickets['ticket_date'] <= tickets['snapshot_date']]

    # =====================================
    # STEP 5: FEATURE ENGINEERING
    # =====================================
    order_agg = orders.groupby('customer_id').agg({
        'order_id': 'count',
        'gross_amount': 'sum'
    }).reset_index()
    order_agg.columns = ['customer_id','frequency','monetary']

    last_order = orders.groupby('customer_id')['order_date'].max().reset_index()
    last_order.columns = ['customer_id','last_order_date']
    last_order = last_order.merge(churn[['customer_id','snapshot_date']])
    last_order['recency'] = (last_order['snapshot_date'] - last_order['last_order_date']).dt.days
    order_agg = order_agg.merge(last_order[['customer_id','recency']], on='customer_id')

    support_agg = tickets.groupby('customer_id').agg({
        'ticket_id': 'count',
        'sentiment_score': 'mean'
    }).reset_index()
    support_agg.columns = ['customer_id','ticket_count','avg_sentiment']

    # =====================================
    # STEP 6: MERGE MODEL DATA
    # =====================================
    df = churn.merge(order_agg, on='customer_id', how='left')
    df = df.merge(support_agg, on='customer_id', how='left')
    df.fillna(0, inplace=True)
    print("✅ Modeling dataset ready:", df.shape)

    # =====================================
    # STEP 7: TRAIN MODEL
    # =====================================
    X = df[['recency','frequency','monetary','ticket_count','avg_sentiment']]
    y = df['churn_next_60d']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)

    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)

    # =====================================
    # STEP 8: EVALUATION
    # =====================================
    y_pred = rf.predict(X_test)
    y_prob = rf.predict_proba(X_test)[:,1]

    print("\n✅ Model Performance:")
    print(classification_report(y_test, y_pred))
    print("ROC AUC:", roc_auc_score(y_test, y_prob))

    # =====================================
    # STEP 9: SAVE MODEL
    # =====================================
    joblib.dump(rf, 'model.pkl')
    print("\n✅ model.pkl saved successfully")

if __name__ == "__main__":
    main()
