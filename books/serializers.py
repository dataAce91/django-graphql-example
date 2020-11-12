from rest_framework import serializers
from . models import Books


class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['bookID','title','authors','average_rating','publisher','isbn13']
