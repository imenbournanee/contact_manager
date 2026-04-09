import json
import os

FILE = "contacts.json"


class Contact:
    def init(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


class ContactManager:
    def init(self):
        self.contacts = self.load()

    def load(self):
        if os.path.exists(FILE):
            with open(FILE) as f:
                return json.load(f)
        return []

    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.contacts, f, indent=2)