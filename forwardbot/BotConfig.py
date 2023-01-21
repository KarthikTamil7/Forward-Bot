from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "11973721")
    API_HASH = environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5949999646:AAGNAzsUTMutsqtnSk2R4MkGgCQ0uMtqbIU")
    STRING_SESSION = environ.get("STRING", "BQBEfsiIKyiEL0vZYfgCzXKVjmv8xhHtu6PUJpold8o6f5veO-XAKoCLXN3bVHvUGkCv9NgwTrWrnc3lZRwNdREsinh9wOZnc9wQOsllTUpvE2Hzbax8rhkji4Roqsaziw-sDdDfGft42t0DbGVlSe7lf_WOxbrFPlfyJ94AMiGpEYBIwT_VKT_QYrDl8IEwlYAuqgKoQVkhNeB0WFIKBYFAt42jVDfeZAZpNMnyQO9F5LVQCsUemf42czKfovAujA6xiIRr9c39y-nsWxxvO6arsCPatQ3uiRXqgvq6rwIcaNqnPBizNRyAAEPnAoLST82Jg3EC5Awet7oH800X8_5dUvF4PAA")
    SUDO_USERS = environ.get("SUDO_USERS", "1391556668 5162208212 5239847373")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
