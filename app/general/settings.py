import os
from datetime import datetime

server_name = os.environ['SERVER_NAME']

date = datetime.today().strftime('%Y-%m-%d')
mods_folder = "/minecraft/mods"
