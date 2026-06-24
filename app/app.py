import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.recommender import people_you_may_know, pages_you_might_like

st.set_page_config(page_title="Social Network Recommender", layout="wide")

@st.cache_data
def get_data():
    return load_data("data/dataset.json")

def main():
    st.title("Social Network Recommendation System")
    st.markdown("A social network recommendation system.")
    
    try:
        data = get_data()
    except FileNotFoundError:
        st.error("Data file not found. Please run `python d_gen.py` first.")
        return
        
    users = data.get("users", [])
    if not users:
        st.warning("No users found in data.")
        return
        
    # User selection
    st.sidebar.header("User Selection")
    user_options = {u["id"]: f"{u['name']} (ID: {u['id']})" for u in users}
    selected_user_id = st.sidebar.selectbox("Select a User:", options=list(user_options.keys()), format_func=lambda x: user_options[x])
    
    # Display User Profile
    target_user = next(u for u in users if u["id"] == selected_user_id)
    
    st.header(f"Profile: {target_user['name']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Age", target_user.get("age", "N/A"))
    col2.metric("Location", target_user.get("location", "N/A"))
    col3.metric("Job Title", target_user.get("job_title", "N/A"))
    
    st.write("**Skills:**", ", ".join(target_user.get("skills", [])))
    st.write(f"**Friends:** {len(target_user.get('friends', []))} connections")
    st.write(f"**Liked Pages:** {len(target_user.get('liked_pages', []))} pages")
    
    st.divider()
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("👥 People You May Know")
        friend_recs = people_you_may_know(selected_user_id, data, top_n=5)
        
        if friend_recs:
            for rec_user, score in friend_recs:
                with st.expander(f"{rec_user['name']} (Score: {score})"):
                    st.write(f"**Location:** {rec_user.get('location', 'N/A')}")
                    st.write(f"**Job:** {rec_user.get('job_title', 'N/A')}")
                    st.write(f"**Skills:** {', '.join(rec_user.get('skills', []))}")
                    # Calculate mutual friends for display
                    mutuals = len(set(target_user.get('friends', [])).intersection(set(rec_user.get('friends', []))))
                    st.write(f"**Mutual Friends:** {mutuals}")
        else:
            st.info("No recommendations found.")
            
    with col_right:
        st.subheader("📄 Pages You Might Like")
        page_recs = pages_you_might_like(selected_user_id, data, top_n=5)
        
        if page_recs:
            for rec_page, score in page_recs:
                with st.expander(f"{rec_page['name']} (Score: {score})"):
                    st.write(f"**Category:** {rec_page.get('category', 'N/A')}")
                    st.write(f"**Followers:** {rec_page.get('follower_count', 'N/A')}")
        else:
            st.info("No recommendations found.")

if __name__ == "__main__":
    main()
