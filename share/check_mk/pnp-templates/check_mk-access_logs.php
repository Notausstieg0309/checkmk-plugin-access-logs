<?php



$opt[1] = "--title \"Total HTTP Responses for $hostname\" -l 0 -X 0 ";




$def[1] = "DEF:101=$RRDFILE[1]:$DS[1]:AVERAGE ";
$def[1] .= "AREA:101#2ed4f2:\"101 - Switching Protocols   \" ";

$def[1] .= "GPRINT:101:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:101:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:101:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:101:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:1xx=$RRDFILE[2]:$DS[2]:AVERAGE ";
$def[1] .= "AREA:1xx#1694aa:\"1xx - Information           \":STACK ";

$def[1] .= "GPRINT:1xx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:1xx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:1xx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:1xx:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "COMMENT:\" \\n\" ";

$def[1] .= "DEF:200=$RRDFILE[3]:$DS[3]:AVERAGE ";
$def[1] .= "AREA:200#41f22e:\"200 - OK                    \" ";

$def[1] .= "GPRINT:200:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:200:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:200:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:200:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:2xx=$RRDFILE[4]:$DS[4]:AVERAGE ";
$def[1] .= "AREA:2xx#00b300:\"2xx - Success               \":STACK ";

$def[1] .= "GPRINT:2xx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:2xx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:2xx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:2xx:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:3xx=$RRDFILE[5]:$DS[5]:AVERAGE ";
$def[1] .= "AREA:3xx#8cba87:\"3xx - Redirection           \":STACK ";

$def[1] .= "GPRINT:3xx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:3xx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:3xx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:3xx:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "COMMENT:\" \\n\" ";

$def[1] .= "DEF:400=$RRDFILE[6]:$DS[6]:AVERAGE ";
$def[1] .= "AREA:400#aa2c16:\"400 - Bad Request           \":STACK ";

$def[1] .= "GPRINT:400:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:400:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:400:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:400:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:401=$RRDFILE[7]:$DS[7]:AVERAGE ";
$def[1] .= "AREA:401#ff806b:\"401 - Unauthorized          \":STACK ";

$def[1] .= "GPRINT:401:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:401:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:401:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:401:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "DEF:403=$RRDFILE[8]:$DS[8]:AVERAGE ";
$def[1] .= "AREA:403#ff6600:\"403 - Forbidden             \":STACK ";

$def[1] .= "GPRINT:403:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:403:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:403:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:403:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:404=$RRDFILE[9]:$DS[9]:AVERAGE ";
$def[1] .= "AREA:404#ffff00:\"404 - Not Found             \":STACK ";

$def[1] .= "GPRINT:404:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:404:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:404:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:404:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "DEF:4xx=$RRDFILE[10]:$DS[10]:AVERAGE ";
$def[1] .= "AREA:4xx#ffbf00:\"4xx - Client Error          \":STACK ";

$def[1] .= "GPRINT:4xx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:4xx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:4xx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:4xx:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "COMMENT:\" \\n\" ";


$def[1] .= "DEF:500=$RRDFILE[11]:$DS[11]:AVERAGE ";
$def[1] .= "AREA:500#8533ff:\"500 - Internal Server Error \":STACK ";

$def[1] .= "GPRINT:500:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:500:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:500:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:500:LAST:\"Last\\: %5.0lf\\n\" ";

$def[1] .= "DEF:502=$RRDFILE[12]:$DS[12]:AVERAGE ";
$def[1] .= "AREA:502#e0ccff:\"502 - Bad Gateway           \":STACK ";

$def[1] .= "GPRINT:502:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:502:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:502:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:502:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:503=$RRDFILE[13]:$DS[13]:AVERAGE ";
$def[1] .= "AREA:503#e600e6:\"503 - Service Unavailable   \":STACK ";

$def[1] .= "GPRINT:503:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:503:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:503:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:503:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:504=$RRDFILE[14]:$DS[14]:AVERAGE ";
$def[1] .= "AREA:504#ff99ff:\"504 - Gateway Timeout       \":STACK ";

$def[1] .= "GPRINT:504:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:504:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:504:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:504:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:5xx=$RRDFILE[15]:$DS[15]:AVERAGE ";
$def[1] .= "AREA:5xx#ff0000:\"5xx - Server Error          \":STACK ";

$def[1] .= "GPRINT:5xx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:5xx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:5xx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:5xx:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "COMMENT:\" \\n\" ";

$def[1] .= "DEF:xxx=$RRDFILE[16]:$DS[16]:AVERAGE ";
$def[1] .= "AREA:xxx#000000:\"xxx - [other status codes]  \":STACK ";

$def[1] .= "GPRINT:xxx:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:xxx:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:xxx:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:xxx:LAST:\"Last\\: %5.0lf\\n\" ";


$def[1] .= "DEF:no_status=$RRDFILE[17]:$DS[17]:AVERAGE ";
$def[1] .= "AREA:no_status#888888:\"<-> - [no status code sent] \":STACK ";

$def[1] .= "GPRINT:no_status:MAX:\"Max\\: %5.0lf /\" ";
$def[1] .= "GPRINT:no_status:MIN:\"Min\\: %5.0lf /\" ";
$def[1] .= "GPRINT:no_status:AVERAGE:\"Avg\\: %5.0lf /\" ";
$def[1] .= "GPRINT:no_status:LAST:\"Last\\: %5.0lf\\n\" ";


$opt[2] = "--title \"HTTP Failure Rate for $hostname\" --vertical-label \"Failure Rate in %\" -l 0 -X 0 ";

$def[2] = "DEF:fail=$RRDFILE[18]:$DS[18]:AVERAGE ";
$def[2] .= "AREA:fail#ffe6e6 ";
$def[2] .= "LINE1.5:fail#ff0000:\"Failure Rate within last 5m\" ";
$def[2] .= "COMMENT:\" \" ";
$def[2] .= "COMMENT:\"  (\" ";

$def[2] .= "GPRINT:fail:MAX:\"Max\\: %3.1lf%% /\" ";
$def[2] .= "GPRINT:fail:MIN:\"Min\\: %3.1lf%% /\" ";
$def[2] .= "GPRINT:fail:AVERAGE:\"Avg\\: %3.1lf%%\" ";


$def[2] .= "COMMENT:\")\\n\" ";

