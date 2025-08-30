# secrets-example.py
# Demo: intentionally hard-coded "secret" using a custom format


def connect_to_service():
    demo_token = "CSEC_DEMO_7L4YJ4Q5Q9X5B2K8D6M1R2A0ABCDEF1"
    print(f"Using demo token: {demo_token[:18]}...")

if __name__ == "__main__":
    connect_to_service()
