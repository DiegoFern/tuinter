from models import db, User, Message
password = User(Name='pep',Password='pep',Email='pep@pep.com')
u2 = User(Name='pep2',Password='pep',Email='pep2@pep.com')
u3 = User(Name='pep3',Password='pep',Email='pep3@pep.com')
u4 = User(Name='pep4',Password='pep',Email='pep4@pep.com', followers=[u2, u3, ])
u1.message.append(Message(text='fddsfadsfdsfdasfsdafdsa'))
u2.message.append(Message(text='asfsdfddsfadsfdsfdasfsdafdsa'))

u1.message.append(  Message(text='asfsdfddsfadsfdsfdasfsdafdsa'))

u1.message.append(  Message(text='2asfsdfddsfadsfdsfdasfsdafdsa'))
u2.followers.append(u3)
u3.followers.append(u2)

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.commit()
