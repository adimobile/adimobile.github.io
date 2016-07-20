
from dominate import document
from dominate.tags import *
import os
print "root prints out directories only from what you specified"
print "dirs prints out sub-directories from root"
print "files prints out all files from root and directories"
print "*" * 20

excluded_folders=['icons','fonts','js','css','.git','connect-scv','connect-ui','ui-library']
root={}
for item in os.listdir("."):
    if not os.path.isfile(os.path.join(".", item)):
        if (item not in excluded_folders):
            print "Folder: ",item
            subfolders=[]
            for item2 in os.listdir(os.path.join(".", item, "ios")):
                if not os.path.isfile(os.path.join(".", item2)):
                    print "subFolder: ",item2
                    subfolders.append(item2)
            root[item]=subfolders

with document(title='adimobile technical doc') as doc:
    for folder in root:
        h1(folder)
        for sub in root[folder]:
            div(a(sub, href='%s/ios/%s/index.html' % (folder,sub)))

with open('index-ios.html', 'w') as f:
    f.write(doc.render())
print root
