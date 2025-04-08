import csv
import os
from datetime import datetime

def generate_audit_log(email, vm_created, extension, pin):
    os.makedirs("sample_output", exist_ok=True)
    filename = f"sample_output/onboarding_report_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Email", "VM Created", "Cisco Extension", "PIN"])
        writer.writerow([datetime.now().isoformat(), email, vm_created, extension, pin])
    print(f"✅ Audit log saved: {filename}")
