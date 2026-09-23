# Utilisez un dictionnaire comme table de conversion, par ex. des unités de temps.
# L'utilisateur fournit une durée (en jours de travail )
# L'application affiche la conversion de cette durée en heures et minutes.
#
# On convient qu'une journée de travail compte 8 heures,
# et qu'une heure de travail compte 60 minutes.
#
# params :
# duration : durée en journée de travail (de 8 h)
# unit : l'unité dans laquelle on convertit la duration

def convert_time(duration, unit):
	convert_d = {
		"minute"	: 8*60,
		"hour"		:    8,
		"day"		:    1,
		"dhour"		:    4,
		"15min"		:  8*4,
	}
	thesaurus_d = {
		"hour"		: "heures",
		"minute"	: "minutes",
		"dhour"		: "heures doubles",
		"15min"		: "quarts d'heure"
	}
	converted_duration = duration * convert_d[unit]
	out_s = f"durée fournie : {duration} jours => conversion : {converted_duration} {thesaurus_d[unit]}"
	print( out_s )


# MAIN
if __name__ == "__main__":
	convert_time( 0.25, "15min" )
	convert_time( 0.8, "15min" )
	convert_time( 0.75, "dhour" )  # heure double
	convert_time( 2, "minute" )
	convert_time( 20, "dhour" )

