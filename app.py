import plotly.graph_objects as go # conda install plotly
import streamlit as st # conda install streamlit

# -------------- SETTINGS --------------
incomes = ["Salary", "Investments", "Other Income"]
expenses = ["Rent", "Utilities", "Food", "Transportation", "Miscellaneous",
            "Phone", "Savings", "Insurance", "Subscriptions"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
