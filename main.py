from typing import Optional

from ulid import ULID


class ApplicationId:
    def __init__(self) -> None:
        self.__id = ULID()

    def get_id_of_private_value(self) -> str:
        return str(self.__id)


class ApplicationAggregate:
    def __init__(self, secret_key: Optional[str] = None) -> None:
        self.__id = ApplicationId()
        self.__secret_key = secret_key

    def get_id(self) -> str:
        return self.__id.get_id_of_private_value()

    def get_secret_key(self) -> Optional[str]:
        return self.__secret_key


if __name__ == "__main__":
    app1 = ApplicationAggregate()
    app2 = ApplicationAggregate()
    app3 = ApplicationAggregate()

    print(app1.get_id())
    print(app2.get_id())
    print(app3.get_id())
