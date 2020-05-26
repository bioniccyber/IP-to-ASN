# Bulk IP to ASN Script

This script performs Autonomous System Numbers (ASNs) lookups for a list of IP addresses. An Autonomous System (AS) is a group of one or more IP prefixes (lists of IP addresses accessible on a network) run by one or more network operators that maintain a single, clearly-defined routing policy. ASN lookups can be used by blue teams to determine the provenance and, in some cases, the legitimacy of IPs and domains. For this reason, Team Cymru maintains a list of ASN to IP mappings based on BGP feeds from 50+ BGP peers, updated at 4 hour intervals. Read more here: https://team-cymru.com/community-services/ip-asn-mapping/

The country code, registry, and allocation date are all based on data obtained directly from the regional registries including: ARIN, RIPE, AFRINIC, APNIC, LACNIC. The information returned relating to these categories will only be as accurate as the data present in the RIR databases.

`IMPORTANT NOTE:` Country codes are likely to vary significantly from actual IP locations, and we must strongly advise that the IP to ASN mapping tool not be used as an IP geolocation (GeoIP) service.

## Script Usage

The script expects a filename which should contain the list of IPs you want to look up. As noted/recommended by the Team Cymru Documentation, the list should be at most a few thousand in order to minimize overall load. Your list should be formatted as shown below. The output will be written to a file (to the current directory) that’s date+time stamped.

(text begin on Line1, the text verbose at Line2, and the text end at the bottom)

```danny@enrich:~/team-cymru$cat ip_list_test.txt
begin
verbose
8.8.8.8
68.22.187.5
207.229.165.18
198.6.1.65
216.90.108.31
end
