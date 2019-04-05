# kills process 'killmenow'
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin/'
}
