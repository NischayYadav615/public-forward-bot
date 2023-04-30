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
    SESSION = os.environ.get("SESSION", "BQBUyUojyblmG27wrfszzn92imiyQUrZ2pSzSgfm-r3_Vo14zycW3tozW3LbWcP3uEHzpj2kZQQ7UZdD6zBz8JDgbGNl7-6Rr4wCg8v6FxLhvyWORNr1ECwMRAyIabXvp3-czmsU-dBgYKuNaduCM34ZRj53VMlV_IwvVVFAQBFQAELlvxpBJBgyqD-uSk10b2HRE-nBgq738Ic6VCNZT8JuNajcQBlRd57ugmgIP_ZLu-csDwIm-SwqwJb1XusLeE4vscrIY1gvnOiI_q3urdis8SPM5DvPIlBLK1Va86M43dYgZwaNcQLRXlR85GNEmPUvPh0mkavf-UbckLV3mUicAAAAAXc-swYA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001553031624"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NY_Forward_robot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
