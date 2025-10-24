import streamlit as s

s.title("Even or Odd Checker")

num = s.number_input("Enter an integer: ")

if s.button("Check"):
    if num % 2 == 0:
        s.success(f"{int(num)} is even")
    else:
        s.warning(f"{int(num)} is odd")