#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ['100.24.255.23', '54.234.80.214']
env.user = 'ubuntu'


def do_pack():
    """
    generates a .tgz archive from the contents of
    he web_static folder of your AirBnB Clone repo,
    using the function do_pack.
    """
    try:
        local('mkdir -p versions')
        moment = datetime.now()
        archive_file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
            moment.year, moment.month, moment.day, moment.hour,
            moment.minute, moment.second)
        local('tar -cvzf {} web_static'.format(archive_file_name))
        print('web_static packed: {} -> {}'
              .format(archive_file_name, path.getsize(archive_file_name)))
        return (archive_file_name)
    except Exception:
        return (None)


def do_deploy(archive_path):
    """
        Fabric script that distributes an archive to your web servers,
        using the function do_deploy
    """
    if not path.exists(archive_path):
        return (False)
    try:
        get_file_name = archive_path.split('/')[-1]
        file_path = '/data/web_static/releases/'
        folder_path = file_path + get_file_name.split('.')[0]
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(folder_path))
        run('tar -xzf /tmp/{} -C {}'.format(get_file_name, folder_path))
        run('rm /tmp/{}'.format(get_file_name))
        run('mv {}/web_static/* {}/'.format(folder_path, folder_path))
        run('rm -rf {}/web_static'.format(folder_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(folder_path))
        print('New version deployed!')
        return (True)
    except Exception:
        return (False)


def deploy():
    """
    Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return (False)
    return do_deploy(archive_path)
