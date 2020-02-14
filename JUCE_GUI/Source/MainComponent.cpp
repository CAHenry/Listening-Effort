/*
  ==============================================================================

    This file was auto-generated!

  ==============================================================================
*/

#include "MainComponent.h"

//==============================================================================
MainComponent::MainComponent()
{
    setSize (600, 400);

    addAndMakeVisible(&OSCConnect);
    OSCConnect.setButtonText("Connect...");
    OSCConnect.onClick = [this] { mediaplayer.connect("127.0.0.1", 7000, "127.0.0.1", 12300); };
    addAndMakeVisible(&playSource);
    playSource.setButtonText("playSource...");
    playSource.onClick = [this] { mediaplayer.playSource(1, 0.0, 1.0, 1.0); };

}

MainComponent::~MainComponent()
{
}

//==============================================================================
void MainComponent::paint (Graphics& g)
{
    // (Our component is opaque, so we must completely fill the background with a solid colour)
    g.fillAll (getLookAndFeel().findColour (ResizableWindow::backgroundColourId));

    g.setFont (Font (16.0f));
    g.setColour (Colours::white);
    g.drawText ("Hello World!", getLocalBounds(), Justification::centred, true);
}

void MainComponent::resized()
{
    OSCConnect.setBounds(10, 10, getWidth() - 20, 20);
    playSource.setBounds(10, 40, getWidth() - 20, 20);
    // This is called when the MainComponent is resized.
    // If you add any child components, this is where you should
    // update their positions.
}
