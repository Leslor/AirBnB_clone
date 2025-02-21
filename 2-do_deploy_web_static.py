#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
from os.path import exists
from fabric.api import put, run, env
env.hosts = ['3.80.49.204', '34.229.127.31']


def do_deploy(archive_path):
    """ Fabric script that  distributes
    an archive to your web servers, using
    the function do_deploy"""
    # archive_path = versions/web_static_220920223.tgz

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path[9:]
        # file_name = web_static_220920223.tgz
        name = file_name[:-4]
        # name = web_static_220920223
        # Upload the archive to the /tmp/ directory of the webserver
        directory = '/tmp/{}'.format(file_name)
        put(archive_path, directory)
        # Uncompress to data/web_static/releases/<archive>
        f_web = "/data/web_static/releases/"
        # Uncompress the archive to the folder /data/web_static/
        run('mv {} {}'.format(directory, f_web))
        # /data/web_static/releases/web_static_098098988
        run('tar -xf {}{}'.format(f_web, name))
        # Delete the archive from the web server
        run('rm {}{}'.format(f_web, file_name))
        # Delete simbolic Link
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(f_web, name))
        return True
    except Exception:
        return False
