# -*- coding: utf-8 -*-

import whatthepatch as wtp


import unittest
from io import StringIO

class PatchTestSuite(unittest.TestCase):

    def test_default_diff(self):
        text = """0a1,6
> This is an important
> notice! It should
> therefore be located at
> the beginning of this
> document!
>
8,14c14
< compress the size of the
< changes.
<
< This paragraph contains
< text that is outdated.
< It will be deleted in the
< near future.
---
> compress anything.
17c17
< check this dokument. On
---
> check this document. On
24a25,28
>
> This paragraph contains
> important new additions
> to this document.
"""

        expected = [
                (None, 1, 'This is an important'),
                (None, 2, 'notice! It should'),
                (None, 3, 'therefore be located at'),
                (None, 4, 'the beginning of this'),
                (None, 5, 'document!'),
                (None, 6, ''),

                (8, None, 'compress the size of the'),
                (9, None, 'changes.'),
                (10, None, ''),
                (11, None, 'This paragraph contains'),
                (12, None, 'text that is outdated.'),
                (13, None, 'It will be deleted in the'),
                (14, None, 'near future.'),
                (None, 14, 'compress anything.'),

                (17, None, 'check this dokument. On'),
                (None, 17, 'check this document. On'),

                (None, 25, ''),
                (None, 26, 'This paragraph contains'),
                (None, 27, 'important new additions'),
                (None, 28, 'to this document.')
                ]

        results = [x for x in wtp.patch.parse_default_diff(text)]
        self.assertEquals(results, expected)

        expected_main = [wtp.patch.diffobj(header=None, changes=expected, text=text)]
        results_main = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results_main, expected_main)

    def test_svn_unified_patch(self):
        with open('tests/casefiles/svn-unified.patch') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/csc.py',
                        new_version=12784,
                        ),
                    changes=[
                        (None, 1, '# This is a basic script I wrote to run Bugxplore over the dataset'),
                        (None, 2, ''),
                        (None, 3, ''),
                        (1, 4, 'import os'),
                        (2, 5, 'import sys'),
                        (3, 6, 'import pickle'),
                        (5, 8, 'import copy'),
                        (6, 9, ''),
                        (7, 10, 'from datetime import date'),
                        (8, None, 'from Main import main'),
                        (9, None, 'from Main import _make_dir'),
                        (None, 11, 'from Bugxplore import main'),
                        (None, 12, 'from Bugxplore import _make_dir'),
                        (10, 13, ''),
                        (11, 14, 'storageDir = \'/tmp/csc/bugs/\''),
                        (12, 15, 'argv = []'),
                        ],
                    text = '\n'.join(lines[:22]) + '\n'
                   ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (46, 46, ''),
                        (47, 47, '    # Configure option parser'),
                        (48, 48, "    optparser = OptionParser(usage='%prog [options] DIFF_FILE', version='0.1')"),
                        (49, None, "    optparser.set_defaults(output_dir='/tmp/sctdiffs',project_name='default_project')"),
                        (None, 49, "    optparser.set_defaults(output_dir='/tmp/diffs')"),
                        (50, 50, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (51, 51, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (52, 52, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (53, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 53, ''),
                        (54, 54, '    # Invoke option parser'),
                        (55, 55, '    (options,args) = optparser.parse_args(argv)'),
                        (56, 56, ''),
                        ],
                    text = '\n'.join(lines[22:40]) + '\n'
                    ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (83, 83, ''),
                        (84, 84, '    # Configure option parser'),
                        (85, 85, "    optparser = OptionParser(usage='%prog [options] BUG_IDS', version='0.1')"),
                        (86, None, "    optparser.set_defaults(output_dir='/tmp/bugs',project_name='default_project')"),
                        (None, 86, "    optparser.set_defaults(output_dir='/tmp/bugs')"),
                        (87, 87, "    optparser.add_option('-u', '--bugzilla-url', dest='bugzilla_url', help='URL of Bugzilla installation root')"),
                        (88, 88, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (89, 89, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (90, 90, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (91, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 91, ''),
                        (92, 92, '    # Invoke option parser'),
                        (93, 93, '    (options,args) = optparser.parse_args(argv)'),
                        (94, 94, '    '),
                        ],
                    text = '\n'.join(lines[40:]) + '\n'
                    )
                    ]

        results = [x for x in wtp.parse_patch(text)]

        self.assertEquals(results, expected)

    def test_svn_context_patch(self):
        with open('tests/casefiles/svn-context.patch') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/csc.py',
                        new_version=12784,
                        ),
                    changes=[
                        (None, 1, '# This is a basic script I wrote to run Bugxplore over the dataset'),
                        (None, 2, ''),
                        (None, 3, ''),
                        (1, 4, 'import os'),
                        (2, 5, 'import sys'),
                        (3, 6, 'import pickle'),
                        (5, 8, 'import copy'),
                        (6, 9, ''),
                        (7, 10, 'from datetime import date'),
                        (8, None, 'from Main import main'),
                        (9, None, 'from Main import _make_dir'),
                        (None, 11, 'from Bugxplore import main'),
                        (None, 12, 'from Bugxplore import _make_dir'),
                        (10, 13, ''),
                        (11, 14, 'storageDir = \'/tmp/csc/bugs/\''),
                        (12, 15, 'argv = []'),
                        ],
                    text = '\n'.join(lines[:32]) + '\n'
                   ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (46, 46, ''),
                        (47, 47, '    # Configure option parser'),
                        (48, 48, "    optparser = OptionParser(usage='%prog [options] DIFF_FILE', version='0.1')"),
                        (49, None, "    optparser.set_defaults(output_dir='/tmp/sctdiffs',project_name='default_project')"),
                        (None, 49, "    optparser.set_defaults(output_dir='/tmp/diffs')"),
                        (50, 50, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (51, 51, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (52, 52, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (53, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 53, ''),
                        (54, 54, '    # Invoke option parser'),
                        (55, 55, '    (options,args) = optparser.parse_args(argv)'),
                        (56, 56, ''),
                        ],
                    text = '\n'.join(lines[32:61]) + '\n'
                    ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_version=12783,
                        new_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (83, 83, ''),
                        (84, 84, '    # Configure option parser'),
                        (85, 85, "    optparser = OptionParser(usage='%prog [options] BUG_IDS', version='0.1')"),
                        (86, None, "    optparser.set_defaults(output_dir='/tmp/bugs',project_name='default_project')"),
                        (None, 86, "    optparser.set_defaults(output_dir='/tmp/bugs')"),
                        (87, 87, "    optparser.add_option('-u', '--bugzilla-url', dest='bugzilla_url', help='URL of Bugzilla installation root')"),
                        (88, 88, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (89, 89, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (90, 90, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (91, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 91, ''),
                        (92, 92, '    # Invoke option parser'),
                        (93, 93, '    (options,args) = optparser.parse_args(argv)'),
                        (94, 94, '    '),
                        ],
                    text = '\n'.join(lines[61:]) + '\n'
                    )
                    ]

        results = [x for x in wtp.parse_patch(text)]

        self.assertEquals(results, expected)

    def test_svn_git_patch(self):
        with open('tests/casefiles/svn-git.patch') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_path='projects/bugs/bugtrace/trunk/src/bugtrace/csc.py',
                        old_version=12783,
                        new_path='projects/bugs/bugtrace/trunk/src/bugtrace/csc.py',
                        new_version=12784,
                        ),
                    changes=[
                        (None, 1, '# This is a basic script I wrote to run Bugxplore over the dataset'),
                        (None, 2, ''),
                        (None, 3, ''),
                        (1, 4, 'import os'),
                        (2, 5, 'import sys'),
                        (3, 6, 'import pickle'),
                        (5, 8, 'import copy'),
                        (6, 9, ''),
                        (7, 10, 'from datetime import date'),
                        (8, None, 'from Main import main'),
                        (9, None, 'from Main import _make_dir'),
                        (None, 11, 'from Bugxplore import main'),
                        (None, 12, 'from Bugxplore import _make_dir'),
                        (10, 13, ''),
                        (11, 14, 'storageDir = \'/tmp/csc/bugs/\''),
                        (12, 15, 'argv = []'),
                        ],
                    text = '\n'.join(lines[:23]) + '\n'
                   ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_path='projects/bugs/bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_version=12783,
                        new_path='projects/bugs/bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (46, 46, ''),
                        (47, 47, '    # Configure option parser'),
                        (48, 48, "    optparser = OptionParser(usage='%prog [options] DIFF_FILE', version='0.1')"),
                        (49, None, "    optparser.set_defaults(output_dir='/tmp/sctdiffs',project_name='default_project')"),
                        (None, 49, "    optparser.set_defaults(output_dir='/tmp/diffs')"),
                        (50, 50, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (51, 51, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (52, 52, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (53, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 53, ''),
                        (54, 54, '    # Invoke option parser'),
                        (55, 55, '    (options,args) = optparser.parse_args(argv)'),
                        (56, 56, ''),
                        ],
                    text = '\n'.join(lines[23:42]) + '\n'
                    ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_path='projects/bugs/bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_version=12783,
                        new_path='projects/bugs/bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        new_version=12784,
                        ),
                    changes=[
                        (83, 83, ''),
                        (84, 84, '    # Configure option parser'),
                        (85, 85, "    optparser = OptionParser(usage='%prog [options] BUG_IDS', version='0.1')"),
                        (86, None, "    optparser.set_defaults(output_dir='/tmp/bugs',project_name='default_project')"),
                        (None, 86, "    optparser.set_defaults(output_dir='/tmp/bugs')"),
                        (87, 87, "    optparser.add_option('-u', '--bugzilla-url', dest='bugzilla_url', help='URL of Bugzilla installation root')"),
                        (88, 88, "    optparser.add_option('-o', '--output-dir', dest='output_dir', help='Output directory')"),
                        (89, 89, "    optparser.add_option('-p', '--project_name', dest='project_name', help='Project name')"),
                        (90, 90, "    optparser.add_option('-d', '--delete_cvs_folder', dest='cvs_delete', help='Deletable CVS checkout folder')"),
                        (91, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 91, ''),
                        (92, 92, '    # Invoke option parser'),
                        (93, 93, '    (options,args) = optparser.parse_args(argv)'),
                        (94, 94, '    '),
                        ],
                    text = '\n'.join(lines[42:]) + '\n'
                    )
                    ]


        results = [x for x in wtp.parse_patch(text)]

        self.assertEquals(results, expected)

    def test_svn_rcs_patch(self):
        with open('tests/casefiles/svn-rcs.patch') as f:
            text = f.read()

        lines = text.splitlines()
        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/csc.py',
                        old_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/csc.py',
                        new_version=None,
                        ),
                    changes=[
                        (None, 1, '# This is a basic script I wrote to run Bugxplore over the dataset'),
                        (None, 2, ''),
                        (None, 3, ''),
                        (8, None, None),
                        (9, None, None),
                        (None, 11, 'from Bugxplore import main'),
                        (None, 12, 'from Bugxplore import _make_dir'),
                        ],
                    text = '\n'.join(lines[:10]) + '\n'
                   ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        new_version=None,
                        ),
                    changes=[
                        (49, None, None),
                        (None, 49, "    optparser.set_defaults(output_dir='/tmp/diffs')"),
                        (53, None, None),
                        (None, 53, ''),
                        ],
                    text = '\n'.join(lines[10:18]) + '\n'
                    ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        new_version=None,
                        ),
                    changes=[
                        (86, None, None),
                        (None, 86, "    optparser.set_defaults(output_dir='/tmp/bugs')"),
                        (91, None, None),
                        (None, 91, ''),
                        ],
                    text = '\n'.join(lines[18:]) + '\n'
                    )
                    ]

        results = [x for x in wtp.parse_patch(text)]
        self.assertEquals(results, expected)


    def test_svn_default_patch(self):
        with open('tests/casefiles/svn-default.patch') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/csc.py',
                        old_path='bugtrace/trunk/src/bugtrace/csc.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/csc.py',
                        new_version=None,
                        ),
                    changes=[
                        (None, 1, '# This is a basic script I wrote to run Bugxplore over the dataset'),
                        (None, 2, ''),
                        (None, 3, ''),
                        (8, None, 'from Main import main'),
                        (9, None, 'from Main import _make_dir'),
                        (None, 11, 'from Bugxplore import main'),
                        (None, 12, 'from Bugxplore import _make_dir'),
                        ],
                    text = '\n'.join(lines[:12]) + '\n'
                   ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/Diffxplore.py',
                        new_version=None,
                        ),
                    changes=[
                        (49, None, "    optparser.set_defaults(output_dir='/tmp/sctdiffs',project_name='default_project')"),
                        (None, 49, "    optparser.set_defaults(output_dir='/tmp/diffs')"),
                        (53, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 53, ''),
                        ],
                    text = '\n'.join(lines[12:22]) + '\n'
                    ),
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path = 'bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        old_version=None,
                        new_path='bugtrace/trunk/src/bugtrace/Bugxplore.py',
                        new_version=None,
                        ),
                    changes=[
                        (86, None, "    optparser.set_defaults(output_dir='/tmp/bugs',project_name='default_project')"),
                        (None, 86, "    optparser.set_defaults(output_dir='/tmp/bugs')"),
                        (91, None, "    optparser.add_option('-a', '--append', action='store_true', dest='app', default=False, help='Append to existing MethTerms2 document')"),
                        (None, 91, ''),
                        ],
                    text = '\n'.join(lines[22:]) + '\n'
                    )
                    ]
        results = [x for x in wtp.parse_patch(text)]
        self.assertEquals(results, expected)


    def test_git_patch(self):
        with open('tests/casefiles/git.patch') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path=None,
                        old_path='novel/src/java/edu/ua/eng/software/novel/NovelFrame.java',
                        old_version='aae63fe',
                        new_path='novel/src/java/edu/ua/eng/software/novel/NovelFrame.java',
                        new_version='5abbc99'
                        ),
                    changes=[
                        (135, 135, '    public void actionPerformed(ActionEvent e) {'),
                        (136, 136, ''),
                        (137, 137, '        if (e.getActionCommand().equals("OPEN")) {'),
                        (138, None, '            prefsDialog(prefs.getImportPane());'),
                        (None, 138, '            prefs.selectImportPane();'),
                        (None, 139, '            prefsDialog();'),
                        (139, 140, '        } else if (e.getActionCommand().equals("SET")) {'),
                        (140, None, '            prefsDialog(prefs.getRepoPane());'),
                        (None, 141, '            prefs.selectRepoPane();'),
                        (None, 142, '            prefsDialog();'),
                        (141, 143, '        } else if (e.getActionCommand().equals("PREFS"))'),
                        (142, 144, '            prefsDialog();'),
                        (143, 145, '        else if (e.getActionCommand().equals("EXIT"))'),
                        (158, 160, '     * Create dialog to handle user preferences'),
                        (159, 161, '     */'),
                        (160, 162, '    public void prefsDialog() {'),
                        (161, None, ''),
                        (162, 163, '        prefs.setVisible(true);'),
                        (163, 164, '    }'),
                        (164, 165, ''),
                        (165, None, '    public void prefsDialog(Component c) {'),
                        (166, None, '        prefs.setSelectedComponent(c);'),
                        (167, None, '        prefsDialog();'),
                        (168, None, '    }'),
                        (169, None, ''),
                        (170, 166, '    /**'),
                        (171, 167, '     * Open software tutorials, most likely to be hosted online'),
                        (172, 168, '     * ')],
                    text = '\n'.join(lines[:34]) + '\n'
                    ),
                    wtp.patch.diffobj(
                        header=wtp.patch.header(
                            index_path=None,
                            old_path='novel/src/java/edu/ua/eng/software/novel/NovelPrefPane.java',
                            old_version='a63b57e',
                            new_path='novel/src/java/edu/ua/eng/software/novel/NovelPrefPane.java',
                            new_version='919f413'
                            ),
                        changes=[
                            (18, 18, ''),
                            (19, 19, '    public abstract void apply();'),
                            (20, 20, ''),
                            (None, 21, '    public abstract void applyPrefs();'),
                            (None, 22, ''),
                            (21, 23, '    public abstract boolean isChanged();'),
                            (22, 24, ''),
                            (23, 25, '    protected Preferences prefs;')],
                        text = '\n'.join(lines[34:]) + '\n'
                        )
                    ]

        results = [x for x in wtp.parse_patch(text)]

        self.assertEquals(results, expected)


    def test_git_header(self):
        text = """
diff --git a/bugtrace/patch.py b/bugtrace/patch.py
index 8910dfd..456e34f 100644
--- a/bugtrace/patch.py
+++ b/bugtrace/patch.py
@@ -8,20 +8,30 @@
"""
        expected = wtp.patch.header(
                index_path = None,
                old_path = 'bugtrace/patch.py',
                old_version = '8910dfd',
                new_path = 'bugtrace/patch.py',
                new_version = '456e34f')

        results = wtp.patch.parse_git_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)

    def test_svn_header(self):
        text = """
Index: bugtrace/trunk/src/bugtrace/csc.py
===================================================================
--- bugtrace/trunk/src/bugtrace/csc.py	(revision 12783)
+++ bugtrace/trunk/src/bugtrace/csc.py	(revision 12784)
@@ -1,3 +1,6 @@
"""
        expected = wtp.patch.header(
                index_path = 'bugtrace/trunk/src/bugtrace/csc.py',
                old_path = 'bugtrace/trunk/src/bugtrace/csc.py',
                old_version = 12783,
                new_path = 'bugtrace/trunk/src/bugtrace/csc.py',
                new_version = 12784)
        results = wtp.patch.parse_svn_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)

    def test_cvs_header(self):
        text = """Index: org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java
===================================================================
RCS file: /cvsroot/eclipse/org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java,v
retrieving revision 1.6.4.1
retrieving revision 1.8
diff -u -r1.6.4.1 -r1.8
--- org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java	23 Jul 2001 17:51:45 -0000	1.6.4.1
+++ org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java	17 May 2002 20:27:56 -0000	1.8
@@ -1 +1 @@
"""
        expected = wtp.patch.header(
                index_path = 'org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java',
                old_path = 'org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java',
                old_version = '1.6.4.1',
                new_path = 'org.eclipse.core.resources/src/org/eclipse/core/internal/localstore/SafeChunkyInputStream.java',
                new_version = '1.8')
        results = wtp.patch.parse_cvs_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)

    def test_unified_header(self):
        text = """--- /tmp/o	2012-12-22 06:43:35.000000000 -0600
+++ /tmp/n	2012-12-23 20:40:50.000000000 -0600
@@ -1,3 +1,9 @@"""

        expected = wtp.patch.header(
                index_path = None,
                old_path = '/tmp/o',
                old_version = '2012-12-22 06:43:35.000000000 -0600',
                new_path = '/tmp/n',
                new_version = '2012-12-23 20:40:50.000000000 -0600')

        results = wtp.patch.parse_unified_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)

    def test_unified_header_notab(self):
        text = """--- /tmp/some file    2012-12-22 06:43:35.000000000 -0600
+++ /tmp/n	2012-12-23 20:40:50.000000000 -0600
@@ -1,3 +1,9 @@"""

        expected = wtp.patch.header(
                index_path = None,
                old_path = '/tmp/some file',
                old_version = '2012-12-22 06:43:35.000000000 -0600',
                new_path = '/tmp/n',
                new_version = '2012-12-23 20:40:50.000000000 -0600')

        results = wtp.patch.parse_unified_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)


    def test_unified_diff(self):
        text = """@@ -1,3 +1,9 @@
+This is an important
+notice! It should
+therefore be located at
+the beginning of this
+document!
+
 This part of the
 document has stayed the
 same from version to
@@ -5,16 +11,10 @@
 be shown if it doesn't
 change.  Otherwise, that
 would not be helping to
-compress the size of the
-changes.
-
-This paragraph contains
-text that is outdated.
-It will be deleted in the
-near future.
+compress anything.

 It is important to spell
-check this dokument. On
+check this document. On
 the other hand, a
 misspelled word isn't
 the end of the world.
@@ -22,3 +22,7 @@
 this paragraph needs to
 be changed. Things can
 be added after it.
+
+This paragraph contains
+important new additions
+to this document.
"""

        expected = [
                (None, 1, 'This is an important'),
                (None, 2, 'notice! It should'),
                (None, 3, 'therefore be located at'),
                (None, 4, 'the beginning of this'),
                (None, 5, 'document!'),
                (None, 6, ''),
                (1, 7, 'This part of the'),
                (2, 8, 'document has stayed the'),
                (3, 9, 'same from version to'),

                (5, 11, 'be shown if it doesn\'t'),
                (6, 12, 'change.  Otherwise, that'),
                (7, 13, 'would not be helping to'),
                (8, None, 'compress the size of the'),
                (9, None, 'changes.'),
                (10, None, ''),
                (11, None, 'This paragraph contains'),
                (12, None, 'text that is outdated.'),
                (13, None, 'It will be deleted in the'),
                (14, None, 'near future.'),
                (None, 14, 'compress anything.'),
                (15, 15, ''),
                (16, 16, 'It is important to spell'),
                (17, None, 'check this dokument. On'),
                (None, 17, 'check this document. On'),
                (18, 18, 'the other hand, a'),
                (19, 19, 'misspelled word isn\'t'),
                (20, 20, 'the end of the world.'),

                (22, 22, 'this paragraph needs to'),
                (23, 23, 'be changed. Things can'),
                (24, 24, 'be added after it.'),
                (None, 25, ''),
                (None, 26, 'This paragraph contains'),
                (None, 27, 'important new additions'),
                (None, 28, 'to this document.')
                ]

        results = [x for x in wtp.patch.parse_unified_diff(text)]
        self.assertEquals(results, expected)

        expected_main = [wtp.patch.diffobj(header=None, changes=expected, text=text)]
        results_main = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results_main, expected_main)

    def test_diff_unified_blah(self):
        with open('tests/casefiles/diff-unified-blah.diff') as f:
            text = f.read()


        expected = [
            wtp.patch.diffobj(
                header=wtp.patch.header(
                    index_path=None,
                    old_path='lao',
                    old_version='2013-01-05 16:56:19.000000000 -0600',
                    new_path='tzu',
                    new_version='2013-01-05 16:56:35.000000000 -0600'
                    ),
                changes=[
                    (1, None, 'The Way that can be told of is not the eternal Way;'),
                    (2, None, 'The name that can be named is not the eternal name.'),
                    (3, 1, 'The Nameless is the origin of Heaven and Earth;'),
                    (4, None, 'The Named is the mother of all things.'),
                    (None, 2, 'The named is the mother of all things.'),
                    (None, 3, ''),
                    (5, 4, 'Therefore let there always be non-being,'),
                    (6, 5, '  so we may see their subtlety,'),
                    (7, 6, 'And let there always be being,'),
                    (9, 8, 'The two are the same,'),
                    (10, 9, 'But after they are produced,'),
                    (11, 10, '  they have different names.'),
                    (None, 11, 'They both may be called deep and profound.'),
                    (None, 12, 'Deeper and more profound,'),
                    (None, 13, 'The door of all subtleties!')],
                text=text)
                ]


        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_diff_context_blah(self):
        with open('tests/casefiles/diff-context-blah.diff') as f:
            text = f.read()


        expected = [
            wtp.patch.diffobj(
                header=wtp.patch.header(
                    index_path=None,
                    old_path='lao',
                    old_version='2013-01-05 16:56:19.000000000 -0600',
                    new_path='tzu',
                    new_version='2013-01-05 16:56:35.000000000 -0600'
                    ),
                changes=[
                    (1, None, 'The Way that can be told of is not the eternal Way;'),
                    (2, None, 'The name that can be named is not the eternal name.'),
                    (3, 1, 'The Nameless is the origin of Heaven and Earth;'),
                    (4, None, 'The Named is the mother of all things.'),
                    (None, 2, 'The named is the mother of all things.'),
                    (None, 3, ''),
                    (5, 4, 'Therefore let there always be non-being,'),
                    (6, 5, '  so we may see their subtlety,'),
                    (7, 6, 'And let there always be being,'),
                    (9, 8, 'The two are the same,'),
                    (10, 9, 'But after they are produced,'),
                    (11, 10, '  they have different names.'),
                    (None, 11, 'They both may be called deep and profound.'),
                    (None, 12, 'Deeper and more profound,'),
                    (None, 13, 'The door of all subtleties!')],
                text=text)
                ]


        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_diff_default_blah(self):
        with open('tests/casefiles/diff-default-blah.diff') as f:
            text = f.read()


        expected = [
            wtp.patch.diffobj(
                header=None,
                changes=[
                    (1, None, 'The Way that can be told of is not the eternal Way;'),
                    (2, None, 'The name that can be named is not the eternal name.'),
                    (3, 1, 'The Nameless is the origin of Heaven and Earth;'),
                    (4, None, 'The Named is the mother of all things.'),
                    (None, 2, 'The named is the mother of all things.'),
                    (None, 3, ''),
                    (5, 4, 'Therefore let there always be non-being,'),
                    (6, 5, '  so we may see their subtlety,'),
                    (7, 6, 'And let there always be being,'),
                    (9, 8, 'The two are the same,'),
                    (10, 9, 'But after they are produced,'),
                    (11, 10, '  they have different names.'),
                    (None, 11, 'They both may be called deep and profound.'),
                    (None, 12, 'Deeper and more profound,'),
                    (None, 13, 'The door of all subtleties!')],
                text=text)
                ]


        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)


    def test_context_header(self):
        text = """*** /tmp/o	2012-12-22 06:43:35.000000000 -0600
--- /tmp/n	2012-12-23 20:40:50.000000000 -0600
***************"""

        expected = wtp.patch.header(
                index_path = None,
                old_path = '/tmp/o',
                old_version = '2012-12-22 06:43:35.000000000 -0600',
                new_path = '/tmp/n',
                new_version = '2012-12-23 20:40:50.000000000 -0600')

        results = wtp.patch.parse_context_header(text)
        self.assertEquals(results, expected)

        results_main = wtp.patch.parse_header(text)
        self.assertEquals(results_main, expected)


    def test_context_diff(self):
        text = """***************
*** 1,3 ****
--- 1,9 ----
+ This is an important
+ notice! It should
+ therefore be located at
+ the beginning of this
+ document!
+
  This part of the
  document has stayed the
  same from version to
***************
*** 5,20 ****
  be shown if it doesn't
  change.  Otherwise, that
  would not be helping to
! compress the size of the
! changes.
!
! This paragraph contains
! text that is outdated.
! It will be deleted in the
! near future.

  It is important to spell
! check this dokument. On
  the other hand, a
  misspelled word isn't
  the end of the world.
--- 11,20 ----
  be shown if it doesn't
  change.  Otherwise, that
  would not be helping to
! compress anything.

  It is important to spell
! check this document. On
  the other hand, a
  misspelled word isn't
  the end of the world.
***************
*** 22,24 ****
--- 22,28 ----
  this paragraph needs to
  be changed. Things can
  be added after it.
+
+ This paragraph contains
+ important new additions
+ to this document.
"""

        expected = [
                (None, 1, 'This is an important'),
                (None, 2, 'notice! It should'),
                (None, 3, 'therefore be located at'),
                (None, 4, 'the beginning of this'),
                (None, 5, 'document!'),
                (None, 6, ''),
                (1, 7, 'This part of the'),
                (2, 8, 'document has stayed the'),
                (3, 9, 'same from version to'),

                # merge the two sections of the hunk so that deletions
                # are followed by the appropriate insertion
                # follow up: that was a horrible idea.
                (5, 11, 'be shown if it doesn\'t'),
                (6, 12, 'change.  Otherwise, that'),
                (7, 13, 'would not be helping to'),
                (8, None, 'compress the size of the'),
                (9, None, 'changes.'),
                (10, None, ''),
                (11, None, 'This paragraph contains'),
                (12, None, 'text that is outdated.'),
                (13, None, 'It will be deleted in the'),
                (14, None, 'near future.'),
                (None, 14, 'compress anything.'),
                (15, 15, ''),
                (16, 16, 'It is important to spell'),
                (17, None, 'check this dokument. On'),
                (None, 17, 'check this document. On'),
                (18, 18, 'the other hand, a'),
                (19, 19, 'misspelled word isn\'t'),
                (20, 20, 'the end of the world.'),

                (22, 22, 'this paragraph needs to'),
                (23, 23, 'be changed. Things can'),
                (24, 24, 'be added after it.'),
                (None, 25, ''),
                (None, 26, 'This paragraph contains'),
                (None, 27, 'important new additions'),
                (None, 28, 'to this document.')
                ]

        results = [x for x in wtp.patch.parse_context_diff(text)]
        self.assertEquals(results, expected)

        expected_main = [wtp.patch.diffobj(header=None, changes=expected, text=text)]
        results_main = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results_main, expected_main)

    def test_ed_diff(self):
        text = """24a

This paragraph contains
important new additions
to this document.
.
17c
check this document. On
.
8,14c
compress anything.
.
0a
This is an important
notice! It should
therefore be located at
the beginning of this
document!

.
"""
        expected = [
                (None, 1, 'This is an important'),
                (None, 2, 'notice! It should'),
                (None, 3, 'therefore be located at'),
                (None, 4, 'the beginning of this'),
                (None, 5, 'document!'),
                (None, 6, ''),

                (8, None, None),
                (9, None, None),
                (10, None, None),
                (11, None, None),
                (12, None, None),
                (13, None, None),
                (14, None, None),

                (None, 14, 'compress anything.'),

                (17, None, None),

                (None, 17, 'check this document. On'),

                (None, 25, ''),
                (None, 26, 'This paragraph contains'),
                (None, 27, 'important new additions'),
                (None, 28, 'to this document.')
                ]

        results = [x for x in wtp.patch.parse_ed_diff(text)]
        self.assertEquals(results, expected)

        expected_main = [wtp.patch.diffobj(header=None, changes=expected, text=text)]
        results_main = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results_main, expected_main)

    def test_rcs_ed_diff(self):
        text="""a0 6
This is an important
notice! It should
therefore be located at
the beginning of this
document!

d8 7
a14 1
compress anything.
d17 1
a17 1
check this document. On
a24 4

This paragraph contains
important new additions
to this document.
"""

        expected = [
                (None, 1, 'This is an important'),
                (None, 2, 'notice! It should'),
                (None, 3, 'therefore be located at'),
                (None, 4, 'the beginning of this'),
                (None, 5, 'document!'),
                (None, 6, ''),

                (8, None, None),
                (9, None, None),
                (10, None, None),
                (11, None, None),
                (12, None, None),
                (13, None, None),
                (14, None, None),

                (None, 14, 'compress anything.'),

                (17, None, None),

                (None, 17, 'check this document. On'),

                (None, 25, ''),
                (None, 26, 'This paragraph contains'),
                (None, 27, 'important new additions'),
                (None, 28, 'to this document.')
                ]

        results = [x for x in wtp.patch.parse_rcs_ed_diff(text)]
        self.assertEquals(results, expected)

        expected_main = [wtp.patch.diffobj(header=None, changes=expected, text=text)]
        results_main = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results_main, expected_main)

    def test_embedded_diff_in_comment(self):
        with open('tests/casefiles/embedded-diff.comment') as f:
            text = f.read()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path=None,
                        old_path='src/org/mozilla/javascript/IRFactory.java',
                        old_version=None,
                        new_path='src/org/mozilla/javascript/IRFactory.java',
                        new_version=None,
                        ),
                    changes=[
                        (2182, 2182, '          case Token.GETELEM:'),
                        (2183, 2183, '              decompileElementGet((ElementGet) node);'),
                        (2184, 2184, '              break;'),
                        (None, 2185, '          case Token.THIS:'),
                        (None, 2186, '              decompiler.addToken(node.getType());'),
                        (None, 2187, '              break;'),
                        (2185, 2188, '          default:'),
                        (2186, 2189, '              Kit.codeBug("unexpected token: "'),
                        (2187, 2190, '                          + Token.typeToName(node.getType()));'),
                        ],
                    text=text
                   ),
                ]

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_mozilla_527452_5_comment(self):
        with open('tests/casefiles/mozilla-527452-5.comment') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='js_instrumentation_proxy/src/org/mozilla/javascript/ast/StringLiteral.java',
                        old_path='js_instrumentation_proxy/src/org/mozilla/javascript/ast/StringLiteral.java',
                        old_version=5547,
                        new_path='js_instrumentation_proxy/src/org/mozilla/javascript/ast/StringLiteral.java',
                        new_version=None,
                        ),
                    changes=[
                        (112, 112, '        // TODO(stevey):  make sure this unescapes everything properly'),
                        (113, 113, '        String q = String.valueOf(getQuoteCharacter());'),
                        (114, 114, '        String rep = "\\\\\\\\" + q;'), # escape the escape that's escaping an escape. wut
                        (115, None, '        String s = value.replaceAll(q, rep);'),
                        (None, 115, '        String s = value.replace("\\\\", "\\\\\\\\");'),
                        (None, 116, '        s = s.replaceAll(q, rep);'),
                        (116, 117, '        s = s.replaceAll("\\n", "\\\\\\\\n");'),
                        (117, 118, '        s = s.replaceAll("\\r", "\\\\\\\\r");'),
                        (118, 119, '        s = s.replaceAll("\\t", "\\\\\\\\t");')
                        ],
                    text = '\n'.join(lines[2:]) + '\n'
                   ),
                ]

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_dos_unified_cvs(self):
        with open('tests/casefiles/mozilla-560291.diff') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
            wtp.patch.diffobj(
                header=wtp.patch.header(
                    index_path='src/org/mozilla/javascript/ast/ArrayComprehensionLoop.java',
                    old_path='src/org/mozilla/javascript/ast/ArrayComprehensionLoop.java',
                    old_version='1.1',
                    new_path='src/org/mozilla/javascript/ast/ArrayComprehensionLoop.java',
                    new_version='15 Sep 2011 02:26:05 -0000'
                ),
                changes=[
                    (79, 79, '    @Override'),
                    (80, 80, '    public String toSource(int depth) {'),
                    (81, 81, '        return makeIndent(depth)'),
                    (82, None, '                + " for ("'),
                    (None, 82, '                + " for " '),
                    (None, 83, '                + (isForEach()?"each ":"")'),
                    (None, 84, '                + "("'),
                    (83, 85, '                + iterator.toSource(0)'),
                    (84, 86, '                + " in "'),
                    (85, 87, '                + iteratedObject.toSource(0)')
                ],
                text = '\n'.join(lines[2:]) + '\n'
            )
        ]

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)


    def test_old_style_cvs(self):
        with open('tests/casefiles/mozilla-252983.diff') as f:
            text = f.read()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path='mozilla/js/rhino/CHANGELOG',
                        old_path='mozilla/js/rhino/CHANGELOG',
                        old_version='1.1.1.1',
                        new_path='mozilla/js/rhino/CHANGELOG',
                        new_version='1.1', # or 'Thu Jan 25 10:59:02 2007'
                        ),
                    changes=[
                        (1, None, 'This file version: $Id: CHANGELOG,v 1.1.1.1 2007/01/25 15:59:02 inonit Exp $'),
                        (None, 1, 'This file version: $Id: CHANGELOG,v 1.1 2007/01/25 15:59:02 inonit Exp $'),
                        (2, 2, ''),
                        (3, 3, 'Changes since Rhino 1.6R5'),
                        (4, 4, '========================='),
                        ],
                    text=text
                   ),
                ]

        results = wtp.patch.parse_cvs_header(text)
        self.assertEquals(results, expected[0].header)

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_apache_attachment_2241(self):
        with open('tests/casefiles/apache-attachment-2241.diff') as f:
            text = f.read()

        lines = text.splitlines()

        expected = [
                wtp.patch.diffobj(
                    header=wtp.patch.header(
                        index_path=None,
                        old_path='src\\main\\org\\apache\\tools\\ant\\taskdefs\\optional\\pvcs\\Pvcs.orig',
                        old_version='Sat Jun 22 16:11:58 2002',
                        new_path='src\\main\\org\\apache\\tools\\ant\\taskdefs\\optional\\pvcs\\Pvcs.java',
                        new_version='Fri Jun 28 10:55:50 2002'
                        ),
                    changes=[
                        (91, 91, ' *'),
                        (92, 92, ' * @author <a href="mailto:tchristensen@nordija.com">Thomas Christensen</a>'),
                        (93, 93, ' * @author <a href="mailto:donj@apogeenet.com">Don Jeffery</a>'),
                        (94, None, ' * @author <a href="snewton@standard.com">Steven E. Newton</a>'),
                        (None, 94, ' * @author <a href="mailto:snewton@standard.com">Steven E. Newton</a>'),
                        (95, 95, ' */'),
                        (96, 96, 'public class Pvcs extends org.apache.tools.ant.Task {'),
                        (97, 97, '    private String pvcsbin;')
                        ],
                    text= '\n'.join(lines) + '\n'
                   ),
                ]

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results, expected)

    def test_space_in_path_header(self):
        with open('tests/casefiles/eclipse-attachment-126343.header') as f:
            text = f.read()

        expected = wtp.patch.header(
                index_path = 'test plugin/org/eclipse/jdt/debug/testplugin/ResumeBreakpointListener.java',
                old_path = '/dev/null',
                old_version = '1 Jan 1970 00:00:00 -0000',
                new_path = 'test plugin/org/eclipse/jdt/debug/testplugin/ResumeBreakpointListener.java',
                new_version = '1 Jan 1970 00:00:00 -0000'
                )

        results = wtp.patch.parse_header(text)
        self.assertEquals(results, expected)

    def test_svn_mixed_line_ends(self):
        with open('tests/casefiles/svn-mixed_line_ends.patch') as f:
            text = f.read()

        expected_header = wtp.patch.header(
                index_path='java/org/apache/catalina/loader/WebappClassLoader.java',
                old_path='java/org/apache/catalina/loader/WebappClassLoader.java',
                old_version=1346371,
                new_path='java/org/apache/catalina/loader/WebappClassLoader.java',
                new_version=None)

        results = [x for x in wtp.patch.parse_patch(text)]
        self.assertEquals(results[0].header, expected_header)



if __name__ == '__main__':
    unittest.main()
