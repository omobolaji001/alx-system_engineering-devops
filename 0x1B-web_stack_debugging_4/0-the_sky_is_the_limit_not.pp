# A puppet manifest that resets the amount of traffic an Nginx server can handle.

exec { 'reset-nginx-limit':
  command => 'sed -i "s/15/16384/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
