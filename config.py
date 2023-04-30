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
    SESSION = os.environ.get("SESSION", "BQBJuGXKH7Y4JMYe8Ryxed9WPrlH6aWi4SP7lwAhJHl3LLy6Mhf4CEg1D63DyyQy6UNWowDLUYOk9xR8vd0SY5XvjkXiXtrcoVT6dw9LG979AzxDsUHDRvFHRVZhLhI_PC1oVBXSHHPgRvQUW8tivo1dyxvBZJQImEDmk84fxzW1haI9vdpihsHLqHmbHKBU7EYp42YB_jNYA3H0ycju-DCR64A2gm2G4i58JVTIKyNfPL5JDp8eXe6tjK2hwPTxO90COKBUmWWZJgGFxaeuG6EcnxUxrmH1S43GtAM_SE3bnQNG18aXjopj0Sngo32-pKm7LRKDlDRxjqC4rfzXMNnjAAAAAXc-swYA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001553031624"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NY_Forward_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
