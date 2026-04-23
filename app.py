import streamlit as st
import pandas as pd
import time

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Smart Volunteer Coordinator", layout="wide")
st.title("🤝 Smart Volunteer Coordinator")
st.markdown("Data-driven resource allocation for disaster relief and social impact.")
st.divider()

# --- 2. GENERATE FAKE DATA (Hackathon Magic) ---
# We use st.session_state so the data doesn't reset every time you click a button
if 'volunteers' not in st.session_state:
    st.session_state.volunteers = pd.DataFrame({
        'ID': ['V1', 'V2', 'V3', 'V4', 'V5', 'V6'],
        'Name': ['Sarah', 'John', 'Priya', 'David', 'Elena', 'Mike'],
        'Primary_Skill': ['Medical', 'Logistics', 'Cooking', 'Logistics', 'Heavy Lifting', 'Medical'],
        'Status': ['Available', 'Available', 'Available', 'Available', 'Available', 'Available']
    })

if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame({
        'Task_ID': ['T1', 'T2', 'T3', 'T4'],
        'Incident': ['Flood Relief Depot', 'Downtown Soup Kitchen', 'Medical Camp', 'Debris Clearing'],
        'Required_Skill': ['Logistics', 'Cooking', 'Medical', 'Heavy Lifting'],
        'Urgency': ['High', 'Medium', 'High', 'Low'],
        'Assigned_To': ['Unassigned', 'Unassigned', 'Unassigned', 'Unassigned']
    })

# --- 3. DASHBOARD UI ---
# Create two columns to show tasks and volunteers side-by-side
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚨 Active Incidents (Tasks)")
    st.dataframe(st.session_state.tasks, use_container_width=True)

with col2:
    st.subheader("🙋 Available Volunteers")
    # Only show volunteers who are currently available
    available_vols = st.session_state.volunteers[st.session_state.volunteers['Status'] == 'Available']
    st.dataframe(available_vols, use_container_width=True)

st.write("") # Add some spacing

# --- 4. THE SMART MATCHING ALGORITHM ---
# This button triggers the logic to match skills
if st.button("🚀 Run Smart Allocation Algorithm", type="primary", use_container_width=True):
    
    # A fake loading spinner adds tension and makes it feel like it's doing complex math!
    with st.spinner("Analyzing skills, urgency, and optimizing resource allocation..."):
        time.sleep(1.5) 
        
        tasks = st.session_state.tasks
        vols = st.session_state.volunteers
        new_assignments = []
        
        # Loop through every task
        for index, task in tasks.iterrows():
            if task['Assigned_To'] == 'Unassigned':
                
                # Find volunteers who are available AND have the exact skill needed
                matching_vols = vols[(vols['Primary_Skill'] == task['Required_Skill']) & (vols['Status'] == 'Available')]
                
                if not matching_vols.empty:
                    # Pick the first person who matches
                    best_match = matching_vols.iloc[0] 
                    
                    # 1. Assign them to the task
                    tasks.at[index, 'Assigned_To'] = best_match['Name']
                    # 2. Change their status to Deployed
                    vols.loc[vols['ID'] == best_match['ID'], 'Status'] = 'Deployed'
                    
                    # 3. Save a record of this match to show the judges
                    new_assignments.append({
                        "Incident": task['Incident'], 
                        "Assigned Volunteer": best_match['Name'], 
                        "Skill Matched": task['Required_Skill']
                    })
        
        # Update the session state with the new data
        st.session_state.tasks = tasks
        st.session_state.volunteers = vols
        # --- 5. SHOW THE RESULTS ---
        st.success("Allocation Complete! Resources successfully deployed.")
        
        if new_assignments:
            st.write("### 🎯 Mission Briefing (New Assignments)")
            st.table(pd.DataFrame(new_assignments))
            st.balloons() # Triggers celebration animation
        else:
            st.warning("No new matches could be made based on current available skills.")