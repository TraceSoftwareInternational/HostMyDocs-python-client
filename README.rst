HostMyDocs-python-client
=========================

|License| |travis|

This library provide a python client for `HostMyDocs`_ documentation hosting system

Example
-------

.. code:: python

    import hostmydocs

    # 1. Create client object connect to your HostMyDocs instance
    hmd_client = hostmydocs.Client(hostmydocs.ServerConfig(
            address="my-hostmydocs-instance.com",
            api_login="my_login",
            api_password="my_password"
        ))

    # 2. Upload your documentation
    my_documentation = hostmydocs.Documentation(
            name="myDocName",
            version="1.2.3.4",
            language="myLanguage",
            zip_archive_path="path/to/my/doc/archive.zip"
        )

    hmd_client.upload_documentation(my_documentation)

    # 3. List all documentations on your server
    for doc in hmd_client.get_all_documentations():
        print(doc.name)


.. _HostMyDocs: https://github.com/TraceSoftwareInternational/HostMyDocs

.. |License| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/gpl-3.0

.. |travis| image:: https://travis-ci.org/TraceSoftwareInternational/HostMyDocs-python-client.svg?branch=master
    :target: https://travis-ci.org/TraceSoftwareInternational/HostMyDocs-python-client
