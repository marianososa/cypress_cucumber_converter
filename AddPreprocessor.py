#!/usr/bin/python3
from pathlib import Path
import os
cwd = os.getcwd()
print (cwd)
for file in os.listdir(cwd):
    if file.endswith(".cy.js"):
        p = Path(file)
        print (p)
        lines = p.read_text().splitlines()
        lines.insert(0, "import{ Given, When, And, Then } from 'cypress-cucumber-preprocessor/steps'")
        dirtyJs = [s for s in lines if not "describe(" in s.lower()]
        del dirtyJs[-1]
        print (dirtyJs)

        with open('cucumber_'+file, 'w') as f:
            for linex in dirtyJs:
                linex = linex.replace("it('Given ", "Given ('" )
                linex = linex.replace("it('When ", "When ('" )
                linex = linex.replace("it('And ", "And('" )
                linex = linex.replace("it('Then ", "Then('" )
                f.write(str(linex))
                f.write('\n')