#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#
# @author:  Ritashugisha
# @contact: ritashugisha@gmail.com

import sys
import utils

# Use cocoadialog to set the download path for downloads to be saved
def setDownloadPath():
    proc = '%s fileselect --title %s --text %s --select-only-directories --stirng-output --float' % (utils.COCOA,
    utils.TITLE, utils.formatSpaces('Set where downloads are saved to by default:'))
    result = utils.runProcess(proc)
    if len(result.split('\n')) < 2:
        sys.exit(0)
    else:
        downloadText = open(utils.DOWNLOADS, 'w')
        downloadText.write('%s/' % result.split('\n')[0])
        downloadText.close()
        utils.displayNotification(utils.TITLE, 'Download path changed', '%s/' % result.split('\n')[0], '')

# Use cocoadialog to display history text         
def displayHistory():
    proc = '%s textbox --title %s --informative-text %s --text-from-file %s --button1 %s --button2 %s --float' % (utils.COCOA,
    utils.TITLE, utils.formatSpaces('Luxinate download history:'), utils.formatSpaces(utils.HISTORY), 'Ok', utils.formatSpaces('Clear History'))
    results = utils.runProcess(proc)
    if results.split('\n')[0] == '2':
        wipeHistory = open(utils.HISTORY, 'w')
        wipeHistory.close()
        utils.displayNotification(utils.TITLE, 'Luxinate history cleared', '', '')

# Use cocoadialog to display about text        
def displayAbout():
    proc = '%s textbox --title %s --informative-text %s --text-from-file %s --button1 %s --float' % (utils.COCOA,
    utils.TITLE, utils.formatSpaces('About Luxinate:'), utils.ABOUT, 'Ok')
    utils.runProcess(proc)

# Use cocoadialog to set default video download format    
def setVideoFormat():
    videoFormats = {
        '5':'FLV 240p', '6':'FLV 270p', '17':'3GP 144p', '18':'MP4 360p', '22':'MP4 720p', '34':'FLV 360p',
        '35':'FLV 480p', '36':'3GP 240p', '37':'MP4 1080p', '43':'WebM 360p', '44':'WebM 480p', '45':'WebM 720p', '46':'WebM 1080p',
        '82':'[3D] MP4 360p', '83':'[3D] MP4 240p', '84':'[3D] MP4 720p', '85':'[3D] MP4 520p', '100':'[3D] WebM 360p', '102':'[3D] WebM 720p'
    }
    videoFormatsList = '"%s"' % '" "'.join(videoFormats.values())
    procCmd = '%s dropdown --title %s --text %s --items %s --string-output --button1 %s --button2 %s --button3 %s --float' % (utils.COCOA, 
    utils.TITLE, utils.formatSpaces('Choose desired video format:'), videoFormatsList, 'Ok', 'Cancel', 'Reset')
    desiredFormat = utils.runProcess(procCmd)
    if desiredFormat.split('\n')[0].lower() == 'cancel':
        sys.exit(0)
    elif desiredFormat.split('\n')[0].lower() == 'reset':
        wipeFormat = open(utils.FORMAT_VIDEO_PATH, 'w')
        wipeFormat.close()
        utils.displayNotification(utils.TITLE, 'Default video download format reset', '', '')
    else:
        for key, value in videoFormats.iteritems():
            if value == desiredFormat.split('\n')[1].replace('\n', ''):
                newFormat = open(utils.FORMAT_VIDEO_PATH, 'w')
                newFormat.write(key)
                newFormat.close()
                utils.displayNotification(utils.TITLE, 'Default video format: %s' % value, '', '')

# Use cocoadialog to set default audio download format    
def setAudioFormat():
    audioFormats = {
        '.mp3':'MP3', '.wav':'WAV', '.ogg':'OGG', '.m4a':'M4A', '.wma':'WMA'
    }
    audioFormatsList = '"%s"' % '" "'.join(audioFormats.values())
    procCmd = '%s dropdown --title %s --text %s --items %s --string-output --button1 %s --button2 %s --button3 %s --float' % (utils.COCOA, 
    utils.TITLE, utils.formatSpaces('Choose default audio format:'), audioFormatsList, 'Ok', 'Cancel', 'Reset')
    desiredFormat = utils.runProcess(procCmd)
    if desiredFormat.split('\n')[0].lower() == 'cancel':
        sys.exit(0)
    elif desiredFormat.split('\n')[0].lower() == 'reset':
        wipeFormat = open(utils.FORMAT_AUDIO_PATH, 'w')
        wipeFormat.close()
        utils.displayNotification(utils.TITLE, 'Default audio download format reset', '', '')
    else:
        for key, value in audioFormats.iteritems():
            if value == desiredFormat.split('\n')[1].replace('\n', ''):
                newFormat = open(utils.FORMAT_AUDIO_PATH, 'w')
                newFormat.write(key)
                newFormat.close()
                utils.displayNotification(utils.TITLE, 'Default audio format: %s' % value, '', '')

# Install SoundCloud API using pip or easy_install
def installSoundCloudAPI():
    validatePip = utils.runProcess('whereis pip')
    if validatePip:
        osaCmd = 'osascript -e \'tell application "Alfred 2" to do shell script "sudo pip install soundcloud" with administrator privileges\''
    else:
        osaCmd = 'osascript -e \'tell application "Alfred 2" to do shell script "sudo easy_install soundcloud" with administrator privileges\''
    utils.displayNotification(utils.TITLE, 'Installing SoundCloud API', 'Please enter your user password...', '')
    utils.runProcess(osaCmd)
    utils.displayNotification(utils.TITLE, 'Installation Complete', '', '')

# Toggle progress bar on and off    
def toggleProgressBar():
    if utils.PROGRESS:
        wipeProgress = open(utils.PROGRESS_BAR, 'w')
        wipeProgress.close()
        utils.displayNotification(utils.TITLE, 'Progress bar turned off', '', '')
    else:
        bumpProgress = open(utils.PROGRESS_BAR, 'w')
        bumpProgress.write('True')
        bumpProgress.close()
        utils.displayNotification(utils.TITLE, 'Progress bar turned on', '', '')

# Check for updates in the raw update file on Luxinate's github                                       
def checkUpdates():
    import ast
    import urllib2
    import webbrowser
    updateDict = ast.literal_eval(urllib2.urlopen('https://raw.github.com/Ritashugisha/luxinate/master/Updates/update.txt').read())
    if updateDict['version'] > utils.VERSION:
        procCmd = '%s msgbox --title %s --text %s --informative-text %s  --button1 %s --button2 %s --button3 %s --string-output --float' % (utils.COCOA, 
        utils.TITLE, utils.formatSpaces('Luxinate %s is available to update!' % updateInfo['version']),
        utils.formatSpaces('Choose which color of Luxinate you would like to update:'), 'Black', 'White', 'Cancel')
        updateResponse = utils.runProcess(procCmd)
        if updateResponse.lower() == 'cancel':
            sys.exit(0)
        else:
            if updateResponse.lower()[0] == 'w':
                webbrowser.open(updateInfo['white'])
            elif updateResponse.lower()[0] == 'b':
                webbrowser.open(updateInfo['black'])
    else:
        procCmd = '%s msgbox --title %s --text %s --button1 %s' % (utils.COCOA, 
        utils.TITLE, utils.formatSpaces('Your version of Luxinate is up to date!'), 'Ok')
        utils.runProcess(procCmd)
