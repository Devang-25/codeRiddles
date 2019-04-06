#!/bin/env python3

def get_str(x, y, pc):
    section_text = pc[x:y]
    section_text = (i['text'] for i in section_text)
    return '\n'.join(section_text)

def gen_content(sec, pc):
    """
    @sec: section data
    @pc: paragraph content
    """
    p = iter(sec)
    ini = next(p)
    try:
        while True:
            fin = next(p)
            yield get_str(ini['ind'], fin['ind'], pc)
            ini = fin 
    except StopIteration:
        pass


if __name__ == '__main__':
    
    # para
    pc = [{'id': 'p0', 'text': 'aaa'},
          {'id': 'p1', 'text': 'bbb'},
          {'id': 'p2', 'text': 'ccc'},
          {'id': 'p3', 'text': 'ddd'},
          {'id': 'p4', 'text': 'eee'},
          {'id': 'p5', 'text': 'fff'},
          {'id': 'p6', 'text': 'ggg'},
          {'id': 'p7', 'text': 'hhh'}]

    # sections
    sec = [
        {'id': 's0', 'ind': 0},
        {'id': 's1', 'ind': 2},
        {'id': 's2', 'ind': 4},
        {'id': 's3', 'ind': 6}
    ]


    generated_content = (l for l in gen_content(sec, pc))
    print('\n-\n'.join(generated_content)) 
