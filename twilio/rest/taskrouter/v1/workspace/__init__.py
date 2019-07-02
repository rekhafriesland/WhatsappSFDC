# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.taskrouter.v1.workspace.activity import ActivityList
from twilio.rest.taskrouter.v1.workspace.event import EventList
from twilio.rest.taskrouter.v1.workspace.task import TaskList
from twilio.rest.taskrouter.v1.workspace.task_channel import TaskChannelList
from twilio.rest.taskrouter.v1.workspace.task_queue import TaskQueueList
from twilio.rest.taskrouter.v1.workspace.worker import WorkerList
from twilio.rest.taskrouter.v1.workspace.workflow import WorkflowList
from twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics import WorkspaceCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics import WorkspaceRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.workspace_statistics import WorkspaceStatisticsList


class WorkspaceList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the WorkspaceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceList
        """
        super(WorkspaceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Workspaces'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkspaceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: Filter by a workspace's friendly name.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.WorkspaceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists WorkspaceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: Filter by a workspace's friendly name.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.WorkspaceInstance]
        """
        return list(self.stream(friendly_name=friendly_name, limit=limit, page_size=page_size, ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkspaceInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by a workspace's friendly name.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return WorkspacePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkspaceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WorkspacePage(self._version, response, self._solution)

    def create(self, friendly_name, event_callback_url=values.unset,
               events_filter=values.unset, multi_task_enabled=values.unset,
               template=values.unset, prioritize_queue_order=values.unset):
        """
        Create a new WorkspaceInstance

        :param unicode friendly_name: Human readable description of this workspace
        :param unicode event_callback_url: If provided, the Workspace will publish events to this URL.
        :param unicode events_filter: Use this parameter to receive webhooks on EventCallbackUrl for specific events on a workspace.
        :param bool multi_task_enabled: Multi tasking allows workers to handle multiple tasks simultaneously.
        :param unicode template: One of the available template names.
        :param WorkspaceInstance.QueueOrder prioritize_queue_order: Use this parameter to configure whether to prioritize LIFO or FIFO when workers are receiving Tasks from combination of LIFO and FIFO TaskQueues.

        :returns: Newly created WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'EventCallbackUrl': event_callback_url,
            'EventsFilter': events_filter,
            'MultiTaskEnabled': multi_task_enabled,
            'Template': template,
            'PrioritizeQueueOrder': prioritize_queue_order,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return WorkspaceInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a WorkspaceContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        return WorkspaceContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WorkspaceContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        return WorkspaceContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceList>'


class WorkspacePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkspacePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspacePage
        """
        super(WorkspacePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkspaceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        return WorkspaceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspacePage>'


class WorkspaceContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the WorkspaceContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        super(WorkspaceContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Workspaces/{sid}'.format(**self._solution)

        # Dependents
        self._activities = None
        self._events = None
        self._tasks = None
        self._task_queues = None
        self._workers = None
        self._workflows = None
        self._statistics = None
        self._real_time_statistics = None
        self._cumulative_statistics = None
        self._task_channels = None

    def fetch(self):
        """
        Fetch a WorkspaceInstance

        :returns: Fetched WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, events_filter=values.unset,
               friendly_name=values.unset, multi_task_enabled=values.unset,
               timeout_activity_sid=values.unset,
               prioritize_queue_order=values.unset):
        """
        Update the WorkspaceInstance

        :param unicode default_activity_sid: The ID of the Activity that will be used when new Workers are created in this Workspace.
        :param unicode event_callback_url: The Workspace will publish events to this URL.
        :param unicode events_filter: Use this parameter to receive webhooks on EventCallbackUrl for specific events on a workspace.
        :param unicode friendly_name: Human readable description of this workspace
        :param bool multi_task_enabled: Enable or Disable Multitasking by passing either true or False with the POST request.
        :param unicode timeout_activity_sid: The ID of the Activity that will be assigned to a Worker when a Task reservation times out without a response.
        :param WorkspaceInstance.QueueOrder prioritize_queue_order: Use this parameter to configure whether to prioritize LIFO or FIFO when workers are receiving Tasks from combination of LIFO and FIFO TaskQueues.

        :returns: Updated WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        data = values.of({
            'DefaultActivitySid': default_activity_sid,
            'EventCallbackUrl': event_callback_url,
            'EventsFilter': events_filter,
            'FriendlyName': friendly_name,
            'MultiTaskEnabled': multi_task_enabled,
            'TimeoutActivitySid': timeout_activity_sid,
            'PrioritizeQueueOrder': prioritize_queue_order,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return WorkspaceInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the WorkspaceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def activities(self):
        """
        Access the activities

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        """
        if self._activities is None:
            self._activities = ActivityList(self._version, workspace_sid=self._solution['sid'], )
        return self._activities

    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.taskrouter.v1.workspace.event.EventList
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventList
        """
        if self._events is None:
            self._events = EventList(self._version, workspace_sid=self._solution['sid'], )
        return self._events

    @property
    def tasks(self):
        """
        Access the tasks

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskList
        """
        if self._tasks is None:
            self._tasks = TaskList(self._version, workspace_sid=self._solution['sid'], )
        return self._tasks

    @property
    def task_queues(self):
        """
        Access the task_queues

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.TaskQueueList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.TaskQueueList
        """
        if self._task_queues is None:
            self._task_queues = TaskQueueList(self._version, workspace_sid=self._solution['sid'], )
        return self._task_queues

    @property
    def workers(self):
        """
        Access the workers

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        """
        if self._workers is None:
            self._workers = WorkerList(self._version, workspace_sid=self._solution['sid'], )
        return self._workers

    @property
    def workflows(self):
        """
        Access the workflows

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        """
        if self._workflows is None:
            self._workflows = WorkflowList(self._version, workspace_sid=self._solution['sid'], )
        return self._workflows

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkspaceStatisticsList(self._version, workspace_sid=self._solution['sid'], )
        return self._statistics

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        """
        if self._real_time_statistics is None:
            self._real_time_statistics = WorkspaceRealTimeStatisticsList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        """
        if self._cumulative_statistics is None:
            self._cumulative_statistics = WorkspaceCumulativeStatisticsList(
                self._version,
                workspace_sid=self._solution['sid'],
            )
        return self._cumulative_statistics

    @property
    def task_channels(self):
        """
        Access the task_channels

        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        """
        if self._task_channels is None:
            self._task_channels = TaskChannelList(self._version, workspace_sid=self._solution['sid'], )
        return self._task_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceContext {}>'.format(context)


class WorkspaceInstance(InstanceResource):
    """  """

    class QueueOrder(object):
        FIFO = "FIFO"
        LIFO = "LIFO"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the WorkspaceInstance

        :returns: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        super(WorkspaceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'default_activity_name': payload['default_activity_name'],
            'default_activity_sid': payload['default_activity_sid'],
            'event_callback_url': payload['event_callback_url'],
            'events_filter': payload['events_filter'],
            'friendly_name': payload['friendly_name'],
            'multi_task_enabled': payload['multi_task_enabled'],
            'sid': payload['sid'],
            'timeout_activity_name': payload['timeout_activity_name'],
            'timeout_activity_sid': payload['timeout_activity_sid'],
            'prioritize_queue_order': payload['prioritize_queue_order'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkspaceContext for this WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceContext
        """
        if self._context is None:
            self._context = WorkspaceContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The ID of the account that owns this Workflow
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The time the Workspace was created, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The time the Workspace was last updated, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def default_activity_name(self):
        """
        :returns: The human readable name of the default activity.
        :rtype: unicode
        """
        return self._properties['default_activity_name']

    @property
    def default_activity_sid(self):
        """
        :returns: The ID of the Activity that will be used when new Workers are created in this Workspace.
        :rtype: unicode
        """
        return self._properties['default_activity_sid']

    @property
    def event_callback_url(self):
        """
        :returns: If provided, the Workspace will publish events to this URL.
        :rtype: unicode
        """
        return self._properties['event_callback_url']

    @property
    def events_filter(self):
        """
        :returns: Use this parameter to receive webhooks on EventCallbackUrl for specific events on a workspace.
        :rtype: unicode
        """
        return self._properties['events_filter']

    @property
    def friendly_name(self):
        """
        :returns: Filter by a workspace's friendly name.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def multi_task_enabled(self):
        """
        :returns: Multi tasking allows workers to handle multiple tasks simultaneously.
        :rtype: bool
        """
        return self._properties['multi_task_enabled']

    @property
    def sid(self):
        """
        :returns: The unique ID of the Workspace
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def timeout_activity_name(self):
        """
        :returns: The human readable name of the timeout activity.
        :rtype: unicode
        """
        return self._properties['timeout_activity_name']

    @property
    def timeout_activity_sid(self):
        """
        :returns: The ID of the Activity that will be assigned to a Worker when a Task reservation times out without a response.
        :rtype: unicode
        """
        return self._properties['timeout_activity_sid']

    @property
    def prioritize_queue_order(self):
        """
        :returns: Use this parameter to configure whether to prioritize LIFO or FIFO when workers are receiving Tasks from combination of LIFO and FIFO TaskQueues.
        :rtype: WorkspaceInstance.QueueOrder
        """
        return self._properties['prioritize_queue_order']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a WorkspaceInstance

        :returns: Fetched WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        return self._proxy.fetch()

    def update(self, default_activity_sid=values.unset,
               event_callback_url=values.unset, events_filter=values.unset,
               friendly_name=values.unset, multi_task_enabled=values.unset,
               timeout_activity_sid=values.unset,
               prioritize_queue_order=values.unset):
        """
        Update the WorkspaceInstance

        :param unicode default_activity_sid: The ID of the Activity that will be used when new Workers are created in this Workspace.
        :param unicode event_callback_url: The Workspace will publish events to this URL.
        :param unicode events_filter: Use this parameter to receive webhooks on EventCallbackUrl for specific events on a workspace.
        :param unicode friendly_name: Human readable description of this workspace
        :param bool multi_task_enabled: Enable or Disable Multitasking by passing either true or False with the POST request.
        :param unicode timeout_activity_sid: The ID of the Activity that will be assigned to a Worker when a Task reservation times out without a response.
        :param WorkspaceInstance.QueueOrder prioritize_queue_order: Use this parameter to configure whether to prioritize LIFO or FIFO when workers are receiving Tasks from combination of LIFO and FIFO TaskQueues.

        :returns: Updated WorkspaceInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.WorkspaceInstance
        """
        return self._proxy.update(
            default_activity_sid=default_activity_sid,
            event_callback_url=event_callback_url,
            events_filter=events_filter,
            friendly_name=friendly_name,
            multi_task_enabled=multi_task_enabled,
            timeout_activity_sid=timeout_activity_sid,
            prioritize_queue_order=prioritize_queue_order,
        )

    def delete(self):
        """
        Deletes the WorkspaceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def activities(self):
        """
        Access the activities

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        """
        return self._proxy.activities

    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.taskrouter.v1.workspace.event.EventList
        :rtype: twilio.rest.taskrouter.v1.workspace.event.EventList
        """
        return self._proxy.events

    @property
    def tasks(self):
        """
        Access the tasks

        :returns: twilio.rest.taskrouter.v1.workspace.task.TaskList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.TaskList
        """
        return self._proxy.tasks

    @property
    def task_queues(self):
        """
        Access the task_queues

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.TaskQueueList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.TaskQueueList
        """
        return self._proxy.task_queues

    @property
    def workers(self):
        """
        Access the workers

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        """
        return self._proxy.workers

    @property
    def workflows(self):
        """
        Access the workflows

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.WorkflowList
        """
        return self._proxy.workflows

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        """
        return self._proxy.statistics

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        """
        return self._proxy.real_time_statistics

    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        """
        return self._proxy.cumulative_statistics

    @property
    def task_channels(self):
        """
        Access the task_channels

        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        """
        return self._proxy.task_channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceInstance {}>'.format(context)
