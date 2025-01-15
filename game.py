import asyncio
import random
turn = 1
from rich.console import Console
from the_finnal_file import finall_task
player_loc = {
}
Console = Console()


table = [
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [1], [0], [2], [1], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
]
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
            Console.print("nemitoni beri balatar !", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("koskhol divar jelote !", style=" red ")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
            Console.print("ahmagh posht player divare ! nemitoni ke", style=" red ")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1] :
            if player_loc[f"player_{turn}"][0]-4 < 0 or player_loc[f"player_{turn}"][0]-5 < 0:
                Console.print("akoskhol az in balatar nemitoni beri !", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-5 , player_loc[f"player_{turn}"][1]-1 , turn )
                update_player_location(player_loc[f"player_{turn}"][0]-4 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])
        elif table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1])

            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])








    elif move == "s":
        if turn == 1 and player_loc["player_1"][0] == 17:
            Console.print("nemitoni beri paiin tar !", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [1]:
            Console.print("koskhol divar poshtete !", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and (table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1]):
            Console.print("ahmagh posht player divare ! nemitoni ke", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] != [0]) and not table[player_loc[f"player_{turn}"][0]+2][player_loc[f"player_{turn}"][1]-1] == [1] :
            if player_loc[f"player_{turn}"][0]+1 > 17 or player_loc[f"player_{turn}"][0]+2 > 17:
                Console.print("akoskhol az in balatar nemitoni beri !", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]+3 , player_loc[f"player_{turn}"][1]-1 , turn )
                update_player_location(player_loc[f"player_{turn}"][0]+4 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])

        elif table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]+1 , player_loc[f"player_{turn}"][1]-1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]+2 , player_loc[f"player_{turn}"][1])
            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])




    elif move == "d":
        if player_loc[f"player_{turn}"][1] == 17: 
            Console.print("az in rast tar nemitoni beri!", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
                Console.print("koskhol divar jelote !", style="red")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]):
            Console.print("ahmagh jeloye player divare ! nemitoni ke", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0]) and not table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1] :
            if player_loc[f"player_{turn}"][1]+1 > 17 or player_loc[f"player_{turn}"][1]+2 > 17:
                Console.print("koskhol az in rast tar nemitoni beri !", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]+3 , turn )
                update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]+4)
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]+1 , turn )
            update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]+2)
            swap_turn()
            Console.print("Move Anjam Shod! !", style="blue")
            await table_printer()
            await take_action()





    elif move == "a":
        if player_loc[f"player_{turn}"][1] == 1: 
            Console.print("az in chap tar nemitoni beri!", style="red")
            return False
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [1]:
                Console.print("koskhol divar poshtete !", style="red")
                return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1]):
            Console.print("ahmagh posht player divare ! nemitoni ke", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-3] != [0]) and not table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-4] == [1] :
            if player_loc[f"player_{turn}"][1]-3 < 0 or player_loc[f"player_{turn}"][1]-4 < 0:
                Console.print("akoskhol az in chap tar nemitoni beri !", style="red")
                return False
            else:
                update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]-5 , turn )
                update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]-4)
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
        elif table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]-2] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-1 , player_loc[f"player_{turn}"][1]-3 , turn )
            update_player_location(player_loc[f"player_{turn}"][0] , player_loc[f"player_{turn}"][1]-2)
            swap_turn()
            Console.print("Move Anjam Shod! !", style="blue")
            await table_printer()
            await take_action()





    elif move == "e":
        if player_loc[f"player_{turn}"][0] <= 2 or player_loc[f"player_{turn}"][1] >= 16:
            Console.print("Shoma mojaz be anjam in move nistid !", style="red")
            return False
        #check out of table moves :
        elif player_loc[f"player_{turn}"][0] == 3 and player_loc[f"player_{turn}"][1] == 15:
            Console.print("shoma mojaz be anjam in move nistid ! ", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] == 3 :
            if table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] == [1]:
                Console.print("shoma mojaz be anjam in move nistid ! ", style="red")
                return False
        elif player_loc[f"player_{turn}"][1] == 15 :
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] == [1]:
                Console.print("shoma mojaz be anjam in move nistid ! ", style="red")
                return False
        else:
            if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+1] != [0] and table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]+2] == [1]:
                if table[player_loc[f"player_{turn}"][0]-1][player_loc[f"player_{turn}"][1]] == [1]:
                    Console.print("Divar Jelote !", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("shoma mojaz be anjam in move nistid ! ", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("Move Anjam Shod! !", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finall_task(player_loc[f"player_{turn}"][-1])
            elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] != [0] and table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [1]:
                if table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [1]:
                    Console.print("Divar Jelote ! ", style="red")
                    return False
                elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]+1] == [1]:
                    Console.print("shoma mojaz be anjam in move nistid ! ", style="red")
                    return False
                else:
                    update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]+1 , turn )
                    update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]+2)
                    if check_winner():
                        swap_turn()
                        Console.print("Move Anjam Shod! !", style="blue")
                        await table_printer()
                        await take_action()
                    else:
                        finall_task(player_loc[f"player_{turn}"][-1])



        # if turn == 2 and player_loc["player_2"][0] == 1:
        #     Console.print("nemitoni beri balatar !", style="red")
        #     return False
        # elif player_loc[f"player_{turn}"][0]-2 <0  or player_loc[f"player_{turn}"][0]-3 < 0:
        #     Console.print("nemitoni beri balatar !", style="red")
        #     return False
        # elif player_loc[f"player_{turn}"][1]-2 <0  or player_loc[f"player_{turn}"][0]-3 < 0:
        # elif table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] == [0] or table[player_loc[f"player_{turn}"][0]-4][player_loc[f"player_{turn}"][1]-1] == [0]:
        #     Console.print("Shoma mojaz be anjam in move nistid !", style="red")
        #     return False
        # elif player_loc[f"player_{turn}"][1]+1 <= 17:
        #     update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]+1 , turn )
        #     update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]+2)
        #     if check_winner():
        #         swap_turn()
        #         Console.print("Move Anjam Shod! !", style="blue")
        #         await table_printer()
        #         await take_action()
        #     else:
        #         finall_task(player_loc[f"player_{turn}"][-1])
        # else:
        #     Console.print("nemitoni beri rast tar !", style="red")
        #     return False
        





    if move == "q":
        if turn == 2 and player_loc["player_2"][0] == 1:
            Console.print("nemitoni beri balatar !", style="red")
            return False
        elif player_loc[f"player_{turn}"][0]-2 < 0 or player_loc[f"player_{turn}"][0]-3 < 0:
            Console.print("nemitoni beri balatar !", style="red")
            return False
        elif (table[player_loc[f"player_{turn}"][0]-2][player_loc[f"player_{turn}"][1]-1] == [0]) or table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-1] == [0]:
            Console.print("Shoma mojaz be anjam in move nistid !", style="red")
            return False
        elif player_loc[f"player_{turn}"][1]-3 >= 0:
            update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-3 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]-2)
            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])
        else:
            Console.print("nemitoni beri chap tar !", style="red")
            return False
        
    if move == "z":
        if turn == 1 and player_loc["player_1"][0] == 17:
            Console.print("nemitoni beri paiintar !", style="red")
            return False
        elif player_loc[f"player_{turn}"][0] > 17 or player_loc[f"player_{turn}"][0]+1 > 17:
            Console.print("nemitoni beri paiin tar !", style="red")
            return False
        elif  (table[player_loc[f"player_{turn}"][0]][player_loc[f"player_{turn}"][1]-1] == [0]) or table[player_loc[f"player_{turn}"][0]+1][player_loc[f"player_{turn}"][1]-1] == [0]:
            Console.print("Shoma mojaz be anjam in move nistid !", style="red")
            return False
        elif player_loc[f"player_{turn}"][1]-3 >= 0 and table[player_loc[f"player_{turn}"][0]-3][player_loc[f"player_{turn}"][1]-3] == [0]:
            update_move_actions(player_loc[f"player_{turn}"][0]-3 , player_loc[f"player_{turn}"][1]-3 , turn )
            update_player_location(player_loc[f"player_{turn}"][0]-2 , player_loc[f"player_{turn}"][1]-2)
            if check_winner():
                swap_turn()
                Console.print("Move Anjam Shod! !", style="blue")
                await table_printer()
                await take_action()
            else:
                finall_task(player_loc[f"player_{turn}"][-1])
        else:
            Console.print("nemitoni beri chap tar !", style="red")
            return False

async def lets_move():
    Console.print("- - - - - - - - - - - -", style="cyan")
    move = input("Please Enter What Direction You Want To Move ? (W , S , A , D for natural moves Q , E , Z , C for secondry moves) : ").lower()
    commands = ["w" , "s" , "a" , "d" , "q" , "e" , "z" , "c"]
    while True:
        if move in commands:
            if await check_move(move):
                break
            else:
                move = input("Pas Dobare Entekhab Kon Koja Mikhay Beri ? (W , S , A , D , Q , E , Z , C) : ").lower()
        else:
            Console.print("Your Choice Is Not Valid ! Try Again (W , S , A , D , Q , E , Z , C) : ", style="red")
            move = input()



first_time = True
async def take_action():
    if first_time:
            print("----------------------------------------------------------")
            print(f"now its your turn {player_loc["player_1"][-1] +"🔴" if turn == 1 else player_loc["player_2"][-1]+"🔵"}")
    move = input("Enter What You Want To Do! m For Move / w For Wall : ").lower()
    while check_winner():
        if move == "m":
            await lets_move()
        elif move == "w":
            break
        else:
            Console.print("Your Choice Is Not Valid ! Try Again (m For Move / w For Wall) : ", style="red")
            move = input()








async def start_the_game(pusername1 , pusername2):
    global table , player_loc , turn,first_time
    turn = random.randint(1,2)
    player_loc["player_1"] = [15 , 7 , pusername1]
    player_loc["player_2"] = [15 , 9 , pusername2]
    await table_printer()
    print("----------------------------------------------------------")
    print(f"The game will start by {player_loc["player_1"][-1]+"🔴" if turn == 1 else player_loc["player_2"][-1]+"🔵"}")
    await take_action()
    first_time = False



asyncio.run(start_the_game("erfan","shayna"))





