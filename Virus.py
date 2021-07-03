import HelperFunctions as hf


# Ο ιός της προσομοίωσης
class Virus:
    def __init__(self, file):
        self.data = hf.read_virus_file(file)

        self.name = self.data["name"]
        self.symptoms = self.data["symptoms"]

        self.general_transmission = self.data["general_transmission"]
        self.mask_transmission = self.data["mask_transmission"]
        self.distance_transmission = self.data["distance_transmission"]

        self.recovery_rate = self.data["recovery_rate"]
        self.mortality_rate = self.data["mortality_rate"]
