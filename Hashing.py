users = [
    "ram@gmail.com",
    "Om@gmail.com",
    "prathvi@gmail.com"
]

def login(email):
    for user in users:
        if user == email:
            return "Login Success"
    return "User not found"

print(login("prathvi@gmail.com"))

# In the above code for the username at the last the worst case scenario will be loop will run all the way to the end reading every email which will consume a lot of time and memory (O(n)) time complexity

# To overcome this problem we use hashing

users = {}

#insert
users["ravi@gmail.com"] = "Ravi Sharma"
users["priya@gmail.com"] = "Priya Patel"
users["chirag@gmail.com"] = "Chirag Babu"

print(users["ravi@gmail.com"])