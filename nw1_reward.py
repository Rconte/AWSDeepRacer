def reward_function(params):

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])
    progress = params['progress']
    
    reward = 1e-3
    
    speed_threshold = 4
    
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
        if speed > speed_threshold:
            reward += progress
    
    ABS_STEERING_THRESHOLD = 15
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7
    
    

    return float(reward)
