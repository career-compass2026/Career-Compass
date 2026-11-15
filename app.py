
import streamlit as st

st.set_page_config(
    page_title="Career Compass",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 Career Compass")
st.subheader("Discover a career that matches your interests!")

st.write(
    "Welcome! Tell us a little about yourself "
    "and let us help you explore your future."
)

name = st.text_input("What is your name?")

skills_list = [
    "Communication",
    "Creativity",
    "Problem Solving",
    "Leadership",
    "Coding",
    "Drawing",
    "Writing",
    "Teamwork",
    "Analytical Thinking"
]

subjects_list = [
    "Mathematics",
    "Science",
    "Computer Science",
    "English",
    "Biology",
    "Commerce",
    "Economics",
    "Arts"
]

skills = st.multiselect(
    "Select your skills:",
    skills_list
)

subjects = st.multiselect(
    "Select your favourite subjects:",
    subjects_list
)

if st.button("Find My Career 🚀"):

    if not name.strip():
        st.warning("Please enter your name.")

    elif not skills and not subjects:
        st.warning("Please select at least one skill or subject.")

    else:
        st.success(f"Hello {name}! Let's explore your future.")

        careers = []

        if "Coding" in skills or "Computer Science" in subjects:
            careers += [
                "Software Developer",
                "Web Developer",
                "Data Scientist"
            ]

        if "Biology" in subjects or "Science" in subjects:
            careers += [
                "Doctor",
                "Biotechnologist",
                "Research Scientist"
            ]

        if "Mathematics" in subjects or "Analytical Thinking" in skills:
            careers += [
                "Data Analyst",
                "Statistician",
                "Financial Analyst"
            ]

        if "Creativity" in skills or "Drawing" in skills:
            careers += [
                "Graphic Designer",
                "Animator",
                "UI/UX Designer"
            ]

        if "Communication" in skills or "English" in subjects:
            careers += [
                "Journalist",
                "Teacher",
                "Content Writer"
            ]

        if "Commerce" in subjects or "Economics" in subjects:
            careers += [
                "Accountant",
                "Economist",
                "Business Analyst"
            ]

        if "Leadership" in skills or "Teamwork" in skills:
            careers += [
                "Business Manager",
                "Entrepreneur",
                "Project Manager"
            ]

        careers = list(dict.fromkeys(careers))

        if careers:
            st.subheader("🌟 Your Suggested Careers")

            for career in careers:
                st.write("✅ " + career)

            st.info(
                "These are initial suggestions based on your "
                "selected interests. Explore each career before "
                "making a decision."
            )

        else:
            st.info(
                "Try selecting more skills or subjects "
                "to discover career suggestions."
            )

st.divider()

st.caption("Career Compass | Explore your interests. Discover your future.")
