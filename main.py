from javascript import require, On
import random
from time import sleep

username = "bot_1"

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
            elif message == f"{username}, где ты?":
                pos = bot.entity.position
                print(pos)
                bot.chat(f"{user}, я на координатах {str(int(pos.x))}, {str(int(pos.y))}, {str(int(pos.z))}")
            try:
                if message.split("на")[0] == f"{username}, иди ":
                    if len(message.split('на')[1].split(', ')) == 3:
                        bot.pathfinder.setMovements(movements)
                        goalblock = goalBlock(message.split("на")[1].split(", ")[0], message.split("на")[1].split(", ")[1], message.split("на")[1].split(", ")[2])
                        bot.chat('ок, режим: [X, Y, Z]')
                        bot.pathfinder.setGoal(goalblock, True)
                    elif len(message.split('на')[1].split(', ')) == 2:
                        bot.pathfinder.setMovements(movements)
                        goalxz = goalXZ(message.split("на")[1].split(", ")[0], message.split("на")[1].split(", ")[1])
                        bot.chat('ок, режим: [X, Z]')
                        bot.pathfinder.setGoal(goalxz, True)          
            except:
                print("[E] ERROR!!!!!")
            print(message)
            





    
    

