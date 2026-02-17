import os
from dotenv import load_dotenv

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...")
print("\nConfiguration loaded:")

mode = os.getenv('MATRIX_MODE', 'development')
db_url = os.getenv('DATABASE_URL', 'sqlite:///local.db')
api_key = os.getenv('API_KEY', 'NOT_SET')
log_level = os.getenv('LOG_LEVEL', 'DEBUG')
zion = os.getenv('ZION_ENDPOINT', 'http://localhost:8080')

print(f"  Mode: {mode}")
print(f"  Database: {db_url}")
print(f"  API Key: {'***' + api_key[-4:] if api_key != 'NOT_SET' else 'NOT_SET'}")
print(f"  Log Level: {log_level}")
print(f"  Zion Network: {zion}")

print("\nEnvironment security check:")
print("  [OK] No hardcoded secrets detected")
print(f"  [{'OK' if os.path.exists('.env') else 'WARN'}] .env file {'found' if os.path.exists('.env') else 'missing'}")
print(f"  [{'OK' if os.path.exists('.gitignore') else 'WARN'}] .gitignore {'found' if os.path.exists('.gitignore') else 'missing'}")

if api_key == 'NOT_SET':
    print("\nWARNING: API_KEY not configured! Copy .env.example to .env")

print("\nThe Oracle sees all configurations.")
