
import json
import random

def generate_data(num_users=100, num_pages=30):
    first_names = ["Amit", "Priya", "Rahul", "Sara", "Neha", "Vikram", "Kunal", "Anjali", "Ravi", "Sneha", "Arjun", "Meera", "Kabir", "Tanya", "Varun", "Rhea", "Ishan", "Simran", "Pooja", "Yash", "Ananya", "Dev", "Aditi", "Rohan", "Nisha", "Gautam", "Kriti", "Harsh", "Naveen", "Ishita"]
    last_names = ["Sharma", "Verma", "Gupta", "Singh", "Patel", "Kumar", "Das", "Bose", "Mehta", "Jain", "Chawla", "Reddy", "Nair", "Iyer", "Rao"]
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai"]
    job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Designer", "Marketing Manager", "HR Specialist", "Business Analyst"]
    skills_pool = ["Python", "Java", "Machine Learning", "Data Analysis", "UI/UX", "SEO", "Project Management", "React", "AWS", "SQL", "Communication", "Marketing"]
    
    page_categories = ["Tech", "Science", "Entertainment", "Sports", "Business", "Lifestyle"]
    page_names = ["Python Developers", "Data Science Enthusiasts", "AI & ML Community", "Web Dev Hub", "Blockchain Innovators", "Cybersecurity Experts", "Cloud Computing Pros", "Competitive Programmers", "Startup Founders", "UI/UX Designers", "Full-Stack Developers", "Tech Entrepreneurs", "IoT Enthusiasts", "Game Developers", "Big Data Analysts", "DevOps Engineers", "Cloud AI Researchers", "5G & Edge Computing", "AR/VR Creators", "Freelance Coders", "Open Source Contributors", "Algorithmic Traders", "Low-Code Developers", "Cyber Ethics Forum", "AI Ethics & Policy", "Digital Nomads", "Women in Tech", "Gadget Geeks", "Quantum Computing", "Tech Startups India"]

    pages = []
    for i in range(1, num_pages + 1):
        pages.append({
            "id": 100 + i,
            "name": page_names[i-1] if i-1 < len(page_names) else f"Page {i}",
            "category": random.choice(page_categories),
            "follower_count": random.randint(100, 10000)
        })

    users = []
    for i in range(1, num_users + 1):
        skills = random.sample(skills_pool, k=random.randint(2, 5))
        users.append({
            "id": i,
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "age": random.randint(20, 45),
            "location": random.choice(cities),
            "job_title": random.choice(job_titles),
            "skills": skills,
            "friends": [], # to be populated
            "liked_pages": random.sample([p["id"] for p in pages], k=random.randint(1, 8))
        })

    # Populate friends
    for user in users:
        # Each user has 2 to 10 friends
        num_friends = random.randint(2, 10)
        potential_friends = [u["id"] for u in users if u["id"] != user["id"]]
        # Pick friends (not purely undirected graph for simplicity, but let's try to make it undirected)
        friends_to_add = random.sample(potential_friends, k=num_friends)
        for f_id in friends_to_add:
            if f_id not in user["friends"]:
                user["friends"].append(f_id)
            # Add reverse link
            f_user = next(u for u in users if u["id"] == f_id)
            if user["id"] not in f_user["friends"]:
                f_user["friends"].append(user["id"])

    # Ensure no duplicates and sorted
    for user in users:
        user["friends"] = sorted(list(set(user["friends"])))

    data = {"users": users, "pages": pages}
    
    with open("dataset.json", "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"Generated dataset.json with {len(users)} users and {len(pages)} pages.")

if __name__ == "__main__":
    generate_data(100, 30)
