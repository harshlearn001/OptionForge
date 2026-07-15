"""
============================================================
OptionForge
Kernel
Exceptions
============================================================
"""


class KernelError(Exception):
    """Base kernel exception."""


class RegistryError(KernelError):
    """Registry failure."""
