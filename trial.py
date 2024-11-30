
import streamlit as st

# Updated dictionary of Indian dishes and their corresponding calorie count (per serving)
dishes_calories = {
    "Paneer Butter Masala": 350,
    "Chicken Biryani": 400,
    "Chole Bhature": 500,
    "Aloo Gobi": 250,
    "Dosa (Plain)": 180,
    "Masoor Dal": 200,
    "Tandoori Chicken": 290,
    "Butter Naan": 270,
    "Palak Paneer": 290,
    "Samosa": 150,
    "Pav Bhaji": 300,
    "Vada Pav": 280,
    "Gulab Jamun": 150,
    "Raita": 120,
    "Methi Thepla": 220,
    "Pulao": 250,
    "Baingan Bharta": 210,
    "Aloo Paratha": 250,
    "Pani Puri": 100,  # Calories per 6-8 pieces
    "Momos (Vegetable)": 150,
    "Methi Thepla": 220,
    "Pesarattu": 220,  # Green gram pancake
    "Tandoori Roti": 150,
    "Kadhi Pakora": 300,
    "Aloo Tikki": 200,
    "Lassi (Sweet)": 250,
    "Chana Masala": 300,
    "Bhel Puri": 250,
    "Malai Kofta": 400,
    "Dhokla": 120,
    "Kachori": 250,
    "Idli (2 pieces)": 140,
    "Dhokla": 120,
    "Bhindi Masala (Okra)": 150,
    "Sev Puri": 220,
    "Keema Pav": 350,
    "Prawn Curry": 300,
    "Pesarattu": 220,  # Green gram pancake
    "Kathi Roll (Chicken)": 350,
    "Mutton Rogan Josh": 400,
    "Egg Curry": 300,
    "Biryani (Vegetarian)": 400,
}

# Function to display calorie information for the selected dish
def display_calories(dish):
    """Function to display calorie information for the selected dish."""
    calories = dishes_calories.get(dish, "Dish not available")
    if calories == "Dish not available":
        st.error("Sorry, calorie information is not available for this dish.")
    else:
        st.write(f"The calorie count for {dish} is: {calories} kcal per serving.")
    
    # Show a picture of a hippo after the result
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f2/Portrait_Hippopotamus_in_the_water.jpg", caption="Here's a hippo!")

# Streamlit App layout
st.title("Indian Dish Calorie Finder")

st.write(
    "Select an Indian dish from the list below to get the calorie count per serving:"
)

# Dropdown menu for dish selection
dish = st.selectbox(
    "Choose a Dish", list(dishes_calories.keys())
)

# Display the calorie information when a dish is selected
if dish:
    display_calories(dish)

# Indicate who designed the app
st.write("App designed by Abhijeet")
