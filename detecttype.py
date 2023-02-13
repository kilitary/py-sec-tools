import filetype
import sys
import magic
from var_dump import var_dump
import yara
import magic

def main():
    yara.set_config(stack_size=65536)
    yara.set_config(max_strings_per_rule=20000)
    yara.set_config(max_match_data=128)
    
    rules = yara.compile('yara.rules')
    
    kind = filetype.guess(sys.argv[1])
    if kind is None:
        print('Cannot guess file type!')
        return
    
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)
    
    print(f'{magic.coerce_filename(sys.argv[1])}')
    print(f'{magic.from_file(sys.argv[1], mime=True)}')
    
    matches = rules.match(sys.argv[1])
    if len(matches):
        for match in matches:
            print(f'{sys.argv[1]}: match {match}')

if __name__ == '__main__':
    main()

# 1f 8b 08 00
