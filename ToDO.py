List = []

def ask():
    return input("What would you like to do? ")

while (True):
    #Ask for entry
    Todo= ask()

    #Stop running
    if Todo.lower()=='stop':
        break

    #Remove entry
    elif 'remove' in Todo.lower():
        item=int(input('Which item would you like to remove?'))
        List.pop(item-1)

    #Change entry
    elif 'change' in Todo.lower():
        item=int(input('Which item would you like to change?'))
        List[item-1]= ask()

    #Add entry
    else:
        List.append(Todo)

    #List entries
    for i in range(0,len(List)):
        print(str(i+1)+": "+List[i])

