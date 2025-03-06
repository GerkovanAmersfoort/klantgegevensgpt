import streamlit as st
import pandas as pd

# Functie om de GPT-prompt te genereren
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
    2. Geef voedingssuggesties die passen bij de doelen en dieetvoorkeuren van {client_name}.
    3. Motiveer {client_name} met berichten en aanmoediging op basis van hun motivatiestijl.
    4. Check periodiek de voortgang en stel aanpassingen voor.
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

# Knop om de GPT-prompt te genereren en op te slaan
if st.button("Genereer Prompt"):
    if client_name and fitness_goal:
        prompt = generate_custom_gpt_prompt(client_name, age, fitness_goal, experience_level, training_preferences, injuries, dietary_restrictions, motivation_style)

        # ✅ Opslaan in een CSV-bestand
        data = {
            "Naam": [client_name],
            "Leeftijd": [age],
            "Doelstelling": [fitness_goal],
            "Ervaringsniveau": [experience_level],
            "Trainingsvoorkeuren": [training_preferences],
            "Blessures": [injuries],
            "Voedingsrestricties": [dietary_restrictions],
            "Motivatiestijl": [motivation_style],
            "GPT Prompt": [prompt]
        }

        df = pd.DataFrame(data)
        df.to_csv("klantgegevens.csv", mode='a', index=False, header=False)  # Voeg toe aan CSV-bestand

        st.success("De klantgegevens zijn opgeslagen en klaar om in je Custom GPT te gebruiken!")

        # ✅ Laat de gegenereerde GPT-prompt zien
        st.text_area("Gegenereerde GPT Prompt", prompt, height=300)
    else:
        st.warning("Vul ten minste de naam en het fitnessdoel in om een prompt te genereren.")

# ✅ Downloadknop om CSV-bestand op te halen
if st.button("Download Klantgegevens"):
    with open("klantgegevens.csv", "rb") as file:
        st.download_button(label="Download klantgegevens", data=file, file_name="klantgegevens.csv", mime="text/csv")
