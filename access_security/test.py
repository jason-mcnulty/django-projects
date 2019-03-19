from bs4 import BeautifulSoup


t = <html lang="en-US" xmlns="http://www.w3.org/1999/xhtml"><head><title>Cluster HealthCheck</title>
</head><body><h1>Health check details:</h1>CPU-UTILIZATION=11;
<br/>SWAP-UTILIZATION=0;
<br/>DISK-UTILIZATION=8;
<br/>SSL-CONNECTION-COUNT=4282;
<br/>USER-COUNT=4391;
<br/>MAX-LICENSED-USERS-REACHED=NO;
<br/>VPN-TUNNEL-COUNT=4200;
<br/></body></html>

bs = BeautifulSoup(t)

results = {}
for row in bs.findAll('tr'):
    aux = row.findAll('td')
    results[aux[0].string] = aux[1].string

print (results)
