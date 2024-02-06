
import requests
import json

class GetPrograms:

  def get_programs(self):
  #   URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    URL = "https://data.cityofnewyork.us/resource/dsg6-ifza.json"

    response = requests.get(URL)
    return response.content

  def programs_agencies(self):
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program["centername"])

    return programs_list

# programs = GetPrograms().get_programs()
# print(programs)
  
programs = GetPrograms()
agencies = programs.programs_agencies()

##create a set to avoid duplicates!!
for agency in set(agencies):
  print(agency)