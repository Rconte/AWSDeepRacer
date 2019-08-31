def reward_function(params):

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    track_width = params['track_width']
    steering = abs(params['steering_angle'])

    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0
    else:
        reward = 1e-3
    
    speed_threshold = 1.5
    if speed > speed_threshold:
        reward *= 1.5

    return float(reward)
