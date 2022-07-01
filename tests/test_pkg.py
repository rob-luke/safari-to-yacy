from safari_to_yacy.main import generate_search_string, get_safari_url, Settings
from unittest import mock
import os


class TestSearchString:

    def test_simple(self):
        """Ensure minimum required strings are returned."""
        ss = generate_search_string("https://search.yacy", "https://random.site")
        assert "https://search.yacy" in ss
        assert "https://random.site" in ss
        assert "crawlingMode" in ss
        assert "crawlingDepth" in ss
        assert "crawlingstart" in ss
        assert "\n" not in ss


class mocked_stdout:
    http = [b"https://www.robertsmagic.site"]

    def readlines(self):
        return self.http

class mocked_Popen:
    stdout = mocked_stdout()


class TestSafari:

    @mock.patch("subprocess.Popen")
    def test_simple(self, mock_safari_call):
        """Ensure correct strings are returned."""
        process_mock = mock.Mock()
        attrs = {"communicate.return_value": ("output", "error")}
        process_mock.configure_mock(**attrs)

        mock_safari_call.return_value = mocked_Popen
        ss = get_safari_url()
        assert ss == "https://www.robertsmagic.site"


class TestSettings:

    @mock.patch.dict(os.environ, {"verbose": "False",
                                  "yacy_url": "https://test.com"})
    def test_simple(self):
        s = Settings()
        assert s.verbose is False
        assert s.yacy_url in "https://test.com"