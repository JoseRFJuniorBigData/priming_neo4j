from neo4j import GraphDatabase

NEO4J_URI = "neo4j+s://add8a73c.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "_aqTggbYjpjnjrP7UDJ0RQ5p6cOnpAm_chLL5enPy5U"

class Neo4jConnector:
    def __init__(self, uri, username, password):
        self._uri = uri
        self._username = username
        self._password = password

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._username, self._password))

    def close(self):
        self._driver.close()

    def list_nodes(self):
        with self._driver.session() as session:
            result = session.run("MATCH (n) RETURN n")
            nodes = [record["n"] for record in result]
            return nodes

if __name__ == "__main__":
    neo4j_connector = Neo4jConnector(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    neo4j_connector.connect()
    nodes = neo4j_connector.list_nodes()

    for node in nodes:
        print(node)

    neo4j_connector.close()
