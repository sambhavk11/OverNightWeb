__author__ = 'sambhav'
path='~/News-Query/JSON/'
fname="dummy.json"
def transContent(search_key):
    if search_key=='Aston Martin':
        fname='JSON/AstonMartin.json'
        print fname
    elif search_key=='Najib Razzak':
        fname='JSON/NajibRazak.json'
        print fname
    elif search_key=='Amari Boulevard':
        fname='JSON/AmariBoulevard.json'
        print fname
    elif search_key=='Fairmont':
        fname='JSON/Fairmont.json'
        print fname
    elif search_key=='Fraser Suites':
        fname='JSON/FraserSuites.json'
        print fname
    elif search_key=='Grand Hyatt':
        fname='JSON/GrandHyatt.json'
        print fname
    elif search_key=='Gran Melia':
        fname='JSON/GranMelia.json'
        print fname
    elif search_key=='Novotel':
        fname='JSON/Novotel.json'
        print fname
    elif search_key=='Robertson Quay':
        fname='JSON/RobertsonQuay.json'
        print fname
    else:
        fname='dummy2.json'
        print("No match found")

    with open(fname, "r") as src:
        with open("dummy.json", "w") as target:
            target.write(src.read())