import in_place
import os
import subprocess

def update():

    update = ['apt-get', 'update']

    #output = subprocess.Popen(update, stdout=subprocess.PIPE).communicate()[0]

    return subprocess.call(update)

    print(update)

def uvim():

    uvim = ['apt', 'upgrade', 'vim']

    return subprocess.call(uvim)
   
    print(uvim)

def iperf():

    iperf = ['apt-get', 'install', 'iperf']

    return subprocess.call(iperf)

    print(iperf)

def export1():

    export1 = ['sudo', 'export', 'LC_ALL=C']

    return subprocess.call(export1)

def  locale():

    locale = ['dpkg-reconfigure', ' locales']

    #output = subprocess.Popen(update, stdout=subprocess.PIPE).communicate()[0]

    return subprocess.call(locale)

def plocate():

    plocate = ['apt-get', 'install', 'plocate']

    return  subprocess.call(plocate)

def ub():

    ub = ['updatedb']

    return subprocess.call(ub)

def nginx():

    nginx = ['apt-get', 'install', 'nginx']

    return subprocess.call(nginx)

def nenable():

    nenable = ['systemctl', 'enable', 'nginx']

    return subprocess.call(nenable)

def nstart():

    nstart = ['systemctl', 'start', 'nginx']

    return subprocess.call(nstart)

def nginxstat():

    sys = ['systemctl', 'status', 'nginx']

    output = subprocess.Popen(sys, stdout=subprocess.PIPE).communicate()[0]

    print(output)

def whoami():

    who = ['ip', 'a']
   
    output = subprocess.Popen(who, stdout=subprocess.PIPE).communicate()[0]

    print(output)

def ip():

   ip = input('Enter the ProxMox IP: ')

   path = input('What is the name of the server? (Enter exactly): ')

   # changeIp = input('What is the current IP: ')

   with in_place.InPlace('/etc/nginx/sites-enables/default') as file:
    for line in file:


            line = line.replace('##' , '')                
            line = line.replace('# available underneath a path with that package name, such as /drupal8.' ,'upstream proxmox {')
            line = line.replace('# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.' , '   server 000.000.000.000:8006;')
            line = line.replace('# Default server configuration' , '      }')
            line = line.replace('index index.html index.htm index.nginx-debian.html;', '')
            line = line.replace('root /var/www/html;'  , '')
            line = line.replace('server_name _;' , '')

            line = line.replace('listen 80 default_server;' , 'listen 443 ssl;')
            line = line.replace('listen [::]:80 default_server;' , 'listen[::]:443 ssl;')
            line = line.replace('# SSL configuration' , 'server_name proxmox.server.com;')
            line = line.replace(' # listen 443 ssl default_server;' , ' ssl_certificate /etc/pve/nodes/NOODLES/pve-ssl.pem;')
            line = line.replace(' # listen [::]:443 ssl default_server;' , ' ssl_certificate_key /etc/pve/nodes/BOODLES/pve-ssl.key;')  
            line = line.replace('# Note: You should disable gzip for SSL traffic.' , 'proxy_redirect off;')
            line = line.replace('# First attempt to serve request as file, then' , 'proxy_pass https://proxmox;')
            line = line.replace('# as directory, then fall back to displaying a 404.' , 'proxy_buffering off;')
            line = line.replace('try_files $uri $uri/ =404;' , 'client_max_body_size 1000; \n# Enable Websockets \n                proxy_http_version 1.1; \n                proxy_set_header Upgrade $http_upgrade; \n                proxy_set_header Connection "upgrade";')
           
            line = line.replace('000.000.000.000' , ip)
            line = line.replace('NOODLES', path)
            line = line.replace('BOODLES', path)

            file.write(line)
           
def restart():

    restart = ['systemctl', 'restart', 'nginx']

    return subprocess.call(restart)




update()
uvim()
iperf()
export1()
locale()
plocate()
ub()
nginx()
nenable()
nstart()
nginxstat()
whoami()
ip()
restart()
