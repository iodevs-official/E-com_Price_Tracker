
import os

class Telegram():
  API_ID = 
  API_HASH = ""
  BOT_TOKEN = ""
  BOT_NICKNAME = "ecom-tracker"  

  ADMIN = 6883997969


  #Foece Sub
  Fusb_name = "@botio_devs"  #channel user name with @
  Fsub_ID = -1002054575318
  Fsub_Link = "https://t.me/+T-rFTAhNFIRkMTc1" #Custom Invite Link to track User Joining

  #LOGGING
  SEND_JOIN_LOG = True
  JOIN_LOG_CHANNEL = LOG_CHANNEL_ID = ERROR_LOGGER_ID = -100
  CHECKER_LOG_TOPIC = 
  ERROR_LOGGER_TOPIC = 

  
  #Button Link
  UPDATES_CHANNEL = "https://t.me/botio_devs"
  SUPPORT_CHANNEL = "https://t.me/botio_devs_discuss" 
  

class Db():
  MONGO_URI = ""
  DB_NAME = "ecom-tracker"

  
class Server():
  PORT = 8080
  IS_SERVER = os.getenv("IS_SERVER", False)
