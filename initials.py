
def get_initials(fullname):
    name_input = fullname
    name_chop = name_input.split()
    initializer = ""
    for name in name_chop:
        initializer += name[0].upper()
    return initializer



  

def main():
    fullname = "Earl James Luckett jr the best"
    fully = get_initials(fullname)
    print("The initials for ", fullname,"are",fully ) 

if __name__=="__main__":
    main()