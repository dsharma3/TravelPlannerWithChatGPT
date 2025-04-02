import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Initialize environment
load_dotenv()

class TravelPlanner:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            st.error("API key not found. Please create a .env file")
            st.stop()
        
        # Initialize OpenAI client with modern syntax
        self.client = openai.Client(api_key=self.api_key)  # Changed from OpenAI() to Client()
    
    def generate_itinerary(self, destination, days, budget, interests):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user",
                    "content": f"""Create a {days}-day itinerary for {destination} with:
                    - Budget: ${budget}
                    - Interests: {', '.join(interests)}
                    - Format: Daily activities with time slots
                    - Include: Estimated costs and local tips"""
                }],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            st.error(f"API Error: {str(e)}")
            return None

# Streamlit App
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("✈️ Minimal Travel Planner")

with st.form("travel_form"):
    destination = st.text_input("Destination")
    days = st.slider("Days", 1, 14, 5)
    budget = st.slider("Budget ($)", 500, 5000, 1500)
    interests = st.multiselect("Interests", ["History", "Food", "Nature"])
    
    if st.form_submit_button("Generate"):
        if not destination:
            st.error("Enter a destination")
        else:
            planner = TravelPlanner()
            with st.spinner("Planning..."):
                itinerary = planner.generate_itinerary(destination, days, budget, interests)
            
            if itinerary:
                st.subheader(f"{destination} Itinerary")
                st.markdown(itinerary)