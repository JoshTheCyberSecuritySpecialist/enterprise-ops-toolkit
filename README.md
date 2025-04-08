# Enterprise IT Operations & Access Control Toolkit (Simulated)

Simulates secure, multi-platform enterprise onboarding including Office 365, VMware, macOS (Jamf), and Cisco Call Manager.

## 💡 What It Does
- Provision M365 user accounts (with Teams & MFA)
- Simulate VM creation using templates (VMware Workstation)
- Simulate macOS Jamf enrollment with FileVault
- Assign Cisco CME phone extension + PIN
- Generate CSV audit logs

## 🚀 How to Run
```bash
python run_onboarding_flow.py
```

## 🧠 Why It Matters
This simulates real-world enterprise onboarding:
- Identity, device, and access lifecycle
- Microsoft 365, Apple, Cisco, VMware coordination
- End-to-end audit trail for compliance

## Workflow Overview

## 📝 Onboarding Process Notes

### 🔹 Create M365 Account
- Set up user account in Microsoft 365 (M365)
- Ensure correct user details and role assignment

### 🔹 Assign License
- Allocate appropriate M365 license (e.g., Business Standard, E3)
- Confirm license activation for services (Outlook, Teams, etc.)

### 🔹 Enable MFA
- Activate Multi-Factor Authentication (MFA) for account security
- Guide user through MFA setup (authenticator app, SMS, etc.)

### 🔹 Add to Teams Group
- Include user in relevant Microsoft Teams group(s)
- Ensure access to correct channels and permissions

### 🔹 Provision VMware VM
- Create and configure VMware virtual machine
- Assign resources (CPU, memory, storage) based on user needs
- Provide access credentials to the user

### 🔹 Enroll macOS Device in Jamf
- Register user’s macOS device into Jamf for MDM
- Apply configuration profiles and security policies

### 🔹 Assign Cisco Phone Extension
- Allocate unique Cisco VoIP phone extension
- Configure user profile in Cisco Unified Communications Manager

### 🔹 Generate Audit Log
- Document all onboarding actions in an audit log
- Include timestamps, responsible personnel, and status of each step
