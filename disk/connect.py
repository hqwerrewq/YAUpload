from dotenv import find_dotenv, load_dotenv
import os
import yadisk

load_dotenv(find_dotenv())

client = yadisk.AsyncClient(token=os.getenv('DISK_TOKEN'))
