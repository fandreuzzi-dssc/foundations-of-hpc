from string import Template
import sys

n_max = int(sys.argv[1])

template = """
#!/bin/bash
### Job Name
#PBS -N ring$P
### Project code
#PBS -l walltime=$walltime
#PBS -q dssc
### Merge output and error files
#PBS -o /u/dssc/fandreuz/HPC/assignment1/ring$P.txt
#PBS -l select=1:ncpus=$P:mpiprocs=$P
### Send email on abort, begin and end
#PBS -m abe
### Specify mail recipient
#PBS -M andreuzzi.francesco@gmail.com

cd /u/dssc/fandreuz/HPC/assignment1

module load openmpi/4.0.3/gnu/9.3.0

mpic++ -D TIME_ONLY -D MAIN_ONLY ring.cpp

### Run the executable
mpirun -np $P a.out
"""

for i in range(2,n_max+1):
	t = Template(template)
	text = t.substitute({'P': i, 'walltime': '00:30:00'})

	text_file = open("ring{}.pbs".format(i), "w")
	text_file.write(text)
	text_file.close()
