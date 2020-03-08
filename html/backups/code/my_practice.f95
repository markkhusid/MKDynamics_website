    program my_practice
        implicit none

        real, dimension (1:5)   :: current, voltage, complex_power
        real                    :: energy

        integer :: i, n=5

        print *, 'Hello World!'

        i = 1           ! Intialize counter variable

        ! Open data files that contains current utilization data and line voltage data,
        ! one element per line, and in floating point format
        open (unit=1, file="current.dat", status="old")
        open (unit=20, file="voltage.dat", status="old")

        ! Traverse through data file and fill array up with data element in file
        do i = 1,n

            read (1, '(f20.10)', END = 1000, ERR = 1000), current(i)
            print *, 'The data element read from current.dat file was ->'
            print '(f20.10)', current(i)

            read (20, '(f20.10)', END = 2000, ERR = 2000), voltage(i)
            print *, 'The data element read from voltage.dat file was ->'
            print '(f20.10)', voltage(i)

        end do


        !voltage = (/50.0, 50.0, 50.0, 50.0, 50.0/)

        complex_power = voltage * current

        print *, 'The calculated power dissipation is ->'
        print '(f20.10)', complex_power

        print *, 'Below is a list of the cumulative energy ->'
        do i = 1,(n)
            energy = energy + (complex_power(i)*i)
            print '(f20.10)', energy
        end do

        print *, 'The accumulated energy is ->'
        print '(f20.10)', energy

1000    close (1)
2000    close (20)
        print *, 'Program completed'

        end program my_practice
