paths = {
    "entrance" : {
        "description" : 'You have reached the entrace of the giant maze....',
        "exits" : {"north": 'stone_door'},
        "items" : []
    },
    "stone_door": {
        "description" : 'You have reached a huge stone door....',
        "exits" : {"west": 'hidden_shrine' , "east": 'dark_forest'},
        "items" : ['magical_orb']
    },
    "dark_forest": {
        "description":'You have reached the dark forest area ...',
        "exits": {"west": 'stone_door'},
        "enemy": 'snake',
        "items": []
        },
    "hidden_shrine": {
        "description" : 'You have reached the hidden shrine of and unknown deity ...',
        "exits" : {"east":'stone_door'},
        "items" : ['sword']
    }
}
inventory = []
current_room = 'entrance'
game_over = False 
def describe_room(room):
    print (paths[room]['description'])
    print(paths[room]['exits'])
    if  paths[room]['items']:
        print(f"There is {','.join(paths[room]['items'])}")
    elif 'enemy' in paths[room]:
        print(f"A bloody {paths[room]['enemy']} is here !!!")


def process_command(command):
    global current_room,inventory,game_over
    #command to quit

    if command in ['quit' , 'exit']:
        print('Thanks for playing!')
        game_over=True
        return
    #command for moving

    elif command.startswith('go'):
        direction = command.split()[1]
        if direction in paths[current_room]['exits']:
            current_room = paths[current_room]['exits'][direction]
            describe_room(current_room)
        else: 
                print("You can't go that way !!!")

    #command for taking items
    elif command.startswith('take '):
        item = command.split()[1]
        if item in paths[current_room]['items']:
            inventory.append(item)
            paths[current_room]['items'].remove(item)
            print(f"You took the{item}")
        else:
            print("There is nothing here except dust and shiny things !")
        #Check inventory
    elif command == 'inventory':
        if inventory:
            print(inventory)
        else: 
            print("No items present in it")
    
    #command for opening door
    elif current_room == 'stone_door' and command =='use key' and 'ancient key' in inventory:
        print("You have found the legendary treasure within . ")
        game_over=True
     
    #command for killing snake
    elif command in ['use sword','use_magical orb'] and ('sword' in inventory or 'magical orb' in inventory) and 'enemy' in paths[current_room]:
        if 'snake' in paths[current_room].get('enemy',''):
            if 'sword' in inventory and 'magical_orb' in inventory:
                print("You have killed the snake . Good job ! You have gotten an ancient key")
                inventory.append('ancient key') 
                del paths[current_room]['enemy']
            elif'sword' in inventory or 'magical_orb' in inventory:
                print("You have almost killed the snake but died of poison !!")
                game_over=True
        else:
            print("There is no enemy to fight")

    #Invalid command 
    else: 
        print("What the hell! GET LOST !!!")
        game_over = True
    #Main game loop
print("Welcome to the mystery temple ")
describe_room(current_room)

while not game_over:
    command = input ("\n>").lower()
    process_command(command)


              
