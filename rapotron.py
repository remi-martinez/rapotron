import random
import sys

def select(l, f):
	n = []
	for o in l:
		if f(o):
			n.append(o)
	return n

class Grammar:
	def __init__(self, rappers = []):
		self.rules = []
		self.rappers = rappers
	def __str__(self):
		s = ""
		for rule in self.rules:
			s += rule.__str__() + "\n"
		return s

	def generate(self):
		todo = [ self.rules[0].left ]
		generated = [ ]
		while len(todo) >0:
			sym = todo.pop()
			if sym.isTerminal():
				generated.append(sym)
			else:
				rule = random.choice(select(self.rules, lambda r: r.left == sym))
				for s in reversed(rule.right):
					todo.append(s)
		return generated


class Rule:
	def __init__(self, l = None, r = []):
		self.left = l
		self.right = r
	def __str__(self):
		s = self.left.__str__() + " -> " 
		for r in self.right:
			s += r.__str__() + " "
		return s


class Symbol:
	def __init__(self, symbol):
		self.symbol = symbol
	def __str__(self):
		return self.symbol
	def isTerminal(self):
		return True


class NonTerminal(Symbol):
	def isTerminal(self):
		return False

class Terminal(Symbol):
	def isTerminal(self):
		return True

#############################################

def generatePunchline(rapper1, rapper2):

	g = Grammar([rapper1, rapper2])

	TEXTE = NonTerminal("TEXTE")
	PHRASE = NonTerminal("PHRASE")

	# Les rIgles sont constituée de rimes. Rime 1A : 1Ire rime (gauche) en A
	RIME_1A = NonTerminal("RIME_1A")
	RIME_1I = NonTerminal("RIME_1I")
	RIME_1O = NonTerminal("RIME_1O")
	RIME_1AN = NonTerminal("RIME_1AN")
	RIME_1OU = NonTerminal("RIME_1OU")
	RIME_1AI = NonTerminal("RIME_1AI")

	RIME_2A = NonTerminal("RIME_2A")
	RIME_2I = NonTerminal("RIME_2I")
	RIME_2O = NonTerminal("RIME_2O")
	RIME_2AN = NonTerminal("RIME_2AN")
	RIME_2OU = NonTerminal("RIME_2EU")
	RIME_2AI = NonTerminal("RIME_2AI")

	# Symboles
	epsilon = Terminal("")
	virgule = Terminal(",")
	point = Terminal(".")

	# Ajout des rIgles
	g.rules.append( Rule(PHRASE, [RIME_1A, virgule, RIME_2A, point]))
	g.rules.append( Rule(PHRASE, [RIME_1I, virgule, RIME_2I, point]))
	g.rules.append( Rule(PHRASE, [RIME_1O, virgule, RIME_2O, point]))
	g.rules.append( Rule(PHRASE, [RIME_1AN, virgule, RIME_2AN, point]))
	g.rules.append( Rule(PHRASE, [RIME_1OU, virgule, RIME_2OU, point]))
	g.rules.append( Rule(PHRASE, [RIME_1AI, virgule, RIME_2AI, point]))

	print(g.rappers[0] + " & " + g.rappers[1])


	Rime1A_nekfeu = [ "Bientôt j'arrête tout ça mama", "Ouais, je veux lever le V d'la vendetta" ]
	Rime2A_damso = [ "mon cœur danse la macarena", "feu de bois, jeu de voix" ]

	RimesArray = []


	# Rimes des rappeurs

	r0 = g.rappers[0]
	r1 = g.rappers[1]

	r1a, r1i, r1o, r1an, r1ou, r1ai = [""], [""], [""], [""], [""], [""]
	r2a, r2i, r2o, r2an, r2ou, r2ai = [""], [""], [""], [""], [""], [""]

	######### R0 #########
	if r0 == 'Nekfeu':
		r1a = [ "Bientôt j'arrête tout ça mama", "Ouais, je veux lever le V d'la vendetta", "On verra bien ce que l'avenir nous réservera" ]
		r1i = [ "À seize ans, j'ai dû voir un psy", "Mon ego démoli, dans mon lit"]
		r1o = [ "Le monde est beau", "On est tous dans le même bateau" ]
		r1an = [ "On dit aussi que l'univers s'étend", "Les petits qui sortent du ruisseau veulent des rivières de diamants" ]
		r1ou = [ "Soit tu subis, soit tu mets les coups", "Quand ça va pas, je bouffe comme un fou", "Ce monde rend fou" ]
		r1ai = [ "Quand je te regardais dormir et que j'écrivais", "Nous qui avons tout, on est pour la paix" ]
	elif r0 == 'Damso':
		r1a = [ "Ces fils de putes ne m'aiment pas" ]
		r1i = [ "Me d'mandez pas c'que j'fais dans la vie", "Baise-la c'est tout sinon elle f'ra des manies"]
		r1o = [ "Sentiments grandissants figeant l'ego" ]
		r1an = [ "J'serais rappeur plus tard maman" ]
		r1ou = [ "J'm'en bats tellement les illes-cou" ]
		r1ai = [ "J'ai mis mes chances dans le barillet" ]
	elif r0 == 'Orelsan':
		r1a = ["J'te baise sur un tas de bois"]
		r1i = [ "J'débarque comme un tsunami", "Jimmy vient t'ôter la vie" ]
		r1o = [ "Tu distribues tes CV dans les MacDo", "Continue de rapper des mythos" ]
		r1an = [ "Si j'dois mettre des gants", "J'pars au taf avec une gueule d'enterrement"]
		r1ou = ["J'ai le flow de passe-partout"]
		r1ai = ["Ton équipe fait pitié"]


	######### R1 #########
	if r1 == 'Damso':
		r2a = [ "mon cœur danse la macarena", "feu de bois, jeu de voix", "un bras d'honneur aux lois" ]
		r2i = ["l'Enfer est comme le Paradis", "c'est ça qu'ça fait d'toujours bosser la nuit", "m'a dit coach Elly"]
		r2o = [ "ils ne me veulent pas du bien, no" ]
		r2an = ["mais qu'est-ce que c'est bon quand j'pelote tes implants", "car de bien aller j'ai fait semblant"]
		r2ou = ["j'm'en bats tellement les illes-cou"]
		r2ai = ["que la nightzer, ouais", "les fils de putains je m'en bats les"]
	elif r1 == 'Nekfeu':
		r2a = ["mais y en a qu'une c'est toi", "j'suis redescendu par les toits"]
		r2i = ["mais faut croire qu'ça m'a pas suffit", "j'me sens à la dérive, ces temps-ci"]
		r2o = [ "mais on accorde peu d'crédit aux vrais quand ils sortent de la bouche des faux", "on est tous dans le même bateau" ]
		r2an = [ "alors j'me fais du mal mais discrètement", "tout le monde est en guerre han, han", "jamais j'insulterai tes parents" ]
		r2ou = [ "les provocateurs de toute violence, c'est vous", "ils se prennent tous pour des voyous"]
		r2ai = [ "quand t'es du $-Crew tu dis jamais \"jamais\"", "j'veux les faire souffrir comme les meufs que j'aimais" ]
	elif r1 == 'Orelsan':
		r2a = [ "j'soulève des meufs qui font deux fois mon poids" ]
		r2i = [ "j'te fais passer sous le baby", "j'ai l'impression de baiser sous la pluie" ]
		r2o = [ "dans tes règles ca fait ketchup/mayo", "pendant tu distribues tes CV dans les MacDo"]
		r2an = [ "j't'arrache la jugulaire avec les dents", "c'est gratuit j'suis bete et méchant"]
		r2ou = [ "depuis on attend que le monde vienne à nous", "ils sont cools ouhouhouh"]
		r2ai = ["y a marqué \"on t'la met profond\" entre les lignes des ma fiche de paie"]



	for s in r1a:
		g.rules.append( Rule(RIME_1A, [ Terminal(s) ]))
	for s in r1i:
		g.rules.append( Rule(RIME_1I, [ Terminal(s) ]))
	for s in r1o:
		g.rules.append( Rule(RIME_1O, [Terminal(s) ]))
	for s in r1an:
		g.rules.append( Rule(RIME_1AN, [ Terminal(s) ]))
	for s in r1ou:
		g.rules.append( Rule(RIME_1OU, [ Terminal(s) ]))
	for s in r1ai:
		g.rules.append( Rule(RIME_1AI, [ Terminal(s) ]))
	for s in r2a:
		g.rules.append( Rule(RIME_2A, [ Terminal(s) ]))
	for s in r2i:
		g.rules.append( Rule(RIME_2I, [ Terminal(s) ]))
	for s in r2o:
		g.rules.append( Rule(RIME_2O, [ Terminal(s) ]))
	for s in r2an:
		g.rules.append( Rule(RIME_2AN, [ Terminal(s) ]))
	for s in r2ou:
		g.rules.append( Rule(RIME_2OU, [ Terminal(s) ]))
	for s in r2ai:
		g.rules.append( Rule(RIME_2AI, [ Terminal(s) ]))	

	for i in range(20):
		g.rules.append( Rule(TEXTE, [ PHRASE, TEXTE ]) )
	g.rules.append( Rule(TEXTE, [ epsilon ]) )


	s = ""
	for sym in g.generate():
		s += str(sym)+" "
	print(s)

#############################################

# Plus qu'à modifier ici ! Vous pouvez assembler qui vous voulez.
# Pour l'instant il n'y a pas Orelsan, Nekfeu et Damso.
generatePunchline(sys.argv[1], sys.argv[2])

#############################################

# Quelle galère tkinter ! Je n'ai pas eu le temps de regarder ça plus en détail.
'''
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title = "Rapotron"
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.raptxt = tk.Button(self)
        self.raptxt["text"] = "Rapotron : Générez des punchlines débiles"
        self.generatebtn = tk.Button(self)
        self.generatebtn["text"] = "Générer"
        self.generatebtn["command"] = self.generate
        self.generatebtn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def generate(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title('Rapotron')
root.geometry('700x400')
# app = Application(master=root)
# app.mainloop()
'''
