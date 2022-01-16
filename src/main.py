from pwn import *
import commandDictionary


class AutomateBandit:

    def __init__(self, level, level_password):
        self.level = level
        self.level_password = level_password
        self.establish_new_connection()
        self.solutionDictionary = commandDictionary.solutionDictionary

    def establish_new_connection(self):
        self.session = ssh('bandit%d' % self.level, 'bandit.labs.overthewire.org', password=self.level_password,
                           port=2220)
        self.io = self.session.process('bash')
        time.sleep(1)
        print()
        print('%sLevel %d Access Granted!%s' % ('\033[91m', self.level, '\033[0m'))
        time.sleep(1)

    def execute_bash_command(self, list_command):
        for command in list_command:
            print('\nSending %s\'%s\'%s to the terminal' % ('\033[93m', command.decode('utf-8'), '\033[0m'), end='')
            self.io.sendline(command)
            self.io.recv()
            time.sleep(0.6)
            print('.', end='')
            time.sleep(0.6)
            print('.', end='')
            time.sleep(0.6)
            print('.', end='')
            time.sleep(1)

    def receive_password(self):
        self.level_password = self.io.recvline().decode('utf-8').strip()
        print('\nBingo! The password in this level is %s%s%s. Let\'s go to the next level!' % (
        '\033[92m', self.level_password, '\033[0m'))
        self.level += 1
        time.sleep(2)

    def solve_level_0_to_10(self):
        for list_command in self.solutionDictionary.values():
            self.execute_bash_command(list_command)
            self.receive_password()
            self.establish_new_connection()
        print()
        print('That\'s everything I can do for you, my friend. Goodbye...')


if __name__ == "__main__":
    automateProcess = AutomateBandit(0, 'bandit0')
    automateProcess.solve_level_0_to_10()
