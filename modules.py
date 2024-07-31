import paramiko


def ssh_connect(host, username, password, port, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password, port=port)
        print("Connection successful")

        stdin, stdout, stderr = client.exec_command(command)

        '''for line in stdout:
            print(line.strip())'''
        output = stdout.read().decode()
        print(f"Output :\n{output}")
        if stderr.channel.recv_exit_status() != 0:
            print(f"Error: {stderr.read().decode()}")

    except Exception as e:
        print(f"Error : {e}")
    finally:
        client.close()


# Example usage
ssh_connect(host='192.168.1.95', username='root', password='Janu@2001', port=22, command="ls")
