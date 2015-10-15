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
    elif search_key=='Melia Bali':
        fname='JSON/MeliaBali.json'
        print fname
    else:
        fname='dummy.json'
        print("No match found")

    with open(fname, "r") as src:
        with open("dummy.json", "w") as target:
            target.write(src.read())