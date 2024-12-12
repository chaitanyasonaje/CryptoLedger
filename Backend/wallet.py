from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

class Wallet:
    def __init__(self):
        # Generate a new private key
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        # Derive the public key from the private key
        self.public_key = self.private_key.public_key()

    def get_public_key(self):
        # Return the public key in PEM format (readable text)
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def sign_message(self, message):
        # Sign a message (transaction) using the private key
        return self.private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    @staticmethod
    def verify_signature(public_key_pem, message, signature):
        # Verify a signature using the public key
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create a new wallet
    wallet = Wallet()

    # Generate public key
    public_key = wallet.get_public_key()
    print("Public Key:", public_key)

    # Sign a transaction (message)
    message = "Transfer 10 coins to Alice"
    signature = wallet.sign_message(message)
    print("Signature:", signature)

    # Verify the transaction
    is_valid = Wallet.verify_signature(public_key, message, signature)
    print("Signature valid?", is_valid)
