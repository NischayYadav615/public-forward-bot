import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19911978"))
    API_HASH = os.environ.get("API_HASH", "e3f5848d4c384af9e6f1f52ca84c19c7")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5881103857:AAHalNAze8aCfNsg28TOyrq_Cdc82NIoOHw")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6205468574")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Nischaybot:Nischaybot@cluster0.thf9kzz.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQEv1SoAYi5uLHrFQ9u_7ncA78tbcWP-7KCV7O2tPMg4w6aPSqAGYjZwBS7chvsKVdfvDjOfurGoIsEjDCNSavt0QkSl9MucB9jKDoxMrFz_M_evNISH-ZMGX7f6I48s_m7DfRk3YJ_OmZ717YjdLiHWY63wkBsDysFuN9zWaARrbQRgzZ-CHsVsPQSjmFNzUQ_t83Fl5TqwprU8_1lLiOayHmgCoP3b8svcYTXd9avsFL6_TrznZct4My11lYkDiOoo0ChV9yYyy9bnFH4OH4NNqw-OSpqIhXHK0QgjUHzdPGILtx3INdk0qcxN4tlOPMhuqDEadyILggFwAMS-W5jQ8pA1ZQAAAAFx3eAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001811894401"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Forward_Ny_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
