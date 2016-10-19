#!/bin/env python3
"""
simple script to get the artist and title of the current playing song
"""

import logging
import logging.config

from mpd import MPDClient


LOGGER = logging.getLogger(__name__)
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
    },
})


def get_title(song):
    """
    get the songtitle
    """
    LOGGER.debug('get_title method called')
    if 'title' in song:
        LOGGER.debug('song has a title')
        shown_name = song['title']
        get_artist(song, shown_name)
    else:
        LOGGER.debug('song has no title')
        shown_name = '!#Â¿@?'
        get_artist(song, shown_name)


def get_artist(song, shown_name):
    """
    get the artist
    """
    LOGGER.debug('get_artist method called')
    if 'artist' in song:
        LOGGER.debug('song has an artist')
        shown_name = song['artist'] + ' - ' + shown_name
        print_statusline(shown_name)
    else:
        LOGGER.debug('song has no artist')
        print_statusline(shown_name)


def print_statusline(shown_name):
    """
    print the songname
    """
    LOGGER.debug('print_statusline method called')
    print(shown_name + ' | ')


def main():
    """
    the main function
    """
    LOGGER.debug('main method called')
    client = MPDClient()
    client.connect("localhost", 6600, timeout=None)
    song = client.currentsong()

    if client.status()['state'] in ('play', 'pause'):
        LOGGER.debug('client is in play or pause mode')
        get_title(song)
    else:
        LOGGER.debug('client has stopped')

if __name__ == '__main__':
    main()
