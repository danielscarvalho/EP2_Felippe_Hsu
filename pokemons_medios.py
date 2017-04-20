import pickle

inspermons_medios= {
	"Machups":{
		"ataque":12,"defesa":8,"vida":30
	},
	"Geogrude":{
		"ataque":10,"defesa":9,"vida":33
	},
	"Goalbate":{
		"ataque":11,"defesa":13,"vida":28
	},
	"Harboqui":{
		"ataque":15,"defesa":11,"vida":29
	},
	"Bidriu":{
		"ataque":12,"defesa":10,"vida":30
	},
	"Sharmilion":{
		"ataque":12,"defesa":10,"vida":31
	},
	"Ivitauro":{
		"ataque":10,"defesa":15,"vida":35
	},
	"Uarturtle":{
		"ataque":15,"defesa":12,"vida":29
	}
}

with open("inspermons_medios.pickle","wb") as arquivo_inspermons_medios:
	pickle.dump(inspermons_medios,arquivo_inspermons_medios)