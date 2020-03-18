import sqlite3
from sqlite3 import Error


def connector(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.Error as error:
        print("Соединение не установлено", error)

    return conn


def db_creator(conn):
    try:
        sql = '''
        create table if not exists tempTab (
            UIN PRIMARY KEY,
            VidKontragenta,
            Klient,
            Postavshik,
            Gruzopoluchatel,
            Gruzootpravitel,
            StranaRegistracii,
            NalogoviyNomer,
            INN,
            KPP,
            KodPoOkpo,
            NaimenovaniePolnoe,
            Naimenovanie,
            GolovnoyKontragent,
            DataRozhdeniya,
            Pol,
            SvodniyOtraslevoyKlassifikator,
            SvodniyOtraslevoyKlassifikatorKod,
            Ogrnip,
            Ogrn,
            Okato,
            VidOtgruzki,
            MechelKod,
            GruppaRSBU,
            GruppaMsfo,
            ApodKod,
            Kommentarii,
            EtranStancii,
            EtranStanciiKod,
            EtranDorogi,
            EtranDorogiKod,
            KodGruzopoluchatelyaNaZHDStancii,
            PometkaUdalenya
        );
        
        create table if not exists tempTab2 (
            UIN PRIMARY KEY,
            VidRinka,
            ChemaKlienta,
            Preyskurant,
            GruppaCen,
            SrokVistavlenyaSCheta,
            GruppaKontirovki,
            ZakazchikTDMechel,
            DopuskNedopostavki,
            DopuskSverhPostavki,
            DopustimiyOtklonenyaNeogranicheni
        );
        
        create table if not exists temptab3 (
            UIN PRIMARY KEY,
            AdresElektronnoyPochti,
            NomerTelephona
        );
        
        create table if not exists temptab4 (
            UIN PRIMARY KEY,
            Strana,
            Indeks,
            Region,
            Rayon,
            Gorod,
            NasPunkt,
            Ulitsa,
            DomVladenieDomovladenie,
            Korpus,
            StroenieLiteraSooruzhenieUchastok,
            Etazh,
            Predstavlenie
        );
        
        create table if not exists temptab5 (
            UIN PRIMARY KEY,
            Strana,
            Indeks,
            Region,
            Rayon,
            Gorod,
            NasPunkt,
            Ulitsa,
            DomVladenieDomovladenie,
            Korpus,
            StroenieLiteraSooruzhenieUchastok,
            Etazh,
            Predstavlenie
        )
        '''
        cur = conn.cursor()
        cur.executescript(sql)
    except sqlite3.Error as error:
        print("Таблица не создана", error)


def main():
    conn=connector("pythonsqlite.db")
    db_create = db_creator(conn)
    conn.commit()
    conn.close()
main()