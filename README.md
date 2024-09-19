Here's a little jig for running SmokePing tests over the Mycelium network.

It consists of:

1. Dockerfile that installs Mycelium into a base SmokePing image. This also can inject some user provided config into the image.
2. Script for generating a base configuration that includes ping targets for the public Mycelium nodes
3. Another script that helps create a Mycelium invocation by generating the --peers option based on the list of public nodes
4. JSON file containing all Mycelium public peers, created by copying the HTML table of peers from the Mycelium repo README and running it through [CSV to JSON converter](https://www.convertcsv.com/csv-to-json.htm)

The idea is that the user will provide some targets of their own, by writing a section of SmokePing target config and placing it into `config/Targets.body`:

```
# config/Targets.body
+ MySSHTargets

menu = SSH
title = SSH
probe = SSH

++ Target1
menu = Target 1
title = Target 1
host = 42a:beeb:842e:acdc:f00f:0:400:2
```

The Dockerfile includes a step that will concatenate the Targets files into one. While bind mounting the config directory is an option, it's somewhat of a hassle due to file permissions.

I do recommend using a volume for data. You will also need to run the container as privileged to be able to create the TUN device for Mycelium. The full process might look like this:

```
$EDITOR config/Targets.body
docker buildx build mycelium-smoketest .
docker run --privileged -v ./data:/data -p 8112:80 mycelium-smoketest
```

Now the web iterface will be available at `localhost:8112`.

## Notes on "the idea"

These tests are motivated by my observation of intermittent connection failures when trying to reach VMs for SSH over Mycelium. The goal is to try to gather some data that shows whether there's a consistent ongoing issue and can help to trace the root cause if so.

I want to assess the following:

1. How is performance from our vantage point to Mycelium public nodes, and also to a set of our own chosen Mycelium hosts?
2. How does this performance compare to connections attempted over a standard internet connection?
3. What's our baseline, in terms of general WAN connectivity to a set of generally highly available peers?

So run these probes on these targets (didn't implement any of the IPv6 routes yet, these require some special Docker config):

1. Ping over Mycelium to Mycelium public nodes
2. Ping over IPv4 to Mycelium public nodes
3. Ping over Mycelium to extra hosts list
4. Ping over IPv6 to extra hosts list (as available)
5. SSH probe over Mycelium to extra hosts
6. SSH probe over IPv6 to extra hosts
7. All pings included in the default config provided with the linuxserver/smokeping container image

Thus can compare the performance and reliability of our chosen hosts versus the Mycelium peers and some benchmark hosts across the internet.
