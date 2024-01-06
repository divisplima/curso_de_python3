"""
Crie um código em Python que teste se o site Pudim está acessível pelo compudador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site não está acessível no momento.")
else:
    print("O site está acessível no momento.")
