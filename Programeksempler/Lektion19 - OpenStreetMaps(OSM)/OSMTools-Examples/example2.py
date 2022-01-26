"""Example 2
What is the English name of the church called "Stephansdom", what address does it have, and which of which denomination is the church?
We use the Overpass API to query the corresponding data:
"""
from OSMPythonTools.overpass import Overpass
overpass = Overpass()
result = overpass.query('way["name"="Stephansdom"]; out body;')
#This time, the result is a number of objects, which can be accessed by result.elements(). We just pick the first one:

stephansdom = result.elements()[0]
#Information about the church can now easily be accessed:

stephansdom.tag('name:en')
# "Saint Stephen's Cathedral"
'%s %s, %s %s' % (stephansdom.tag('addr:street'), stephansdom.tag('addr:housenumber'), stephansdom.tag('addr:postcode'), stephansdom.tag('addr:city'))
# 'Stephansplatz 3, 1010 Wien'
stephansdom.tag('building')
# 'cathedral'
stephansdom.tag('denomination')
# 'catholic'

print((stephansdom.tag('addr:street'), stephansdom.tag('addr:housenumber'), stephansdom.tag('addr:postcode'), stephansdom.tag('addr:city')))
