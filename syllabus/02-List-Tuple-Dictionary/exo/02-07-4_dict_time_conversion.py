# Utilisez un dictionnaire comme table de conversion, par ex. des unités de temps.
# L'utilisateur fournit une durée (en jours de travail )
# L'application affiche la conversion de cette durée en heures et minutes.
#
# On convient qu'une journée de travail compte 8 heures,
# et qu'une heure de travail compte 60 minutes.

def convert_time(duration):
	convert_d = {
		"minute": 8*60,
		"hour":   8,
		"day":    1
	}
	duration_hour = duration * convert_d["hour"]
	duration_minute = duration * convert_d["minute"]

	out_s = "durée fournie : {0} jours => conversion : {1} heures ou {2} minutes "
	print( out_s.format( duration, duration_hour, duration_minute) )


# MAIN
convert_time( 0.25 )
convert_time( 0.75 )
convert_time( 2 )
convert_time( 20 )
