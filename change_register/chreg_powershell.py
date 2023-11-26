import subprocess

ps_command = 'Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies" -Name "ActiveDesktop" -Value "0"'