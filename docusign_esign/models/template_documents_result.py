# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TemplateDocumentsResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, template_documents=None, template_id=None):
        """
        TemplateDocumentsResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'template_documents': 'list[EnvelopeDocument]',
            'template_id': 'str'
        }

        self.attribute_map = {
            'template_documents': 'templateDocuments',
            'template_id': 'templateId'
        }

        self._template_documents = template_documents
        self._template_id = template_id

    @property
    def template_documents(self):
        """
        Gets the template_documents of this TemplateDocumentsResult.
        

        :return: The template_documents of this TemplateDocumentsResult.
        :rtype: list[EnvelopeDocument]
        """
        return self._template_documents

    @template_documents.setter
    def template_documents(self, template_documents):
        """
        Sets the template_documents of this TemplateDocumentsResult.
        

        :param template_documents: The template_documents of this TemplateDocumentsResult.
        :type: list[EnvelopeDocument]
        """

        self._template_documents = template_documents

    @property
    def template_id(self):
        """
        Gets the template_id of this TemplateDocumentsResult.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :return: The template_id of this TemplateDocumentsResult.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this TemplateDocumentsResult.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :param template_id: The template_id of this TemplateDocumentsResult.
        :type: str
        """

        self._template_id = template_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
