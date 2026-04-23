import os

print("Running BOLA Test...")
os.system("python scanner/bola_test.py")

print("\nRunning Rate Limit Test...")
os.system("python scanner/rate_limit_test.py")

print("\nChecking API Key Exposure...")
os.system("python scanner/api_key_test.py")
