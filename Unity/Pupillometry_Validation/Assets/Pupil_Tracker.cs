
using System.Runtime.InteropServices;
using UnityEngine;

namespace ViveSR.anipal.Eye
{
    public class Pupil_Tracker : MonoBehaviour
    {
        public float left_width = 3;
        public float right_width = 3;

        private static EyeData eye_data = new EyeData();
        public bool eye_callback_registered = false;
        public int test = 0;
        // Start is called before the first frame update
        private void Start()
        {
            if (!SRanipal_Eye_Framework.Instance.EnableEye)
            {
                enabled = false;
                return;
            }
        }

        private void Update()
        {
            //if (SRanipal_Eye_Framework.Status != SRanipal_Eye_Framework.FrameworkStatus.WORKING &&
            //    SRanipal_Eye_Framework.Status != SRanipal_Eye_Framework.FrameworkStatus.NOT_SUPPORT) return;

            //if (SRanipal_Eye_Framework.Instance.EnableEyeDataCallback == true && eye_callback_registered == false)
            //{
            //    SRanipal_Eye.WrapperRegisterEyeDataCallback(Marshal.GetFunctionPointerForDelegate((SRanipal_Eye.CallbackBasic)EyeCallback));
            //    eye_callback_registered = true;
            //    test = 1;
            //}
            //else if (SRanipal_Eye_Framework.Instance.EnableEyeDataCallback == false && eye_callback_registered == true)
            //{
            //    SRanipal_Eye.WrapperUnRegisterEyeDataCallback(Marshal.GetFunctionPointerForDelegate((SRanipal_Eye.CallbackBasic)EyeCallback));
            //    eye_callback_registered = false;
            //    test = 2;
            //}
            //else
            //{
            //    SRanipal_Eye.WrapperUnRegisterEyeDataCallback(Marshal.GetFunctionPointerForDelegate((SRanipal_Eye.CallbackBasic)EyeCallback));
            //    test = 3;
            //}
            SRanipal_Eye_API.GetEyeData(ref eye_data);
            left_width = eye_data.verbose_data.left.pupil_diameter_mm;
            right_width = eye_data.verbose_data.right.pupil_diameter_mm;
        }
        private void Release()
        {
            if (eye_callback_registered == true)
            {
                SRanipal_Eye.WrapperUnRegisterEyeDataCallback(Marshal.GetFunctionPointerForDelegate((SRanipal_Eye.CallbackBasic)EyeCallback));
                eye_callback_registered = false;
            }
        }

        private static void EyeCallback(ref EyeData eyedata)
        {
            eye_data = eyedata;
        }
    }
}


