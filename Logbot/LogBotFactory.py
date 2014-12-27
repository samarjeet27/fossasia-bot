from twisted.internet import reactor, protocol

class LogBotFactory(protocol.ClientFactory):
    """A factory for LogBots.

    A new protocol instance will be created each time we connect to the server.
    """

    def __init__(self, channel, filename, nick):
        self.channel = channel
        self.filename = filename
        self.nick = nick

    def buildProtocol(self, addr):
        p = LogBot(self.nick)
        p.factory = self
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()