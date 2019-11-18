
using UnityEngine;
using UnityEngine.UI;

public class Display_eye_width : MonoBehaviour
{
    public Text width;
    public ViveSR.anipal.Eye.Pupil_Tracker getWidth;
    public bool left;
    void Start()
    {
        width = GetComponent<Text>();
        getWidth = GameObject.Find("Pupil Width Tracking").GetComponent<ViveSR.anipal.Eye.Pupil_Tracker>();

    }

    // Update is called once per frame
    void Update()
    {
        if (left)
            width.text = getWidth.left_width.ToString();
        else
            width.text = getWidth.right_width.ToString();

    }
}
