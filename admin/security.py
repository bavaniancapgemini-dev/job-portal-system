
import hashlib
import secrets


def hash_password(password):

    salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        200000
    ).hex()

    return f"pbkdf2_sha256${salt}${password_hash}"


def verify_password(password, stored_password):

    try:

        algorithm, salt, original_hash = stored_password.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            200000
        ).hex()

        return secrets.compare_digest(
            new_hash,
            original_hash
        )

    except ValueError:
        return False
