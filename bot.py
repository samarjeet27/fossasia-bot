# twisted imports
from twisted.python import log
from Logbot import *
# system imports
import time, sys

if __name__ == '__main__':
    # initialize logging
    log.startLogging(sys.stdout)
    
    # log_bot_factory(channel_name, log_file, nick)
    f = LogBotFactory('fossasia', 'fossasia_channel.log', 'fossasia-bot')

    # connect factory to this host and port
    reactor.connectTCP("irc.freenode.net", 6667, f)

    # run bot
    reactor.run()