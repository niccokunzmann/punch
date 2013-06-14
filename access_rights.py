

# OSError: [WinError 10013] Der Zugriff auf einen Socket war aufgrund der Zugriffsrechte des Sockets unzulässig


def error_hints_at_previleged_rights(error):
    """works for windows
    todo: Linux, ..."""
    return isinstance(error, OSError) and error.winerror == 10013


class RequiresHigherPrevileges(Exception):
    """to execute this you need higer provileges = root or administrator rights """
    pass

help_text = """
You need administrator or root rights to make this program execute properly.

under windows:
    start this program as adminitrator

under linux:
    use sudo of gksudo or equal to start this program
"""

class PrevilegeContext(object):
    def __enter__(self):
        return self

    def __exit__(self, ty, error, tb):
        if error is None:
            return
        if error_hints_at_previleged_rights(error):
            error = RequiresHigherPrevileges(help_text)
            raise error.with_traceback(tb)

ensure_rights = PrevilegeContext()
