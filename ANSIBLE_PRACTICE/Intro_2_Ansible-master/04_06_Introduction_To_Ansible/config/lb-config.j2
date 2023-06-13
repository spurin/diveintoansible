ProxyRequests off
<Proxy balancer://webcluster >
  {% for hosts in groups['webservers'] %}
    BalancerMember http://{{hostvars[hosts]['ansible_host']}}
  {% endfor %}
    ProxySet lbmethod=byrequests
</Proxy>

# Optional
<Location /balancer-manager>
  SetHandler balancer-manager
</Location>

ProxyPass /balancer-manager !
ProxyPass / balancer://webcluster/