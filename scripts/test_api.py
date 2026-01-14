"""Test script to validate Groq API keys."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("=" * 60)
print("Groq API Key Validator")
print("=" * 60)

if not api_key:
    print("❌ ERROR: GROQ_API_KEY not set in .env or environment")
    sys.exit(1)

print(f"✓ API Key found: {api_key[:20]}...")

try:
    from groq import Groq
    print("✓ Groq library imported successfully")
except Exception as e:
    print(f"❌ Failed to import Groq: {e}")
    sys.exit(1)

try:
    client = Groq(api_key=api_key)
    print("✓ Groq client created")

    # Test with a simple call
    print("\nTesting API call...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Say 'API is working!' briefly."}],
        max_tokens=10,
    )

    result = response.choices[0].message.content.strip()
    print(f"✅ SUCCESS! API is working.")
    print(f"Response: {result}")

except Exception as e:
    error_str = str(e)
    print(f"❌ API Error: {error_str}")

    if "insufficient_quota" in error_str:
        print("\n⚠️  CAUSE: Your Groq account has exceeded quota or no credits.")
        print("   Solution: Check your account at https://console.groq.com/")
    elif "401" in error_str or "invalid" in error_str.lower():
        print("\n⚠️  CAUSE: Invalid or expired API key.")
        print("   Solution: Check your API key at https://console.groq.com/keys")
    elif "429" in error_str:
        print("\n⚠️  CAUSE: Rate limit exceeded.")
        print("   Solution: Wait a moment and try again.")
    else:
        print(f"\n⚠️  CAUSE: {error_str[:200]}")

    sys.exit(1)

print("\n" + "=" * 60)
print("You can now use this API key in the Streamlit app!")
print("=" * 60)
