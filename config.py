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
    SESSION = os.environ.get("SESSION", "BQF5M1cAoCtVPAPW-yFetlKbxbjuEjqKkOGDv-i0-BGtXkVmbGr_0Qa26Em_aZow-AYxungNmXVKc8a1cbKbzqxisYGcrDoDyHj2P-SuPG-qsfaekxJPDPoLAEhLX-CfXcHCs3HTiOkNG9JsVSC2mmvYxLjOQxNn6UfZr4Y_tQSfAW1Ex7_UBvytbuUTVnhkk-ek_4tQ2HdcSzpOTFHD1W3DzjmkP92Py9bpNG5XzAUAvZ6R-yHxp_jdXGM7dhd-LvPGnrVR87ufVX1JJma_pvLOz4b6Cra0paCGTC_L55g7dnV8wGJeL-GN3y1DZ6Uoy6r67Qw4PlCWxnrzao7d1Jzz82b4EAAAAAF3PrMGAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001553031624"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NY_Forward_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
