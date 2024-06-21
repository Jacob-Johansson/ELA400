import numpy as np;

# Membership functions for all they fuzzy sets

# Triangle membership function
# a, b, c: the three points of the triangle
# x: input value
def TriangleMembershipFunction(a, b, c, x):
    if x <= a or x >= c:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)

# Trapezoid membership function
# a, b, c, d: the four points of the trapezoid
# x: input value
def TrapezoidMembershipFunction(a, b, c, d, x):
    return max(min((x-a)/(b-a), 1, (d-x)/(d-c)), 0)

# Square membership function
# x0: center of the square
# width: width of the square
# x: input value
def SquareMembershipFunction(x0, width, x):
    if x0 + width/2 <= x <= x0 + width:
        return 1
    else:
        return 0

# Moisture Dry membership function
def MoistureDry(x):
    if x > 320:
        return 1
    else:
        return TriangleMembershipFunction(300, 321, 321, x)
    
# Moisture Medium membership function
def MoistureMedium(x):
    return TriangleMembershipFunction(290, 300, 310, x)
# Moisture Wet membership function
def MoistureWet(x):
    if x < 270:
        return 1
    else:
        return TriangleMembershipFunction(269, 269, 300, x)

# Temperature Cold membership function    
def TemperatureCold(x):
    if x < 10:
        return 1
    else:
        return TriangleMembershipFunction(0, 9, 12, x)
    
# Temperature Medium membership function
def TemperatureMedium(x):
    return TriangleMembershipFunction(10, 20, 30, x)

# Temperature Hot membership function
def TemperatureHot(x):
    if x > 30:
        return 1
    else:
        return TriangleMembershipFunction(28, 30, 31, x)

# Humidity Low membership function
def HumidityLow(x):
    if x < 30:
        return 1
    else:
        return TriangleMembershipFunction(29, 29, 35, x)

# Humidity Medium membership function
def HumidityMedium(x):
    return TriangleMembershipFunction(30, 50, 70, x)

# Humidity High membership function
def HumidityHigh(x):
    if x > 70:
        return 1
    else:
        return TriangleMembershipFunction(60, 71, 71, x)
    
# Moisture Low membership function
def MoistureLow(x):
    if x > 320:
        return 1
    else:
        return TriangleMembershipFunction(300, 321, 321, x)
    
# Moisture Medium membership function
def MoistureMedium(x):
    return TriangleMembershipFunction(285, 295, 305, x)

# Moisture High membership function
def MoistureHigh(x):
    if x < 270:
        return 1
    else:
        return TriangleMembershipFunction(269, 269, 285, x)

# Light Low membership function
def LightLow(x):
    if x < 3:
        return 1
    else:
        return TriangleMembershipFunction(2.9, 2.9, 3.6, x)

# Light Medium membership function
def LightMedium(x):
    return TrapezoidMembershipFunction(3.2, 3.5, 4, 4.5, x)

# Light High membership function
def LightHigh(x):
    if x > 5:
        return 1
    else:
        return TriangleMembershipFunction(4.2, 5.1, 5.1, x)
    
# Watering None membership function
def WateringNone(x):
    if x < 10:
        return 1
    else:
        return TrapezoidMembershipFunction(0, 5, 10, 15, x)
# Watering None Area membership function
def WateringNoneArea():
    return ((10 - 0) * 1 + (15 - 10) * 0.5)
def WateringNoneCenter(): return 7.5
    
# Watering Low membership function
def WateringLow(x):
    return TrapezoidMembershipFunction(10, 20, 30, 40, x)
# Watering Low Area membership function
def WateringLowArea():
    return ((20 - 10) * 0.5 + (30 - 20) * 1 + (40 - 30) * 0.5)
def WateringLowCenter(): return 25

# Watering Medium membership function
def WateringMedium(x):
    return TrapezoidMembershipFunction(30, 40, 50, 60, x)
# Watering Medium Area membership function
def WateringMediumArea():
    return (40 - 30) * 0.5 + (50 - 40) * 1 + (60 - 50) * 0.5
def WateringMediumCenter(): return 45

# Watering High membership function
def WateringHigh(x):
    if x > 60:
        return 1
    else:
        return TrapezoidMembershipFunction(50, 60, 70, 80, x)
# Watering High Area membership function
def WateringHighArea():
    return (60 - 50) * 0.5 + (80 - 60) * 1
def WateringHighCenter(): return 65