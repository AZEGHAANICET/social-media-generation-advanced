from fastapi import HTTPException
from typing import Optional, Dict
import requests
import streamlit as st
class APIClient:
    def __init__(self, base_url:str="http://localhost:8000"):
        self.base_url = base_url

    def generate_caption(self, data:Dict)->Optional[Dict]:
        try:
            response = requests.post(f"{self.base_url}/api/generate/caption", json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def generate_hashtags(self, data: Dict) -> Optional[Dict]:
        try:
            response = requests.post(f"{self.base_url}/api/generate/hashtags", json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            st.error(f"API Error: {str(e)}")
            return None

    def generate_post_ideas(self, data: Dict) -> Optional[Dict]:
        try:
            response = requests.post(f"{self.base_url}/api/generate/post-ideas", json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            st.error(f"API Error: {str(e)}")
            return None