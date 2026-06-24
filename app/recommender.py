def calculate_jaccard_similarity(set1, set2):
    """
    Calculate Jaccard Similarity between two sets.
    """
    if not set1 and not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union > 0 else 0.0

def calculate_user_similarity(user1, user2):
    """
    Calculate a similarity score between 0 and 1 for two users.
    Weights:
    - Friends similarity: 40%
    - Skills similarity: 40%
    - Location match: 20%
    """
    friends_sim = calculate_jaccard_similarity(set(user1.get("friends", [])), set(user2.get("friends", [])))
    skills_sim = calculate_jaccard_similarity(set(user1.get("skills", [])), set(user2.get("skills", [])))
    location_sim = 1.0 if user1.get("location") == user2.get("location") else 0.0
    
    return (friends_sim * 0.4) + (skills_sim * 0.4) + (location_sim * 0.2)

def people_you_may_know(user_id, data, top_n=10):
    """
    Recommend friends for a user based on user similarity.
    Returns a list of tuples: (user_dict, similarity_score)
    """
    users = data.get("users", [])
    user_map = {u["id"]: u for u in users}
    
    if user_id not in user_map:
        return []
        
    target_user = user_map[user_id]
    target_friends = set(target_user.get("friends", []))
    
    suggestions = []
    
    for u in users:
        # Don't recommend themselves or existing friends
        if u["id"] == user_id or u["id"] in target_friends:
            continue
            
        sim_score = calculate_user_similarity(target_user, u)
        if sim_score > 0:
            suggestions.append((u, round(sim_score, 3)))
            
    # Sort by similarity score descending
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions[:top_n]

def pages_you_might_like(user_id, data, top_n=10):
    """
    Recommend pages based on what similar users like (Collaborative Filtering).
    Returns a list of tuples: (page_dict, recommendation_score)
    """
    users = data.get("users", [])
    pages = data.get("pages", [])
    
    user_map = {u["id"]: u for u in users}
    page_map = {p["id"]: p for p in pages}
    
    if user_id not in user_map:
        return []
        
    target_user = user_map[user_id]
    target_liked_pages = set(target_user.get("liked_pages", []))
    
    # Calculate similarity to all other users
    user_similarities = {}
    for u in users:
        if u["id"] != user_id:
            user_similarities[u["id"]] = calculate_user_similarity(target_user, u)
            
    # Score pages based on how similar users liked them
    page_scores = {}
    
    for u in users:
        if u["id"] == user_id:
            continue
            
        sim = user_similarities[u["id"]]
        if sim <= 0:
            continue
            
        for pid in u.get("liked_pages", []):
            if pid not in target_liked_pages:
                page_scores[pid] = page_scores.get(pid, 0.0) + sim
                
    # Format suggestions
    suggestions = []
    for pid, score in page_scores.items():
        if pid in page_map:
            suggestions.append((page_map[pid], round(score, 3)))
            
    # Sort by score descending
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions[:top_n]
