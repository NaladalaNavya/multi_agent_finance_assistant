import streamlit as st

def show_allocation_chart(data_dict):
    import matplotlib.pyplot as plt

    labels = list(data_dict.keys())
    sizes = list(data_dict.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
