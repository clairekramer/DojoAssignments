class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = 0

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry {}, {} Hospital is full".format(patient.name, self.name)
            return self
        else:
            self.patients.append(patient)
            patient.bed += 1
            print patient.name, "has been admitted."
            return self
    def discharge(self, name):
        for patient in self.patients:
            if name == patient.name:
                self.patients.remove(patient)
                patient.bed = 0
                print "{} has been discharged from {}".format(patient.name, self.name)
            return self
    def display_patients(self):
        for patient in self.patients:
            print patient.name
        return self

patient1 = Patient(1, 'Jamee', 'None')
patient2 = Patient(2, 'Bruce', 'Penicilin')
patient3 = Patient(3, 'Greg', 'None')
hospital1 = Hospital('Grey Sloan', 2)
hospital1.admit(patient1).admit(patient2).admit(patient3)
hospital1.discharge('Jamee')
