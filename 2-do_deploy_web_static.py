#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
from os.path import exists
from fabric.api import put, run, env
env.hosts = ['3.80.49.204', '34.229.127.31']


def do_pack():
    """Fabric script that generates a .tgz archive
    from the contents of the web_static folder
    of your AirBnB Clone repo,
    using the function do_pack. """
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = 'versions/web_static_{}.tgz'.format(today)

    folder_version = exists("versions")
    if folder_version is False:
        local('mkdir -p versions')
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ Fabric script that  distributes
    an archive to your web servers, using
    the function do_deploy"""
    # archive_path = versions/web_static_220920223.tgz
    if exists(archive_path):
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
        # run('mkdir -p {}'.format(f_web))
        run('mv {} {}'.format(directory, f_web))
        # /data/web_static/releases/web_static_098098988
        run('tar -xf {}{}'.format(f_web, name))
        # Delete the archive from the web server
        # Delete /tmp/web_static_898980.tgz
        run('rm {}{}'.format(f_web, file_name))
        # Delete simbolic Link
        # run("rm -rf {}web_static".format(f_web))
        run("rm -rf /data/web_static/current")
        run("ln -s {}name /data/web_static/current".format(f_web))
        return True
    return False
