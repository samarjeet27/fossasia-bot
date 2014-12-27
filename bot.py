# twisted imports
from twisted.python import log
from Logbot import *
# system imports
import time, sys

if __name__ == '__main__':
    # initialize logging
    log.startLogging(sys.stdout)
    
    # create factory protocol and application
    f = LogBotFactory('fossasia', 'fossasia_channel.log', 'fossasia-bot')

    # connect factory to this host and port
    reactor.connectTCP("irc.freenode.net", 6667, f)

    # run bot
    reactor.run()