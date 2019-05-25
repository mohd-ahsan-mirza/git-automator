import subprocess
import paramiko
import sys
import os
from os.path import join, dirname, splitext
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)