program FFTW_from_data_file
    
    use, intrinsic      :: iso_c_binding
    include 'fftw3.f03'
    
    type(C_PTR)         					:: plan
    
    integer, parameter						:: num_expected_args=3				! Input file name, output file name and number of bins
    
    real(C_DOUBLE), dimension(:), allocatable			:: in						! FFTW input array
    complex(C_DOUBLE_COMPLEX), dimension(:), allocatable	:: out						! FFTW output array
        
    real(C_DOUBLE), dimension(:), allocatable			:: temp_real_array					! Holds the data read from the input file
    real(C_DOUBLE)						:: magnitude, phase, temp_real				! Used to perform complex math
    
    integer							:: EOF_marker					! For checking if EOF reached
    integer							:: file_good1, file_good2, file_good3		! For checking if files opened successfully
    integer							:: good_write1, good_write2			! For checking if files written successfully
    integer							:: i						! Counter used to traverse arrays
    integer							:: num_args					! Contains number of arguments for verification of proper command line call
    integer							:: num_bins_int					! Holds obtained number of bins
    integer							:: status1, status2, status3			! Holds memory allocation status of arrays
    
    character(len=80)						:: input_file, output_mag_file			! Holds file names
    character(len=80)						:: output_phase_file	
    
    ! Verify that the number of arguments is correct.  Should be 3, otherwise display
    ! error and terminate program
    num_args = command_argument_count()
    if (num_args .ne. num_expected_args) then
      print *, 'Improper number of arguments'
      print *, 'Argument list:'
      print *, '<input file name> <output magnitude file name> <output phase file name> <number of bins>'
      goto 2000								! Graceful exit, no cleanup  
    end if
    
    ! Call subroutines that obtain the command line arguments and load the appropriate variables
    call get_command_argument (1, input_file)
    call get_command_argument (2, output_mag_file)
    call get_command_argument (3, output_phase_file)
    
    ! Debug code that ensures command line arguments were passed in properly
    print *, 'The first argument is ->'
    print *, input_file
    
    print *, 'The second argument is ->'
    print *, output_mag_file
    
    print *, 'The third argument is ->'
    print *, output_phase_file
    
    
    ! Begin to open files
    open (unit=1, file=TRIM(input_file), status="old", IOSTAT=file_good1, form="formatted", access="sequential", action="read")
    !open (unit=1, file=TRIM(input_file), IOSTAT=file_good1)
    if (file_good1 .ne. 0) then
      print *, 'Error opening input file!'
      goto 2000
    else if (file_good1 .eq. 0) then
      print *, 'Input file opened successfully...'
    end if
    
    open (unit=10, file=TRIM(output_mag_file), status="replace", IOSTAT=file_good2, form="formatted", access="sequential")
    if (file_good2 .ne. 0) then
      print *, 'Error creating output magnitude file!'
      goto 2000
    else if (file_good2 .eq. 0) then
      print *, 'Output magnitude file created successfully...'
    end if

    open (unit=20, file=TRIM(output_phase_file), status="replace", IOSTAT=file_good3, form="formatted", access="sequential")
    if (file_good3 .ne. 0) then
      print *, 'Error creating output phase file!'
      goto 2000
    else if (file_good3 .eq. 0) then
      print *, 'Output phase file created successfully...'
    end if
    
    
    
!    	Debug code follows.  Tests to see if file opened properly.
!     read (unit=1, fmt='(f20.10)', IOSTAT = EOF_marker), temp_real
!     print *, 'The status of EOF_marker is'
!     print *, EOF_marker
!     print *, 'The first element read was'
!     print *, temp_real
!	Debug code ends

! Traverse through data file and count number of data elements in file
    ! Get first data element from file to see whether it is the EOF character
      i = 1
      read (1, '(f20.10)', IOSTAT = EOF_marker), temp_real
!   Debug code starts here
!     write (*, '(a, i4)'), 'The EOF marker is ->', EOF_marker
!     write (*, '(a, i4)'), 'The counter is ->', i
!     write (*, '(a, 10f10.4)'), 'The data element was ->', temp_real
!     print *
!     print *
!   Debug code ends here

      if (EOF_marker < 0) then
	print *, 'ERROR: Input file is empty'
	goto 2000
      end if

! Establish loop that will count number of elements in file
 count_loop:	do
      if (EOF_marker < 0) then
	exit count_loop
      else
	i = i + 1
	read (1, '(f20.10)', IOSTAT = EOF_marker), temp_real
      end if
    end do count_loop

    ! Copy over the number of counted elements into the num_bins_int variable less one for the EOF character
    num_bins_int = i - 1

    ! Allocate memory based on the number of bins
    ! Display success status of memory allocation
    ! If there is a problem with memory allocation, display error and terminate
    allocate (in(num_bins_int), stat=status1)
    print *, 'Was memory allocated successfully for input array? ->'
    print *, allocated(in)
    if (status1 .ne. 0) then
      print *, 'Memory allocation error on input array'
      goto 2000
    end if
    
    allocate (out(num_bins_int), stat=status2)
    print *, 'Was memory allocated successfully for output array? -> ->'
    print *, allocated(out)
    if (status2 .ne. 0) then
      print *, 'Memory allocation error on output array'
      deallocate (in)
      goto 2000
    end if
    
    allocate (temp_real_array(num_bins_int), stat=status3)
    print *, 'Was memory allocated successfully for scratchpad array? ->'
    print *, allocated(temp_real_array)
    if (status3 .ne. 0) then
      print *, 'Memory allocation error on scratchpad array'
      deallocate (in)
      deallocate (out)
      goto 2000
    end if
    
    ! Bring file pointer for input file back to first element 
    rewind(1)
    
    !Establish a loop that reads the file from 1 to num_bins_int
    do i=1, num_bins_int
      read (1, '(f20.10)', IOSTAT = EOF_marker), temp_real_array(i)		! read data element from file
      ! Debug code starts here
	write (*, '(a, i4)'), 'The EOF marker is ->', EOF_marker
	write (*, '(a, i4)'), 'The counter is ->', i
	write (*, '(a, 10f10.4)'), 'The data element was ->', temp_real_array(i)
	print *
	print *
      ! Debug code ends here
    end do

    
    ! *************** FFT COMPUTATION SECTION **********************
    
    ! Establish array of reals that is the input the FFTW3 function
    in = temp_real_array
    
    ! Use built in fucntion to create FFTW3 plan.  Tells FFTW3 what to do.
    plan = fftw_plan_dft_r2c_1d(num_bins_int, in, out, FFTW_ESTIMATE)
    call fftw_print_plan(plan)
    
    print *
    print *
         
    ! Execute FFTW3 to produce DFFT on data from file stored in array
    print *, "Executing DFT on input array..."
    call fftw_execute_dft_r2c(plan, in, out)
     
    ! Debug code starts here
!     print *, "The contents of the output array is ->"
!     do i = 1,num_bins_int			 
!       print *, out(i)
!     end do
    ! Debug code ends here
    
    print *

    ! Traverse through output array that contains the complex DFFT, calculate magnitude and
    ! write results to output file
    do i = 1,num_bins_int
    ! Line below for debug
!     print *, out(i)
      magnitude = sqrt((real(out(i))**2) + (aimag(out(i))**2))
      phase = atan(aimag(out(i)) / real(out(i)))
      
      write (10, '(f20.10)', IOSTAT = good_write1), magnitude
      write (20, '(f20.10)', IOSTAT = good_write2), phase

      if (good_write1 .ne. 0) then
	print *, 'The state of good_write1 is:'
	print *, good_write1
	print *, 'Error writing to magnitude file!'
	goto 1000
      else if (good_write2 .ne. 0) then
	print *, 'The state of good_write2 is:'
	print *, good_write2
	print *, 'Error writing to phase file!'
	goto 1000
      end if

    end do

    ! Tell user that output file was written successfully
    if (good_write1 .eq. 0) then
      print *, 'Output magnitude file written successfully....'
    endif
    
    if (good_write2 .eq. 0) then
      print *, 'Output phase file written successfully....'
    endif
    
    ! Deallocate memory held by plan
    call fftw_destroy_plan(plan)
    print *, 'Plan destroyed successfully....'
! 
! !   The following debug code checks to see if the Inverse DFFT will produce the original input data  
! !   print *, "Output file written successfully!"
! !     
! !   Swapping arrays to see if I can retrieve signal in time domain from signal in frequency domain
! !   in = out
! !     
! !   plan = fftw_plan_dft_1d(n, in, out, FFTW_BACKWARD, FFTW_ESTIMATE)
! !     
! !   print *, "The contents of the input array is ->"
! !   do i = 1,num_bins_int
! !     print *, in(i)
! !   end do
! !     
! !   print *
! !     
! !   print *, "Executing DFT on input array..."
! !   call fftw_execute_dft(plan, in, out)
! !     
! !   print *, "The contents of the output array is ->"
! !   do i = 1,num_bins_int
! !     print *, out(i)
! !   end do
! !     
! !   print *
! !     
! !   call fftw_destroy_plan(plan)
! !     


1000		close (1)
		close (10)
		close (20)
		deallocate (in)
		deallocate (out)
		deallocate (temp_real_array)
		print *, 'Files closed and memory deallocated'
		goto 4000

2000		close(1)
		close(10)
		close(20)
		print *, 'Files closed.....'
		goto 4000
		
3000		print *, 'Program completed successfully'
		
4000		print *, 'Exiting.....'

end program FFTW_from_data_file




