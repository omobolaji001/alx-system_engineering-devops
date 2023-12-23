# Execute a command that kills a process with pkill
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['usr/bin', 'usr/sbin'],
}
