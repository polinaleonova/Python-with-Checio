# -*- coding: utf8 -*-


class Friends:

    """
    Returns a new Friends instance. "connections" is an iterable of sets with
        two elements in each. Each connection contains two names as strings.
    Connections can be repeated in the initial data, but inside it's stored once.
    Each connection has only two states - existing or not.
    """

    def __init__(self, connections):
        self.connections = {frozenset(con) for con in connections}

    def add(self, connection):
        """
        Add a connection in the instance;
        :param connection: a set of two names (strings)
        :return:True  - if this connection is new;
                False  - if this connection exists already
        """
        if connection in self.connections:
            return False
        else:
            self.connections.add(frozenset(connection))
            return True

    def remove(self, connection):
        """
        Remove a connection from the instance;
        :param connection: a set of two names (strings)
        :return: True - if this connection exists.
                False - if this connection is not in the instance.
        """
        if connection in self.connections:
            self.connections.discard(frozenset(connection))
            return True
        else:
            return False

    def names(self):
        """

        :return:Returns a set of names. The set contains only names which
                are connected with somebody.
        """
        self.names = set()
        for con in self.connections:
            for item in con:
                self.names.add(item)
        return self.names

    def connected(self, name):
        """

        :param name: string
        :return: a set of names which is connected with the given "name"
                 If "name" does not exist in the instance, then return an empty set.
        """
        self.connected = set()
        for connection in self.connections:
                if name in connection:
                    tmp_list = list(connection)
                    tmp_list.remove(name)
                    self.connected.add(tmp_list[0])
        if len(self.connected) == 0:
            return set()
        return self.connected



f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
