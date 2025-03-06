import streamlit as st  # Hiermee maken we de website

# Functie om de GPT-prompt te maken
def generate_custom_gpt_prompt(client_name, age, fitness_goal, experience_level, training_preferences, injuries, dietary_restrictions, motivation_style):
    return f"""
    Je bent een virtuele personal trainer genaamd {client_name}'s AI-Coach. Je begeleidt {client_name} in hun fitnessreis door op maat gemaakte adviezen en motivatie te geven. Houd rekening met de volgende klantgegevens:
    
    - Leeftijd: {age} jaar
    - Doelstelling: {fitness_goal}
    - Ervaringsniveau: {experience_level}
    - Trainingsvoorkeuren: {training_preferences}
    - Blessures/beperkingen: {injuries}
    - Dieetvoorkeuren/beperkingen: {dietary_restrictions}
    - Motivatiestijl: {motivation_style} (bijv. streng, ondersteunend, speels, data-gedreven)
    
    **Jouw taken:**
    1. Geef gepersonaliseerde trainingsadviezen.
    2. Geef voedingssuggesties.
    3. Motiveer {client_name} met berichten.
    4. Check de voortgang en stel aanpassingen voor.
    5. Beantwoord vragen over training, voeding en herstel.
    """

# Titel van de website
st.title("GPT Prompt Generator voor Personal Trainers")

# Invoervelden voor de gebruiker
client_name = st.text_input("Naam van de klant")
age = st.number_input("Leeftijd", min_value=10, max_value=100, step=1)
fitness_goal = st.text_area("Wat is het fitnessdoel?")
experience_level = st.selectbox("Ervaringsniveau", ["Beginner", "Gemiddeld", "Gevorderd"])
training_preferences = st.text_area("Voorkeursvormen van training")
injuries = st.text_area("Blessures of lichamelijke beperkingen")
dietary_restrictions = st.text_area("Voedingsvoorkeuren of restricties")
motivation_style = st.selectbox("Motivatiestijl", ["Streng", "Ondersteunend", "Speels", "Data-gedreven"])

# Knop om de GPT-prompt te genereren
if st.button("Genereer Prompt"):
    if client_name and fitness_goal:
        prompt = generate_custom_gpt_prompt(client_name, age, fitness_goal, experience_level, training_preferences, injuries, dietary_restrictions, motivation_style)
        st.text_area("Gegenereerde GPT Prompt", prompt, height=300)
    else:
        st.warning("Vul ten minste de naam en het fitnessdoel in om een prompt te genereren.")
