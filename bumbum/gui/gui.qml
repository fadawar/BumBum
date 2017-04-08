import QtQuick 2.0

Rectangle {
    id: root
    width: 550
    height: 90
    color: cBg


    property var cBg: String("#556270")
    property var cMain: String("#4ecdc4")
    property var sizeMargin: 10
    property var sizeRadius: 4

    signal downloadVideo(string url)

    function setStatus(text) {
        status.text = text;
    }

    FontLoader {
        id: mainFont
        source: './fonts/lato/Lato-Regular.ttf'
    }


    Rectangle {
    	id: searchRect
    	anchors.horizontalCenter: parent.horizontalCenter
    	anchors.right: parent.right
       	anchors.top: parent.top
      	anchors.margins: sizeMargin
    	radius: sizeRadius
    	height: 50
    	color: cMain

    	TextInput {
    	    id: searchInput
    	    anchors.fill: parent
    	    anchors.margins: sizeMargin
    	    focus: true
    	    font.family: mainFont.name
    	    font.pixelSize: 22
    	    color: '#ffffff'

    	    Keys.onReturnPressed: {
                root.downloadVideo(text)
                text = ''
                status.text = 'Downloading...'
            }

    	    Text {
    	        anchors.fill: parent
    	        font.pixelSize: parent.font.pixelSize
    	        color: '#245d58'
    	        text: 'Paste url & hit Enter'
    	        visible: parent.text == ''
    	    }
    	}
    }

    Text {
        id: status
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.margins: sizeMargin
        text: ''
    }
}