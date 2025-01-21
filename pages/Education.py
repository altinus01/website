import streamlit as st

st.set_page_config(page_title="Edu", layout="wide", initial_sidebar_state="auto")
col7, col8 = st.columns([4,8])

with col7:
    st.image("grad.png",use_container_width=True,caption="Graduation day")
    st.write("B.Science Degree in Chemical Engineering: 2013-2016")
    st.write("M.Science Degree in Chemical Engineering: 2016-2018")
    st.link_button(label="IST", url="https://tecnico.ulisboa.pt/en/")
    st.link_button(label="Dissertation", url='''https://fenix.tecnico.ulisboa.pt/cursos/meq/dissertacao/1409728525632174''')

with col8:
    st.image("ist_black.png",width=100)
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
