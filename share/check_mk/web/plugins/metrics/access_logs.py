#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Metrics beginning with numbers and ending with letters needs to be renamed (???)
check_metrics["check_mk-access_logs"] = {
        "1XX"   : { "name" : "s1XX" },
        "2XX"   : { "name" : "s2XX" },
        "3XX"   : { "name" : "s3XX" },
        "4XX"   : { "name" : "s4XX" },
        "5XX"   : { "name" : "s5XX" },
        }


# Status 1xx

metric_info["101"] = {
    "title" : _("101 - Switching Protocols"),
    "unit"  : "count",
    "color" : "41/a",
}

metric_info["s1XX"] = {
    "title" : _("1XX - (Information)"),
    "unit"  : "count",
    "color" : "41/b",
}


# Status 2xx

metric_info["200"] = {
    "title" : _("200 - OK"),
    "unit"  : "count",
    "color" : "26/a",
}

metric_info["s2XX"] = {
    "title" : _("2XX - Successful"),
    "unit"  : "count",
    "color" : "26/b",
}


# Status 3xx

metric_info["s3XX"] = {
    "title" : _("3XX - Successful"),
    "unit"  : "count",
    "color" : "24/a",
}


# Status 4xx

metric_info["400"] = {
    "title" : _("400 - Bad Request"),
    "unit"  : "count",
    "color" : "21/a",
}

metric_info["401"] = {
    "title" : _("401 - Unauthorized"),
    "unit"  : "count",
    "color" : "16/a",
}

metric_info["403"] = {
    "title" : _("403 - Forbidden"),
    "unit"  : "count",
    "color" : "15/a",
}

metric_info["404"] = {
    "title" : _("404 - Not Found"),
    "unit"  : "count",
    "color" : "14/a",
}

metric_info["s4XX"] = {
    "title" : _("4XX - Client Error"),
    "unit"  : "count",
    "color" : "13/a",
}


# Status 5xx

metric_info["500"] = {
    "title" : _("500 - Internal Server Error"),
    "unit"  : "count",
    "color" : "12/a",
}

metric_info["502"] = {
    "title" : _("502 - Bad Gateway"),
    "unit"  : "count",
    "color" : "11/a",
}

metric_info["503"] = {
    "title" : _("503 - Service Unavailable"),
    "unit"  : "count",
    "color" : "46/a",
}

metric_info["504"] = {
    "title" : _("504 - Gateway Timeout"),
    "unit"  : "count",
    "color" : "45/a",
}

metric_info["s5XX"] = {
    "title" : _("5XX - Server Error"),
    "unit"  : "count",
    "color" : "12/b",
}


# everything else

metric_info["XXX"] = {
    "title" : _("XXX - [other status codes]"),
    "unit"  : "count",
    "color" : "51/a",
}

metric_info["no_status"] = {
    "title" : _("No status code"),
    "unit"  : "count",
    "color" : "52/a",
}

metric_info["failure_rate"] = {
    "title" : _("Failure Rate"),
    "unit"  : "%",
    "color" : "14/a",
}

graph_info.append({
   "title"         : ("HTTP Response Status Codes"),
   "metrics"       : [
                        ( "no_status", "area" ),
                        ( "XXX", "stack" ),
                        ( "s5XX", "stack" ),
                        ( "504", "stack" ),
                        ( "503", "stack" ),
                        ( "502", "stack" ),
                        ( "500", "stack" ),
                        ( "s4XX", "stack" ),
                        ( "404",  "stack" ),
                        ( "403",  "stack" ),
                        ( "401",  "stack" ),
                        ( "400",  "stack" ),
                        ( "s3XX", "stack" ),
                        ( "s2XX", "stack" ),
                        ( "200",  "stack" ),
                        ( "s1XX", "stack" ),
                        ( "101", "stack")
                     ],
    "omit_zero_metrics" : True,
})

graph_info.append({
   "title"         : ("HTTP Failure Rate"),
   "metrics"       : [
                        ( "failure_rate", "line")
                     ],
    "omit_zero_metrics" : True,
})


