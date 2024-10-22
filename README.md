# FANUC M-10iA robot simulation

## Note
This project demonstrates a robotic arm control system using hand gestures. It leverages the OpenCV and MediaPipe libraries for hand detection and tracking, and integrates with RoboDK for robot manipulation.

### I invite you to look at the result
https://youtu.be/0ObS_tZWpkY

## 1. RoboDK Setup
- ``` RDK = robolink.Robolink() ```: Establishes a connection to RoboDK.
- ``` robot = RDK.Item('Fanuc M-10iA', robolink.ITEM_TYPE_ROBOT) ```: Selects the 'Fanuc M-10iA' robot from RoboDK (replace with your robot name if different).

## 2. Movement Control Map
- ``` controls = { ... } ```: Defines a dictionary that maps fingertip and base joint indices (based on MediaPipe hand landmark IDs) to robot joint control parameters:
- ``` tip ```: Index of the fingertip landmark for angle calculation.
- ``` base ```: Index of the base landmark for angle calculation.
- ``` min_angle ```: Minimum angle limit for the corresponding robot joint.
- ``` max_angle ```: Maximum angle limit for the corresponding robot joint.
- ```min_dist```: Minimum distance threshold (in pixels) for angle calculation.
- ```max_dist```: Maximum distance threshold (in pixels) for angle calculation.

## 3. Distance and Angle Calculation
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
