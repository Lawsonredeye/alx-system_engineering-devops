# Provision script that installs flask 2.1.0 on shell
exec { 'pip3 install flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
