import pickle

with open('facebook_cookies_01.pkl', 'rb') as file:
    data = pickle.load(file)

print(data)
