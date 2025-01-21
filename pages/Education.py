import streamlit as st

st.set_page_config(page_title="Edu", layout="wide", initial_sidebar_state="auto")
col7, col8 = st.columns([4,8])

with col7:
    st.image("photos/grad.png",use_container_width=True,caption="IST Graduation day")
    st.write("B.Science Degree in Chemical Engineering: 2013 - 2016")
    st.write("M.Science Degree in Chemical Engineering: 2016 - 2018")
    st.link_button(label="IST", url="https://tecnico.ulisboa.pt/en/")
    st.link_button(label="Dissertation", url='''https://fenix.tecnico.ulisboa.pt/cursos/meq/dissertacao/1409728525632174''')
    st.container(height=80,border=False)
    st.image("photos/lew_photo.png",use_container_width=True,caption="Le Wagon Graduation day")
    st.write("Data Science & A.I. Bootcamp: Oct - Dec 2024")
    st.image("photos/demo1.png",use_container_width=True,caption="Demo day")
    st.image("photos/demo2.png",use_container_width=True,caption="Frontend demo")
    st.link_button(label="Le Wagon", url="https://www.lewagon.com/")
    st.link_button(label="Demo day album", url="https://www.lourenco.photo/C/EMPRESAS/LeWagon/n-Pmb29k/241206/i-zzVPBnn")
with col8:
    st.image("logos/ist_black.png",width=100)
    st.subheader("IST - Técnico Lisboa")
    st.subheader("Integrated Masters Degree in Chemical Engineering")
    st.write('''After high school, I began my academic journey at IST in Lisbon,
             the largest school of Engineering, Architecture, Science, and
             Technology in Portugal, and one of the most reputable institutions
             in Europe.''')
    st.write('''I thoroughly enjoyed exploring deep mathematical concepts, was
             captivated by my physics classes, and found my chemistry courses
             engaging. However, my true passion lay in engineering. I
              particularly enjoyed designing equipment, learning process
              control, and experimenting with programming in Fortran and
              MATLAB.''')
    st.write('''After completing my Bachelor's degree, I had the opportunity
             to specialize during my Master's program. My choices included
             Petroleum Engineering, Pharmaceutical Engineering, and continuing
             with Chemical Engineering. I decided to continue along the
             path of Chemical Engineering.''')
    st.write('''During my Master's studies, I selected Surfaces, Interfaces,
             and Colloids (due to its use of Physical-Chemistry concepts),
             Advanced Process Control, and Catalysis and Catalytic Processes
             as optional courses. Among these, I was especially fascinated by
             my catalysis class, where I encountered an incredible
             concept—photocatalysts. This discovery inspired me to focus on
             heterogeneous photocatalysis for my dissertation.''')
    st.write('''As a research collaborator at CATHPRO (CQE-IST), I developed
             a heterogeneous photocatalytic unit for ethylene degradation
             and authored my dissertation on optimizing catalyst
             loading methods for the unit.''')
    st.image("logos/lwaglogo.png",width=115)
    st.subheader("Le Wagon Lisboa")
    st.subheader("Data Science & A.I.")
    st.write('''After teaching Math, Physics, and Chemistry for four years,
             I took my friend Susana Martins' advice and decided to transition
             into Data Science. I had always been curious about the field,
             and given my strong background in Math, I was the kind of person
             who would open MATLAB or Excel to perform calculations
             for hobbies or work.''')
    st.write('''To kickstart this new career, I chose Le Wagon for a Data
             Science bootcamp. I was influenced not only by my friend's
             recommendation but also by the program's excellent online ratings
             and challenging curriculum. I opted for a bootcamp over a
             postgraduate program because of the intensive, full-time approach.
             I wanted a fast-paced environment to quickly gain certification
             and enter the workforce.''')
    st.write('''The bootcamp covered all the key topics essential from a
             professional perspective. A “midway” project had us collaborating
             on a Data Analytics problem, ensuring we gained hands-on
             experience. During the final two weeks, we tackled a capstone
             project. Through a voting process, I joined a team working
             on a recommendation system app for restaurants. This system
             evaluated establishments based on sentiment analysis of user
             reviews rather than traditional star ratings.''')
    st.write('''We used Yelp's public dataset for the recommendation system,
             focusing on the U.S. city with the highest number of restaurant
             reviews. This led to the creation of Philly Bites, a
             recommendation system for restaurants based in Philadelphia.''')
    st.write('''After conducting extensive data analysis and feature
             engineering, we uploaded the processed data to Google BigQuery.
             For sentiment analysis of restaurant reviews, we employed a BERT
             transformer model. Additionally, we vectorized restaurant
             categories and user preferences (based on liked restaurants)
             and applied cosine similarity to generate the best recommendations
             for each user.''')
    st.write('''The project was containerized using Docker, which allowed
                us to offer an API endpoint where users could retrieve
                personalized restaurant recommendations. Another API endpoint
                integrated with OpenAI's Gemini to generate personalized
                restaurant reviews written in the style of The Fresh
                Prince of Bel-Air.''')
    st.write('''The frontend provided several features: users could select
                from preloaded random profiles, view restaurants pinpointed
                on a map with relevant information, and receive personalized
                recommendations on demand.''')
    st.write('''The project's scope involved a significant amount of Data
             Engineering, Deep Learning, and MLOps. Despite the challenges of completing
             such a mature project within two weeks as a three-person team,
             the experience was immensely rewarding.''')
    st.write('''Looking back, I feel confident in my decisions and excited
             about exploring the opportunities in this dynamic field.''')
