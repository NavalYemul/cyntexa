import streamlit as st
from databricks_langchain import ChatDatabricks
from langchain_core.prompts import PromptTemplate

# Page configuration
st.set_page_config(
    page_title="🌍 Travel Guide Itinerary",
    page_icon="🌍",
    layout="wide"
)

# Initialize the LLM
@st.cache_resource
def get_llm():
    return ChatDatabricks(endpoint="databricks-gemma-3-12b")

# Create the prompt template
prompt_template = PromptTemplate(
    input_variables=["city", "month", "budget", "days", "num_people"],
    template="""You are an expert travel planner and guide.
    
    Create a detailed travel itinerary for the following trip:
    - Destination: {city}
    - Travel Month: {month}
    - Budget: ${budget} USD
    - Duration: {days} days
    - Number of Travelers: {num_people} people
    
    Please provide:
    1. Day-by-day itinerary with must-visit attractions
    2. Recommended accommodations within the budget
    3. Local cuisine and restaurant suggestions
    4. Transportation tips
    5. Budget breakdown (accommodation, food, activities, transport)
    6. Important travel tips and cultural considerations
    
    Make the itinerary practical, exciting, and suitable for the group size and budget.
    """
)

# Header
st.title("🌍 Travel Guide Itinerary Generator")
st.markdown("### Plan your perfect trip with AI-powered personalized itineraries")
st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Trip Details")
    
    # Input fields
    city = st.text_input(
        "Destination City",
        placeholder="e.g., Paris, Tokyo, New York",
        help="Enter the city you want to visit"
    )
    
    month = st.selectbox(
        "Travel Month",
        options=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ],
        help="Select the month of your travel"
    )
    
    budget = st.number_input(
        "Total Budget (USD)",
        min_value=100,
        max_value=100000,
        value=2000,
        step=100,
        help="Enter your total budget in USD"
    )

with col2:
    st.subheader("👥 Travel Information")
    
    days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=30,
        value=5,
        step=1,
        help="How many days will you be traveling?"
    )
    
    num_people = st.number_input(
        "Number of People",
        min_value=1,
        max_value=20,
        value=2,
        step=1,
        help="How many people are traveling?"
    )

st.markdown("---")

# Generate button
generate_button = st.button(
    "🚀 Generate My Itinerary",
    type="primary",
    use_container_width=True
)

# Generate itinerary when button is clicked
if generate_button:
    if city:
        with st.spinner("🔄 Generating your personalized travel itinerary..."):
            try:
                # Format the prompt
                formatted_prompt = prompt_template.format(
                    city=city,
                    month=month,
                    budget=budget,
                    days=days,
                    num_people=num_people
                )
                
                # Get response from LLM
                llm = get_llm()
                response = llm.invoke(formatted_prompt)
                
                # Display the itinerary
                st.markdown("---")
                st.subheader("✈️ Your Personalized Itinerary")
                
                # Display trip summary
                st.info(f"**Destination:** {city} | **Month:** {month} | **Budget:** ${budget:,} USD | **Duration:** {days} days | **Travelers:** {num_people} people")
                
                # Display the generated content
                st.markdown(response.content)
                
                st.success("✅ Itinerary generated successfully!")
                
            except Exception as e:
                st.error(f"⚠️ An error occurred: {str(e)}")
                st.info("Please try again or check your inputs.")
    else:
        st.warning("⚠️ Please enter a destination city to generate an itinerary.")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>💡 Powered by Databricks Cyntexa</div>",
    unsafe_allow_html=True
)