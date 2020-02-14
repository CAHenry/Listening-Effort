/*
  ==============================================================================

    OSCHandler.h
    Created: 13 Feb 2020 3:02:12pm
    Author:  craig

  ==============================================================================
*/

#pragma once
#include <JuceHeader.h>

class OSCHandler : public Component
{
public:
    OSCHandler();
    ~OSCHandler();

    void connect(const String& addressUnity, const int& portUnity, const String& addressBiTA, const int& portBiTA);
    void playSource(const int& sourceNumber, const float& positionX, const float& positionY, const float& level);

private:
    OSCSender unityOSCOut;
    OSCSender BiTAOSCOut;
    Random randomNumberGenerator;
    void showConnectionErrorMessage(const String&);

};