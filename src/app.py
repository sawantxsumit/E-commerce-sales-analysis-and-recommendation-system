import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Sales & Recs", page_icon="🛒", layout="wide")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")

@st.cache_data
def load_csv(filename):
    file_path = os.path.join(DATA_DIR, filename)
    return pd.read_csv(file_path)

# Load your processed data
customer_data = load_csv("customer_data_cleaned.csv")
df = load_csv("ecommerce_data_clean.csv")
merged_data = load_csv("merged_data.csv")
top_products = load_csv("top_products_per_cluster.csv")

st.title("📊 Sales Analysis & Recommendation System")

# Sidebar for user inputs
st.sidebar.header("Customer Input")
customer_id = st.sidebar.text_input("Enter Customer ID:")
st.sidebar.text("Try customer id :\n 12350 , 14346 , 18150 ,16293 ,18280")


def recommend_products(customer_id, merged_df, top_products_df, n=5):
    # Step 1: Find customer cluster
    try:
        cluster = merged_df.loc[merged_df["customerid"] == customer_id, "cluster_y"].values[0]
    except IndexError:
        return [f"CustomerID {customer_id} not found in dataset."]
    
    # Step 2: Get top products of that cluster
    cluster_products = top_products_df[top_products_df["cluster"] == cluster]["description"].tolist()
    
    # Step 3: Get products already purchased by customer
    purchased = merged_df[merged_df["customerid"] == customer_id]["description"].unique().tolist()
    
    # Step 4: Filter out purchased products
    recommendations = [p for p in cluster_products if p not in purchased]
    
    # Return top N
    return recommendations[:n]

if customer_id:
    customer_id = int(customer_id)  # Convert to int if needed
    
    # Customer summary
    customer_summary = customer_data.loc[customer_data['customerid'] == customer_id, [
        'customerid','cluster','Days_Since_Last_Purchase',
        'total_spend','Favorite_Shopping_Day','Favorite_Shopping_Hour'
    ]].drop_duplicates()

    st.write("### Customer Summary")
    st.dataframe(customer_summary)

    # Purchased products
    customer_products = (
        df.loc[df['customerid'] == customer_id,
                        ['stockcode','description','quantity']]
        .groupby(['stockcode','description'])
        .sum()
        .reset_index()
        .sort_values(by='quantity', ascending=False)
    )

    st.write("### Products Purchased by Customer")
    st.dataframe(customer_products.head(10))
    
    recs= recommend_products(customer_id, merged_data, top_products, n=5)
    
    st.subheader("Product Recommendations for Customer ID: {}".format(customer_id))
    if recs:
        for product in recs:
            st.success(product)
    else:
        st.warning("No recommendations available for this customer.")
    
else:
    st.write("Enter a valid customer ID to see details.")




# Cluster information
clusters = {
    "Cluster 0": {
        "Profile": "Sporadic Shoppers with a Preference for Weekend Shopping",
        "Insights": [
            "Tend to spend less, with fewer transactions and products purchased.",
            "Slight tendency to shop during weekends.",
            "Low monthly spending variation.",
            "Low cancellation frequency and rate.",
            "Lower average transaction value."
        ]
    },
    "Cluster 1": {
        "Profile": "Infrequent Big Spenders with a High Spending Trend",
        "Insights": [
            "Moderate spending but infrequent transactions.",
            "High spending trend that has been increasing.",
            "Prefer shopping late in the day, mostly in the UK.",
            "Medium cancellation rate.",
            "High average transaction value."
        ]
    },
    "Cluster 2": {
        "Profile": "Frequent High-Spenders with a High Rate of Cancellations",
        "Insights": [
            "High total spend with many unique products.",
            "Frequent transactions with high cancellation rate.",
            "Tend to shop early in the day.",
            "Spending patterns vary significantly month-to-month.",
            "Despite high spending, trend may be declining."
        ]
    }
}

st.title("Customer Segmentation Explorer")

# Dropdown to select cluster
selected_cluster = st.selectbox("Select a cluster to explore:", list(clusters.keys()))

# Display cluster profile
st.subheader(f"🧑‍🤝‍🧑 {selected_cluster}")
st.write(f"**Profile:** {clusters[selected_cluster]['Profile']}")

# Display insights
st.markdown("### Key Insights")
for point in clusters[selected_cluster]['Insights']:
    st.markdown(f"- {point}")
    
# Global insights
st.subheader("Top Products by Cluster")
# (Use the top_10_products_per_cluster DataFrame you built)

select_cluster= st.selectbox("Select a cluster to view top products:", top_products['cluster'].unique())

# st.dataframe(top_products)
st.subheader(f"Cluster {select_cluster}")

if select_cluster==0:
    cluster0 = top_products.loc[top_products['cluster'] == 0].head(10)
    st.dataframe(cluster0, use_container_width=True)
elif select_cluster==1:
    cluster1 = top_products.loc[top_products['cluster'] == 1].head(10)
    st.dataframe(cluster1, use_container_width=True)
else:
    cluster2 = top_products.loc[top_products['cluster'] == 2].head(10)
    st.dataframe(cluster2, use_container_width=True)
