import os, sys
try:
    __import__("bookmark_enc").main()
except Exception as e:
    exit(str(e))
