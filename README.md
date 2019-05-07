# OpenBLAS bug

This repository reproduces the different behaviour when doing matrix multiplications between R/python(compiled with foss/2016b) and R/python(compiled with foss/2018b). 

The expected output is that the last line of the output, both in R and in Python, should read 'True'.

## R

### foss/2016b

```
$ module load R/3.4.1-X11-20160819 
$ Rscript check.R
R version 3.4.1 (2017-06-30)
Platform: x86_64-pc-linux-gnu (64-bit)
Running under: Red Hat Enterprise Linux Server 7.6 (Maipo)

Matrix products: default
BLAS/LAPACK: ${install_location_eb_softwate}/OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1/lib/libopenblas_haswellp-r0.2.18.so

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

attached base packages:
[1] stats     graphics  grDevices utils     datasets  base     

loaded via a namespace (and not attached):
[1] compiler_3.4.1
[1] TRUE

```

### foss/2018b

```
$ module load R/3.5.1
$ Rscript check.R
R version 3.5.1 (2018-07-02)
Platform: x86_64-pc-linux-gnu (64-bit)
Running under: Red Hat Enterprise Linux Server 7.6 (Maipo)

Matrix products: default
BLAS/LAPACK: ${install_location_eb_softwate}/OpenBLAS/0.3.1-GCC-7.3.0-2.30/lib/libopenblas_haswellp-r0.3.1.so

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

loaded via a namespace (and not attached):
[1] compiler_3.5.1
[1] "Mean relative difference: 0.03459669"

```


## Python

### foss/2016b

```
$ module load Python/3.5.2
$ python check.py 
openblas_info:
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1/lib']
    libraries = ['openblas', 'openblas']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
openblas_lapack_info:
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1/lib']
    libraries = ['openblas', 'openblas']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
blas_mkl_info:
  NOT AVAILABLE
lapack_opt_info:
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1/lib']
    libraries = ['openblas', 'openblas']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
blas_opt_info:
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.2.18-GCC-5.4.0-2.26-LAPACK-3.6.1/lib']
    libraries = ['openblas', 'openblas']
    define_macros = [('HAVE_CBLAS', None)]
    language = c
True

```


### foss/2018b

```
$ module load Python/3.6.6
$ python check.py 
blas_mkl_info:
  NOT AVAILABLE
blis_info:
  NOT AVAILABLE
openblas_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.3.1-GCC-7.3.0-2.30/lib']
    language = c
    define_macros = [('HAVE_CBLAS', None)]
blas_opt_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.3.1-GCC-7.3.0-2.30/lib']
    language = c
    define_macros = [('HAVE_CBLAS', None)]
lapack_mkl_info:
  NOT AVAILABLE
openblas_lapack_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.3.1-GCC-7.3.0-2.30/lib']
    language = c
    define_macros = [('HAVE_CBLAS', None)]
lapack_opt_info:
    libraries = ['openblas', 'openblas']
    library_dirs = ['${install_location_eb_softwate}/OpenBLAS/0.3.1-GCC-7.3.0-2.30/lib']
    language = c
    define_macros = [('HAVE_CBLAS', None)]
False
Traceback (most recent call last):
  File "check.py", line 12, in <module>
    np.testing.assert_array_equal(n1, n2)
  File "${install_location_eb_softwate}/Python/3.6.6-foss-2018b/lib/python3.6/site-packages/numpy-1.15.0-py3.6-linux-x86_64.egg/numpy/testing/_private/utils.py", line 856, in assert_array_equal
    verbose=verbose, header='Arrays are not equal')
  File "${install_location_eb_softwate}/Python/3.6.6-foss-2018b/lib/python3.6/site-packages/numpy-1.15.0-py3.6-linux-x86_64.egg/numpy/testing/_private/utils.py", line 780, in assert_array_compare
    raise AssertionError(msg)
AssertionError: 
Arrays are not equal

(mismatch 15.646023594182026%)
 x: array([2339.239341, 2219.418399, 2375.465724, ..., 1869.714533,
       1803.79818 , 1978.712923])
 y: array([2339.239341, 2219.418399, 2375.465724, ..., 1869.714533,
       1803.79818 , 1978.712923])

```
