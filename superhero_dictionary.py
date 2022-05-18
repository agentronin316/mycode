doreen_green= {"name": "Squirrel Girl", "civilian-identity" : "Doreen Green", "debut": "November, 1991", "creators" : ["Will Murray", "Steve Ditko"], "villains-defeated": ["Doctor Doom", "Abomination", "Maelstrom", "M.O.D.O.K.", "Thanos", "Terrax", "Bi-Beast", "Deadpool", "Fin Fang Foom", "Kraven the Hunter", "Galactus", "Brain Drain", "Enigmo", "Ultron", ]}

print(doreen_green)

ProfessorX={'name':'Professor Charles Xavier','aliases':['Professor X','Onslaught','Consort-Royal','Founder','X','Warlord','Entity'],'base of operations':'Salem Center, New York','creator':['Stan Lee','Jack Kirby'],'bio':'Professor X (Professor Charles Xavier) is the founder of the superhero team The X-Men in the Marvel Universe and an incredibly powerful mutant hero.'}
# name, aliases[7], base of operations, creator[2], bio

print(f"Full Name: {ProfessorX['name']}\nAlias: {ProfessorX['aliases'][4]}\nBase of Operations: {ProfessorX['base of operations']}\nBiography: {ProfessorX['bio']}")


doreen_green["origin"]= "born this way"
print(doreen_green.keys())
choice= input("Select a key: ")
print(doreen_green.get(choice, "invalid key"))