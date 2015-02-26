! This is a test of git
program FFTW_from_data_file
    
    use, intrinsic      :: iso_c_binding
    include 'fftw3.f03'
    
    type(C_PTR)         					:: plan
    
    integer, parameter						:: num_expected_args=4				! Input file name, output file name and number of bins
    
    complex(C_DOUBLE_COMPLEX), dimension(:), allocatable	:: in, out
        
    real, dimension(:), allocatable				:: temp_real					! Holds the data read from the input file
    real							:: magnitude, phase
    
    integer							:: EOF_marker
    integer							:: file_good1, file_good2, file_good3
    integer							:: good_write1, good_write2
    integer							:: i,j
    integer							:: num_args					! Contains number of arguments for verification of proper command line call
    integer							:: num_bins_int
    integer							:: status1, status2, status3
    
    character(len=80)						:: input_file, output_mag_file 
    character(len=80)						:: output_phase_file, num_bins_chr	
    
    ! Verify that the number of arguments is correct.  Should be 3, otherwise display
    ! error and terminate program
    num_args = command_argument_count()
    if (num_args .ne. num_expected_args) then
      print *, 'Improper number of arguments'
      print *, 'Argument list:'
      print *, '<input file name> <output magnitude file name> <output phase file name> <number of bins>'
      goto 1000								! Graceful exit
    end if
    
    ! Call subroutines that obtain the command line arguments and load the appropriate variables
    call get_command_argument (1, input_file)
    call get_command_argument (2, output_mag_file)
    call get_command_argument (3, output_phase_file)
    call get_command_argument (4, num_bins_chr)
    
    ! Debug code that ensures command line arguments were passed in properly
    print *, 'The first argument is ->'
    print *, input_file
    
    print *, 'The second argument is ->'
    print *, output_mag_file
    
    print *, 'The third argument is ->'
    print *, output_phase_file
    
    print *, 'The fourth argument is (as str)->'
    print *, num_bins_chr
    read (num_bins_chr, *) num_bins_int
    
    print *, 'The fourth argument is (as int) ->'
    print *, num_bins_int
    
    ! Allocate memory based on the number of bins command line argument.
    ! Display success status of memory allocation
    ! If there is a problem with memory allocation, display error and terminate
    allocate (in(num_bins_int), stat=status1)
    print *, 'Was memory allocated successfully for input array? ->'
    print *, allocated(in)
    if (status1 .ne. 0) then
      print *, 'Memory allocation error on input array'
      goto 1000
    end if
    
    allocate (out(num_bins_int), stat=status2)
    print *, 'Was memory allocated successfully for output array? -> ->'
    print *, allocated(out)
    if (status2 .ne. 0) then
      print *, 'Memory allocation error on output array'
      deallocate (in)
      goto 1000
    end if
    
    allocate (temp_real(num_bins_int), stat=status3)
    print *, 'Was memory allocated successfully for scratchpad array? ->'
    print *, allocated(temp_real)
    if (status3 .ne. 0) then
      print *, 'Memory allocation error on scratchpad array'
      deallocate (in)
      deallocate (out)
      goto 1000
    end if
    
    ! Begin to open files
    open (unit=1, file=TRIM(input_file), status="old", IOSTAT=file_good1, form="formatted", access="sequential", action="read")
    !open (unit=1, file=TRIM(input_file), IOSTAT=file_good1)
    if (file_good1 .ne. 0) then
      print *, 'Error opening input file!'
      goto 1000
    else if (file_good1 .eq. 0) then
      print *, 'Input file opened successfully...'
    end if
    
    open (unit=10, file=TRIM(output_mag_file), status="replace", IOSTAT=file_good2, form="formatted", access="sequential")
    if (file_good2 .ne. 0) then
      print *, 'Error creating output magnitude file!'
      goto 1000
    else if (file_good2 .eq. 0) then
      print *, 'Output magnitude file created successfully...'
    end if

    open (unit=20, file=TRIM(output_phase_file), status="replace", IOSTAT=file_good3, form="formatted", access="sequential")
    if (file_good3 .ne. 0) then
      print *, 'Error creating output phase file!'
      goto 1000
    else if (file_good3 .eq. 0) then
      print *, 'Output phase file created successfully...'
    end if
    
!	Debug code follows
!     read (unit=1, fmt='(f20.10)', IOSTAT = EOF_marker), temp_real(1)
!     print *, 'The status of EOF_marker is'
!     print *, EOF_marker
!     print *, 'The first element read was'
!     print *, temp_real(1)
!	Debug code ends

    ! Traverse through data file and fill array up with data element in file
    ! Get first data element from file to see whether it is the EOF character
    i = 1
    read (1, '(f20.10)', IOSTAT = EOF_marker), temp_real(i)
!   Debug code starts here
!     write (*, '(a, i4)'), 'The EOF marker is ->', EOF_marker
!     write (*, '(a, i4)'), 'The counter is ->', i
!     write (*, '(a, 10f10.4)'), 'The data element was ->', temp_real(i)
!     print *
!     print *
!   Debug code ends here
    
    !Establish a loop that reads until the EOF character is reached, then exit loop
 read_loop:   do
      if (EOF_marker < 0) then						! EOF reached
	exit read_loop
      else
	i = i + 1							! increment counter
	read (1, '(f20.10)', IOSTAT = EOF_marker), temp_real(i)		! read next data element from file
      
      ! Debug code starts here
! 	write (*, '(a, i4)'), 'The EOF marker is ->', EOF_marker
! 	write (*, '(a, i4)'), 'The counter is ->', i
! 	write (*, '(a, 10f10.4)'), 'The data element was ->', temp_real(i)
! 	print *
! 	print *
      ! Debug code ends here
      end if
     end do read_loop
    
    !Decrement counter i by one to account for the EOF character
    i = i - 1
    
    ! Debug code starts here
!    print *, EOF_marker
!    print *, i
!    print *, num_bins_int
    ! Debug code ends here
    
    ! Error checking section
    ! EOF_marker < 0 means end-of-file reached
    if ((EOF_marker .ne. 0) .and. (i < num_bins_int)) then
      print *, 'Number of data elements within input file and number of bins do not match...'
      print *, 'The number of data elements within the input file is:', i
      print *, 'Routine is expecting', num_bins_int, 'elements'
      goto 1000
    else if ((EOF_marker .ne. 0) .and. (i > num_bins_int)) then
      print *, 'Insufficient number of bins to match number of elements in file.'
      print *, 'The last data element read from file at position ', i, 'was ->'
      print '(f20.10)', temp_real(i)
      print *
      goto 1000
    else if ((EOF_marker .ne. 0) .and. (i .eq. (num_bins_int))) then
      print *, 'Number of data elements in file and number of bins match.'
      ! Debug code starts here
!       do j = 1 , i
! 	print *, 'The data element read from file at position ', j, 'was ->'
! 	print '(f20.10)', temp_real(j)
! 	print *
!       end do
      ! Debug code ends here
    end if
    
    ! *************** FFT COMPUTATION SECTION **********************
    
    ! Establish array of reals that is the input the FFTW3 function
    in = temp_real
    
    ! Use built in fucntion to create FFTW3 plan.  Tells FFTW3 what to do.
    plan = fftw_plan_dft_1d(num_bins_int, in, out, FFTW_FORWARD, FFTW_ESTIMATE)

    print *
    print *
         
    ! Execute FFTW3 to produce DFFT on data from file stored in array
    print *, "Executing DFT on input array..."
    call fftw_execute_dft(plan, in, out)
     
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
      print *, out(i)
      magnitude = sqrt((real(out(i))**2) + (aimag(out(i))**2))
      phase = atan(aimag(out(i)) / real(out(i)))
      
      write (10, '(f20.10)', IOSTAT = good_write1), magnitude
      write (20, '(f20.10)', IOSTAT = good_write2), phase

      if (good_write1 .ne. 0) then
	print *, 'Error writing to magnitude file!'
	goto 1000
      else if (good_write2 .ne. 0) then
	print *, 'Error writing to phase file!'
      end if

    end do

    ! Tell user that output file was written successfully
    if (good_write1 .eq. 0) then
      print *, 'Output magnitude file written successfully....'
    else
      print *, 'IO error writing magnitude file!'
    endif
    
    if (good_write2 .eq. 0) then
      print *, 'Output phase file written successfully....'
    else
      print *, 'IO error writing phase file!'
    endif
    
    ! Deallocate memory held by plan
    call fftw_destroy_plan(plan)

!   The following debug code checks to see if the Inverse DFFT will produce the original input data  
!   print *, "Output file written successfully!"
!     
!   Swapping arrays to see if I can retrieve signal in time domain from signal in frequency domain
!   in = out
!     
!   plan = fftw_plan_dft_1d(n, in, out, FFTW_BACKWARD, FFTW_ESTIMATE)
!     
!   print *, "The contents of the input array is ->"
!   do i = 1,num_bins_int
!     print *, in(i)
!   end do
!     
!   print *
!     
!   print *, "Executing DFT on input array..."
!   call fftw_execute_dft(plan, in, out)
!     
!   print *, "The contents of the output array is ->"
!   do i = 1,num_bins_int
!     print *, out(i)
!   end do
!     
!   print *
!     
!   call fftw_destroy_plan(plan)
!     


1000		close (1)
		close (10)
		close (20)
		deallocate (in)
		deallocate (out)
		deallocate (temp_real)
		print *, 'Exiting.....'
		
end program FFTW_from_data_file




