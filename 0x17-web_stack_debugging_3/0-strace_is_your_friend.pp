# A puppet manifest to fix wordpress file on a server

$edit_file = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => ['/bin','/usr/bin']
}
