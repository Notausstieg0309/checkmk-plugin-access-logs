#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from .agent_based_api.v1 import Service,Metric,Result,State,register,render

import re

def parse_access_logs(string_table):
    
    block = None
    result = {}
    for line in string_table:
        line_complete = " ".join(line)

        if line_complete.startswith("[") and line_complete.endswith("]"):
            block = line_complete[1:-1]
            result[block] = []
        else:
            result[block].append(line)

        if line_complete.startswith("error:"):
            result[block] = line_complete

    return result


def discover_access_logs(section):
    for item in section.keys():
        yield Service(item=item)


def check_access_logs(item, params, section):
    base_regex= {
                 '101': '101',
                 '1XX': '1(?:0[023456789]|[1-9]\d)',
                 '200': '200',
                 '2XX': '2(?:0[1-9]|[1-9]0)',
                 '3XX': '3[0-9]{2}',
                 '400': '400',
                 '401': '401',
                 '403': '403',
                 '404': '404',
                 '4XX': '4(?:0[256789]|[1-9]\d)',
                 '500': '500',
                 '502': '502',
                 '503': '503',
                 '504': '504',
                 '5XX': '5(?:0[156789]|[1-9]\d)',
                 'XXX': '[06-9]\d\d',
                 'no_status': '\d*\D+\d*',
                }
    
    good_requests = ('101', '1XX', '200', '2XX', '3XX')
    counter = {}
    request_sum = 0
    failure_rate = 0.0

    severity = State.OK
  
    perfdata = []

    for key in base_regex.keys():
        counter[key] = 0

    if not item in section:
        yield Result(state=State.UNKN, summary="missing data in agent output")
        return
    
    if section[item] and isinstance(section[item], str):
        raise Exception("error in agent plugin - " + section[item])
    
    for line in section[item]:
        (code, requests) = line

        for key, value in base_regex.items():
            if re.match(value, code):
                counter[key] += int(requests)
                
        request_sum += int(requests)

    
    if request_sum > 0:
        failure_rate = 100.0 - ((float(sum([counter[x] for x in good_requests])/float(request_sum)))*100.0)
        text = "%d request%s, failure rate %s" % (request_sum, "s" if request_sum != 1 else "", render.percent(failure_rate))
    else:
        text = "no new request found"
        
    if params:
        if "failure_rate" in params:
            (warn, crit) = params["failure_rate"]

            if failure_rate > crit:
                severity = State.CRIT
                text += " (over %0.2f%%)" % crit 
            elif failure_rate > warn:
                severity = State.WARN
                text += " (over %0.2f%%)" % warn
    
    yield Result(state=severity, summary=text)             
                    

    for key in counter.keys():
        yield Metric(name=("count_%s" % key), value=counter[key])

    yield Metric(name="failure_rate", value=failure_rate) 
    

register.agent_section(
    name="access_logs",
    parse_function = parse_access_logs,
)

register.check_plugin(
    name="access_logs",
    check_function = check_access_logs,
    discovery_function = discover_access_logs,
    service_name = 'HTTP Access Log %s',
    check_ruleset_name = "access_logs",
    check_default_parameters = {}
)
