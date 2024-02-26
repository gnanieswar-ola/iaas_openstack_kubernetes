"""
This type stub file was generated by pyright.
"""

"""
Autocall capabilities for IPython.core.

Authors:

* Brian Granger
* Fernando Perez
* Thomas Kluyver

Notes
-----
"""
class IPyAutocall:
    """ Instances of this class are always autocalled
    
    This happens regardless of 'autocall' variable state. Use this to
    develop macro-like mechanisms.
    """
    _ip = ...
    rewrite = ...
    def __init__(self, ip=...) -> None:
        ...
    
    def set_ip(self, ip): # -> None:
        """Will be used to set _ip point to current ipython instance b/f call

        Override this method if you don't want this to happen.

        """
        ...
    


class ExitAutocall(IPyAutocall):
    """An autocallable object which will be added to the user namespace so that
    exit, exit(), quit or quit() are all valid ways to close the shell."""
    rewrite = ...
    def __call__(self): # -> None:
        ...
    


class ZMQExitAutocall(ExitAutocall):
    """Exit IPython. Autocallable, so it needn't be explicitly called.
    
    Parameters
    ----------
    keep_kernel : bool
      If True, leave the kernel alive. Otherwise, tell the kernel to exit too
      (default).
    """
    def __call__(self, keep_kernel=...): # -> None:
        ...
    


