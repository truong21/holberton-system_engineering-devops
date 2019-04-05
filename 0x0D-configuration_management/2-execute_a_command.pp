# kills process 'killmenow'
exec { 'kills killmenow':
  command => 'pkill killmenow',
  path    => [ '/usr/local/bin/', '/bin/' ]
}
