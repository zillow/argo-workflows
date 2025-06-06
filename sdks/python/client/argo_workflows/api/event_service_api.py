"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argo-workflows.readthedocs.io/en/release-3.5/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.api_client import ApiClient, Endpoint as _Endpoint
from argo_workflows.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError
from argo_workflows.model.io_argoproj_workflow_v1alpha1_workflow_event_binding_list import IoArgoprojWorkflowV1alpha1WorkflowEventBindingList


class EventServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_workflow_event_bindings_endpoint = _Endpoint(
            settings={
                'response_type': (IoArgoprojWorkflowV1alpha1WorkflowEventBindingList,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/api/v1/workflow-event-bindings/{namespace}',
                'operation_id': 'list_workflow_event_bindings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'list_options_label_selector',
                    'list_options_field_selector',
                    'list_options_watch',
                    'list_options_allow_watch_bookmarks',
                    'list_options_resource_version',
                    'list_options_resource_version_match',
                    'list_options_timeout_seconds',
                    'list_options_limit',
                    'list_options_continue',
                ],
                'required': [
                    'namespace',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'list_options_label_selector':
                        (str,),
                    'list_options_field_selector':
                        (str,),
                    'list_options_watch':
                        (bool,),
                    'list_options_allow_watch_bookmarks':
                        (bool,),
                    'list_options_resource_version':
                        (str,),
                    'list_options_resource_version_match':
                        (str,),
                    'list_options_timeout_seconds':
                        (str,),
                    'list_options_limit':
                        (str,),
                    'list_options_continue':
                        (str,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'list_options_label_selector': 'listOptions.labelSelector',
                    'list_options_field_selector': 'listOptions.fieldSelector',
                    'list_options_watch': 'listOptions.watch',
                    'list_options_allow_watch_bookmarks': 'listOptions.allowWatchBookmarks',
                    'list_options_resource_version': 'listOptions.resourceVersion',
                    'list_options_resource_version_match': 'listOptions.resourceVersionMatch',
                    'list_options_timeout_seconds': 'listOptions.timeoutSeconds',
                    'list_options_limit': 'listOptions.limit',
                    'list_options_continue': 'listOptions.continue',
                },
                'location_map': {
                    'namespace': 'path',
                    'list_options_label_selector': 'query',
                    'list_options_field_selector': 'query',
                    'list_options_watch': 'query',
                    'list_options_allow_watch_bookmarks': 'query',
                    'list_options_resource_version': 'query',
                    'list_options_resource_version_match': 'query',
                    'list_options_timeout_seconds': 'query',
                    'list_options_limit': 'query',
                    'list_options_continue': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.receive_event_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/api/v1/events/{namespace}/{discriminator}',
                'operation_id': 'receive_event',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'discriminator',
                    'body',
                ],
                'required': [
                    'namespace',
                    'discriminator',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'discriminator':
                        (str,),
                    'body':
                        (bool, date, datetime, dict, float, int, list, str, none_type,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'discriminator': 'discriminator',
                },
                'location_map': {
                    'namespace': 'path',
                    'discriminator': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def list_workflow_event_bindings(
        self,
        namespace,
        **kwargs
    ):
        """list_workflow_event_bindings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_workflow_event_bindings(namespace, async_req=True)
        >>> result = thread.get()

        Args:
            namespace (str):

        Keyword Args:
            list_options_label_selector (str): A selector to restrict the list of returned objects by their labels. Defaults to everything. +optional.. [optional]
            list_options_field_selector (str): A selector to restrict the list of returned objects by their fields. Defaults to everything. +optional.. [optional]
            list_options_watch (bool): Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. +optional.. [optional]
            list_options_allow_watch_bookmarks (bool): allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. +optional.. [optional]
            list_options_resource_version (str): resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
            list_options_resource_version_match (str): resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset +optional. [optional]
            list_options_timeout_seconds (str): Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. +optional.. [optional]
            list_options_limit (str): limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.. [optional]
            list_options_continue (str): The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            IoArgoprojWorkflowV1alpha1WorkflowEventBindingList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['namespace'] = \
            namespace
        return self.list_workflow_event_bindings_endpoint.call_with_http_info(**kwargs)

    def receive_event(
        self,
        namespace,
        discriminator,
        body,
        **kwargs
    ):
        """receive_event  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.receive_event(namespace, discriminator, body, async_req=True)
        >>> result = thread.get()

        Args:
            namespace (str): The namespace for the io.argoproj.workflow.v1alpha1. This can be empty if the client has cluster scoped permissions. If empty, then the event is \"broadcast\" to workflow event binding in all namespaces.
            discriminator (str): Optional discriminator for the io.argoproj.workflow.v1alpha1. This should almost always be empty. Used for edge-cases where the event payload alone is not provide enough information to discriminate the event. This MUST NOT be used as security mechanism, e.g. to allow two clients to use the same access token, or to support webhooks on unsecured server. Instead, use access tokens. This is made available as `discriminator` in the event binding selector (`/spec/event/selector)`
            body (bool, date, datetime, dict, float, int, list, str, none_type): The event itself can be any data.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['namespace'] = \
            namespace
        kwargs['discriminator'] = \
            discriminator
        kwargs['body'] = \
            body
        return self.receive_event_endpoint.call_with_http_info(**kwargs)

