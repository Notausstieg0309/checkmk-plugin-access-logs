#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.plugins.metrics import (
   metric_info,
   graph_info,
)



# Status 1xx

metric_info["count_101"] = {
    "title" : _("101 - Switching Protocols"),
    "unit"  : "count",
    "color" : "41/a",
}

metric_info["count_1XX"] = {
    "title" : _("1XX - (Information)"),
    "unit"  : "count",
    "color" : "41/b",
}


# Status 2xx

metric_info["count_200"] = {
    "title" : _("200 - OK"),
    "unit"  : "count",
    "color" : "26/a",
}

metric_info["count_2XX"] = {
    "title" : _("2XX - Successful"),
    "unit"  : "count",
    "color" : "26/b",
}


# Status 3xx

metric_info["count_3XX"] = {
    "title" : _("3XX - Redirection"),
    "unit"  : "count",
    "color" : "24/a",
}


# Status 4xx

metric_info["count_400"] = {
    "title" : _("400 - Bad Request"),
    "unit"  : "count",
    "color" : "21/a",
}

metric_info["count_401"] = {
    "title" : _("401 - Unauthorized"),
    "unit"  : "count",
    "color" : "16/a",
}

metric_info["count_403"] = {
    "title" : _("403 - Forbidden"),
    "unit"  : "count",
    "color" : "15/a",
}

metric_info["count_404"] = {
    "title" : _("404 - Not Found"),
    "unit"  : "count",
    "color" : "14/a",
}

metric_info["count_4XX"] = {
    "title" : _("4XX - Client Error"),
    "unit"  : "count",
    "color" : "13/a",
}


# Status 5xx

metric_info["count_500"] = {
    "title" : _("500 - Internal Server Error"),
    "unit"  : "count",
    "color" : "12/a",
}

metric_info["count_502"] = {
    "title" : _("502 - Bad Gateway"),
    "unit"  : "count",
    "color" : "11/a",
}

metric_info["count_503"] = {
    "title" : _("503 - Service Unavailable"),
    "unit"  : "count",
    "color" : "46/a",
}

metric_info["count_504"] = {
    "title" : _("504 - Gateway Timeout"),
    "unit"  : "count",
    "color" : "45/a",
}

metric_info["count_5XX"] = {
    "title" : _("5XX - Server Error"),
    "unit"  : "count",
    "color" : "12/b",
}


# everything else

metric_info["count_XXX"] = {
    "title" : _("XXX - [other status codes]"),
    "unit"  : "count",
    "color" : "51/a",
}

metric_info["count_no_status"] = {
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
                        ( "count_no_status", "area" ),

                        ( "count_XXX", "stack" ),
                        ( "count_5XX", "stack" ),
                        ( "count_504", "stack" ),
                        ( "count_503", "stack" ),
                        ( "count_502", "stack" ),
                        ( "count_500", "stack" ),
                        ( "count_4XX", "stack" ),
                        ( "count_404",  "stack" ),
                        ( "count_403",  "stack" ),
                        ( "count_401",  "stack" ),
                        ( "count_400",  "stack" ),
                        ( "count_3XX", "stack" ),
                        ( "count_2XX", "stack" ),
                        ( "count_200",  "stack" ),
                        ( "count_1XX", "stack" ),
                        ( "count_101", "stack")
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


