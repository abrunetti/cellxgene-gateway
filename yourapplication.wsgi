import sys

# TODO: Modificare in base a percorsi
sys.path.insert(0, '/home/antonio/cellxgene_itb/cellxgene_venv/bin')
sys.path.insert(0, '/home/antonio/cellxgene_itb/cellxgene_venv/lib/python3.6/site-packages')
sys.path.insert(0, '/home/antonio/cellxgene_itb/cellxgene-gateway')
sys.path.insert(0, '/home/antonio/cellxgene_data')

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

from cellxgene_gateway.gateway import app as application
