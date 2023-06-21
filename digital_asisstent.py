import wolframalpha
import wikipedia

#library za sintezu govora
import pyttsx3

client = wolframalpha.Client("ATVE7L-94QT4PX37R")

# user input
upit = "neki upit"

# odabrani_jezik = self.odabir_jezika_asistenta.get()
#print("sad cu govoriti na: ", odabrani_jezik, "jeziku.")
def get_the_answer(upit):
    try:
        #wikipedia.set_lang(odabrani_jezik)
        wiki_rezultat = wikipedia.summary(upit, sentences=2)
        return wiki_rezultat
        #print(wiki_rezultat)

    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(upit).results).text
        print("tražio sam na wolframu")
        return wolfram_res
        #print(wolfram_res)

    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(upit).results).text
        print("i sada sam tražio na wolframu")
        return wolfram_res
        #print(wolfram_res)

#get_the_answer("who is einstein?")