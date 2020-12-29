register_check_parameters(
    subgroup_applications,
    "access_logs",
    _("HTTP Access Log"),
    Dictionary(
        elements = [
            ("failure_rate",
                Tuple(
                title = _("check failure rate"),
                elements = [
                    Percentage(title = _("warning if higher than"), help = _("Generate a WARNING if the failure rate is higher than the configured value.") ),
                    Percentage(title = _("critical if higher than"),  help= _("Generate a CRITICAL if the failure rate is higher than the configured value.") ),
                    ]
             )),
        ],
    ),
    TextAscii(
        title = _("log file"),
        help = _("The full path of the logfile.")
    ),
    "dict"
)


register_rule(
    "agents/" + _("Agent Plugins"),
    "agent_config:access_logs",
    Alternative(
        title = _("HTTP Access Logs"),
        help = _("This will deploy the agent plugin <tt>access_logs</tt> "
                 "for checking various HTTP access logs of webservers "
                 "like Apache, Nginx, Tomcat. It counts the latest number of requests "
                 "per status code for a configurable period of time."
                ),
        style = "dropdown",
        elements = [
            Dictionary(
                title = _("Deploy the HTTP Access Logs plugin"),
                elements = [
                   ( "log_files",
                     ListOfStrings(
                        title = _("Logfile Patterns"),
                        help = _('A list of additional access log file patterns that should be considered for discovery. The path can contain globbing wildcards (<tt>*</tt> & <tt>?</tt>) to mask variable parts. Only the newest file which matches a pattern will be used for analysis.'),
                        valuespec = TextAscii(
                            size = 80,
                            regex = "^/(/?[^\0/])+|/$",
                            regex_error = _("Logfile pattern must begin with <tt>/</tt>."),
                        ),
                        allow_empty = False,
                     )
                   ),
                   ( "read_back",
                     Age(
                        title = _("Readback Age"),
                        help = _('The time period which should be considered when reading the access logfile (based on the current time'),
                        display = ["minutes", "seconds"],
                        label = "reading the last",
                        default_value = 300
                     )
                   ),
                   ( "line_regexp",
                     ListOfStrings(
                        title = _("Line Regexp Patterns"),
                        help = _("A list of custom regular expression which will be applied against each line of the access log file to extract the date and response status."
                                 "The pattern must be capture the date as named group 'date' (via <tt>(?P<date>.+)</tt> and the status as named group 'status' (via <tt>(?P<status>\d+)</tt><br><br>"
                                 ),
                        allow_empty = False,
                        valuespec = RegExp(
                                        size = 80,
                                        regex = "^(?=.*\(\?P\<status\>)(?=.*\(\?P\<date\>).*$",
                                        regex_error = _("The regular expression does not contain both group captures to extract the date <tt>(?P<date>.+)</tt> and status code <tt>(?P<status>\d+)</tt><br><br>Please add both named groups!"),
                                        mingroups = 2,
                                        maxgroups = 2,
                                        mode = "prefix"
                                    ),
                        default_value = [ r'^(?:\S+\s+)+\[(?P<date>[^\]]+) \+\d\d\d\d\]\s+"[^"]*"\s+(?P<status>\d+)' ]
                     )
                   ),
                   ( "date_formats",
                     ListOfStrings(
                        title = _("Date Format Strings"),
                        help = _("A list of custom date format string which will be used to parse a date/time entry which is extracted by a line regexp to determine the exact timestamp of a request. The python function datetime.strptime() will be used for this, see Python documentation (<tt>https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes</tt>) to get the full list of placeholders."),
                        allow_empty = False,
                        valuespec = TextAscii(
                            size = 80,
                            regex = r"^.*%.*$",
                            regex_error = _("The given pattern does not contain any placeholder to extract date/time informations.")
                        )
                     )
                   )
                ],
                optional_keys = True,
            ),
            FixedValue(None, title = _("Do not deploy the HTTP Access Logs plugin"), totext = _("(disabled)") ),
        ],
    ),
    match="dict"
)


