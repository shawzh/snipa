import QtQuick 2.4
import QtQuick.Controls 1.4

Rectangle {

    signal clicked;

    id: window;
    width: 800;
    height: 600;
    focus: true;
    color: "#272822";

    Text {
        id: helloText
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Hello World!!!\n Traditional first app using PyQt5"
        horizontalAlignment: Text.AlignHCenter
        color:"#FFFFFF"
    }


    Text {

        id:displayMsg
        x:300
        y:300
    }

    MouseArea {
        onClicked:{

        }
    }

    ComboBox {

        id: cardList
        width:200
        x:100
        y:100
        model: ListModel {

         id: cardComboModel


     }
    }
    Button {
        id: startS
        text:"start"

        x:200
        y:200

        onClicked: {
            mw.startDefaultSniff()
        }


    }

    function setText(text){
        helloText.text = text
    }

    function setCard(list){
        list.forEach(function(e){
            cardComboModel.append({text: e})
        })
        }


    function getCardComboCurrentText(){
          return cardList.currentText
    }


    function getData(){
        
    }


}