#Builtins
import textwrap, re

#Third party
from pygments import highlight
from pygments.formatters import TerminalTrueColorFormatter
from pygments.lexers import get_lexer_by_name

def print_with_highlight(text):
	lexer = get_lexer_by_name('markdown')
	print(highlight(text, lexer, TerminalTrueColorFormatter(style='fruity')).rstrip())
