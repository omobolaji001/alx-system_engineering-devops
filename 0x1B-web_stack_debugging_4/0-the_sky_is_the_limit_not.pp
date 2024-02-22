# A puppet manifest that resets the amount of traffic an Nginx server can handle

exec { 'fix nginx limit':
  command => 'sed -i "s/15/16384/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
