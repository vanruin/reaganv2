import base64

# Read the encoded file
with open("reaganv2-ENC.py", "rb") as f:
    encoded_data = f.read()

try:
    # Decode the Base64 content
    decoded_data = base64.b64decode(encoded_data)

    # Save the decoded script as a temporary file
    with open("reaganv2-decoded.py", "wb") as f:
        f.write(decoded_data)

    print("Decoded script saved as 'reaganv2-decoded.py'. You can now run it.")

except base64.binascii.Error as e:
    print(f"Error decoding Base64: {e}")
