
import os
output = os.popen('CI=true npm test src/__tests__/componentTest.js' + '&> Output.txt').read()
with open("Output.txt", "r") as f:
   contents = f.read()
   print(contents)
   if "failed" in contents:
       print("error")
       print(contents)
   else:
       print(contents)

