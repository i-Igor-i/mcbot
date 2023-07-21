from javascript import require, On
import random
from time import sleep

username = "bot_1"
curx = 0
curz = 0
antiafk = False

mineflayer = require("mineflayer")
pathfinder = require("mineflayer-pathfinder")
autoeat = require("mineflayer-auto-eat")
goalXZ = pathfinder.goals.GoalXZ
goalFollow = pathfinder.goals.GoalFollow
goalBlock = pathfinder.goals.GoalBlock
bot = mineflayer.createBot({
    "host":"nect0rineHRD.aternos.me",
    "username": username,
    "version":"1.16.5"
})
bot.loadPlugin(pathfinder.pathfinder)
bot.loadPlugin(autoeat.plugin)

@On(bot,"spawn")
def spawn(*args):
    bot.autoEat.enable()
    mc_data = require("minecraft-data")(bot.version)
    movements = pathfinder.Movements(bot,mc_data)
    @On(bot,'chat')
    def msg_handler(this, user, message, *args):
        if user != username:
            if message == f"привет, {username}":
                bot.chat(f"привет, {user}")
            elif message == f"{username}#pos":
                pos = bot.entity.position
                print(pos)
                bot.chat(f"position: [{str(int(pos.x))}, {str(int(pos.y))}, {str(int(pos.z))}]")
            try:
                if message.split("goto [")[0] == f"{username}#":
                    message = message.replace("]","")
                    print(message)
                    if len(message.split('goto [')[1].split(', ')) == 3:
                        bot.pathfinder.setMovements(movements)
                        print(message.split("goto [")[1].split(", ")[0], message.split("goto [")[1].split(", ")[1], message.split("goto [")[1].split(", ")[2])
                        goalblock = goalBlock(message.split("goto [")[1].split(", ")[0], message.split("goto [")[1].split(", ")[1], message.split("goto [")[1].split(", ")[2])
                        bot.chat('OK, coords mode: [X, Y, Z]')
                        bot.pathfinder.setGoal(goalblock, True)
                    elif len(message.split('goto [')[1].split(', ')) == 2:
                        bot.pathfinder.setMovements(movements)
                        goalxz = goalXZ(message.split("goto [")[1].split(", ")[0], message.split("goto [")[1].split(", ")[1])
                        bot.chat('OK, coords mode: [X, Z]')
                        bot.pathfinder.setGoal(goalxz, True)          
            except:
                print("[E] ERROR!!!!!")
            if message == f"{username}#antiafk_toggle":
                global antiafk
                antiafk = not antiafk
                bot.chat(f'antiafk: {antiafk}')
                pos = bot.entity.position
                global curx
                global curz
                curx = pos.x
                curz = pos.z
            print(f"<{user}> {message}")
            if message.split(" ")[0] == f"{username}#drop":
                id = eval(f"bot.registry.itemsByName.{message.split(' ')[1]}.id")
                invent = bot.inventory.items()
                print(invent)
                fltinv = []
                for item in invent:
                    if item.type==id:
                        fltinv.append(item)
                print(fltinv)
                for stack in fltinv:
                    bot.tossStack(stack)
    @On(bot,"time")
    def time(*args):
        global antiafk
        if antiafk == True:
            newx = curx+random.randint(-1,1)
            newz = curz+random.randint(-1,1)
            goal = goalXZ(newx,newz)
            bot.pathfinder.setGoal(goal,True)
            
#syntax: bot_1#pos - get bot pos
#        bot_1#goto [x, z] or [x, y, z] - goto pos
#        bot_1#antiafk_toggle - toggle antiafk




    
    

