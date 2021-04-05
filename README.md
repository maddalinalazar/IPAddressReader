To run the main script: 
* cd to the root of the package, in my case: ````
* Run the follwing command: ``python3 ip_address_reader/cli.py --path  resources/test-log-file.log --ip 180.76.15.0/24`` 
or ``python3 ip_address_reader/cli.py --path  resources/test-log-file.log --ip 180.76.15.0/24``

**I'm using python3 mainly because I don't have an alias yet for it, but to be sure this is the version of python I'm running with**: ``Python 3.7.4``

The unit tests aren't curently running in the command line due to an import issue. I am able to partially run them in PyCharm.
To run them locally I was trying with something like: ``python3 -m unittest test.ip_filter_test.IPFilterTest.test_check_mask_for_ipv4_ip_w_mask``
I'm still trying to make them work.
