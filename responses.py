import random
import requests

def handle_response(username) -> str:
    if username.startswith('help'):
        return "Usage: !leetcode <username> for public or ?leetcode <username> for private"
    else:
        try:
            response = requests.get(f"https://leetcode-stats-api.herokuapp.com/{username}")
            data = response.json()
            total_solved = data['totalSolved']
            easy_solved = data['easySolved']
            medium_solved = data['mediumSolved']
            hard_solved = data['hardSolved']
            ranking = data['ranking']
            
            if ranking == 0:
                return "Please enter a valid leetcode username."

            return f"{username}:\nTotal Solved: {total_solved}\nEasy Solved: {easy_solved}\nMedium Solved: {medium_solved}\nHard Solved: {hard_solved}\nRanking: {ranking}"
        except Exception as e:
            print(e)
            return "Error retrieving user data from LeetCode."
    
    