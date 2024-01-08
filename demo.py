import streamlit as st
st.set_page_config(page_title="Cats")
st.header("types of cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./Persiancat.jpg",caption="Persian Cat", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Ragdoll cat")
  st.image("./Ragdollcat.jpg",caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Rugdoll cats are cute")
