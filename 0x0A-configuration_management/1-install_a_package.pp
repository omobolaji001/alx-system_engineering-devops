# Install an especific version of flask (2.1.0)
package { 'python':
  ensure  => 'present',
}

package { 'python3-pip':
  ensure  => present,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
