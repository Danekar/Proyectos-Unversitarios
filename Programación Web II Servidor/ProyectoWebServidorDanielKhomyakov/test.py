from urllib.request import urlopen

'''
TESTEO DE LA APLICACIÓN
'''

def test_connection(module):
    production = False
    if (production == False):
        try:
            if(urlopen("http://davidpefue.pythonanywhere.com/{}/test".format(module)).read() != b'OK'):
                print("Error: {} has issues!".format(module))
        except:
            print("Error: {} unreachable!".format(module))
    else:
        pass

test_connection("moduleIndex")
test_connection("moduleLoginPass")