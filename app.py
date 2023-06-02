import calendar # core python module 
from datetime import datetime # core python module

import plotly.graph_objects as go # conda install plotly
import streamlit as st # conda install streamlit

# -------------- SETTINGS --------------
incomes = ["Salary", "Investments", "Other Income"]
expenses = ["Rent", "Utilities", "Food", "Transportation", "Insurance",
            "Phone", "Subscriptions", "Savings", "Miscellaneous"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

# --- INPUT & SAVE PERIODS ---
st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key="month")
    col2.selectbox("Select Year:", years, key="year")
           
    "---"
    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
    with st.expander("Expenses"):
        for expense in expenses: 
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment here ...")
    
    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.success("Data Saved!")

# --- PLOT PERIODS ---
st.header("Data Visualization")
with st.form("saved_periods"):
    period = st.selectbox("Select Period:", ["June_2023"])
    submitted = st.form_submit_button("Plot Period")
    if submitted:
        comment = "Comment"
        incomes = {'Salary': 3000, 'Investments': 400, 'Other Income': 600}
        expenses = {'Rent': 1500, 'Utilities': 40, 'Food': 200, 'Transportation': 60, 'Insurance': 300,
                    'Phone': 25, 'Subscriptions': 125, 'Savings': 1000, 'Miscellaneous': 750}

        # Create metrics
        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        remaining_budget = total_income - total_expense
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"{total_income}{currency}")
        col2.metric("Total Expense", f"{total_expense}{currency}")
        col3.metric("Remaining Budget", f"{remaining_budget}{currency}")
        st.text(f"Comment: {comment}")

        # Create sankey chart
        label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
        source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
        target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
        value = list(incomes.values()) + list(expenses.values())

        # Data to dict, dict to sankey
        link = dict(source=source, target=target, value=value)
        node = dict(label=label, pad=20, thickness=30, color="#E694FF")
        data = go.Sankey(link=link, node=node)
