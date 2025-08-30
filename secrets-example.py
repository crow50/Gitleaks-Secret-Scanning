# secrets-example.py
# Demo: intentionally hard-coded "secret" using a custom format
# NOTE: This should bypass GitHub's native secret scanning/push protection,
#       but be caught by Gitleaks via a custom rule.

def connect_to_service():
    demo_token = "CSEC_DEMO_7L4YJ4Q5Q9X5B2K8D6M1R2A0ABCDEF1"  # 32 chars after prefix
    print(f"Using demo token: {demo_token[:18]}...")

if __name__ == "__main__":
    connect_to_service()
