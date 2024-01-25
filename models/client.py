class Client():
    def __init__(self, id:str, name:str, email:str, cel:str) -> None:
        self.__id = id
        self.__name = name
        self.__email = email
        self.__cel = cel

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def set_name(self, name:str):
        self.__name = name
        return
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email:str):
        self.__email = email
        return
    
    def get_cel(self):
        return self.__cel
    
    def set_cel(self, cel:str):
        self.__cel = cel
        return
    
    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "cel": self.__cel
        }