import pytest
from lib.centaur import *

def test_it_has_name():
    centaur = Centaur("George", "Palomino")
    assert centaur.name == "George"

def test_it_has_a_horse_breed():
    centaur = Centaur("George", "Palomino")
    assert centaur.breed == "Palomino"

def test_it_has_excellent_bow_skills():
    centaur = Centaur("George", "Palomino")
    assert centaur.shoot() == "Twang!!!"

def test_it_makes_a_horse_sound_when_it_runs():
    centaur = Centaur("George", "Palomino")
    assert centaur.run() == "Clop clop clop clop!!!"

def test_when_first_created_it_is_not_cranky():
    centaur = Centaur("George", "Palomino")
    assert centaur.is_cranky() == False

def test_when_first_created_it_is_standing_up():
    centaur = Centaur("George", "Palomino")
    assert centaur.is_standing() == True

def test_after_running_or_shooting_a_bow_three_times_it_gets_cranky():
    centaur = Centaur("George", "Palomino")
    assert centaur.is_cranky() == False
    centaur.shoot()
    centaur.run()
    assert centaur.is_cranky() == False
    centaur.shoot()
    assert centaur.is_cranky() == True

def test_when_cranky_it_will_not_shoot_a_bow():
    centaur = Centaur("George", "Palomino")
    centaur.shoot()
    centaur.shoot()
    centaur.shoot()
    assert centaur.shoot() == "NO!"

def test_when_cranky_it_will_not_run():
    centaur = Centaur("George", "Palomino")
    centaur.shoot()
    centaur.shoot()
    centaur.shoot()
    assert centaur.run() == "NO!"

#
#   def test_when_standing_it_will_not_sleep
#     skip
#     centaur = Centaur.new("George","Palomino")
#     assert_equal "NO!", centaur.sleep
#   end
#
#   def test_after_laying_down_it_is_not_standing
#     skip
#     centaur = Centaur.new("George","Palomino")
#     centaur.lay_down
#     refute centaur.standing?
#     assert centaur.laying?
#   end
#
#   def test_it_can_sleep_when_laying_down
#     skip
#     centaur = Centaur.new("George","Palomino")
#     centaur.lay_down
#     refute_equal "NO!", centaur.sleep
#   end
#
#   def test_when_laying_down_it_cannot_shoot_a_bow
#     skip
#     centaur = Centaur.new("George","Palomino")
#     centaur.lay_down
#     assert_equal "NO!", centaur.shoot
#   end
#
#   def test_when_laying_down_it_cannot_run
#     skip
#     centaur = Centaur.new("George","Palomino")
#     centaur.lay_down
#     assert_equal "NO!", centaur.run
#   end
#
#   def test_it_can_stand_up
#     skip
#     centaur = Centaur.new("George","Palomino")
#     centaur.lay_down
#     centaur.stand_up
#     assert centaur.standing?
#   end
#
#   def test_after_sleeping_it_is_no_longer_cranky
#     skip
#     centaur = Centaur.new("George","Palomino")
#
#     centaur.shoot
#     centaur.run
#     centaur.shoot
#
#     assert centaur.cranky?
#
#     centaur.lay_down
#     centaur.sleep
#
#     refute centaur.cranky?
#
#     centaur.stand_up
#
#     assert_equal "Twang!!!", centaur.shoot
#     assert_equal "Clop clop clop clop!!!", centaur.run
#   end
#
#   def test_becomes_rested_after_drinking_a_potion
#     skip
#     # your code here
#   end
#
#   def test_can_only_drink_potion_while_standing
#     skip
#     # your code here
#   end
#
#   def test_gets_sick_if_drinks_potion_while_rested
#     skip
#     # your code here
#   end
