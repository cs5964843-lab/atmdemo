import streamlit as st

# Page Configuration
st.set_page_config(page_title="Python Quiz App", page_icon="🧠", layout="centered")

st.title("🧠 Python  Quiz")
st.write("Test your knowledge! Answer all 6 questions below and click **Submit Quiz** to see your score.")

# Define 6 questions, their options, and correct answers
questions = [
    {
        "question": "1. Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "2. Which of the following data types is immutable in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    {
        "question": "3. How do you write a single-line comment in Python?",
        "options": ["// This is a comment", "/* This is a comment */", "# This is a comment", "<!-- This is a comment -->"],
        "answer": "# This is a comment"
    },
    {
        "question": "4. Which built-in function is used to find the length of a list or string?",
        "options": ["length()", "size()", "len()", "count()"],
        "answer": "len()"
    },
    {
        "question": "5. What is the correct file extension for Python source files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "question": "6. Which statement is used to handle exceptions in Python?",
        "options": ["try-except", "try-catch", "do-except", "catch-throw"],
        "answer": "try-except"
    }
]

with st.form("quiz_form"):
    user_answers = []
    
    
    for i, q in enumerate(questions):
        st.subheader(q["question"])
        ans = st.radio("Choose an option:", q["options"], key=f"q_{i}", index=None)
        user_answers.append(ans)
        st.markdown("---")
        
    submit_button = st.form_submit_button(label="Submit Quiz")
if submit_button:
    
    if None in user_answers:
        st.warning("⚠️ Please answer all 6 questions before submitting!")
    else:
        score = 0
        for i, q in enumerate(questions):
            if user_answers[i] == q["answer"]:
                score += 1
        
        # Display results
        st.success(f"🎉 Quiz Completed! Your final score is **{score} / 6**")
        
        if score == 6:
            st.balloons()
            st.markdown("### 🏆 Perfect Score! Amazing job!")
        elif score >= 4:
            st.markdown("### 👍 Great job! You know your Python basics well.")
        else:
            st.markdown("### 💪 Good effort! Review some Python concepts and try again.")
            
        with st.expander("View Detailed Answer Key"):
            for i, q in enumerate(questions):
                user_choice = user_answers[i]
                correct_choice = q["answer"]
                status = "✅" if user_choice == correct_choice else "❌"
                st.write(f"**Q{i+1}:** {q['question']}")
                st.write(f"- Your answer: {user_choice} {status}")
                if user_choice != correct_choice:
                    st.write(f"- Correct answer: **{correct_choice}**")