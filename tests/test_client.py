#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import logging
import unittest
import hostmydocs
import os


class TestClient(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logging.disable(logging.CRITICAL)
        self.doc_zip_archive = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/sampleDoc.zip")
        self.hmd_client = hostmydocs.Client(hostmydocs.ServerConfig(
            address="127.0.0.1",
            port=8080,
            use_tls=False,
            api_login="login",
            api_password="password"
        ))

    def test_upload_documentation_not_existing_server(self):

        server_config = hostmydocs.ServerConfig(
            address="someNotExistingBadServer.com",
            api_login="",
            api_password=""
        )

        doc = hostmydocs.Documentation(
            name="HostMyDocs-python-client",
            version="1.2.3.4",
            language="Python",
            zip_archive_path=self.doc_zip_archive
        )

        client = hostmydocs.Client(server_config)
        self.assertFalse(client.upload_documentation(doc))

    def test_upload_documentation_not_existing_zip_archive(self):

        doc = hostmydocs.Documentation(
            name="HostMyDocs-python-client",
            version="1.2.3.4",
            language="Python",
            zip_archive_path="notExist.zip"
        )

        self.assertFalse(self.hmd_client.upload_documentation(doc))

    def test_upload_documentation(self):

        doc = hostmydocs.Documentation(
            name="HostMyDocs-python-client",
            version="1.2.3.4",
            language="Python",
            zip_archive_path=self.doc_zip_archive
        )

        self.assertTrue(self.hmd_client.upload_documentation(doc))

    def test_get_all_documentations_not_existing_server(self):

        server_config = hostmydocs.ServerConfig(
            address="someNotExistingBadServer.com",
            api_login="",
            api_password=""
        )
        client = hostmydocs.Client(server_config)
        self.assertIsNone(client.get_all_documentations())

    def test_get_all_documentations(self):

        doc = hostmydocs.Documentation(
            name="HostMyDocs-python-client",
            version="9.8.7.6",
            language="Python",
            zip_archive_path=self.doc_zip_archive
        )

        self.assertTrue(self.hmd_client.upload_documentation(doc))

        list_of_documentations = self.hmd_client.get_all_documentations()
        self.assertIsNotNone(list_of_documentations)
        self.assertGreaterEqual(len(list_of_documentations), 1)

        doc_expected = hostmydocs.Documentation(
            name="HostMyDocs-python-client",
            version="9.8.7.6",
            language="Python"
        )
        self.assertIn(doc_expected, list_of_documentations)


