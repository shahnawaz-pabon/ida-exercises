# 🧩 Student Task 5: Build a mini-dashboard using the crime-incidents data in `dataset.csv`. You have the freedom to decide what your 
# dashboard should include and look like. Minimally you have add the following to your dashboard:
#
# Show a preview of the dataset.
# Provide filters such as crime type, year, location description, and arrest (yes/no).
# Let users choose which columns to visualize.
# Include at least one meaningful visualization (e.g., map, scatter, line, or bar).
# Optionally integrate one of the Map widgets or components to geolocate the crime locations
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Chicago Crime Dashboard",
    page_icon="🚨",
    layout="wide"
)

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('dataset.csv')
    # Convert Date column to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Convert Year to numeric if it exists
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    return df

df = load_data()

# Title
st.title("🚨 Chicago Crime Incidents Dashboard")
st.markdown("Explore police-reported crime incidents in Chicago from 2001 onward")

# Sidebar for filters
st.sidebar.header("🔍 Filters")

# Year filter
years = sorted(df['Year'].dropna().unique())
selected_years = st.sidebar.multiselect(
    "Select Year(s)",
    options=years,
    default=[]  # No default - show all
)

# Primary Type filter
crime_types = sorted(df['Primary Type'].dropna().unique())
selected_crime_types = st.sidebar.multiselect(
    "Select Crime Type(s)",
    options=crime_types,
    default=[]  # No default - show all
)

# Location Description filter
location_descriptions = sorted(df['Location Description'].dropna().unique())
selected_locations = st.sidebar.multiselect(
    "Select Location Description(s)",
    options=location_descriptions,
    default=[]  # No default - show all
)

# Arrest filter
arrest_options = ['All', 'Yes', 'No']
selected_arrest = st.sidebar.selectbox(
    "Arrest Made",
    options=arrest_options,
    index=0
)

# Apply filters
filtered_df = df.copy()

if selected_years and 'Year' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Year'].isin(selected_years)]

if selected_crime_types and 'Primary Type' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Primary Type'].isin(selected_crime_types)]

if selected_locations and 'Location Description' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Location Description'].isin(selected_locations)]

if selected_arrest != 'All' and 'Arrest' in filtered_df.columns:
    arrest_bool = selected_arrest == 'Yes'
    filtered_df = filtered_df[filtered_df['Arrest'] == arrest_bool]

# Display summary statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Incidents", len(filtered_df))

with col2:
    if 'Arrest' in filtered_df.columns:
        arrest_count = filtered_df['Arrest'].sum() if filtered_df['Arrest'].dtype == bool else (filtered_df['Arrest'] == True).sum()
        st.metric("Arrests Made", int(arrest_count))
    else:
        st.metric("Arrests Made", "N/A")

with col3:
    if 'Primary Type' in filtered_df.columns:
        unique_crimes = filtered_df['Primary Type'].nunique()
        st.metric("Crime Types", unique_crimes)
    else:
        st.metric("Crime Types", "N/A")

with col4:
    if 'Year' in filtered_df.columns:
        year_range = f"{int(filtered_df['Year'].min())}-{int(filtered_df['Year'].max())}"
        st.metric("Year Range", year_range)
    else:
        st.metric("Year Range", "N/A")

# Create tabs for different views
tab1, tab2, tab3 = st.tabs(["📊 Data Preview", "📈 Visualizations", "🗺️ Map View"])

with tab1:
    st.header("Dataset Preview")
    
    # Show number of rows
    st.write(f"Showing {len(filtered_df)} rows (out of {len(df)} total)")
    
    # Display dataframe
    st.dataframe(filtered_df, width='stretch')
    
    # Show basic statistics
    st.subheader("Dataset Statistics")
    st.dataframe(filtered_df.describe(), width='stretch')

with tab2:
    st.header("Data Visualizations")
    
    # Visualization type selector
    viz_type = st.selectbox(
        "Select Visualization Type",
        options=["Crime Type Distribution", "Crimes by Year", "Location Description Distribution", 
                 "Arrest Rate by Crime Type"]
    )
    
    if viz_type == "Crime Type Distribution":
        if 'Primary Type' in filtered_df.columns:
            crime_counts = filtered_df['Primary Type'].value_counts().head(15)
            fig, ax = plt.subplots(figsize=(12, 6))
            crime_counts.plot(kind='barh', ax=ax, color='steelblue')
            ax.set_xlabel('Number of Incidents')
            ax.set_ylabel('Crime Type')
            ax.set_title('Top 15 Crime Types by Frequency')
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Primary Type column not available")
    
    elif viz_type == "Crimes by Year":
        if 'Year' in filtered_df.columns:
            year_counts = filtered_df['Year'].value_counts().sort_index()
            fig, ax = plt.subplots(figsize=(12, 6))
            year_counts.plot(kind='line', ax=ax, marker='o', color='crimson')
            ax.set_xlabel('Year')
            ax.set_ylabel('Number of Incidents')
            ax.set_title('Crime Incidents by Year')
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Year column not available")
    
    elif viz_type == "Location Description Distribution":
        if 'Location Description' in filtered_df.columns:
            location_counts = filtered_df['Location Description'].value_counts().head(15)
            fig, ax = plt.subplots(figsize=(12, 6))
            location_counts.plot(kind='barh', ax=ax, color='darkgreen')
            ax.set_xlabel('Number of Incidents')
            ax.set_ylabel('Location Description')
            ax.set_title('Top 15 Location Descriptions by Frequency')
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Location Description column not available")
    
    elif viz_type == "Arrest Rate by Crime Type":
        if 'Primary Type' in filtered_df.columns and 'Arrest' in filtered_df.columns:
            # Calculate arrest rates
            arrest_rates = filtered_df.groupby('Primary Type')['Arrest'].apply(
                lambda x: (x == True).sum() / len(x) * 100 if len(x) > 0 else 0
            ).sort_values(ascending=False).head(15)
            
            fig, ax = plt.subplots(figsize=(12, 6))
            arrest_rates.plot(kind='barh', ax=ax, color='orange')
            ax.set_xlabel('Arrest Rate (%)')
            ax.set_ylabel('Crime Type')
            ax.set_title('Top 15 Crime Types by Arrest Rate')
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.warning("Required columns (Primary Type, Arrest) not available")
with tab3:
    st.header("Geographic Distribution")
    
    # Filter out rows with missing coordinates (if any)
    map_df = filtered_df.dropna(subset=['Latitude', 'Longitude'])
    
    if len(map_df) > 0:
        st.write(f"Showing {len(map_df)} incidents with valid coordinates")
        
        # Limit points for performance
        max_points = st.slider("Maximum points to display", 100, min(1000, len(map_df)), 500)
        map_df_sample = map_df.head(max_points)
        
        # Create map using Plotly
        fig = px.scatter_map(
            map_df_sample,
            lat='Latitude',
            lon='Longitude',
            hover_name='Primary Type' if 'Primary Type' in map_df_sample.columns else None,
            hover_data=['Date', 'Description'] if 'Description' in map_df_sample.columns else ['Date'],
            color='Primary Type' if 'Primary Type' in map_df_sample.columns else None,
            zoom=10,
            height=600,
            title="Crime Incidents Map"
        )
        
        fig.update_layout(
            mapbox_style="open-street-map",
            margin=dict(l=0, r=0, t=30, b=0)
        )
        
        st.plotly_chart(fig, width='stretch')
    else:
        st.warning("No data points with valid coordinates available")

# Footer
st.markdown("---")
st.markdown("**Data Source:** Chicago Police Department Crime Incidents Dataset")