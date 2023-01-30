import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
col1, col2 = st.columns(2)

label = ['', 'Satisfied']
val = [20, 80]
colors = ['white', 'lightgreen']

# append data and assign color
label.append("")
val.append(sum(val))  # 50% blank

# plot
plt.figure(figsize=(8,6),dpi=100)

wedges, labels=plt.pie(val, wedgeprops=dict(width=0.4,edgecolor='w',linewidth=4),labels=label, colors=colors)
# I tried this method
wedges[-1].set_visible(False)
plt.tight_layout()

with col1:
    st.pyplot()



