from nose2.compat import unittest
from nose2.tools import params
import re

class TestBasicReFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_match_something_at_the_beginning(self):
        # re.match only works at the beginning of string
        match = re.match(r"^abc", "abcdefabc")
        assert match.group(0) == "abc"
        assert match.start(0) == 0

        # So string in the middle doesn't work \n re.match(r'abc', 'xabc') = ",
        match = re.match(r'abc', 'xabc')
        assert match == None

    def test_002_search_for_one_match(self):
        match = re.search(r'(?:abc)adf', 'abcadfasdfadfabcasdfasdfabc')

        # Remember, group(0) is the entire match
        assert match.group(0) == "abcadf"
        assert match.start(0) == 0
        assert match.end(0) == 6

    def test_003_search_for_multiple_match(self):
        # Search for multiple matches using findall \n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc')"
        match = re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc')
        assert len(match) == 3

        # finditer is more useful for finding more information about the match
        match = re.finditer(r'abc', 'abcadfasdfadfabcasdfasdfabc')
        assert sum(1 for _ in match) == 3


    def test_004_print_debug_expression(self):
        # Debug expression by printing more informationsearch \n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.DEBUG)"
        match = re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.DEBUG)

    def test_005_match_ignorecase(self):
        # We can ignore case \n re.findall(r'abc', 'ABC', re.I)",
        match = re.findall(r'abc', 'ABC', re.I)

        assert len(match) == 1

    def test_006_match_multiline(self):
        multiline_text = """
        some Varying TEXT

        DSJFKDAFJKDAFJDSAKFJADSFLKDLAFKDSAF
        [more of the above, ending with a newline]
        [yep, there is a variable number of lines here]

        some Varying TEXT

        DSJFKDAFJKDAFJDSAKFJADSFLKDLAFKDSAF
        [more of the above, ending with a newline]
        [yep, there is a variable number of lines here]

        """
        regex = re.compile(r'^(.+)(?:\n|\r\n?)((?:(?:\n|\r\n?).+)+)', re.MULTILINE)
        match = regex.search(multiline_text)
        # We can search multiline \n re.compile(r'^(.+)(?:\\n|\\r\\n?)((?:(?:\\n|\\r\\n?).+)+) = ', re.MULTILINE)",
        assert match.groups() == ('        some Varying TEXT', '\n        DSJFKDAFJKDAFJDSAKFJADSFLKDLAFKDSAF\n        [more of the above, ending with a newline]\n        [yep, there is a variable number of lines here]')

    def test_007_match_dotall(self):
        # DOTALL can be used to match pattern on multiline\n re.compile('some\\s*fancy', re.DOTALL)",
        fancy_text = """
        <div>I'm some
               fancy text that needs
               to be found</div>
               """
        regex = re.compile('some\s*fancy', re.DOTALL)
        match = regex.search(fancy_text)
        assert match.group() == "some\n               fancy"

    def test_010_print_verbose_expression(self):
        # "Debug expression by printing more informationsearch\n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.VERBOSE)",
        re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.VERBOSE)

    def test_011_split_string(self):
        # Split string is easy\n re.split(r',', 'hello,the,world')",
        splitted_strings = re.split(r',', 'hello,the,world')
        assert splitted_strings == ['hello', 'the', 'world']

    def test_012_substitute(self):
        # Substitute string is easy\n re.sub(r'hello', 'hi', 'hello,the,world')",
        new_string = re.sub(r'hello', 'hi', 'hello,the,world')
        assert new_string == 'hi,the,world'

    def test_013_escape(self):
        # Regex can escape string\n",
        escaped_string = re.escape('A$^a|string-*.withmetacharacters')
        assert escaped_string == "A\$\^a\|string\-\*\.withmetacharacters"
