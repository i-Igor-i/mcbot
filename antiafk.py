from javascript import require, On
import random
from time import sleep

username = "bot_1"
counter = 0
mineflayer = require("mineflayer")
pathfinder = require("mineflayer-pathfinder")
autoeat = require("mineflayer-auto-eat")
goalXZ = pathfinder.goals.GoalXZ
bot = mineflayer.createBot({
    "host":"nect0rineHRD.aternos.me",
    "username": username,
    "version":"1.16.5"
})
bot.loadPlugin(pathfinder.pathfinder)
@On(bot,"spawn")
def spawn(*args):
    bot.autoEat.enable()
    mc_data = require("minecraft-data")(bot.version)
    movements = pathfinder.Movements(bot,mc_data)
    bot.pathfinder.setMovements(movements)
    curpos = bot.entity.position
    curx = curpos.x
    curz = curpos.z
    @On(bot,"time")
    def time(*args):
        newx = curx+random.randint(-1,1)
        newz = curz+random.randint(-1,1)
        goal = goalXZ(newx,newz)
        bot.pathfinder.setGoal(goal,True)
        counter = 0