import urllib.parse
import rdflib
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import FOAF, RDF

from SPARQLWrapper import SPARQLWrapper, BASIC, POST

import requests

import logging

try:
    # query api
#    result = requests.get(url = "https://dog.ceo/api/breeds/image/random", timeout=2 )
    result = requests.get(url = "https://reqres.in/api/users", timeout=2 )
    import time
    time.sleep(2)
    if result.ok :
        responseJSON = result.json()
        print(responseJSON)
        namedGraph = Graph()
        namedGraph.bind("foaf", FOAF)

        # connect to GraphDB
        sparql = SPARQLWrapper("http://127.0.0.1:7200/repositories/curso-kg/statements")
        sparql.setMethod(POST)

        # create named graph
        for entry in responseJSON['data']:
            url_encode = urllib.parse.quote(str(entry['id']))
            person = URIRef(f'http://example.org/people/{url_encode}')
            firstName = Literal(entry['first_name'])
            lastName = Literal(entry['last_name'])
            mailbox = Literal(entry['email'])
            thumbnail = Literal(entry['avatar'])

            namedGraph.add((person, RDF.type, FOAF.Person))
            namedGraph.add((person, FOAF.firstName, firstName))
            namedGraph.add((person, FOAF.lastName, lastName))
            namedGraph.add((person, FOAF.mbox, mailbox))
            namedGraph.add((person, FOAF.thumbnail, thumbnail))

            for s, p, o in namedGraph:
                if o.__class__ == rdflib.term.Literal:
                    query = f""" 
                        INSERT DATA {{
                            GRAPH <http://example.org/toy/graph> {{
                                <{s}> <{p}> "{o}"
                            }}
                        }}
                    """
                else:
                    query = f""" 
                        INSERT DATA {{
                            GRAPH <http://example.org/toy/graph> {{
                                <{s}> <{p}> <{o}>
                            }}
                        }}
                """
                logging.info(query)
                print(query)
                sparql.setQuery(query)
                sparql.query()
    else:
        Exception("Request returns empty")

except Exception as e:
    logging.error(F"Error when querying the API: {e}")