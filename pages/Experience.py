import streamlit as st

st.set_page_config(page_title="Edu", layout="wide", initial_sidebar_state="auto")
col7, col8 = st.columns([4,8])

with col7:
    st.image("photos/sugal.png",use_container_width=True,caption="Sugal Azambuja")
    st.link_button(label="Sugal Group", url="https://sugal-group.com/en/")
    st.image("photos/esa.png",use_container_width=True,caption="High School in Azambuja")
    st.link_button(label="Azambuja School District", url="https://www.aeazb.pt/")
    st.image("photos/symp.png",use_container_width=True,caption="Digital Changeon Symposium")
    st.image("photos/symp2.png",use_container_width=True,caption="Presentation")
    st.link_button(label="Digital Changeon", url="https://digitalchangeon.com/")
with col8:
    st.subheader('''During college''')
    st.write('''I began my professional journey at the age of 16, spending the
             summer working in a logistics warehouse where I unpacked and
             repacked items for promotions and filmed wooden pallets. After
             that, I spent subsequent summers working in various roles. Some
             years, I assisted full-time in my family’s paints and hardware
              retail business, while in others, I worked at Sugal Group, a
              tomato paste and concentrate factory in Azambuja, as a Quality
              Control Analyst in their laboratory. I maintained this pattern
              throughout college, combining summer jobs with academic
              commitments.''')
    st.subheader('''Tutoring''')
    st.write('''During the academic year, I tutored high school students,
             preparing them for national exams. In my final year of college,
             I took on a research collaborator role while working on my
             dissertation over the summer while tutoring at Lápis do
             Chapim in Odivelas.''')
    st.subheader('''Subject Matter Expert''')
    st.write('''After defending my thesis, I worked full-time at Lápis do
             Chapim as a Subject Matter Expert. In this role, I tutored
             students, provided scientific training to collaborators, and
             contributed to its daycare operations.''')
    st.subheader('''Process and Safety Enginner''')
    st.write('''In 2019, I transitioned to working as a Process and Safety
             Engineer at Bana Tintas. My responsibilities included optimizing
             chemical manufacturing processes for paints and soaps and
             preparing technical and safety documentation for the products.
             I also applied business data analytics extensively to enhance
              operations and support decision-making.''')
    st.subheader('''Teaching''')
    st.write('''In 2020, following the onset of the pandemic, I returned to my
             earlier passion for education and began teaching. I initially
             taught middle school mathematics at a public school in Castanheira
             do Ribatejo. This role was highly rewarding and provided valuable
             insights into working with children. I also taught students
             enrolled in professional courses, which presented unique
             challenges. Many of these students faced significant social issues
             that affected their classroom behavior and academic progress.
             This experience helped me develop resilience in managing unruly
             classrooms and deepened my understanding of the educational
             system's bureaucratic processes.''')
    st.write('''After the school year, I decided to continue teaching but
             sought opportunities closer to home. I was fortunate to secure
             contracts teaching Chemistry, Physics, and Mathematics in my
             hometown of Azambuja for the next three years. This was a rare
             and fortunate opportunity in Portugal, where such positions are
             typically difficult to find locally. During this time, I taught
             middle school, high school, and adult education (night classes).
             I also formed meaningful friendships and even participated in a
             symposium in Tokat, Türkiye, where I presented STEM teaching
             methodology in the classroom in a topic developed with a Natural
             Sciences colleague.''')
    st.write('''In my final year, I served as the headteacher for 9th graders,
             guiding them through national exams and their transition to high
             school. However, the increasing administrative responsibilities
             and local bureaucratic challenges created a stifling environment.
             It became evident that these issues were more localized than
             systemic, but they influenced my decision to explore new
             opportunities.''')
    st.subheader('''Recently''')
    st.write('''My interest then shifted to Data Science. I was eager to
             pursue this field and was fortunate to have a friend recommend Le
             Wagon's bootcamp as a stepping stone into this exciting domain.
             This opportunity has opened new doors for me and allowed me to
             refocus my career toward data-driven solutions and innovation.''')
