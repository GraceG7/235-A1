class Publisher:

    def __init__(self, publisher_name: str):
        if isinstance(publisher_name, str):
            publisher_name = publisher_name.strip()
            if publisher_name == "":
                self.__name = "N/A"
            else:
                self.__name = publisher_name
        else:
            self.__name = "N/A"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        if isinstance(publisher_name, str):
            if publisher_name.strip() != "":
                self.__name = publisher_name.strip()

    def __repr__(self):
        # we use access via the property here
        return "<Publisher {}>".format(self.__name)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__name == self.__name

    def __lt__(self, other):
        return self.__name < other.__name

    def __hash__(self):
        return hash(self.__name)