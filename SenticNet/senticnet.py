raw_data = """<?xml version="1.0"?>
<rdf:RDF
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:dbp="http://dbpedia.org/ontology/"
xmlns:dbprop="http://dbpedia.org/property/"
xmlns:foaf="http://xmlns.com/foaf/0.1/">
	<rdf:Description rdf:about="http://sentic.net/api/en/concept/a_little">
		<rdf:type rdf:resource="http://sentic.net/api/concept"/>
		<text xmlns="http://sentic.net/api">a little</text>
		<semantics xmlns="http://sentic.net/api" rdf:resource="http://sentic.net/api/en/concept/least"/>
		<semantics xmlns="http://sentic.net/api" rdf:resource="http://sentic.net/api/en/concept/little"/>
		<semantics xmlns="http://sentic.net/api" rdf:resource="http://sentic.net/api/en/concept/small_amount"/>
		<semantics xmlns="http://sentic.net/api" rdf:resource="http://sentic.net/api/en/concept/shortage"/>
		<semantics xmlns="http://sentic.net/api" rdf:resource="http://sentic.net/api/en/concept/scarce"/>
		<pleasantness xmlns="http://sentic.net/api" rdf:datatype="http://www.w3.org/2001/XMLSchema#float">-0.99</pleasantness>
		<attention xmlns="http://sentic.net/api" rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</attention>
		<sensitivity xmlns="http://sentic.net/api" rdf:datatype="http://www.w3.org/2001/XMLSchema#float">0</sensitivity>
		<aptitude xmlns="http://sentic.net/api" rdf:datatype="http://www.w3.org/2001/XMLSchema#float">-0.709</aptitude>
		<polarity xmlns="http://sentic.net/api" rdf:datatype="http://www.w3.org/2001/XMLSchema#float">-0.566</polarity>
	</rdf:Description>
</rdf:RDF>"""


#parsed_graph.objects(predicate=URIRef(self.senticapi_base_uri+sentic)).next().toPython()

import rdflib
from rdflib import URIRef
graph = rdflib.Graph()
graph.parse(location='test.rdf.xml')


objects = graph.objects(subject=URIRef("http://sentic.net/api/en/concept/32_teeth"),predicate = URIRef("http://sentic.net/apipolarity"))


for s,p,o in graph:

    print (s)

for o in objects:
    print (o)

