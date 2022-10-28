#!/usr/bin/python3
from pathlib import Path
import re,os
cwd = os.getcwd()
print (cwd)
for file in os.listdir(cwd):
    if file.endswith(".cy.js"):
        p = Path(file)
        print (p)
        lines = p.read_text().splitlines()
        unWantedWords = ['describe(', 'it(']
        
        dirtyGherkin = [s for s in lines if "describe" in s.lower() or "'given" in s.lower() or "'and" in s.lower() or "'when" in s.lower() or "'then" in s.lower()]
        cleanGherkin = [re.sub('[^a-zA-Z0-9\s]+', '', c) for c in dirtyGherkin]
        
        file = file.replace(".cy.js","")
        with open(file+'.feature', 'w') as f:
            for linex in cleanGherkin:
                linex = linex.replace("describe", "Scenario: " )
                linex = linex.replace("itGiven", "Given" )
                linex = linex.replace("itWhen", "When" )
                linex = linex.replace("itAnd", "And" )
                linex = linex.replace("itThen", "Then" )
                f.write(str(linex))
                f.write('\n')