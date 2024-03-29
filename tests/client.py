#!/usr/bin/env python
'''test/client.py
This is test code of filt client.
'''

import unittest

from filt.client import FiltClient 


class TestFiltClient(unittest.TestCase):
    '''
    Test class of filt/client.py
    '''

    def test_send_request(self):
        '''
        Test method for send filt some data
        '''
        # params
        target = "hello world"
        url = "https://localhost:3000"

        # send
        filt = FiltClient(url)
        result = filt.send(target, verify=False)
        
        print(result)

    def test_send_request_with_option(self):
        '''
        Test method for send filt some data with option
        '''
        # params
        target = "hello world"
        url = "https://localhost:3000"
        option = {"hello": "world"}

        # send
        filt = FiltClient(url)
        result = filt.send(target, option=option, verify=False)
        
        print(result)

    def test_argument_error(self):
        '''
        Test method for check argument error
        '''
        
        # params
        correct = {
            'target': 'hello world',
            'url': 'https://localhost:3000',
            'option': {}
        }

        incorrect = {
            'url': 2,
            'option': 3
        }
        
        # check argument error
        filt = FiltClient(correct['url'])

        self.assertRaises(TypeError, lambda: FiltClient(incorrect['url']))
        self.assertRaises(TypeError, lambda: filt.send(correct['target'], incorrect['option'], verify=False))


if __name__ == '__main__':
    # run scanner
    unittest.main()
