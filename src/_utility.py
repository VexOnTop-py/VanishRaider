import random, json, re
from colorama import Fore, Style
from base64 import b64encode as b
import httpx
class Utility:
    def getProxy(self):
        return None
    def getBuildNum(self):
        return "133852"
    def getContextProperties(self, guildId: str, channelId: str) -> str:
        return b(json.dumps({"location":"Join Guild","location_guild_id":guildId,"location_channel_id":channelId,"location_channel_type":0}, separators=(',', ':')).encode()).decode()
    def getInviteInfo(self, rawInvite):
        res = httpx.get(f'https://discord.com/api/v10/invites/{rawInvite}?with_counts=true', headers={
        "Authorization": "undefined"}, timeout=30).json()
        return res

class MPrint:
    def w_print(self, message: str):
        """Print warning"""
        print(f"{Fore.WHITE}[{Fore.YELLOW}WARN{Fore.WHITE}] {message}")
    def s_print(self, message: str):
        """Print SUCCESS"""
        print(f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}] {message}")
    def f_print(self, message: str):
        """Print FAIL"""
        print(f"{Fore.WHITE}[{Fore.RED}FAILURE{Fore.WHITE}] {message}")
console = MPrint()