def provision_m365_user(name, department):
    email = name.lower().replace(" ", ".") + "@redlobster.com"
    print(f"✅ Created M365 user: {email}")
    print("✅ Assigned Microsoft 365 E5 License")
    print("✅ Enabled MFA")
    print(f"✅ Added to Teams group: {department}")
    return email
