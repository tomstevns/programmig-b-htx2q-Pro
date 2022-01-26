"""Example 1
Which object does the way with the id 5887599 represent?

We can use the OSM API to answer this question:
"""
from OSMPythonTools.api import Api
api = Api()
way = api.query('way/5887599')
#The resulting object contains information about the way, which can easily be accessed:

way.tag('building')
# 'castle'
way.tag('architect')
# 'Johann Lucas von Hildebrandt'
way.tag('website')
# 'http://www.belvedere.at'

print("The build is a",way.tag('building'))
print("The architect of this building is",way.tag('architect'))
print("You can find more information here", way.tag('website'))
#Please implement other tags
