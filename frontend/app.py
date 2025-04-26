import streamlit as st
import requests
import random

st.set_page_config(layout="wide")

st.title("Pick 5 Pokémon to Start Your Epic Adventure!")

if st.button("Pick", type="primary"):
    rand_numbers = []
    while len(rand_numbers) < 6:
        number = random.randint(1, 1017)
        response = requests.get(f"http://127.0.0.1:8000/pokemon/{number}")
        pokemon = response.json()
        if pokemon["sprites"]["other"]["dream_world"]["front_default"]:
            rand_numbers.append(number)

    col = st.columns(5, border=True)
    for i in range(5):
        response = requests.get(f"http://127.0.0.1:8000/pokemon/{rand_numbers[i]}")
        pokemon = response.json()
        with col[i]:
            # Show image
            st.image(pokemon["sprites"]["other"]["dream_world"]["front_default"])

            # Show name
            st.subheader(pokemon["name"].capitalize())

            # Show types (can be 1 or 2 types)
            types = [t["type"]["name"].capitalize() for t in pokemon["types"]]
            st.markdown(f"**Type:** {', '.join(types)}")

            # Show abilities
            abilities = [ab["ability"]["name"].capitalize() for ab in pokemon["abilities"]]
            st.markdown(f"**Abilities:** {', '.join(abilities)}")

            # Height and Weight
            st.markdown(f"**Height:** {pokemon['height']/10} m")
            st.markdown(f"**Weight:** {pokemon['weight']/10} kg")

            # Base Experience
            st.markdown(f"**Base Experience:** {pokemon['base_experience']} XP")

            # Base Stats
            st.markdown("**Base Stats:**")
            stats = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon["stats"]}
            st.write(f"🗡️ Attack: {stats.get('attack', 'N/A')}")
            st.write(f"🛡️ Defense: {stats.get('defense', 'N/A')}")
            st.write(f"⚡ Speed: {stats.get('speed', 'N/A')}")

            # Sound
            st.audio(pokemon["cries"]["latest"])
