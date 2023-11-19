3import datetime
from sqlalchemy import create_engine, Column, DateTime, Integer, String, Float, MetaData, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///savarankiskas.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column('f_name', String)
    l_name = Column('l_name', String)
    email = Column('email', String)
    order = relationship('Order')

    def __repr__(self):
        return f"{self.id}, {self.f_name}, {self.l_name}, {self.email}"

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    order = relationship('Order')

    def __repr__(self):
        return f"{self.id}, {self.name}"


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price = Column('price', Float)
    product_order = relationship('Product_order')

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}"


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer')
    date_ = Column('date_', DateTime, default=datetime.datetime.utcnow)
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship('Status')

    def __repr__(self):
        return f'{self.id}, {self.status_id}'

class Product_order(Base):
    __tablename__='product_order'
    id = Column(Integer, primary_key=True)
    order_id = Column("order_id", Integer, ForeignKey('order.id'))
    order = relationship("Order")
    product_id = Column("project_id", Integer, ForeignKey('product.id'))
    product = relationship("Product")
    quantity = Column("quantity", Integer)



    def __repr__(self):
        return f"{self.id}, {self.quantity}"


Base.metadata.create_all(engine)
while True:
    pasirinkimas =int(input("""
    Pasirinkite pageidaujamą veiksmą:
    1 - Pridėti pirkėją
    2 - Pridėti produktą
    3 -	Pridėti statusą
    4 -	Pridėti užsakymą
    5 -	Ištraukti užsakymą pagal id
    6 -	Pakeisti užsakymo statusą pagal užsakymo id
    7 -	Pridėti į užsakymą produktus su kiekiais
    8 - Išeiti\n
"""))

    if pasirinkimas == 1:
        print('NAUJO PIRKĖJO ĮVEDIMAS')
        name = input('Įveskite vardą: ')
        surname = input('Įveskite pavardę: ')
        emailas = input('Įveskite elektronio pašto adresą')
        pirkejas = Customer(f_name = name, l_name = surname, email=emailas)
        session.add(pirkejas)
        session.commit()

    elif pasirinkimas == 2:
        print('NAUJO PRODUKTO ĮVEDIMAS')
        prod_name = input('Įveskite produkto pavadinimą: ')
        prod_price = float(input('įveskite kainą: '))
        preke = Product(name=prod_name, price = prod_price)
        session.add(preke)
        session.commit()

    elif pasirinkimas == 3:
        print('STATUSO ĮVEDIMAS')
        statusas = input('Įveskite statusą:')
        stat = Status(name = statusas)
        session.add(stat)
        session.commit()

    elif pasirinkimas == 4:
        print('ĮVESTI UŽSAKYMĄ: ')
        cus_id = int(input("Įveskite kliento id: "))
        date_z =input('Įveskite datą: ')
        # date_a =datetime.datetime.strptime(date_z ,'%Y=%m-%d')
        status_idz = int(input('Įveskite statuso id: '))
        uzsakymas = Order(customer_id = cus_id,  status_id = status_idz)
        session.add(uzsakymas)
        session.commit()

    elif pasirinkimas == 5:
        print('UŽSAKYMO PERŽIŪRA')
        uzsak_id = int(input('Įveskite užsakymo id peržiūrai: '))
        uzsakymas_view =session.get(Order, uzsak_id)




    elif pasirinkimas == 8:
        break

