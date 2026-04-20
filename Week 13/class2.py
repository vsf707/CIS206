class Patient:
    def __init__(self, first_name, middle_name, last_name,
                 address, city, state, zip_code,
                 phone, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    # Accessors
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_phone(self):
        return self.phone

    def get_emergency_contact(self):
        return f"{self.emergency_name} - {self.emergency_phone}"

class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charges(self):
        return self.charges

patient = Patient(
    "Issac", "", "Johnson",
    "123 Main St", "Los Angeles", "California", "90011",
    "+1 (323) 777-1001",
    "Jane Johnson", "+1 (323) 111-7777"
)

proc1 = Procedure("Physical Exam", "04/19/2026", "Dr. Irvine", 250.00)
proc2 = Procedure("X-ray", "04/19/2026", "Dr. Jamison", 500.00)
proc3 = Procedure("Blood Test", "04/29/2026", "Dr. Smith", 200.00)

total = proc1.get_charges() + proc2.get_charges() + proc3.get_charges()

print("=== PATIENT INFORMATION ===")
print("Name:", patient.get_full_name())
print("Address:", patient.get_address())
print("Phone:", patient.get_phone())
print("Emergency Contact:", patient.get_emergency_contact())

print("\n=== PROCEDURES ===")
print(f"{proc1.get_name()} | {proc1.get_date()} | {proc1.get_practitioner()} | ${proc1.get_charges():.2f}")
print(f"{proc2.get_name()} | {proc2.get_date()} | {proc2.get_practitioner()} | ${proc2.get_charges():.2f}")
print(f"{proc3.get_name()} | {proc3.get_date()} | {proc3.get_practitioner()} | ${proc3.get_charges():.2f}")

print("\nTOTAL CHARGES: $", f"{total:.2f}")