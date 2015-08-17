"""For creating an Organization"""
from .base_api import BaseAPI


class Organization(BaseAPI):
    # A list of all arguments for a Organization
    keyword_arguments = [
        "address",
        "billing_id",
        "city",
        "company",
        "contact_fname",
        "contact_lname",
        "country",
        "crm_id",
        "custom_fields",
        "date_create",
        "date_edit",
        "dept",
        "email",
        "fax",
        "latitude",
        "logs",
        "longitude",
        "notes",
        "notification_append",
        "phone",
        "state",
        "theme",
        "title",
        "tollfree",
        "updated_by",
        "zip",
    ]

    uri = '/api/organization'

    @classmethod
    def find(cls, search_string, **kwargs):
        """Find an Organization based on its name"""
        return super().find(
            uri=cls.uri,
            search_spec='company',
            search_string=search_string,
        )

    @classmethod
    def get_uri(cls, company, **kwargs):
        """Get the URI for an item

            :param company: The name of the company you need the URI for

            :return: returns servers response to the GET request
        """
        return super().get_uri(uri=cls.uri, search_spec='company', search_string=company)

    @classmethod
    def create(cls, company, **kwargs):
        """Creates an item on the server"""
        payload = cls.payload(company=company, **kwargs)

        return super().create(
            uri=cls.uri,
            search_spec='company',
            search_string=company,
            payload=payload
        )