# REGULAR EXPRESSION (REGEXP)

Regular expression are just characters matching or the process of creating matching patterns to match a specific sequence of characters (which are also known as strings).

Regexp is mostly used for finding or replacing texts in different system like linux command line, Perl, Ruby and other language.

Regex flavour is a way of saying that the regex syntax in one programming language or regex engine is different from another. This makes a lot of sense as Regex has different engines in different languages such that the regex syntax in Python is totally different from Javascript as well as Ruby.

When learning the all powerful RegEx its important to learn it based on the language youre working with.

>>example of linux Regex Flavor
`$ ls *`

In regular expressions, most patterns uses the ASCII, which involves some special characters, digits and symbols.

Regexp also involves some metacharacter for pattern matching and for numbers `\d` is used to represent characters from 0-9.

The backward slash distinguish it from the d character and its used to indicate that this is a `metacharacter`.

## Definitions
1. *Literal Character:* A literal character is the most basic regular expression you can use. It simply matches the actual character you write. So if you are trying to represent an “r,” you would write r. 
Metacharacter: Metacharacters signify to the regex engine that the following character has a special meaning. You typically include a \  in front of the metacharacter and they can do things like signify the beginning of a line, end of a line, or to match any single character. 

2. *Character Class:* A character class (or character set) tells the engine to look for one of a list of characters. It is signified by [ and ] with the characters you are looking for in the middle of the brackets. 
Capture Group: A capture group is signified by opening and closing, round parenthesis. They allow you to group regexes together to apply other regex features like quantifiers (see below) to the group.

3. *Metacharacter:* Metacharacters signify to the regex engine that the following character has a special meaning. You typically include a \  in front of the metacharacter and they can do things like signify the beginning of a line, end of a line, or to match any single character.

4. *Capture Group:* A capture group is signified by opening and closing, round parenthesis. They allow you to group regexes together to apply other regex features like quantifiers (see below) to the group. 

## Regular Expression Metacharacters

Metacharacters are reserved symbols used to assist in matching of characters.

Basic metacharacters used in several language or command line i.e LINUX are as follows:

`\n . [] * ^ [^] $`

Regexp also in involves the use of wildcards and one the wildcard is .[dot] metacharacter.

This is used to match any single character from letters, whitespace, digits, everything.

To ensure that you want to look for characters with the .[dot] use the `\.` to match only period.

The .[dot] is sometimes too powerful when it comes to matching characters and we can then use square brackets to match characters that we only need/seem want to match

>>example

Task	Text	 
Match	can
Match	man
Match	fan
Skip	dan
Skip	ran	
Skip	pan

`[fmc]an`

The code above would match charatcers that starts with either *f, m or c* and ends with *an*.

### More characters and meaning
`*` => matches all characters
`\*` => match only asterisk characters
`{} `=> specifies the range or amount of occurence
`.` => matches all character excluding space
`\.` => matches only .[dot] character
`[abc]` => specifies either a, b or c characters
`[123]` => specifies either 1, 2 or 3 numbers
`[0-9]` => searches from 0-9
`[a-z]` => searches from a-z (case sensitive)
`+ `=> 1 or more
`^  or \A` => match start of line
`$ or \Z` => match end of line
`\b` => matches character at the start of a word eg \b*bee*\b == *bee*s
`\B` => matches character at the middle of non special characters eg \b*ee*\b == b*ee*s
`\w` => match word characters
`\W` => match non word characters
`\s` => matches white spaces
`\S` => matches non white-spaces

*Please see all on the cheatsheet for regexes, link is below*

## Importance of REGEXES

Regexes can be used for so many thing but heres a quick look of what it can help you do;

1. Checking for emails within a long wall of strings
2. Checking for urls in a file
3. Finding and replacing texts
4. Finding dates in a long wall of list


### Important Links
Below are links to help you get started on some flavors of *regular expression*;

1. [Regular Expression, everythin you need to know with practice](https://regexone.com/lesson/introduction_abcs)!
2. [Regular Expression Cheatsheet](https://images.datacamp.com/image/upload/v1665049611/Marketing/Blog/Regular_Expressions_Cheat_Sheet.pdf)
3. [RegEx Youtube](https://youtu.be/sa-TUpSx1JA?si=CBrLLjKuYKTcf-al)