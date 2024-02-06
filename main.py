class Form:
    def __init__(self):
        self.fields = []
    def add_field(self, field):
        self.fields.append(field)
    def __str__(self):
        return "\n".join(self.fields)

class FormBuilder:
    def __init__(self):
        self.form = Form()

    def add_name_field(self):
        self.form.add_field("Name:____")
        return self
    def add_adress_field(self):
        self.form.add_field("Adress:____")
        return self
    def add_email_field(self):
        self.form.add_field("email:____")
        return self
    def add_field_country(self):
        self.form.add_field("Country:____")
        return self
    def build(self):
        return self.form

builder = FormBuilder()
form = builder.add_email_field().add_adress_field().add_field_country().add_name_field().build()
print(form)
