from Beliczky_Zsolt_ibiza import euclid,euclid_extended,check_euclid_extended,is_congruent,fast_modular_exponentiation

def test_euclid():
    assert euclid(5,3) == 1
    assert euclid(48,18) == 6
    assert euclid(100,100) == 100
    assert euclid(10,20) == 10
    assert euclid(0,0) == None
    assert euclid(5,0) == 5
    assert euclid(0,5) == 5
    assert euclid(-500,300) == 100
    assert euclid(-500,-1) == 1
    assert euclid(111,-27) == 3
    
def test_euclid_extended():
    assert euclid_extended(5,3) == (1,-1,2)
    assert euclid_extended(48,18) == (6,-1,3)
    assert euclid_extended(100,100) == (100,0,1)
    assert euclid_extended(10,20) == (10,0,1)
    assert euclid_extended(0,0) == None
    assert euclid_extended(5,0) == (5,1,0)
    assert euclid_extended(0,5) == (5,1,0)
    assert euclid_extended(-500,300) == (100,-1,2)
    assert euclid_extended(-500,-1) == (1,0,1)
    assert euclid_extended(111,-27) == (3,1,-4)
    
def test_check_euclid_extended():
    assert check_euclid_extended(5,3) == True
    assert check_euclid_extended(48,18) == True
    assert check_euclid_extended(100,100) == True
    assert check_euclid_extended(10,20) == True
    assert check_euclid_extended(0,0) == True
    assert check_euclid_extended(5,0) == True
    assert check_euclid_extended(0,5) == True
    assert check_euclid_extended(-500,300) == True
    assert check_euclid_extended(-500,-1) == True
    assert check_euclid_extended(111,-27) == True
    
def test_is_congruent():
    assert is_congruent(18,3,5) == True
    assert is_congruent(13,8,5) == True
    assert is_congruent(18,8,5) == True
    assert is_congruent(25,-10,7) == True
    assert is_congruent(25,10,7) == False

def test_fast_modular_exponentiation():
    assert fast_modular_exponentiation(6,73,100) == 16
    assert fast_modular_exponentiation(129,97,171) == 108
    assert fast_modular_exponentiation(23,209,211) == 156
    assert fast_modular_exponentiation(9,22,79) == 73
    assert fast_modular_exponentiation(82,5,7) == 3
    assert fast_modular_exponentiation(5,126,127) == 1
    assert fast_modular_exponentiation(7,180,181) == 1
    assert fast_modular_exponentiation(14,340,410) == 286