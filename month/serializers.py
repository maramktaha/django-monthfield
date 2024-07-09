import datetime
from rest_framework import fields, serializers

from month import Month

class MonthField(fields.DateField):

  def to_internal_value(self, value):
        if isinstance(value, Month):
            month = value
        elif isinstance(value, datetime.date) or isinstance(value,str):
            print(value,type(value))

            if isinstance(value,str):
                month = Month.from_string(value)
            else:
                month = Month.from_date(value)
            print(str(month.year))
            if len(str(month.year)) < 4:
                raise serializers.ValidationError(
                    self.error_messages["invalid_year"],
                    code="invalid_year",
                    params={"value": value},
                )
        return month

  def to_representation(self, value):

        return value.strftime(str(value))