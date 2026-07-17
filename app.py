from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pages/glitch")
def glitch():
    return render_template("pages/glitch.html")

@app.route("/pages/series")
def series():
    return render_template("pages/series.html")

@app.route("/pages/tienda")
def tienda():
    return render_template("pages/tienda.html")

@app.route("/pages/anuncios")
def anuncios():
    return render_template("pages/anuncios.html")

@app.route("/pages/fanarts")
def fanarts():
    return render_template("pages/fanarts.html")

@app.route("/pages/juegos")
def juegos():
    return render_template("pages/juegos.html")

@app.route("/pages/redes")
def redes():
    return render_template("pages/redes.html")

# ==========================
# THE AMAZING DIGITAL CIRCUS
# ==========================

@app.route("/series/tadc")
def tadc():
    return render_template("series/tadc/index.html")

@app.route("/series/tadc/informacion")
def tadc_informacion():
    return render_template("series/tadc/informacion.html")

@app.route("/series/tadc/capitulos")
def tadc_capitulos():
    return render_template("series/tadc/capitulos.html")

@app.route("/series/tadc/personajes")
def tadc_personajes():
    return render_template("series/tadc/personajes.html")

@app.route("/series/tadc/people")
def tadc_people():
    return render_template("series/tadc/participantes.html")

@app.route("/series/tadc/musica")
def tadc_musica():
    return render_template("series/tadc/musica.html")

@app.route("/series/tadc/curiosidades")
def tadc_curiosidades():
    return render_template("series/tadc/curiosidades.html")

@app.route("/series/tadc/redes")
def tadc_redes():
    return render_template("series/tadc/redes.html")

@app.route("/series/tadc/people/creadores")
def tadc_creadores():
    return render_template("series/tadc/people/creators/creators.html")

@app.route("/series/tadc/people/productores")
def tadc_productores():
    return render_template("series/tadc/people/productores/productores.html")

@app.route("/series/tadc/people/actores_voz")

def tadc_actores_voz():
    return render_template("series/tadc/people/voice_actors/voice_actors.html")

@app.route("/series/tadc/characters/pomni")
def pomni():
    return render_template("series/tadc/characters/pomni.html")

@app.route("/series/tadc/characters/jax")
def jax():
    return render_template("series/tadc/characters/jax.html")

@app.route("/series/tadc/characters/ragatha")
def ragatha():
    return render_template("series/tadc/characters/ragatha.html")

@app.route("/series/tadc/characters/gangle")
def gangle():
    return render_template("series/tadc/characters/gangle.html")

@app.route("/series/tadc/characters/zooble")
def zooble():
    return render_template("series/tadc/characters/zooble.html")

@app.route("/series/tadc/characters/kinger")
def kinger():
    return render_template("series/tadc/characters/kinger.html")

@app.route("/series/tadc/characters/caine")
def caine():
    return render_template("series/tadc/characters/caine.html")

@app.route("/series/tadc/characters/bubble")
def bubble():
    return render_template("series/tadc/characters/bubble.html")

@app.route("/series/tadc/characters/gummigoo")
def gummigoo():
    return render_template("series/tadc/characters/gummigoo.html")

@app.route("/series/tadc/characters/kaufmo")
def kaufmo():
    return render_template("series/tadc/characters/kaufmo.html")

@app.route("/series/tadc/characters/queenie")
def queenie():
    return render_template("series/tadc/characters/queenie.html")

@app.route("/series/tadc/characters/ribbit")
def ribbit():
    return render_template("series/tadc/characters/ribbit.html")

# =================
# MURDER DRONES
# =================

@app.route("/series/md")
def md():
    return render_template("series/md/index.html")

@app.route("/series/md/informacion")
def md_informacion():
    return render_template("series/md/informacion.html")

@app.route("/series/md/capitulos")
def md_capitulos():
    return render_template("series/md/capitulos.html")

@app.route("/series/md/personajes")
def md_personajes():
    return render_template("series/md/personajes.html")

@app.route("/series/md/musica")
def md_musica():
    return render_template("series/md/musica.html")

@app.route("/series/md/curiosidades")
def md_curiosidades():
    return render_template("series/md/curiosidades.html")

@app.route("/series/md/redes")
def md_redes():
    return render_template("series/md/redes.html")

@app.route("/series/md/people")
def md_people():
    return render_template("series/md/people/index.html")

@app.route("/series/md/people/creadores")
def md_creadores():
    return render_template("series/md/people/creators/creators.html")

@app.route("/series/md/people/productores")
def md_productores():
    return render_template("series/md/people/productores/productores.html")

@app.route("/series/md/people/actores_voz")
def md_actores_voz():
    return render_template("series/md/people/voice_actors.html")

@app.route("/series/md/people/otros")
def md_otros():
    return render_template("series/md/others/people/otros.html")

# =================
# PERSONAJES - MURDER DRONES
# =================

@app.route("/series/md/characters/alice")
def md_alice():
    return render_template("series/md/characters/alice.html")

@app.route("/series/md/characters/cyn")
def md_cyn():
    return render_template("series/md/characters/cyn.html")

@app.route("/series/md/characters/cynessa")
def md_cynessa():
    return render_template("series/md/characters/cynessa.html")

@app.route("/series/md/characters/doll")
def md_doll():
    return render_template("series/md/characters/doll.html")

@app.route("/series/md/characters/j")
def md_j():
    return render_template("series/md/characters/j.html")

@app.route("/series/md/characters/khan")
def md_khan():
    return render_template("series/md/characters/khan.html")

@app.route("/series/md/characters/lizzy")
def md_lizzy():
    return render_template("series/md/characters/lizzy.html")

@app.route("/series/md/characters/n")
def md_n():
    return render_template("series/md/characters/n.html")

@app.route("/series/md/characters/nori")
def md_nori():
    return render_template("series/md/characters/nori.html")

@app.route("/series/md/characters/tessa")
def md_tessa():
    return render_template("series/md/characters/tessa.html")

@app.route("/series/md/characters/thad")
def md_thad():
    return render_template("series/md/characters/thad.html")

@app.route("/series/md/characters/uzi")
def md_uzi():
    return render_template("series/md/characters/uzi.html")

@app.route("/series/md/characters/v")
def md_v():
    return render_template("series/md/characters/v.html")

@app.route("/series/md/characters/yeva")
def md_yeva():
    return render_template("series/md/characters/yeva.html")

# =========================
# KNIGHTS OF GUINEVERE
# =========================

@app.route("/series/knights_of_guinevere")
def knights_of_guinevere():
    return render_template("series/knights_of_guinevere/index.html")

@app.route("/series/knights_of_guinevere/informacion")
def kog_informacion():
    return render_template("series/knights_of_guinevere/informacion.html")

@app.route("/series/knights_of_guinevere/capitulos")
def kog_capitulos():
    return render_template("series/knights_of_guinevere/capitulos.html")

@app.route("/series/knights_of_guinevere/personajes")
def kog_personajes():
    return render_template("series/knights_of_guinevere/personajes.html")

@app.route("/series/knights_of_guinevere/musica")
def kog_musica():
    return render_template("series/knights_of_guinevere/musica.html")

@app.route("/series/knights_of_guinevere/curiosidades")
def kog_curiosidades():
    return render_template("series/knights_of_guinevere/curiosidades.html")

@app.route("/series/knights_of_guinevere/redes")
def kog_redes():
    return render_template("series/knights_of_guinevere/redes.html")

@app.route("/series/knights_of_guinevere/people")
def kog_people():
    return render_template("series/knights_of_guinevere/people/index.html")

@app.route("/series/knights_of_guinevere/people/creadores")
def kog_creadores():
    return render_template("series/knights_of_guinevere/people/creadores.html")

@app.route("/series/knights_of_guinevere/people/productores")
def kog_productores():
    return render_template("series/knights_of_guinevere/people/productores.html")

@app.route("/series/knights_of_guinevere/people/actores_voz")
def kog_actores_voz():
    return render_template("series/knights_of_guinevere/people/actores_voz.html")

@app.route("/series/knights_of_guinevere/people/otros")
def kog_otros():
    return render_template("series/knights_of_guinevere/people/otros.html")

@app.route("/series/knights_of_guinevere/characters/andi")
def kog_andi():
    return render_template("series/knights_of_guinevere/characters/andi.html")

@app.route("/series/knights_of_guinevere/characters/frankie")
def kog_frankie():
    return render_template("series/knights_of_guinevere/characters/frankie.html")

@app.route("/series/knights_of_guinevere/characters/gwen")
def kog_gwen():
    return render_template("series/knights_of_guinevere/characters/gwen.html")

@app.route("/series/knights_of_guinevere/characters/olivia_park")
def kog_olivia_park():
    return render_template("series/knights_of_guinevere/characters/olivia_park.html")

@app.route("/series/knights_of_guinevere/characters/orville_park")
def kog_orville_park():
    return render_template("series/knights_of_guinevere/characters/orville_park.html")

@app.route("/series/knights_of_guinevere/characters/sparky")
def kog_sparky():
    return render_template("series/knights_of_guinevere/characters/sparky.html")


# Arranque
if __name__ == "__main__":
    app.run(debug=True)