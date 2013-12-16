#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#
# @author:  Ritashugisha
# @contact: ritashugisha@gmail.com

import utils

# Use osascript to search either Safari or Chrome for all currently opened tabs
#
# @param browser ('Safari' or 'Chrome')
# @return [URL0, URL1, URL2]
def process(browser):
    osaCmd = "osascript -e 'tell application \"%s\" to get URL of every Tab of every Window'" % browser
    return utils.runProcess(osaCmd).replace('\n', '').split(', ')

# Get open tabs, validate for download, add item to Alfred feed
#
# @param query '{query}' (null)
# @param browser ('Safari' or 'Chrome')
def LuxinateBrowser(query, browser):
    feed = utils.Feedback()
    for i in process(browser):
        try:
            (mediaTitle, mediaFile) = utils.getMediaInfo(i)
            if utils.determineMediaType(mediaFile) == 1:
                q = "{'node':%s,'url':\'%s\','title':\'%s\','file':\'%s\'}" % ('1',
                i, utils.formatDict(mediaTitle), utils.formatDict(mediaFile))
                feed.add_item(mediaTitle, i, q, '', '', 'Icons/_download.png')
            elif utils.determineMediaType(mediaFile) == 2:
                q = "{'node':%s,'url':\'%s\','title':\'%s\','file':\'%s\'}" % ('2',
                i, utils.formatDict(mediaTitle), utils.formatDict(mediaFile))
                feed.add_item(mediaTitle, i, q, '', '', 'Icons/_download.png')
        except ValueError:
            feed.add_item('No download', 'Invalid URL %s' % i, "{'node':%s}" % '0', '', '', 'Icons/_x.png')
    print feed

# Tell application Alfred 2 to search for the default lux option and pass the selected URL
#
# @param query Dictionary of download information    
def openLuxDefault(query):
    osaCmd = 'osascript -e \'tell application "Alfred 2" to search "lux ► " & "' + query['url'] + '"\''
    utils.runProcess(osaCmd)
    