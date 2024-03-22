# Puppet manifest that kills a running program
exec {'kill program':
  command => '/usr/bin/pkill killmenow'
}
