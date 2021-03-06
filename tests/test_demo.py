import pytest
import unittest

def test_Vacuum_dV():
    """Tests the function to find vacuum dV"""

    from rocketsim.rocket import Vacuum_dV

    assert 0 == Vacuum_dV(300,100,100)
    print("pass 1")
    # assert .1 <= abs(Vacuum_dV(300,100,50) - 1885.33)
    print("pass2")
    #assert 0 < Vacuum_dV(300,100,150)
    #print("pass3")

def test_Mass_of_spaceship():
    """Tests the function Mass_of_spaceship"""

    from rocketsim.rocket import Mass_of_spaceship


    assert 0==Mass_of_spaceship(0,0,0,0)
    assert 98.5==Mass_of_spaceship(100,5,50,3)
    assert 100==Mass_of_spaceship(100,5,50,0)

def test_Force_Gravity():

    """Tests the function rocket.Force_Gravity that determines the force of gravity
    on the rocket at timestep i"""

    from rocketsim.rocket import Force_Gravity

    assert 0==Force_Gravity(0,0)
    # assert

def test_Acceleration():

    """Tests the function rocket.Acceleration() """

    from rocketsim.rocket import Acceleration

    assert 0==Acceleration(0,0,1,0)
    assert 25==Acceleration(1000,500,10,250)
    #assert float('Inf') == Vacuum_dV(300,0,1)
    #assert float('NaN') == Vacuum_dV(300,1,0)

def test_Atmosphere_Density():

    """Tests the function rocket.Atmosphere_Density for each thermocline"""

    from rocketsim.rocket import Atmosphere_Density
    from numpy import isclose

    assert 1.225 == Atmosphere_Density(0)
    assert True == isclose(Atmosphere_Density(10000),0.412707,1.0e-5)
    assert True == isclose(Atmosphere_Density(15000),0.193669,1.0e-5)
    assert True == isclose(Atmosphere_Density(25000),0.0394636,1.0e-6)
    assert True == isclose(Atmosphere_Density(35000),0.00821081,1.0e-7)
    assert True == isclose(Atmosphere_Density(50000),0.000979214,1.0e-8)
    assert True == isclose(Atmosphere_Density(60000),0.000287784,1.0e-8)
    assert True == isclose(Atmosphere_Density(80000),0.0000156489,1.0e-9)

def test_Drag():

    """Tests the function rocket.Drag"""

    from rocketsim.rocket import Drag

    assert 4593.75 == Drag(1.225,100,1)

def test_Velocity():

    """Tests the rocket.Velocity function """

    from rocketsim.rocket import Velocity

    assert 101 == Velocity(100,10,.1)
    assert 99.02 == Velocity(100,-9.8,.1)
    assert -100.98 == Velocity(-100,-9.8,.1)

def test_Altitude():

    """Tests the rocket.Altitude function """

    from rocketsim.rocket import Altitude

    assert 1010 == Altitude(1000,100,.1)
    assert 990 == Altitude(1000,-100,.1)

def test_Position_downrange():

    """Tests the rocket.Position_downrange function """

    from rocketsim.rocket import Position_downrange
    from numpy import isclose

    assert True == isclose(Position_downrange(1000,100,45),1007.071, 1.0e-2)

def test_Freefall_acceleration():

    """Tests the rocket.free_fall_acceleration function"""

    from rocketsim.rocket import free_fall_acceleration
    from numpy import isclose

    assert -2.5 == free_fall_acceleration(1000,200,500)

def test_Apogee():

    """Tests the rocket.Apogee function """

    from rocketsim.rocket import Apogee
    from numpy import isclose

    assert True == isclose(Apogee(100),509.858,.01)
    assert 0 == Apogee(-50)

# def test_initialize_variables():
#
#     """Tests to make sure variables are properly initialized"""
#
#     from rocketsim.rocket import initialize_variables
#
#     assert 1, 1, 1, 1, 1, 1 == initialize_variables()
