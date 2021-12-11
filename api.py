from config import *
from requests.auth import HTTPBasicAuth

headers = {
    'Accept': 'application/json',
    'Authorization': API_KEY
    }

def fetch_current_price(slug:str):
    "Fetch Data For Standard Price"

    res = requests.get(
        f"https://api-beta.stakingrewards.com/v1/assets/overview/{slug}",
        headers= headers
    ).json()
    
    
    if 'message' in res.keys():
        return None, res['message']
    
    elif res['price'] == 0:
        return None, "Invalid Slug"
    
    else:
        return res, None