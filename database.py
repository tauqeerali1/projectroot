class NEODatabase:
    def __init__(self, neos, approaches):
        self.neos = neos
        self.approaches = approaches

    def get_neo_by_designation(self, designation):
        for neo in self.neos:
            if neo.designation == designation:
                return neo
        return None

    def get_neo_by_name(self, name):
        for neo in self.neos:
            if neo.name == name:
                return neo
        return None

    def query(self, filters):
        for approach in self.approaches:
            if all(f(approach) for f in filters):
                yield approach
