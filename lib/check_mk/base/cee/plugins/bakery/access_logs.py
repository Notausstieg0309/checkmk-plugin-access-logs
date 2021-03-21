#!/usr/bin/env python


from pathlib import Path

from .bakery_api.v1 import (
    OS,
    Plugin,
    PluginConfig,
    register,
    quote_shell_string,
    FileGenerator,
)


def access_logs_files(conf):

    yield Plugin(
        base_os=OS.LINUX,
        source=Path("access_logs.linux.py"),
        target=Path("access_logs.py"),
    )
    # create config file
    if len(conf) > 0:
        conf_lines = []

        for key in conf:
            conf_lines.append("%s = %r" % (key,  conf[key]))
        
        yield PluginConfig(
                base_os=OS.LINUX,
                lines = conf_lines,
                target = Path("access_logs.conf"),
                include_header=True,
            )

register.bakery_plugin(
    name="access_logs",
    files_function=access_logs_files,
)
