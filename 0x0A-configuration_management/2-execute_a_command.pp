# Execute a command that kills a process with pkill
exec { 'kill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
