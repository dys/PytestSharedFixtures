cmd = """
python -c 'from libraries.library_one import library_one
l1 = library_one()
print l1.config'
"""
print cmd
from subprocess import check_output
config = check_output(cmd, shell=True)
print config
