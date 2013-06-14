

# OSError: [WinError 10013] Der Zugriff auf einen Socket war aufgrund der Zugriffsrechte des Sockets unzulässig


def error_hints_at_previleged_rights(error):
    """works for windows
    todo: Linux, ..."""
    return isinstance(error, OSError) and error.winerror == 10013
