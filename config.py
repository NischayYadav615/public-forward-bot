import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24720215"))
    API_HASH = os.environ.get("API_HASH", "c0d3395590fecba19985f95d6300785e")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5858006797:AAHvD6U81nTd40oK5r_PSq0Q0HUWy__GVoI")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6295565062")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQF5M1cAStKsn0Edn3gnmRVdaiKalRyaZ6taJkfpK9ctkOcKs50MYhPGeQj6Ge7FzO89KquRKQ-IhpnMWH3VOsNFLLRbgsVIw8UTP4EGMXjS2AUcqo7B-bm1fYbNyztFKXacIC9jIu6i4A_hPhh7XoshQwJPtKeN90TEyNP5ZQQtbHiKMxQbPyFEUqXR3q7m071OguoWykIHujBLYIJ0s8O5VjNvcPA29dG6W6LdIuNvYXKP5oWrAAtknRW2Jo7s316Ph88gqub7NVV6qXhpf92_pDobosBfeg4o2uxtwMg2PE3X_wB9zKenZOK453LpwJHW2i5IRbj3Wr4WZW9HocPPuPVQxQAAAAF3PrMGAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001553031624"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NY_Forward_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
