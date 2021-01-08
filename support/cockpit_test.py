from playhouse.postgres_ext import *

database = PostgresqlDatabase('cockpit-test',
                              **{'host': '192.168.1.5', 'port': 5435, 'user': 'postgres', 'password': 'postgres'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class AlembicVersion(BaseModel):
    version_num = CharField(primary_key=True)

    class Meta:
        table_name = 'alembic_version'


class Alert(BaseModel):
    code = CharField(index=True)
    duration = IntegerField()
    thing_id = IntegerField(index=True)
    timestamp = DateTimeField()

    class Meta:
        table_name = 'alert'


class CompanyThingTypeReport(BaseModel):
    company_id = IntegerField(index=True)
    data = BinaryJSONField()
    tag = CharField()
    timestamp = DateTimeField()
    type_id = IntegerField(index=True)

    class Meta:
        table_name = 'company_thing_type_report'


class EnergyGroup(BaseModel):
    company_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    name = CharField()

    class Meta:
        table_name = 'energy_group'


class Target(BaseModel):
    company_id = IntegerField(index=True)
    oee = DoubleField(null=True)
    operation_rate = DoubleField(null=True)
    organization_id = IntegerField(index=True, null=True)
    performance_rate = DoubleField(null=True)
    timestamp = DateTimeField()
    yield_rate = DoubleField(null=True)

    class Meta:
        table_name = 'target'
        indexes = (
            (('organization_id', 'company_id'), True),
        )


class ThingEnergyGroup(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=EnergyGroup)
    percentage = DoubleField(constraints=[SQL("DEFAULT '1'::double precision")])
    thing_id = IntegerField(index=True)

    class Meta:
        table_name = 'thing_energy_group'


class ThingInputDataRecord(BaseModel):
    company_id = IntegerField(index=True)
    deletable = BooleanField(constraints=[SQL("DEFAULT false")])
    finished = BooleanField(constraints=[SQL("DEFAULT false")])
    fix_production = IntegerField(null=True)
    fix_production_beat = IntegerField(null=True)
    fix_yield_number = IntegerField(null=True)
    product_name = CharField(index=True)
    production = IntegerField(null=True)
    production_beat = IntegerField(null=True)
    thing_id = IntegerField(index=True)
    timestamp = DateTimeField()
    yield_number = IntegerField(null=True)

    class Meta:
        table_name = 'thing_input_data_record'


class ThingRealData(BaseModel):
    company_id = IntegerField(index=True)
    data = BinaryJSONField()
    thing_id = IntegerField(unique=True)
    timestamp = DateTimeField()
    type_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'thing_real_data'


class ThingReport(BaseModel):
    company_id = IntegerField(index=True)
    data = BinaryJSONField()
    tag = CharField()
    thing_id = IntegerField(index=True)
    timestamp = DateTimeField()
    type_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'thing_report'


if __name__ == '__main__':
    result = ThingReport().select(ThingReport.data["standby_time"].as_json().alias("standby")).where(
        ThingReport.company_id == 8,
        ThingReport.tag == 'day',
        ThingReport.thing_id == 14,
        ThingReport.timestamp == '2021-01-05 00:00:00'
    )
    for i in result:
        # print(i.data)
        print(i.standby)
    print(result)
