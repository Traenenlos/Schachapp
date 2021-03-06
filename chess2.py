import streamlit as st

text_a1 = "An dem Beispiel einer Partie zwischen Caturman(1966) und Traenenlos345(1880) möchte ich ihnen die Wichtigkeit und Dominaz von Bauernketten erklären."
bild_1 = "./images/Bildschirmfoto_chess1.png"
text_a2 = "Mit dem Zug e5 wird der Bauer auf d4 gedeckt und es bildet sich die erste kleine Bauernkette. "
bild_2 = "./images//Bildschirmfoto_chess2.png"
text_b = "Die Rochade wird gezogen. Die Idee des Zuges ist den Turm auf e1 zu stellen und damit den Angriff des Schwarzen zu verlangsamen."
bild_3 = "./images/Bildschirmfoto_chess3.png"
text_c = "Die Bauern wollen nach vorne! Nachdem Schwarz den Bauern auf e4 gezogen hat, bildet sich ein erster Eindruck der Bauermacht und wie schlecht Weiß noch seine Figuren bewegen."
bild_4 = "./images/Bildschirmfoto_chess4.png"
text_d = "Springer d2 kommt. Dies ist der einzig mögliche Zug damit der Springer nicht verloren geht."
bild_5 = "./images/Bildschirmfoto_chess5.png"
text_e = "An dieser Stelle zog Traenenlos den Läufer auf f5, den Bauer aber direkt auf f5 zu spielen wäre sehr viel besser gewesen da es die  Bauernmacht noch mehr unterstüzt und Druck erzeugt."
bild_6 = "./images/Bildschirmfoto_chess6.png"
text_f = "Weiß hätte hier seine Chanche nutzen müssen und b4 ziehen müssen, um c5 zu drohen. Damit würde er Schwarz ein Tempo wegnehmen das er gerne gehabt hätte. Statdessen zog Weiß Läufer g4."
bild_7 = "./images/Bildschirmfoto_chess7.png"
text_g = "Hätte Schwarz jetzt g6 gezogen wäre die Stellung deutlich einfacher. Auf Springer schlägt e4 könnte man ganz einfach mit dem Läufer nehmen und auf Turm e1 f5 spielen. Schwarz zog aber etwas anderes in der Partie."
bild_8 = "./images/Bildschirmfoto_chess8.png"
text_h = "Weiß hätte jetzt seine Chanche nutzen müssen,indem er mit dem Springer auf e4 schlägt darauf muss man Läufer schlägt e4 spielen und dann kann man Turm e1 spielen , worauf dann kein f5 mehr geht."
bild_9 = "./images/Bildschirmfoto_chess9.png"
text_i = "Turm e1 kam und zerstörte die Weißen Chanchen. Sie können gerne raten wie Schwarz jetzt wieder in großen Vorteil kommen kann."
bild_10 = "./images/Bildschirmfoto_chess10.png"
text_j = "F5. F5 lässt Schwarz wieder strahlen. Die Stellung ist Kompakt, ein dritter Bauer stärkt die Bauernkette und es gibt keinen Schwächepunkt bei Schwarz. Die Stellung ist glatt gewonnen."
bild_11 = "./images/Bildschirmfoto_chess11.png"
text_k = "Läufer h3 kam, kein guter aber auch kein schlechter Zug. Weiß hätte aber auch mit b4 auf Kompensation gehen können."
bild_12 = "./images/Bildschirmfoto_chess12.png"
text_l = "Läufer e7 kommt von Schwarz. Schwarz versucht damit aus der Fesslung vom Turm auf e1 raus zu kommen, um besser die Bauerkette voran schieben zu können."
bild_13 = "./images/Bildschirmfoto_chess13.png"
text_m = "Weiß hätte immernoch versuchen sollen mit b4 etwas zu erreichen, zog aber stattdessen f3 was Schwarz nur einlied die Bauernkette weiter auszubauen und zu verbessern."
bild_14 = "./images/Bildschirmfoto_chess14.png"
text_n = "E3. Der beste Zug den Schwarz hätte spielen können. Der Zug sträkt die Stellung, engt Weiß noch mehr ein und zwingt den Gegner regelrecht noch ein Tempo abzugeben, indem man de Springer zieht."
bild_15 = "./images/Bildschirmfoto_chess15.png"
text_o = "Springer b3 kommt und stellt den Bauern auf c4 ein. Die bekannte Idee mit b4 wäre hier immernoch am besten."
bild_16 = "./images/Bildschirmfoto_chess16.png"
text_p = "Springer schlägt c4. Der bestmöglichste Zug und bereitet Ideen wie d3 vor"
bild_17 = "./images/Bildschirmfoto_chess17.png"
text_q = "Die Idee hinter Dame d3 ist schon richtig (den Springer vertreiben damit es kein d3 geben kann). Besser wäre aber Dame c2 gewesen. Sie könne gerne überlegen warum."
bild_18 = "./images/Bildschirmfoto_chess18.png"
text_r = "Die Antwort auf die davor gestellte Frage lautet: Springer e5. Springer e5 erlaubt Schwarz nämlich den Springer mit Tempo wegzuziehe, da die Dame angegriffen wird. Dies wäre nicht passiert wäre die Dame auf c2 gezogen."
bild_19 = "./images/Bildschirmfoto_chess19.png"
text_s = "Dame b5 wollte wahrscheinlich noch irgendwelche Drohungen stellen. Dafür ist es aber bereits schon zu spät"
bild_20 = "./images/Bildschirmfoto_chess20.png"
text_t = "Die Rochade kam. Sicherlich gibt es hier auch bessere Züge wie f4, Schwarz wollte wahrscheinlich erstmal auf Sicherheit gehen, denn besser steht er immernoch."
bild_21 = "./images/Bildschirmfoto_chess21.png"
text_u = "A4 kam. Weiß wollte den letzen Angriff starten der aber auch wenn Schwarz nichts tuen würde zum scheitern verurteilt wäre."
bild_22 = "./images/Bildschirmfoto_chess22.png"
text_v = "F4 kommt und stärk die Bauerstellung imenz. Die Idee hinter f4 ist, den d-Bauern vorspielen zu können um den Weißen vor große Probleme zu stellen."
bild_23 = "./images/Bildschirmfoto_chess23.png"
text_w = "Springer a3 kommt und man merkt das der Weiße keine Ideen mehr hat und im inneren schon kapituliert hat."
bild_24 = "./images/Bildschirmfoto_chess24.png"
text_x = "D3 kommt und droht d2 (eine sogennante Gabel) zu ziehen"
bild_25 = './images/Bildschirmfoto_chess25.png'
text_y = "Turm d1 kommt, da d2 mit einer Gabel gedroht hatte."
bild_26 = "./images/Bildschirmfoto_chess26.png"
text_z = "Schwarz zog d2 und es dauerte nur noch ein paar Züge bis Weiß aufgab. Ich bedanke mich für das besuchen der Website und hoffe das Beispiel für die Bauerndominanz hat ihnen gefallen."
bild_27 = "./images/Bildschirmfoto_chess27.png"


st.title("Schach: Die Dominanz von Bauernketten/Die Dominanz des Zentrums")

st.button("Cookie Klicker 2.0")

auswahlmöglichkeit = st.radio(
    "Mit welchem Tool möchten Sie die Website steuern", ("Selectbox", "Slider")
)
if auswahlmöglichkeit == "Selectbox":
    st.write("Gute Wahl")
    number_selectbox = st.sidebar.selectbox("Auf welche Seite möchtest du", range(27))
    number = number_selectbox
# else:
# ("Du hast Selectbox nicht ausgewählt")
elif auswahlmöglichkeit == "Slider":
    st.write("Gute Wahl")
    number_slider = st.slider("Wähle eine Seite", 0, 26, 1)
    number = number_slider
# else:
# ("Du hast Slider nicht ausgewählt")


bilder = [
    bild_1,
    bild_2,
    bild_3,
    bild_4,
    bild_5,
    bild_6,
    bild_7,
    bild_8,
    bild_9,
    bild_10,
    bild_11,
    bild_12,
    bild_13,
    bild_14,
    bild_15,
    bild_16,
    bild_17,
    bild_18,
    bild_19,
    bild_20,
    bild_21,
    bild_22,
    bild_23,
    bild_24,
    bild_25,
    bild_26,
    bild_27,
]
texte = [
    text_a1,
    text_a2,
    text_b,
    text_c,
    text_d,
    text_e,
    text_f,
    text_g,
    text_h,
    text_i,
    text_j,
    text_k,
    text_l,
    text_m,
    text_n,
    text_o,
    text_p,
    text_q,
    text_r,
    text_s,
    text_t,
    text_u,
    text_v,
    text_w,
    text_x,
    text_y,
    text_z,
]


def slideshow(number, texte, bilder):
    st.write(texte[number])
    st.image(bilder[number])


slideshow(number, texte, bilder)
