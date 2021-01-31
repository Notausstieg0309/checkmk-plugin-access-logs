# CheckMK Plugin "access_logs"

The plugin "access_logs" analyzes all existing HTTP access logs on a system for multiple HTTP server software (like Apache, Tomcat or nginx).

It reads the current access log file backwards an catches all requests within the last 5 minutes (can be configured). It counts the HTTP response status codes to generate an overview and checks the percentual failure rate.

Requirements on the target machine (to be monitored):
------
* `tac` command available within PATH environment. (part of GNU [coreutils](http://www.gnu.org/software/coreutils/)) 
* `gzip` command available within PATH environment. Needed, in case your access logs get gzip'ed during log rotation
