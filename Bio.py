import streamlit as st
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Altinus", layout="wide", initial_sidebar_state="auto")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.subheader("Diogo Ribeiro")

col1, col2 = st.columns([0.3,0.7],vertical_alignment="top")


with col2:
    st.subheader("Adjust reading time if needed:")
    time = st.select_slider(label="",
    options=[
        "~1 min",
        "~2 min",
        "~3 min",
    ],
)
    container_2=st.container()
    if time == "~1 min":
        container_2.write('''I am a Portuguese citizen residing in Türkiye,
                    with a multidisciplinary background that combines engineering,
                    education, and data science. My career began with an engineering
                    foundation, providing me with substantial experience in data analysis
                    and problem-solving. For the past four years, I have taught Mathematics,
                    Chemistry, and Physics in public schools.''')
        container_2.write('''Recently, I completed an intensive Data Science bootcamp at Le Wagon,
                    where I reskilled to align my analytical expertise with modern
                    data-driven technologies. I approach challenges with precision
                    and curiosity, constantly seeking opportunities to learn.''')
        container_2.write('''My unique combination of technical skills, teaching experience,
                    and an innate enthusiasm for tackling complex problems makes
                    me well-suited for roles in Data Science and Data Analytics.''')
    if time == "~2 min":
        container_2.write('''I am a Portuguese citizen residing in Türkiye,
                    with a multidisciplinary background that combines
                    chemical engineering, education, and data science. My career
                    began with a chemical engineering foundation,
                    providing me with substantial experience in data analysis
                    and problem-solving. For the past four years, I have taught
                    Mathematics, Chemistry, and Physics in public schools, where I
                    honed my communication and instructional skills.''')
        container_2.write('''Recently, I completed an intensive Data Science &
                    A.I. bootcamp at Le Wagon, where I reskilled to align my
                    analytical expertise with modern data-driven
                    technologies. This experience deepened my knowledge
                    of data analysis, machine learning, and programming,
                    enhancing my ability to extract insights and drive
                    decision-making through data.''')
        container_2.write('''I love tackling complex challenges with
                    curiosity, always seeking opportunities
                    to grow and learn. My unique blend of technical
                    expertise, teaching experience, and enthusiasm
                    for problem-solving positions me as an ideal candidate
                    for roles in Data Science and Data Analytics.''')
        container_2.write('''I am eager to use my previously acquired
                    skills on a new role. My journey has taught me to embrace change,
                    value lifelong learning, and approach every
                    challenge as an opportunity for growth.
                    I am excited about the prospect of applying
                    these principles where I can continue to evolve while contributing
                    to the success of a forward-thinking organization.''')
    if time == "~3 min":
        container_2.write('''I am a Portuguese citizen residing in Türkiye,
                    with a unique and multidisciplinary background that
                    seamlessly integrates chemical engineering, education,
                    and data science. My professional journey has been
                    shaped by a passion for understanding complex systems and a
                    commitment to continuous learning, both of which have
                    defined my success across these diverse roles.''')
        container_2.write('''I began my career with a solid foundation
                    in engineering, where I gained substantial experience
                    in data analysis, problem-solving, and technical
                    decision-making. These experiences not only
                    strengthened my analytical skills but also taught
                    me the importance of precision and adaptability in
                    dynamic and demanding environments. My chemical engineering
                    background provided the perfect platform for my
                    transition into scientific education, where I applied my
                    technical knowledge and criativity in innovative ways
                    to engage and inspire students.''')
        container_2.write('''Over the past four years, I have taught Mathematics,
                    Chemistry, and Physics in public schools, where I
                    refined my skill to communicate complex concepts
                    effectively. Teaching these subjects
                    required more than just subject-matter expertise;
                    it also demanded patience, enormous responsability, and a knack
                    for simplifying challenging material. This experience
                    allowed me to develop the ability
                    to connect with individuals from diverse
                    backgrounds and learning styles.''')
        container_2.write('''Recently, I embarked on a new chapter of my
                    professional journey by completing an intensive
                    Data Science & A.I. bootcamp at Le Wagon.
                    This transformative experience allowed me to reskill
                    and align my engineering and analytical expertise
                    with data-driven technologies. At Le Wagon,
                    I gained hands-on experience with data analysis,
                    machine learning, Python programming, and data
                    visualization.''')
        container_2.write('''I approach challenges with a combination of
                    curiosity, and a drive to
                    continuously expand my knowledge. Whether
                    designing solutions to complex engineering
                    problems, teaching intricate scientific concepts,
                    or extracting insights from data, I am motivated by
                    the opportunity to make a meaningful impact.''')


with col1:
    st.image("photos/me.png",caption="Me")
    container_1=st.container()
    with container_1:
        st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/diogo-ribeiro/")
        st.link_button(label="Instagram", url="https://www.instagram.com/altinus/")
        st.link_button(label="Facebook", url="https://www.facebook.com/diogo.ribeiro.7169709/")
        st.link_button(label="GitHub", url="https://github.com/altinus01")
