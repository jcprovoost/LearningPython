choice = None
sons = {"Harry": ("Jesper","Henk"), "Jan": ("Mark", "Gert"),
            "Ben": ("Bob", "Ben Jr"),}
            
while choice != 0:
    print(""" Choose 1 to search for father, choose 2 to add an entry, choose 3 to remove an entry """)
    choice = int(input('\You chose: '))

    elif choice == 1:
        son = input('What is the name of the son ')
        son = son.title()
        if son in sons:
            print('The father of', son,'is', sons[son][0])
        else:
            print(son,'does not exist.')

    elif choice == 2:
        son = input('What is the name of the son ')
        son = son.title()
        dad = input('What is his dad's name? ')
        sons[son] = (dad.title())

    elif choice == 3:
        son = input('What is the name of the son? ')
        son = son.title()
        if son in sons:
            del sons[son]
            print(son,'has been removed')
        else:
            print(son,'does not exist')
