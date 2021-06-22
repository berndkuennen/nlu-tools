
##
## - based on code sample from https://polyglot.readthedocs.io/en/latest/Detection.html
## - uses polyglot to detect language
## - converts polyglot answer to json
##

from polyglot.detect import Detector

import json

mixed_text = u"""
China (simplified Chinese: 中国; traditional Chinese: 中國),
officially the People's Republic of China (PRC), is a sovereign state
located in East Asia.
"""

resultset = { 'records': [], 'count': 0}
count = 0

for language in Detector(mixed_text).languages:
  line = str(language)
  newline = " ".join(line.split())\
  .replace(" read bytes:", ", \"read bytes\":")\
  .replace(" confidence:", "\", \"confidence\":")\
  .replace(" code: ", "\", \"code\": \"")\
  .replace("name: ","\"name\": \"")

  resultset['records'].append( json.loads( "{" + newline + "}" ) )
  count += 1

resultset['count'] = count
print(json.dumps(resultset,indent=4, sort_keys=True))

