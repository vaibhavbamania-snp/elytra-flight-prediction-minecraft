Total_range= float(input('Enter the range: '))
pf_stats= input("""Enter the number for the option below:

1. Velocity low, range high
2. Velocity med, range high
3. Velocity high, range med
4. Velocity highest, range low

Enter here: """)

if pf_stats== '1':
    print('Angle: 3.3')
    Constant_speed= 30.75  
    print('Constant Avg flight speed:',Constant_speed)
    Subtracted_range= Total_range-500 # The distribution step to handle the acceleration
    print('Uniform motion range:',Subtracted_range)
    Constant_time= (Subtracted_range)/Constant_speed # The time after the 1k blocks
    print('Constant Avg flight time:',Constant_time)
    Total_time= 20.5+Constant_time
    #time_error_term= (Total_time/100)*2.15
    #print("The time error is:",time_error_term)
    True_error_free_time= Total_time#+(time_error_term/2)
    print('The total time should be: ###',True_error_free_time)
    Constant_height= Constant_time*3.03 # The height needed after 1k blocks travelled
    print('The height (uniform motion):',Constant_height)
    Variable_height= 65 # The height to be added in constant height later for total height
    print('The 1k crossing height:',Variable_height)
    Total_height= Variable_height+Constant_height # The Constant and Variable height added for total height
    print('Total required height for precise prediction:',Total_height)
    print("Height for flat world testing:",Total_height-60)
    range_error_term= (Total_height/100)*0.8
    Error_free_total_height= Total_height+range_error_term
    print("The true height adjusted is: ###",Error_free_total_height)
    print("The true height needed for flat world: ###",Error_free_total_height-60)


elif pf_stats== '2':
    print('Angle: 12')
    Constant_speed= 60084/1038.57  # Ohhh this one is left to be done yaar!
    print('Constant Avg flight speed:',Constant_speed)
    Subtracted_range= Total_range-1000
    print('Uniform motion range:',Subtracted_range)
    Constant_time= (Subtracted_range)/Constant_speed # The time after the 1k blocks
    print('Constant Avg flight time:',Constant_time)
    Total_time= 21.93+Constant_time
    time_error_term= (Total_time/100)*1.3
    True_error_free_time= Total_time#+time_error_term
    print('The total time should be: ###',True_error_free_time)
    Constant_height= Constant_time*9.30 # The height needed after 1k blocks travelled
    print('The height (uniform motion):',Constant_height)
    Variable_height= 205 # The height to be added in constant height later for total height
    print('The 1k crossing height:',Variable_height)
    Total_height= Variable_height+Constant_height # The Constant and Variable height added for total height
    print('Total required height for precise prediction:',Total_height)
    print("Height for flat world testing:",Total_height-60)
    range_error_term= (Total_height/100)*1.3819
    Error_free_total_height= Total_height+range_error_term
    print("The true height adjusted is: ###",Error_free_total_height)
    print("The true height needed for flat world: ###",Error_free_total_height-60)
    
# The calibration point for this left for now, I'll calibrate this one when its the time to record the video! I would try this in front of the viewers! To show How I reached this point!
   
elif pf_stats== '3':
    print('Angle: 37.3')
    Constant_speed= 60084/1038.57  # 57.855
    #print('Constant Avg flight speed:',Constant_speed)
    Subtracted_range= Total_range-1000
    #print('Uniform motion range:',Subtracted_range)
    Constant_time= (Subtracted_range)/Constant_speed # The time after the 1k blocks
    #print('Constant Avg flight time:',Constant_time)
    Total_time= 21.93+Constant_time
    time_error_term= (Total_time/100)*1.3
    True_error_free_time= Total_time#+time_error_term
    print('The total time should be: ###',True_error_free_time)
    Constant_height= Constant_time*9.30 # The height needed after 1k blocks travelled
    #print('The height (uniform motion):',Constant_height)
    Variable_height= 205 # The height to be added in constant height later for total height
    #print('The 1k crossing height:',Variable_height)
    Total_height= Variable_height+Constant_height # The Constant and Variable height added for total height
    #print('Total required height for precise prediction:',Total_height)
    #print("Height for flat world testing:",Total_height-60)
    range_error_term= (Total_height/100)*1.3819
    Error_free_total_height= Total_height+range_error_term
    print("The true height adjusted is: ###",Error_free_total_height)
    print("The true height needed for flat world: ###",Error_free_total_height-60)
# The calibration range for this was at 60084 Blocks

elif pf_stats== '4':
    print('Angle: 51.3')
    Constant_speed= 8511/125.1 # ~67.5
    print('Constant Avg flight speed:',Constant_speed)
    Subtracted_range= Total_range-1077
    print('Uniform motion range:',Subtracted_range)
    Constant_time= (Subtracted_range)/Constant_speed # The time after the 1k blocks
    print('Constant Avg flight time:',Constant_time)
    Total_time= 21+Constant_time
    #print('The total time should be: ###',Total_time)
    Constant_height= Constant_time*17.81 # The height needed after 1k blocks travelled
    print('The height (uniform motion):',Constant_height)
    Variable_height= 365 # The height to be added in constant height later for total height
    print('The 1k crossing height:',Variable_height)
    Total_height= Variable_height+Constant_height # The Constant and Variable height added for total height
    print('Total required height for precise prediction:',Total_height)
    print("Height for flat world testing:",Total_height-60)
    range_error_term= (Total_height/100)*3.16   
    Error_free_total_height= Total_height+range_error_term
    print("The true height adjusted is: ###",Error_free_total_height)
    print("The true height needed for flat world: ###",Error_free_total_height-60)
    print("The true total time is:", Total_time+(Total_time/100*0.832))    

# The calibration range for this was 5k

else:
    print("Invalid input!")
