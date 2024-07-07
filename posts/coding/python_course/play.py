import time
import sys

loading = ['|', '/', '-', '\\']
sys.stdout.write('\n\n')
for i in range(1000):
    sys.stdout.write(f"{loading[i % len(loading)]}\r")
    time.sleep(0.15)
