def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)
    
    
#In the above code, we first gather the parameters for track width and the distance from the center line (we’ll discuss all the #parameters available to you in more detail later). Then, we create three markers based off of the track width - one at 10% of #the track width, another at 25% width, and the last at half of the track width.

#From there, it’s a simple if/else statement that gives different, decreasing rewards based on the vehicle being within a given #marker or not. If it is outside all three markers, notice that the reward is almost effectively zero.

#While we’ll go much more in-depth with reward functions later on, what changes do you think might be helpful to the above #reward function in future iterations?


#action space 0	
#-30degrees
#0.5m/s

#action space 1	
#-30degrees
#1m/s

#action space 2	
#-15degrees
#0.5m/s

#action space 3	
#-15degrees
#1m/s

#action space 4	
#0degrees
#0.5m/s

#action space 5	
#0degrees
#1m/s

#action space 6	
#15degrees
#0.5m/s

#action space 7	
#15degrees
#1m/s

#action space 8	
#30degrees
#0.5m/s

#action space 9	
#30degrees
#1m/s
