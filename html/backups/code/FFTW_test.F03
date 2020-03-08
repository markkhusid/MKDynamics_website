
program FFTW_test
    
    use, intrinsic      :: iso_c_binding
    include 'fftw3.f03'
    
    type(C_PTR)         :: plan
    
    complex(C_DOUBLE_COMPLEX), dimension(8)     :: in, out
    
    integer					:: i
        
    in(1:4) = (1,0)
    in(5:8) = (0,0)
    
    plan = fftw_plan_dft_1d(8, in, out, FFTW_FORWARD, FFTW_ESTIMATE)
    
    print *, "The contents of the input array is ->"
    do i = 1,8
      print *, in(i)
    end do
    
    print *
    
    print *, "Executing DFT on input array..."
    call fftw_execute_dft(plan, in, out)
    
    print *, "The contents of the output array is ->"
    do i = 1,8
      print *, out(i)
    end do
    
    print *
    
    call fftw_destroy_plan(plan)
    
    !Swapping arrays to see if I can retrieve signal in time domain from signal in frequency domain
    in = out
    
    plan = fftw_plan_dft_1d(8, in, out, FFTW_BACKWARD, FFTW_ESTIMATE)
    
    print *, "The contents of the input array is ->"
    do i = 1,8
      print *, in(i)
    end do
    
    print *
    
    print *, "Executing DFT on input array..."
    call fftw_execute_dft(plan, in, out)
    
    print *, "The contents of the output array is ->"
    do i = 1,8
      print *, out(i)
    end do
    
    print *
    
    call fftw_destroy_plan(plan)
    
    
end program FFTW_test




