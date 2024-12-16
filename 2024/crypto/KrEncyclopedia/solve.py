import random
import string 
import requests

alphabet = string.ascii_lowercase

def fetch_random_wikipedia_article():
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "format": "json",
        "action": "query",
        "generator": "random",
        "grnnamespace": 0,
        "prop": "extracts",
        "exchars": 4000,
        "explaintext": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        pages = data["query"]["pages"]

        for page_id, page_data in pages.items():
            return page_data["extract"]
            

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Wikipedia: {e}")

def fetch_random_encryptedarticle():
    
    try:
        url = "http://localhost:5000/wiki"
        response = requests.get(url)
        data = response.text.split('\n')[5][3:-4]
        return data
    except:
        print("Error requesting article")
def fetch_flag():

    try:
        url = "http://localhost:5000/flag"
        response = requests.get(url)
        data = response.text.split('\n')[5][3:-4]
        return data
    except:
        print("Error requesting article")

# frequency_dict = {}

# for i in range(0,200):
#     randomArticle = fetch_random_wikipedia_article().lower()
#     res = ''.join(list(filter(lambda ch: ch in alphabet, randomArticle)))
#     for c in res:
#         try:
#             frequency_dict[c] += 1
#         except:
#             frequency_dict[c] = 1
# sortedFreq = dict(sorted(frequency_dict.items(), reverse=True, key=lambda item: item[1]))
# print(sortedFreq)

# encryptedFreq = {}
# for i in range(0,200):
#     randomArticle = fetch_random_encryptedarticle().lower()
#     res = ''.join(list(filter(lambda ch: ch in alphabet, randomArticle)))
#     for c in res:
#         try:
#             encryptedFreq[c] += 1
#         except:
#             encryptedFreq[c] = 1

# encryptedFreqSorted = dict(sorted(encryptedFreq.items(), reverse=True, key=lambda item: item[1]))
# print(encryptedFreqSorted)

#already ran data to make testing faster, uncomment above code if you want to run it.
sortedFreq = {'e': 16370, 'a': 13178, 't': 11015, 'i': 10945, 'n': 10645, 'o': 9875, 'r': 9610, 's': 9420, 'h': 6401, 'l': 6247, 'd': 5370, 'c': 4843, 'm': 3662, 'u': 3622, 'f': 3174, 'p': 2802, 'g': 2795, 'b': 2471, 'y': 2262, 'w': 2254, 'v': 1386, 'k': 1116, 'j': 382, 'x': 263, 'z': 247, 'q': 126}
encryptedFreqSorted = {'t': 16145, 'b': 13092, 'c': 11353, 'o': 10861, 's': 10685, 'w': 9844, 'i': 9622, 'y': 9237, 'v': 6146, 'x': 5888, 'l': 5296, 'g': 4791, 'f': 3727, 'k': 3656, 'u': 3209, 'h': 2853, 'j': 2645, 'a': 2277, 'm': 2234, 'n': 2097, 'z': 1461, 'e': 1099, 'q': 480, 'p': 258, 'r': 248, 'd': 122}


cipherKey = dict(zip(encryptedFreqSorted, sortedFreq))
print(cipherKey)
eFlag = fetch_flag()
flag = ''.join(list(map(lambda ch: cipherKey[ch], eFlag)))
print(flag)