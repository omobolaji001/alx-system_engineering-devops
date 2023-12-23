# Install an especific version of flask (2.1.0)
python_packages = ['python 3.8.10', 'flask 2.1.0', 'werkzeug 2.1.1']

package { $python_packages:
  ensure   => 'installed',
  provider => 'pip3',
}
