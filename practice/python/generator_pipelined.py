#!/bin/env python3


DEBUG=False
# DEBUG=True

def get_str(x, y, pc):
    section_text = pc[x:y]
    section_text = (i['text'] for i in section_text)
    if DEBUG:
        print('..yeilded')
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
        fin = len(pc)
        yield get_str(ini['ind'], fin, pc)



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
    sec_case_1 = [
        {'id': 's0', 'ind': 0},
        {'id': 's1', 'ind': 2},
        {'id': 's2', 'ind': 4},
        {'id': 's3', 'ind': 6}
    ]

    # section pattern 2 for testing
    sec_case_2 = [
        {'id': 's0', 'ind': 0},
        {'id': 's1', 'ind': 4},
        {'id': 's3', 'ind': 6}
    ]


    # replace with 'sec_case_2' here for new pattern
    generated_content = (l for l in gen_content(sec_case_1, pc))

    if DEBUG:
        print('nothing executed yet. generator pipelining is cool')
        print("output: ")
    
    print('\n-\n'.join(generated_content)) 
