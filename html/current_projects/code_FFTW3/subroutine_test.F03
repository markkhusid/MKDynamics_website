program module_test
  implicit none
  
  interface
    function my_func(test)
      integer 			:: my_func
      integer, intent(in) 	:: test
    end function my_func
  end interface
  
  integer :: bree, meow
  
  print *, 'This is a test of the module placement section'
  meow = 5
  bree = my_func(meow)
  
  print *, bree
  
end program module_test

function my_func(test)
      integer :: my_func
      integer, intent(in) :: test
      print *, 'This is a function'
      my_func = test * 5
end function