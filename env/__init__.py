import os
import dev

envs = {
    'dev': dev
}

if os.environ.get('YUCA_ENV'):
    env = os.environ['YUCA_ENV']
else:
    with open('tmp/YUCA_ENV') as env_file:
        env = env_file.readline().rstrip('\n')

config = envs[env]
