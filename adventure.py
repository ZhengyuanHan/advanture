import json
import re
import sys


def print_room_info(cur_room):
    exit_str = 'Exits:'
    item_str = 'Items:'

    print('> ' + cur_room['name'] + '\n')

    if 'environment_desc' in cur_room:
        print(cur_room['desc'])
        print(cur_room['environment_desc'] + '\n')
    else:
        print(cur_room['desc'] + '\n')

    if 'items' in cur_room and len(cur_room['items']) > 0:
        for item in cur_room['items']:
            item_str = item_str + ' ' + item + ','

        print(item_str.rstrip(',') + '\n')

    if 'npc' in cur_room:
        print("npc: " + cur_room['npc']['name'] + '\n')

    if 'exits' in cur_room and len(cur_room['exits']) > 0:

        for exit_dir in cur_room['exits'].keys():
            exit_str = exit_str + ' ' + exit_dir

    print(exit_str + '\n')


# py adventure.py asset.map
# py adventure.py loop.map
if __name__ == '__main__':
    map_name = sys.argv[1]
    with open(map_name, 'r') as f:
        whole_map = json.load(f)

    inventory_list = []

    cur_room = whole_map[0]
    print_room_info(cur_room)
    print('What would you like to do?', end=" ")

    # is_loop = 1
    # verb = input()
    while True:
        try:
            verb = input()

            if re.match(r'\s*go\s*$', verb, re.I):
                print("Sorry, you need to 'go' somewhere.")
                print('What would you like to do?', end=" ")

            elif re.match(r'\s*go\s*(north|south|west|east|northwest|northeast|southwest|southeast)\s*$', verb, re.I):
                direction = re.search(r'(north|south|west|east|northwest|northeast|southwest|southeast)$', verb, re.I).group().lower()
                if direction in cur_room['exits']:
                    room_id = cur_room['exits'][direction]

                    if 0 <= room_id < len(whole_map):
                        if "unlock_condition" in whole_map[room_id] and whole_map[room_id]["unlock_condition"] not in inventory_list:
                            print('The direction is locked, you should find the key first.')
                            print('What would you like to do?', end=" ")
                        else:

                            if whole_map[room_id]["name"] == "system room":
                                if 'h size battery' not in inventory_list:
                                    if 'm size battery' in inventory_list:
                                        print(whole_map[room_id]['lose_desc2'])
                                        break
                                    else:
                                        print(whole_map[room_id]['lose_desc1'])
                                        break
                                else:
                                    print(whole_map[room_id]['win_desc'])
                                    break

                            print('You go ' + direction + '.' + '\n')
                            cur_room = whole_map[room_id]
                            print_room_info(cur_room)
                            print('What would you like to do?', end=" ")

                    else:
                        print("Room does not exist.")
                        print('What would you like to do?', end=" ")

                else:
                    print("There's no way to go " + direction + ".")
                    print('What would you like to do?', end=" ")

            elif re.match(r'\s*look\s*$', verb, re.I):
                print_room_info(cur_room)
                print('What would you like to do?', end=" ")

            elif re.match(r'\s*inventory\s*$', verb, re.I):
                if len(inventory_list) <= 0:
                    print("You're not carrying anything.")
                    print('What would you like to do?', end=" ")
                else:
                    print('Inventory:')
                    for hold in inventory_list:
                        print('  ' + hold)
                    print('What would you like to do?', end=" ")

            elif re.match(r'\s*get\s*$', verb, re.I):
                print("Sorry, you need to 'get' something.")
                print('What would you like to do?', end=" ")

            elif re.match(r'\s*get\s*.+\s*$', verb, re.I):
                item_name = re.search(r'\s*get\s*(.+)\s*$', verb, re.I).group(1).lower()
                if 'items' in cur_room:
                    if item_name in cur_room['items']:
                        inventory_list.append(item_name)
                        cur_room['items'].remove(item_name)
                        print('You pick up the ' + item_name + '.')

                        if cur_room['name'] == "branch road":
                            cur_room['environment_desc'] = cur_room['environment_desc_backup'][0]

                        print('What would you like to do?', end=" ")
                    else:
                        print("There's no " + item_name + " anywhere.")
                        print('What would you like to do?', end=" ")
                else:
                    print("There's no " + item_name + " anywhere.")
                    print('What would you like to do?', end=" ")

            elif re.match(r'\s*talk\s*$', verb, re.I):
                if 'npc' in cur_room:
                    print(cur_room['npc']['name'] + ': ' + cur_room['npc']['dialog'])
                    print('What would you like to do?', end=" ")
                else:
                    print("Nobody around here.")
                    print('What would you like to do?', end=" ")

            elif re.match(r'\s*give\s*$', verb, re.I):
                print("Sorry, you need to 'give' something.")
                print('What would you like to do?', end=" ")

            elif re.match(r'\s*give\s*.+\s*$', verb, re.I):
                gift_name = re.search(r'(?<=give\s).+', verb, re.I).group().lower()
                if gift_name in inventory_list:
                    if 'require' not in cur_room['npc']:
                        print("This guy doesn't need anything.")
                        print('What would you like to do?', end=" ")
                    elif cur_room['npc']['require'] != gift_name:
                        print("This guy doesn't need that.")
                        print('What would you like to do?', end=" ")
                    else:
                        inventory_list.remove(gift_name)
                        print('You give the ' + gift_name + '.')
                        print(cur_room['npc']['name'] + ': ' + cur_room['npc']['answer'] + '\n')
                        cur_room['npc']['dialog'] = cur_room['npc_dialog_after_giving']
                        inventory_list.append(cur_room['npc']['give_back'])
                        print('You get the ' + cur_room['npc']['give_back'] + '.')
                        print('What would you like to do?', end=" ")

                else:
                    print("You are not hanging " + gift_name + ".")
                    print('What would you like to do?', end=" ")

            elif re.match(r'\s*quit\s*$', verb, re.I):
                print("Goodbye!")
                break

            else:
                print("Invalid command, please check your spell.")
                print('What would you like to do?', end=" ")

        except EOFError:
            print("Use 'quit' to exit.")
            print('What would you like to do?', end=" ")
            continue
