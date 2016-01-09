# Auth0 job application

This project sends data from kodi to webtask.io so you can see how much time you've wasted on watching series/movies.


### Usage:

- to run it locally first you need to build the kodi add-on, for this run: `make dist-addon` this will create a zip file in the project's root
- here is how you can install the add-on: http://kodi.wiki/view/HOW-TO:Install_add-ons_from_zip_files
- once it's installed you can start play movies and once you stop them it will send the filename and the elapsed time to the webtask endpoint
```
18:15:35 T:123145302839296   DEBUG: ### [TimeWasted] - https://webtask.it.auth0.com/api/run/wt-dominis-haxor_hu-0/dummy?webtask_no_cache=1&title=Straight.Outta.Compton.2015.1080p.HC.WEBRip.x264.AAC2.0-FGT.mp4&time=884.132019043
18:15:43 T:123145302839296   DEBUG: ### [TimeWasted] - https://webtask.it.auth0.com/api/run/wt-dominis-haxor_hu-0/dummy?webtask_no_cache=1&title=Bridge.of.Spies.2015.DVDScr.XVID.AC3.HQ.Hive-CM8.avi&time=4873.3984375
```
- you can query the stats using:
```
[:~/src/hacking/job-tests/auth0] master ± http https://webtask.it.auth0.com/api/run/wt-dominis-haxor_hu-0/timewasted?webtask_no_cache=1
HTTP/1.1 200 OK
connection: close
content-type: application/json
date: Sat, 09 Jan 2016 19:30:00 GMT
transfer-encoding: chunked
x-auth0-proxy-stats: {"proxy_host":"172.31.200.56","proxy_pid":6,"sandbox_route":"172.31.201.57:30039","sandbox_image":"docker.auth0.com/auth0-sandbox:2.0.0.568ed7606bc94eaa63cbec1f","container_id":"172.31.201.57.39","time":679,"uptime":164740.309,"memory":{"rss":248725504,"heapTotal":166880512,"heapUsed":47960720},"requests":236701,"req_id":"1452367799633.808621"}
x-auth0-stats: {"response":{"200":3},"time":470,"uptime":194.611,"memory":{"rss":75689984,"heapTotal":58682624,"heapUsed":34202888}}

"Total time wasted: 2.65 hours"
```


### TODO

- add "registration" to the add-on config so we can store stats separetely
- it would be better to display in days the wasted time
