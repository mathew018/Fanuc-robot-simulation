# FANUC M-10iA robot simulation

## Note
This project demonstrates a robotic arm control system using hand gestures. It leverages the OpenCV and MediaPipe libraries for hand detection and tracking, and integrates with RoboDK for robot manipulation.

## Code Breakdown
## 1. Imports:
- ``` math ```: Provides mathematical functions.
- ``` cv2 ```: Handles computer vision tasks (OpenCV library).
- ``` mediapipe ```: Facilities hand landmark detection and tracking (MediaPipe library).
- ``` from robodk import robolink ```: Enables interaction with Robodk for robot control.

## 2. RoboDK Setup
- ``` RDK = robolink.Robolink() ```: Establishes a connection to RoboDK.
- ``` robot = RDK.Item('Fanuc M-10iA', robolink.ITEM_TYPE_ROBOT) ```: Selects the 'Fanuc M-10iA' robot from RoboDK (replace with your robot name if different).

## 3. Video Capture and hand Detection
- ``` cap = cv2.VideoCapture(1) ```: Initializes video capture from the webcam (index 1).
- ``` hands = mp.solutions.hands.Hands(...) ```: Creates a MediaPipe hand detection object with specified confidence tresholds.
- ``` mp_drawing = mp.solutions.drawing_utils ```: Provides utilities for drawing hand landmarks on the video frame.

## 4. Movement Control Map
- ``` controls = { ... } ```: Defines a dictionary that maps fingertip and base joint indices (based on MediaPipe hand landmark IDs) to robot joint control parameters:
- ``` tip ```: Index of the fingertip landmark for angle calculation.
- ``` base ```: Index of the base landmark for angle calculation.
- ``` min_angle ```: Minimum angle limit for the corresponding robot joint.
- ``` max_angle ```: Maximum angle limit for the corresponding robot joint.
- ```min_dist```: Minimum distance threshold (in pixels) for angle calculation.
- ```max_dist```: Maximum distance threshold (in pixels) for angle calculation.

## 5. Distance and Angle Calculation
- ``` calculate_angle(tip, base, img_shape, control) ```:
    - Takes fingertip, base landmark objects, image shape, and control dictionary as input.
    - Calculates the distance between the fingertip and base landmarks using the Pythagorean theorem.
    - Maps the distance to an angle within the specified joint limits based on the min_dist and max_dist values.
    - Returns the calculated angle, ensuring it stays within the joint's range.

## Additional Considerations
- Replace ```Fanuc M-10iA``` with the actual name of your robot in RoboDK.
- Adjust ````min_detection_confidence```` and ````min_tracking_confidence```` in hands if needed for hand detection sensitivity.
- The ```controls``` dictionary can be customized for different finger combinations and robot joint mappings.
- Consider error handling for potential issues like RoboDK connection failures or missing landmarks.
- Explore advanced grasping techniques for more complex robot manipulation tasks.
- Also in the IDE configure the RoboDK Python path as interpreter.