from scripts.m365_provisioning import provision_m365_user
from scripts.macos_enrollment import enroll_macos
from scripts.cisco_extension_setup import setup_cisco_extension
from scripts.generate_audit_log import generate_audit_log

def main():
    name = input("Enter full name: ")
    department = input("Department: ")
    device = input("Primary device [macOS/Windows]: ")

    email = provision_m365_user(name, department)
    
    vm_created = f"{department}Template01"
    print(f"✅ Created VM image: {vm_created} on VMware Workstation (simulated)")
    
    if device.lower() == "macos":
        enroll_macos(email)

    extension, pin = setup_cisco_extension(email)
    
    generate_audit_log(email, vm_created, extension, pin)

if __name__ == "__main__":
    main()
