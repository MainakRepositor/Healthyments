import subprocess
cmd = ['python3','-m','textblob.download_corpora']
subprocess.run(cmd)
print("Working")