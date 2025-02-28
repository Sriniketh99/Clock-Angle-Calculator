import streamlit as st
import re

# Function to find hour and minutes from input string
def parse_time(s):
    match = re.match(r"^(\d{1,2}):(\d{1,2})$", s)
    if not match:
        return None, None
    
    h, m = int(match.group(1)), int(match.group(2))
    return h, m

# Function to calculate angle
def calculate_angle(hour, minute):
    if not (0 <= hour < 24 and 0 <= minute < 60):
        return None

    # Convert 24-hour format to 12-hour format
    hour = hour % 12

    hr_angle = (hour * 30) + (minute * 0.5)
    min_angle = minute * 6

    # Find the smaller angle
    angle = abs(hr_angle - min_angle)
    return min(angle, 360 - angle)

# Streamlit UI
st.title("⏰ Clock Angle Calculator")
st.write("Enter a time in **HH:MM** format to calculate the angle between the hour and minute hands.")

# User input box
user_input = st.text_input("Enter time (HH:MM)", placeholder="E.g. 03:15")

# Button to calculate
if st.button("Calculate Angle"):
    hour, minute = parse_time(user_input)
    
    if hour is None or minute is None:
        st.error("❌ Invalid format! Please enter time as HH:MM.")
    else:
        angle = calculate_angle(hour, minute)
        if angle is not None:
            st.success(f"✅ The angle between the hands is **{angle:.2f}°**.")
        else:
            st.error("❌ Invalid time input.")

