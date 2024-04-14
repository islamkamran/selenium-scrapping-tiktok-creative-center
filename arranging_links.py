links = """https://www.happycow.net
	https://www.eatmikeys.com
	https://www.ro.co
    https://www.onegreenplanet.org
	https://www.nexthealth.de
 	https://www.tastesalud.com
	https://www.gvmled.com
	https://www.popl.co
	https://www.speechify.com
	https://www.latercase.com
	https://www.hypershop.com
	https://www.soulnation.com
	https://www.ember.com
	https://www.invideo.io
	https://www.fairlife.com
	https://www.knowseafood.com
	https://www.ellevest.com
	https://www.kiinde.com
	https://www.skillshare.com
	https://www.thefutur.com
	https://www.trello.com
	https://www.klaviyo.com
	https://www.evernote.com
	https://www.getpocket.com
	https://www.superhuman.com
	https://www.sproutsocial.com
	https://www.playermaker.com
	https://www.imagen-ai.com
	https://www.luma-touch.com
	https://www.editorskeys.com
	https://www.freewellgear.com
    https://www.frame.io
	https://www.udacity.com
	https://www.web.meetcleo.com
	https://www.padlet.com
	https://www.freshbooks.com
	https://www.sage.com
	https://www.nearpod.com
	https://www.quizlet.com
	https://www.gong.io
	https://www.vidyard.com
	https://www.plaito.ai
	https://www.syte.ai
	https://www.dice.fm
	https://www.nothing.tech
	https://www.starlingbank.com
	https://www.prezi.com
	https://www.focusmate.com
	https://www.meetup.com
	https://www.tagged.com
	https://www.elitesingles.com
	https://www.happn.com
	https://www.pocketsmith.com
	https://www.titan.com
	https://www.qapital.com
	https://www.monese.com
	https://www.earnin.com
	https://www.stash.com
	https://www.okcupid.com
	https://www.paired.com
	https://www.tofurky.com
	https://www.noevilfoods.com
	https://www.friidesigns.com
	https://www.dxo.com
	https://www.filmicpro.com
	https://www.lumen5.com
	https://www.invisionapp.com
	https://www.intercom.com
	https://www.loom.com
    https://www.fitafy.com
    https://www.templify.video
    https://www.invoke.ai
    https://www.goflyy.com
    https://www.vanguardworld.com
    https://www.greetabl.com
    https://www.mealime.com
    https://www.snacklins.com
    https://www.spoonfulofcomfort.com
    https://www.eatglonuts.com
    https://www.brunekitchen.com
    https://www.momofuku.com
    https://www.japancandystore.com
    https://www.flybyjing.com
    https://www.kbbqkit.com
    https://www.naturespath.com
    https://www.kindsnacks.com
    https://www.tastybite.co.in
    https://www.lovelycandystore.com
    https://www.neatorobotics.com
    https://www.oxo.com
    https://www.rubbermaid.com
    https://www.eatmmmly.com
    https://www.burgesspetcare.com
    https://www.rosebud.ai
    https://www.blink.la
    https://www.livingwithcandella.com
    https://www.iask.ai"""

links = links.strip()
links = links.split("\n")
# print(links)

links1 = []
links = ['https://www.happycow.net', '\thttps://www.eatmikeys.com', '\thttps://www.ro.co', '    https://www.onegreenplanet.org', '\thttps://www.nexthealth.de', ' \thttps://www.tastesalud.com', '\thttps://www.gvmled.com', '\thttps://www.popl.co', '\thttps://www.speechify.com', '\thttps://www.latercase.com', '\thttps://www.hypershop.com', '\thttps://www.soulnation.com', '\thttps://www.ember.com', '\thttps://www.invideo.io', '\thttps://www.fairlife.com', '\thttps://www.knowseafood.com', '\thttps://www.ellevest.com', '\thttps://www.kiinde.com', '\thttps://www.skillshare.com', '\thttps://www.thefutur.com', '\thttps://www.trello.com', '\thttps://www.klaviyo.com', '\thttps://www.evernote.com', '\thttps://www.getpocket.com', '\thttps://www.superhuman.com', '\thttps://www.sproutsocial.com', '\thttps://www.playermaker.com', '\thttps://www.imagen-ai.com', '\thttps://www.luma-touch.com', '\thttps://www.editorskeys.com', '\thttps://www.freewellgear.com', '    https://www.frame.io', '\thttps://www.udacity.com', '\thttps://www.web.meetcleo.com', '\thttps://www.padlet.com', '\thttps://www.freshbooks.com', '\thttps://www.sage.com', '\thttps://www.nearpod.com', '\thttps://www.quizlet.com', '\thttps://www.gong.io', '\thttps://www.vidyard.com', '\thttps://www.plaito.ai', '\thttps://www.syte.ai', '\thttps://www.dice.fm', '\thttps://www.nothing.tech', '\thttps://www.starlingbank.com', '\thttps://www.prezi.com', '\thttps://www.focusmate.com', '\thttps://www.meetup.com', '\thttps://www.tagged.com', '\thttps://www.elitesingles.com', '\thttps://www.happn.com', '\thttps://www.pocketsmith.com', '\thttps://www.titan.com', '\thttps://www.qapital.com', '\thttps://www.monese.com', '\thttps://www.earnin.com', '\thttps://www.stash.com', '\thttps://www.okcupid.com', '\thttps://www.paired.com', '\thttps://www.tofurky.com', '\thttps://www.noevilfoods.com', '\thttps://www.friidesigns.com', '\thttps://www.dxo.com', '\thttps://www.filmicpro.com', '\thttps://www.lumen5.com', '\thttps://www.invisionapp.com', '\thttps://www.intercom.com', '\thttps://www.loom.com', '    https://www.fitafy.com', '    https://www.templify.video', '    https://www.invoke.ai', '    https://www.goflyy.com', '    https://www.vanguardworld.com', '    https://www.greetabl.com', '    https://www.mealime.com', '    https://www.snacklins.com', '    https://www.spoonfulofcomfort.com', '    https://www.eatglonuts.com', '    https://www.brunekitchen.com', '    https://www.momofuku.com', '    https://www.japancandystore.com', '    https://www.flybyjing.com', '    https://www.kbbqkit.com', '    https://www.naturespath.com', '    https://www.kindsnacks.com', '    https://www.tastybite.co.in', '    https://www.lovelycandystore.com', '    https://www.neatorobotics.com', '    https://www.oxo.com', '    https://www.rubbermaid.com', '    https://www.eatmmmly.com', '    https://www.burgesspetcare.com', '    https://www.rosebud.ai', '    https://www.blink.la', '    https://www.livingwithcandella.com', '    https://www.iask.ai']

for link in links:
    link = link.replace(" ", "").replace("\t","")
    links1.append(link)
print(links1)
