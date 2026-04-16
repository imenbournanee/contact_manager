def add(self, contact):
        self.contacts.append(contact)
        self.save()

    def delete(self, index):
        if 0 <= index < len(self.contacts):
            removed = self.contacts.pop(index)
            self.save()
            return removed
        return None

    def search(self, query):
        query = query.lower()
        return [
            c for c in self.contacts
            if query in c.name.lower() or query in c.phone or query in c.email.lower()
        ]