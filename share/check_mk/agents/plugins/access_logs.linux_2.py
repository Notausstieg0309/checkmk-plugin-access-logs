#!/usr/bin/env python2

import glob
import os
import gzip
import sys
import subprocess
import re
import datetime
import string

# default values
default_log_files = (
    "/var/log/tomcat6/access.*.log",
    "/var/log/tomcat7/access.*.log",
    "/var/log/tomcat8/access.*.log",
    "/var/log/apache2/access.log",
    "/var/log/apache2/access_log",
    "/var/log/httpd/access_log",
    "/var/log/httpd/access.log",
    "/var/log/nginx/access.log"
)

default_line_regexps = ( r'^(?:\S+\s+)+\[(?P<date>[^\]]+) \+\d\d\d\d\]\s+"[^"]*"\s+(?P<status>\d+)', )

default_date_formats = ( "%d/%b/%Y:%H:%M:%S", )


# configurable variables
log_files = []
line_regexps = []
date_formats = []
read_back = 300


config_dir = os.getenv("MK_CONFDIR", "/etc/check_mk")
config_file = config_dir + "/access_logs.conf"

if not os.path.exists(config_file):
    config_file = config_dir + "/access_logs.cfg"

if os.path.exists(config_file):
    exec(open(config_file).read())

# add default list items to configured values
log_files.extend(default_log_files)
line_regexps.extend(default_line_regexps)
date_formats.extend(default_date_formats)

if not all(x in globals() for x in ["log_files", "line_regexps", "date_formats", "read_back"]):
    print("<<<access_logs>>>")
    print("error: missing config values")
    sys.exit()


def total_seconds(dt):
    # Keep backward compatibility with Python 2.6 which doesn't have
    # this method
    if hasattr(dt, 'total_seconds'):
        return dt.total_seconds()
    else:
        return (dt.microseconds + (dt.seconds + dt.days * 24 * 3600) * 10**6) / 10**6


def get_files(search_dir):

    files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))

    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files

def read_backwards(filename):
    stdout = None
    if filename.endswith(".gz"):
        p_gzip = subprocess.Popen(["gzip", "-cd", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        p_tac = subprocess.Popen(["tac"], stdin=p_gzip.stdout, stdout=subprocess.PIPE)
        p_gzip.stdout.close()
        (stdout, stderr) = p_tac.communicate()
    else:

        p_tac = subprocess.Popen(["tac", filename], stdout=subprocess.PIPE)
        (stdout, stderr) = p_tac.communicate()
    if stdout:

        for line in stdout.decode("utf-8").split('\n'):
            if line:
                yield line


class ReadBackReached(Exception):
    pass

class NoDateFormatString(Exception):
    pass

class NoLineRegexp(Exception):
    pass


def read_file_pattern(pattern, read_back):

    files = get_files(pattern)

    result = {}

    regexp = None
    date_format = None

    now = datetime.datetime.now()

    if files:
        print('['+pattern+"]")

    try:
        for filename in files:

            for line in read_backwards(filename):
                if regexp is None:
                    for item in line_regexps:
                        if re.match(item, line):
                            regexp = re.compile(item)
                    if regexp is None:
                        raise NoLineRegexp(line)

                match = regexp.match(line)

                if match:

                    if date_format is None:
                        for item in date_formats:
                            try:
                                test = datetime.datetime.strptime(match.group("date"),item)
                                date_format = item
                                break
                            except ValueError:
                                continue
                        if date_format is None:
                            raise NoDateFormatString(match.group("date"))

                    line_date = datetime.datetime.strptime(match.group("date"),date_format)

                    delta = now - line_date
                    if total_seconds(delta) < read_back:
                        if not match.group("status") in result:
                            result[match.group("status")] = 0
                        result[match.group("status")] += 1
                    else:
                        raise ReadBackReached

    except ReadBackReached:
        pass
    except NoDateFormatString as e:
        print("error: No suitable date format string configured to decode date '"+str(e)+"'")
        return
    except NoLineRegexp as e:
        print("error: No suitable regular expression configured to extract date and status code from line '"+str(e)+"'")

    if result:
        for code,counter in result.iteritems():
            print(str(code)+" "+str(counter))


print('<<<access_logs>>>')
for item in log_files:
    read_file_pattern(item, read_back)

