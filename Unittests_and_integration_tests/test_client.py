#!/usr/bin/env python3
"""Unittests_and_integration_tests"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from requests.cookies import MockResponse
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient class """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ test_org """
        github_org_client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"fake_key": "fake_value"}
        response = github_org_client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, {"fake_key": "fake_value"})

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ test_public_repos_url """
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/some_org/repos'}
        client = GithubOrgClient("some_org")
        self.assertEqual(
            client._public_repos_url,
            'https://api.github.com/orgs/some_org/repos')

    @patch('client.get_json', return_value=[
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ])
    def test_public_repos(self, mock_get_json):
        """ test_public_repos """
        mock_payload = {"repos_url": "https://mocked_url.com"}
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = mock_payload["repos_url"]
            client = GithubOrgClient("dummy_thick_org")
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertListEqual(client.public_repos(), expected_repos)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_payload["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "my_license"}}, "other_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test_has_license """
        self.assertEqual(GithubOrgClient.has_license(repo,
                                                     license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith("/orgs/dummy_org"):
                return MockResponse(cls.org_payload)
            elif url.endswith("/orgs/dummy_org/repos"):
                return MockResponse(cls.repos_payload)
            else:
                return MockResponse({})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass """
        cls.get_patcher.stop()
