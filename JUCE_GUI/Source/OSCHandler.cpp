/*
  ==============================================================================

    OSCHandler.cpp
    Created: 13 Feb 2020 3:02:12pm
    Author:  craig

  ==============================================================================
*/

#include "OSCHandler.h"


OSCHandler::OSCHandler()
{

}

OSCHandler::~OSCHandler()
{
    unityOSCOut.disconnect();
    BiTAOSCOut.disconnect();
}

void OSCHandler::connect(const String& addressUnity, const int& portUnity, const String& addressBiTA, const int& portBiTA)
{
    if (!unityOSCOut.connect(addressUnity, portUnity))
        showConnectionErrorMessage("Error: could not connect to UDP port" + String(portUnity));
    if (!BiTAOSCOut.connect(addressBiTA, portBiTA))
        showConnectionErrorMessage("Error: could not connect to UDP port" + String(portBiTA));
}

void OSCHandler::playSource(const int& sourceNumber, const float& positionX, const float& positionY, const float& level)
{
    String sourceAddress = "/3DTI-OSC/source" + String(sourceNumber);
    float test = randomNumberGenerator.nextFloat();
    BiTAOSCOut.send(sourceAddress + "/seek", randomNumberGenerator.nextFloat());
    BiTAOSCOut.send(sourceAddress + "/pos", positionX, positionY, 0.0f);
    BiTAOSCOut.send(sourceAddress + "/gain", level);
    BiTAOSCOut.send(sourceAddress + "/play");
}

void OSCHandler::showConnectionErrorMessage(const String& messageText)
{
    AlertWindow::showMessageBoxAsync(AlertWindow::WarningIcon,
        "Connection error",
        messageText,
        "OK");
}
