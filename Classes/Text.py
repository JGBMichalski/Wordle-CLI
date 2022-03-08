# CLI Text output effects - similar to `colorama`
class Colours:
    # Text Colours:
    BLACK               = '\033[30m'
    DARK                = '\033[90m'
    RED                 = '\033[91m'
    GREEN               = '\033[92m'
    YELLOW              = '\033[93m'
    BLUE                = '\033[94m'
    PURPLE              = '\033[95m'
    LIGHTBLUE           = '\033[96m'
    WHITE               = '\033[97m'
    GREY                = '\033[98m'

    #Remove Formatting
    END                 = '\033[0m'

class Accents:
    # Text Accents
    BOLD                = '\033[1m'
    ITALICS             = '\033[3m'
    UNDERLINE           = '\033[4m'

    #Remove Formatting
    END                 = '\033[0m'

class Highlights:
    # Highlights
    GREY                = '\033[100m'
    RED                 = '\033[101m'
    GREEN               = '\033[102m'
    YELLOW              = '\033[103m'
    BLUE                = '\033[104m'
    PURPLE              = '\033[105m'
    AQUA                = '\033[106m'
    WHITE               = '\033[107m'
    WHITE_CONTRAST      = '\033[7m'    #White highlight, Black Text

    #Remove Formatting
    END                 = '\033[0m'