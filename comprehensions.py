def good_enough(password):
	return True in [ result for result in\
				[ password.upper() != password and password.lower() != password\
				and char in "0123456789"\
				for char in password ] if result ]

def strength(password):
	return len([char for char in password if password.upper() != password and\
			password.lower() != password])\
			*\
			len([char for char in password if char in "0123456789.?!&#.;:-_*"])

print "password abcdefg"
print "good_enough: " + str(good_enough("abcdefg"))
print "password abcdEfG0#"
print "good_enough: " + str(good_enough("abcdEfG0#"))
print "strength: " + str(strength("abcdEfG0#"))
