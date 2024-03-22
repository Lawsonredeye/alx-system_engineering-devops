# Provision script that installs flask 2.1.0 on shell
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
exec { '/usr/bin/pip3 install Flask==2.1.0':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
