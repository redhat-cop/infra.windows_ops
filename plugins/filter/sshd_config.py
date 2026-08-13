"""Filter to render sshd_config from an options dictionary."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


def sshd_config(options):
    """Convert an sshd options dictionary to sshd_config file content.

    Args:
        options: Dictionary of sshd_config directives. Values can be:
            - A string or number for simple key-value pairs
            - A list of strings for multi-value directives
            - A list of strings under a 'Match ...' key for Match blocks

    Returns:
        String content suitable for writing to sshd_config with CRLF line endings.
    """
    if not options:
        return ""

    lines = []
    for key, value in options.items():
        if isinstance(value, (str, int, float)):
            lines.append("{0} {1}".format(key, value))
        elif isinstance(value, list):
            if key.startswith("Match"):
                lines.append(key)
                for entry in value:
                    lines.append("    {0}".format(entry))
            else:
                for entry in value:
                    lines.append("{0} {1}".format(key, entry))

    return "\r\n".join(lines) + "\r\n"


class FilterModule(object):
    """Ansible filter plugin for sshd_config generation."""

    def filters(self):
        return {
            "sshd_config": sshd_config,
        }
