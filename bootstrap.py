from api import app, EVENTS
from model.event import Event
from model.user import User
from model.visibility import Visibility
import services.userService
import services.eventService



def development():
	user = User(username='cpi', password='unq')
	user.save()

	public = Visibility(name='Public')
	public.save()


	private = Visibility(name='Private')
	private.save()

	event = Event(
	    date= 'Thu Sep 24 2015 17=24=10 GMT-0300 (ART)',
	    description= 'Lollapalooza se caracteriza por presentar a las bandas mas importantes y vanguardistas de la escena internacional y nacional. Algunas de las que ya formaron parte son= Red Hot Chilli Peppers, Jack White',
	    image= 'http://static.passto.com.ar.s3.amazonaws.com/lollapalooza/lolla-banner-nuevo.jpg',
	    name= 'Lollapalooza 2016',
	    tag= 'LollaAR',
	    time= '10:00',
	    venue= 'Hipodromo de san isidro',
		owner = user,
		visibility = public
	)

	event.save()

	event2 = Event(
	    date= 'Thu Sep 24 2015 17=24=10 GMT-0300 (ART)',
	    description= 'Choripateada de TPI',
	    image= 'http://www.pasqualinonet.com.ar/images/Chorizos-765w%20007b.jpg',
	    name= 'Choripateada 2015',
	    tag= 'chori_2015',
	    time= '10:00',
	    venue= 'Universidad Nacional de Quilmes (UNQ)',
		owner = user,
		visibility = private
	)

	event2.save()



if __name__ == '__main__':
	development()

