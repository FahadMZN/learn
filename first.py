# pyright: reportMissingImports=false
import streamlit as st

st.title("حاسبة مؤشر كتلة الجسم (BMI)")

weight = st.number_input("أدخل الوزن (كجم):", min_value=1.0, value=70.0)
height = st.number_input("أدخل الطول (سم):", min_value=1.0, value=170.0)

if st.button("احسب الـ BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"مؤشر كتلة الجسم الخاص بك: **{bmi:.2f}**")
    
    if bmi >= 25:
        st.warning("Above normal weight")
    elif bmi >= 18.5:
        st.success("Normal weight")
    else:
        st.info("Below normal weight")