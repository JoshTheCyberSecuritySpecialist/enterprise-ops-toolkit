import random
def setup_cisco_extension(email):
    ext = random.randint(7000, 7999)
    pin = random.randint(1000, 9999)
    print(f"✅ Assigned Cisco extension: {ext} | PIN: {pin}")
    return ext, pin
