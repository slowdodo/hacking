import subprocess

def control_computers(command):
  # List of IP addresses of the computers to control
  computers = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

  # Iterate over the list of computers
  for computer in computers:
    # Use the subprocess module to run the command on the remote computer
    subprocess.run(["ssh", computer, command])

# Example usage: run the command "ls" on all the computers
control_computers("ls")
