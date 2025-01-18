import asyncio
import random
import time 
turn = 1
from datetime import datetime
from rich.console import Console
from the_finnal_file import finall_task
from save_game import take_table , p1walls , p2walls , loc1 , loc2 , savethegame 
player_loc = {
}
player_1_walls = 0
player_2_walls = 0
Console = Console()
from rich.panel import Panel


gameid = 0

table = []

# table[0][8] = [2]
# table[16][8] = [1]


# table =  [
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [2] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] ,
# [[0] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [1] , [0] , [0] , [0] , [0] , [0] , [0] , [0] , [0]] 
# ]
# ⚫⚪⚫⚪⚫⚪⚫⚪🔵⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪🔴⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪🔵⚪⚫⚪⚫⚪⚫⚪⚫
# ⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪
# ⚫⚪⚫⚪⚫⚪⚫⚪🔴⚪⚫⚪⚫⚪⚫⚪⚫


async def UP_check():
    global table
    if turn == 2 and player_loc["player_2"][0] == 1: 
        pass # tah row bashe
    elif table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
        pass#divar jelosh bashe
    elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1] :
        if player_loc[f"player_{turn}"][0]-4 < 0 or player_loc[f"player_{turn}"][0]-5 < 0:
            pass # age ziadi bala bashe o bere akhar table
        else:
            table[player_loc[f"player_{turn}"][0]-5][player_loc[f"player_{turn}"][1]-1] = [3] # player jelosh bashe o divar jelosh nabashe
    elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
        try:
            if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [0]:
                table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] = [3]
        except:
            pass
        if (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] == [0]) and player_loc[f"player_{turn}"][1]-3 >= 0:
            table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] = [3]
    else:
        table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] = [3] # jelosh chizi nabashe o ok bashe


async def DOWN_check():
    global table
    try:
        if turn == 1 and player_loc["player_1"][0] == 17: 
            pass # aval row bashe
        elif table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [1]:
            pass#divar poshtesh bashe
        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and (table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1]):
            try:
                if table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] == [0]:
                    table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] = [3]
            except:
                pass
            if (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] == [0]) and player_loc[f"player_{turn}"][1]-3 >= 0:
                table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] = [3]


        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1] :
            if player_loc[f"player_{turn}"][0]+2 > 17 :
                pass # age ziadi paiin bashe o bere birone table
            else:
                table[player_loc[f"player_{turn}"][0]+3][player_loc[f"player_{turn}"][1]-1] = [3] # player paiinesh bashe o divar poshtesh nabashe
        else:
            table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] = [3] # paiinesh chizi nabashe o ok bashe
    except:
        pass





async def LEFT_check():
    if player_loc[f"player_{turn}"][1] == 1: 
            pass # sar radif bashe
    elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [1]:
            pass#divar chapesh bashe
    elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and not table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1] :
        if player_loc[f"player_{turn}"][1]-3 < 0 or player_loc[f"player_{turn}"][1]-5 < 0:
            pass # age ziadi chap bashe o bere akhar radif
        else:
            table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-5] = [3] # player jelosh bashe o divar jelosh nabashe
    elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1]: #  player poshtesh bashe o divar poshtesh bashe
            if player_loc[f"player_{turn}"][0]+1 > 17:
                pass 
            else:
                if table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] == [0]:
                    table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] = [3]
            if player_loc[f"player_{turn}"][0]-3 < 0:
                pass 
            else:
                if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] == [0]:
                    table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] = [3]
    else:

        table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] = [3] # jelosh chizi nabashe o ok bashe




async def RIGHT_check():
    global table
    try:
        if player_loc[f"player_{turn}"][1] == 17: 
            pass # akhar radif bashe
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
            pass #divar jelosh bashe
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [0] :
            if player_loc[f"player_{turn}"][1]+2 > 17 or player_loc[f"player_{turn}"][1]+4 > 17:
                pass # age ziadi paiin bashe o bere birone table
            else:
                table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+3] = [3] # player jelosh bashe o divar jelosh nabashe
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]: #  player poshtesh bashe o divar poshtesh bashe
            if player_loc[f"player_{turn}"][0]+1 > 17:
                pass 
            else:
                if table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] == [0]:
                    table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] = [3]
            if player_loc[f"player_{turn}"][0]-3 < 0:
                pass 
            else:
                if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [0]:
                    table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] = [3]
        else:
            table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] = [3] # jelosh chizi nabashe o ok bashe
    except:
        pass



def delete_yellows():
    for row in range(17):
        for radif in range(17):
            if table[row][radif] == [3]:
                table[row][radif] = [0]


def finishthegame():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    dictionary = {
    "player1_username": player_loc["player_1"][-1],
    "player2_username": player_loc["player_2"][-1],
    "p1walls": player_1_walls,
    "p2walls": player_2_walls,
    "player1_position": player_loc["player_1"][:-1],
    "player2_position": player_loc["player_2"][:-1],
    "table": table,
    "current_turn": f"{player_loc["player_1"][-1] if turn == 1 else player_loc["player_2"][-1]}",
    "timer": round(time.time(),2),
    "game_result": "Finished",
    "date" : formatted_time
    }
    savethegame(gameid , dictionary)
    winner = player_loc[f"player_{turn}"][-1]
    if turn == 1:
        loser = player_loc["player_2"][-1]
    else:
        loser = player_loc["player_1"][-1]
    finall_task(winner , loser)




async def table_printer():
    global table
    await UP_check()
    await DOWN_check()
    await LEFT_check()
    await RIGHT_check()
    for num in range(17):
        table_text = ""
        row = table[num]
        if not num % 2:
            for block in range(len(row)):
                if not block % 2:
                    if row[block] == [0] :
                        table_text += "⚫"
                    elif row[block] == [1]:
                        table_text += "🔴"
                    elif row[block] == [2]:
                        table_text += "🔵"
                    else:
                        table_text += "🟡"
                else:
                        if row[block] == [0]:
                            table_text += "⚪"
                        else:
                            table_text += "🧱"
        else:
            for block in range(len(row)):
                if row[block] == [0]:
                    table_text += "⚪"
                elif row[block] == [1]:
                    table_text += "🧱"
        print(table_text)
    delete_yellows()

        


def update_player_location(x , y):
    global player_loc
    player_loc[f"player_{turn}"][0] = x
    player_loc[f"player_{turn}"][1] = y




def update_move_actions( x , y , turn ):
    global table
    table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-1] = [0]
    table[x][y] = [turn]




def swap_turn():
    global turn
    if turn == 1 :
        turn = 2
    else:
        turn = 1


def check_winner():
    return False if player_loc["player_1"][0] == 1 or player_loc["player_2"][0] == 17 else True




async def check_move(move):
    global player_loc , turn , table
    if move == "w":
        if turn == 2 and player_loc["player_2"][0] == 1:
            Console.print("You can't go higher than this!", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("The wall is ahead!", style=" red ")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
            Console.print("There's a wall behind the player! You can't.", style=" red ")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1] :
            if player_loc[f"player_{turn}"][0]-4 < 0 or player_loc[f"player_{turn}"][0]-5 < 0:
                Console.print("You can't go higher than this!", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-5 , player_loc[f"player_{turn}"][1]-1 , turn )
                update_player_location(player_loc[f"player_{turn}"][0]-4 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
            else:
                finishthegame()
        elif table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1])

            if check_winner():
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
            else:
                finishthegame()








    elif move == "s":
        if turn == 1 and player_loc["player_1"][0] == 17:
            Console.print("You can't go any lower than this!", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [1]:
            Console.print("There is a wall behind you!", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and (table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1]):
            Console.print("There's a wall behind the player! You can't.", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1] :
            if player_loc[f"player_{turn}"][0]+1 > 17 or player_loc[f"player_{turn}"][0]+2 > 17:
                Console.print("You can't go higher than this!", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]+3 , player_loc[f"player_{turn}"][1]-1 , turn )
                update_player_location(player_loc[f"player_{turn}"][0]+4 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
            else:
                finishthegame()

        elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]-1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
            else:
                finishthegame()




    elif move == "d":
        if player_loc[f"player_{turn}"][1] == 17: 
            Console.print("az in rast tar nemitoni beri!", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
                Console.print("The wall is ahead!", style="red")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]):
            Console.print("There is a wall in front of the player! You can't.", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and not table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1] :
            if player_loc[f"player_{turn}"][1]+1 > 17 or player_loc[f"player_{turn}"][1]+2 > 17:
                Console.print("You can't go any further right than this.", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]+3 , turn )
                update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]+4)
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]+1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]+2)
            swap_turn()
            Console.print("The move was made.", style="blue")
            await table_printer()
            await take_action()





    elif move == "a":
        if player_loc[f"player_{turn}"][1] == 1: 
            Console.print("You can't go any further left than this.", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [1]:
                Console.print("There is a wall behind you!", style="red")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1]):
            Console.print("There's a wall behind the player! You can't.", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and not table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1] :
            if player_loc[f"player_{turn}"][1]-3 < 0 or player_loc[f"player_{turn}"][1]-4 < 0:
                Console.print("You can't go any further left than this.", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]-5 , turn )
                update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]-4)
                swap_turn()
                Console.print("The move was made.", style="blue")
                await table_printer()
                await take_action()
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]-3 , turn )
            update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]-2)
            swap_turn()
            Console.print("The move was made.", style="blue")
            await table_printer()
            await take_action()





    elif move == "e":
        if player_loc[f"player_{turn}"][0] <= 2 or player_loc[f"player_{turn}"][1] >= 16:
            Console.print("You are not allowed to do this!", style="red")
            return False
        #check out of table moves :
        elif player_loc[f"player_{turn}"][0] == 3 and player_loc[f"player_{turn}"][1] == 15:
            Console.print("You are not allowed to do this!", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] == 3 :
            if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        elif player_loc[f"player_{turn}"][1] == 15 :
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        else:
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0] and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]:
                if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
                    Console.print("The wall is ahead!", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()
            elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0] and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
                if table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
                    Console.print("The wall is ahead! ", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()



 


    elif move == "q":
        if player_loc[f"player_{turn}"][0] <= 2 or player_loc[f"player_{turn}"][1] <= 2:
            Console.print("You are not allowed to do this!", style="red")
            return False
        #check out of table moves :
        elif player_loc[f"player_{turn}"][0] == 3 and player_loc[f"player_{turn}"][1] == 3:
            Console.print("You are not allowed to do this!", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] == 3 :
            if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        elif player_loc[f"player_{turn}"][1] == 3 :
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False

        else: 
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0] and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1]:
                if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [1]:
                    Console.print("The wall is ahead!", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-3 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]-2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()
            elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0] and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
                if table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
                    Console.print("The wall is ahead! ", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-3 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]-2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()







    elif move == "z":
        if player_loc[f"player_{turn}"][0] >= 16 or player_loc[f"player_{turn}"][1] <= 2:
            Console.print("You are not allowed to do this!", style="red")
            return False
        #check out of table moves :
        elif player_loc[f"player_{turn}"][0] == 3 and player_loc[f"player_{turn}"][1] == 15:
            Console.print("You are not allowed to do this!", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] == 15 :
            if table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        elif player_loc[f"player_{turn}"][1] == 3 :
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False

        else: 
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0] and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1]:
                if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [1]:
                    Console.print("The wall is ahead!", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]-3 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1]-2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()
            elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0] and table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1]:
                if table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [1]:
                    Console.print("The wall is ahead! ", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-3] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]-3 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1]-2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()

    elif move == "c":
        if player_loc[f"player_{turn}"][0] >= 16 or player_loc[f"player_{turn}"][1] >= 16:
            Console.print("You are not allowed to do this!", style="red")
            return False
        #check out of table moves :
        elif player_loc[f"player_{turn}"][0] == 15 and player_loc[f"player_{turn}"][1] == 15:
            Console.print("You are not allowed to do this!", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] == 15 :
            if table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        elif player_loc[f"player_{turn}"][1] == 15 :
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] == [1]:
                Console.print("You are not allowed to do this!", style="red")
                return False
        else:
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0] and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]:
                if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
                    Console.print("a wall is ahead!", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()
            elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0] and table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1]:
                if table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [1]:
                    Console.print("The wall is ahead! ", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("You are not allowed to do this!", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("The move was made.", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finishthegame()

async def check_wall(x , y , direction):
    global player_2_walls , player_1_walls
    secondryx = x - 1
    secondryy = 17 - y
    if (x % 2 != 0) or (y % 2 != 0):
        Console.print("Your X or Y cannot be even!", style="red")
        return False
    if direction == "v" and ((table[secondryy][secondryx] != [0] ) or (table[secondryy-1][secondryx] != [0] ) or (table[secondryy+1][secondryx] != [0] )):
        Console.print("A wall has already been built in this place!", style="red")
        return False
    elif direction == "h" and ((table[secondryy][secondryx] != [0] ) or (table[secondryy][secondryx+1] != [0] ) or (table[secondryy][secondryx-1] != [0] )):
        Console.print("A wall has already been built in this place!", style="red")
        return False
    else:
        if direction == "v":
            table[secondryy][secondryx] = [1]
            table[secondryy+1][secondryx] = [1]
            table[secondryy-1][secondryx] = [1]
        else:
            table[secondryy][secondryx] = [1]
            table[secondryy][secondryx+1] = [1]
            table[secondryy][secondryx-1] = [1]
        if turn == 1 :
            player_1_walls -= 1
        else:
            player_2_walls -= 1
        swap_turn()
        Console.print("The wall was built!", style="blue")
        await table_printer()
        await take_action()
    
    
    





async def lets_move():
    Console.print("- - - - - - - - - - - -", style="cyan")
    move = input("Please Enter What Direction You Want To Move ? (W , S , A , D for natural moves Q , E , Z , C for secondry moves) : ").lower()
    commands = ["w" , "s" , "a" , "d" , "q" , "e" , "z" , "c"]
    while True:
        if move in commands:
            if await check_move(move):
                break
            else:
                move = input("So choose again where you want to go? (W , S , A , D , Q , E , Z , C) : ").lower()
        else:
            Console.print("Your Choice Is Not Valid ! Try Again (W , S , A , D , Q , E , Z , C) : ", style="red")
            move = input()


async def place_wall():
    Console.print("- - - - - - - - - - - -", style="cyan")
    while True:
        while True:
                x = input("Please select the horizontal component of the wall. (2 ≤ x ≤ 16) :")
                if x.isdigit():
                    x = int(x)
                    if x >= 2 and x <= 16:
                        break
                    else:
                        Console.print("Please enter a number between 2 and 16!", style="red")
                else:
                    Console.print("Please enter only the number as input.", style="red")
        while True:
            y = input("Select the vertical component of the wall. (2 ≤ y ≤ 16):")
            if y.isdigit():
                y = int(y)
                if y >= 2 and y <= 16:
                    break
                else:
                    Console.print("Please enter a number between 2 and 16! ", style="red")
            else:
                Console.print("Please enter only numbers as input.", style="red")
        while True:
            direction = input("Choose the direction of the wall. (H Or V) : ").lower()
            if direction in ["h" , "v"]:
                break
            else:
                Console.print("Use the correct terms vertical and horizontal.", style="red")
        if await check_wall(x , y , direction):
            break
        else:
            Console.print("So choose another coordinate.", style="red")

            



first_time = True
async def take_action():
    global gameid
    if first_time:
            print("----------------------------------------------------------")
            print(f"now its your turn {player_loc["player_1"][-1] +"🔴" if turn == 1 else player_loc["player_2"][-1]+"🔵"}")
            Console.print(f"You have {player_1_walls if turn == 1 else player_2_walls} wall(s) !", style="green bold")
    
    move = input("Enter What You Want To Do! m For Move / w For Wall (Save for save and exit!): ").lower()
    while check_winner():
        if move == "save":
            save_the_game(gameid)
        if move == "m":
            await lets_move()
        elif move == "w":
            if (turn == 1 and player_1_walls) or turn == 2 and player_2_walls:
                await place_wall()
            else:
                Console.print("hich divari baraye estefade nadari !", style="red bold")

        else:
            Console.print("Your Choice Is Not Valid ! Try Again (m For Move / w For Wall)(Save for save and exit!) : ", style="red")
            move = input()




def save_the_game(gameid):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    dictionary = {
    "player1_username": player_loc["player_1"][-1],
    "player2_username": player_loc["player_2"][-1],
    "p1walls": player_1_walls,
    "p2walls": player_2_walls,
    "player1_position": player_loc["player_1"][:-1],
    "player2_position": player_loc["player_2"][:-1],
    "table": table,
    "current_turn": f"{player_loc["player_1"][-1] if turn == 1 else player_loc["player_2"][-1]}",
    "timer": round(time.time(),2),
    "game_result": "In Progress",
    "date": formatted_time
    }

    savethegame(gameid , dictionary)
    Console.print(Panel("Your Game Has Been Saved ! Bye ", style="bold red"))
    quit()

async def table_creator(gameid):
    global table
    table = take_table(gameid)


async def start_the_game(pusername1 , pusername2, gameidd):
    global table , player_loc , turn,first_time , player_1_walls , player_2_walls , gameid
    gameid = gameidd
    player_1_walls = p1walls(gameid)
    player_2_walls = p2walls(gameid)
    turn = random.randint(1,2)
    player_loc["player_1"] = loc1(gameid)
    player_loc["player_2"] = loc2(gameid)
    player_loc["player_1"].append(pusername1)
    player_loc["player_2"].append(pusername2)
    await table_creator(gameid)
    await table_printer()
    print("----------------------------------------------------------")
    print(f"The game will start by {player_loc["player_1"][-1]+"🔴" if turn == 1 else player_loc["player_2"][-1]+"🔵"}")
    await take_action()
    first_time = False






