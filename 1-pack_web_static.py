#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from datetime import datetime
from fabric.api import local
from os import path


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
    except Exception:
        return (None)
