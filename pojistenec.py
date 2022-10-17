class Pojistenec:

    def __init__(self, jmeno, prijmeni, telefon, vek):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._telefon = telefon
        self._vek = vek

    @property
    def jmeno(self):
        return self._jmeno.capitalize()

    @property
    def prijmeni(self):
        return self._prijmeni.capitalize()

    @property
    def telefon(self):
        return self._telefon

    @property
    def vek(self):
        return self._vek

    @property
    def hledat_jmeno(self):
        return self._jmeno.upper()

    @property
    def hledat_prijmeni(self):
        return self._prijmeni.upper()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.telefon}, {self.vek}"
