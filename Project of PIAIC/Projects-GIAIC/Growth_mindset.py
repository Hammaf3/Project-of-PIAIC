import streamlit as st

st.set_page_config(page_title= "GROWTH MINDSET AI DESIGNED BY AISHA SIDDIQUI",page_icon= "🤖✦")
st.title("WELCOME TO AI GROWTH MINDSET CHALLANGE")

st.header("WELCOME TO GROWTH JOURNEY")
st.write("Embrace Challenges, Learn From Mistakes, And Unlock Your Full Potential. This Is AI-Powered App Helps You Build a Growth Mindset With Reflection, Challenges And Achievments! 🌟")

#QUOTES SECTION

st.header("Today's Growth Mindset Quote 👀")
st.write("Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.")

st.header("What's Your Challenge Today?⚔️")
user_input = st.text_input("Describe a Challenge You're Facing:")


#condition
if user_input:
    st.success(f"yor are facing💪: {user_input}. keep pushing forward toward goals! 🚀" )
else:
    st.warning("Tell Us About Your Challenge to Get Started!")

#refelexing
st.header("🧠 Reflect In Your Learning!")
refelextion =st.text_area("write your outcome here")

if refelextion:
    st.success(f"Great Inside Your Refelextion:{refelextion}")
else:
    st.info("Reflecting On Past Experience Help You Grow! Share Your Difficulties.")


#achievement

st.header("CELEBERATE YOUR ACHIVEMENT")
achivement =st.text_input("Share Something You've Recently Accomplished:💫")

if achivement:
    st.success(f"Amazing  You Are Achived: , {achivement}")
else:
    st.info("Practice And Patience And You Will Achieve Your Goals😎")

#footer
st.write("-  -  -")
st.write("🚀 Keep Believing In Yourself. Growth Is a Journey, Not a Destination! 🌟")
st.write("**✴️CREATED BY AISHA SIDDIQUI**")