import streamlit as st

st.set_page_config(page_title="Edu", layout="wide", initial_sidebar_state="auto")
col7, col8 = st.columns([4,8])

with col7:
    st.image("photos/prer.png",use_container_width=True,caption="MtG Pre-release Event")
    st.image("photos/bass.png",use_container_width=True,caption="Playing Bass in School Orchestra")
with col8:
    st.subheader('''Childhood''')
    st.write('''I have always enjoyed games, ever since I can remember. My
             earliest memory of this is my father teaching me how to play
             chess. We had a glass chess set, and we would play together when I
             got home from school. I also loved electronic games, starting with
             "Super Mario 64" on the Nintendo 64. Later, I received a
             PlayStation 2 around the age of 10, and one of my first games was
             the 2006 release "Final Fantasy XII." I was captivated by its
             stunning visuals and spent countless hours conquering the game
             through multiple save files.''')
    st.subheader('''Early Teens''')
    st.write('''Eventually, I ventured into offline activities and took up
              table tennis practice, continuing until I was 18 when college
              responsibilities required my full attention. Around the age of
              14, I started learning guitar in the school orchestra and began
              playing "Magic: The Gathering," a trading card game, in local
              tournaments with my cousin. These hobbies were a source of joy
              until high school, when my focus shifted to online games like
              "League of Legends." While I enjoyed it, I've never been
              particularly skilled at the game despite many years of
              playing.''')
    st.subheader('''Teenage years''')
    st.write('''Later, I discovered "World of Warcraft" during the Mists of
             Pandaria expansion. Initially, I struggled to find my place in the
             game, but during the Legion expansion, I started raiding as a
             healer and found that I was quite good at it. Although I had to
             pause raiding mid-expansion to focus on my studies, I returned and
             achieved a top-50 world performance as a Mistweaver Monk on a
             raid boss.''')
    st.subheader('''Early Twenties''')
    st.write('''For several years, I continued playing WoW with my Portuguese
             guild, managing raid healers, overseeing their preparation, and
             occasionally raid-leading weekend raids. Despite being a "casual"
             guild, we achieved decent results. However, over time, conflicts
             over guild decisions involving players close to me led to my
             group's departure. We attempted to establish our own guild but
             struggled to maintain momentum, and I eventually stopped playing
             due to dissatisfaction with my performance and the game's
             direction. I started playing Final Fantasy XIV and
             sporadically still do.''')
    st.subheader('''Late Twenties''')
    st.write('''In recent years, I have rekindled my love for chess, taken up
             playing the bass guitar, and even rejoined the school
             orchestra—this time as a teacher. Additionally, I've rediscovered
             my passion for "Magic: The Gathering" and continue to participate
             in tournaments to this day.''')
