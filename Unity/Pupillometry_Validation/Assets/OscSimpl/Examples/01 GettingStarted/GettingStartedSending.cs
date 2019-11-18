/*
	Created by Carl Emil Carlsen.
	Copyright 2016-2018 Sixth Sensor.
	All rights reserved.
	http://sixthsensor.dk
*/

using UnityEngine;

namespace OscSimpl.Examples
{
	public class GettingStartedSending : MonoBehaviour
	{
		[SerializeField] OscOut _oscOut;

        public ViveSR.anipal.Eye.Pupil_Tracker getWidth;
        OscMessage _message; // Cached message.

		const string address = "/Pupil_width";


		void Start()
		{
            getWidth = GameObject.Find("Pupil Width Tracking").GetComponent<ViveSR.anipal.Eye.Pupil_Tracker>();

            // Ensure that we have a OscOut component.
            if ( !_oscOut ) _oscOut = gameObject.AddComponent<OscOut>();

			// Prepare for sending messages locally on this device on port 7000.
			_oscOut.Open( 12300 );

			// ... or, alternatively target remote devices with a IP Address.
			//oscOut.Open( 7000, "192.168.1.101" );

			// If you want to send a message with multiple values, then you
			// need to create a message, add your values and send it.
			// Always cache the messages you create, so that you can reuse them.
			_message = new OscMessage(address);
		}


		void Update()
		{
			// We update the content of message2 and send it again.
			_message.Set( 0, getWidth.left_width);
			_message.Set( 1, getWidth.right_width);
			_oscOut.Send( _message );
		}
	}
}