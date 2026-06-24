import pytest
from app.recommender import calculate_jaccard_similarity, calculate_user_similarity

def test_jaccard_similarity():
    set1 = {"A", "B", "C"}
    set2 = {"B", "C", "D"}
    # Intersection: {"B", "C"} -> 2
    # Union: {"A", "B", "C", "D"} -> 4
    # Score -> 0.5
    assert calculate_jaccard_similarity(set1, set2) == 0.5
    
    # Disjoint sets
    assert calculate_jaccard_similarity({"A"}, {"B"}) == 0.0
    
    # Identical sets
    assert calculate_jaccard_similarity({"A", "B"}, {"A", "B"}) == 1.0

def test_user_similarity():
    user1 = {
        "friends": [1, 2, 3],
        "skills": ["Python", "AWS"],
        "location": "Mumbai"
    }
    user2 = {
        "friends": [2, 3, 4], # Jaccard: 2/4 = 0.5 -> * 0.4 = 0.2
        "skills": ["Python", "Java"], # Jaccard: 1/3 = 0.333 -> * 0.4 = 0.133
        "location": "Mumbai" # Match = 1 -> * 0.2 = 0.2
    }
    
    score = calculate_user_similarity(user1, user2)
    assert round(score, 3) == 0.533
