# Puppet script to update client configureation file
exec { 'configure identity file':
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}

exec { 'configure password auth':
  command => 'echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}
